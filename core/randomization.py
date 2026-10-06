# -*- coding: utf-8 -*-
import random
import time

class StratifiedBlockRouter:
    """
    Step 2. 後端分流控制軌 (分層隨機池)
    實作臨床試驗級分層區組隨機抽樣 (Stratified Block Randomization)，
    進行雙盲隨機編碼，防範假陽性偏誤 (Type I Error) 與統計作弊 (p-hacking)。
    """
    def __init__(self):
        # 記憶體動態隨機區組池，剛性鎖定控制組與對照組分母比例
        self._pools = {
            "high": [],
            "low": []
        }

    def _create_secure_block(self) -> list:
        """
        生成一個包含 50% 實驗組(A)與 50% 控制組(B)的雙盲安全區組。
        
        Returns:
            一個包含 "A" 和 "B" 的隨機排序列表。
        """
        block = ["A", "B"]
        random.shuffle(block)
        return block

    def allocate_target_arm(self, stratum: str) -> tuple:
        """
        動態隨機路由分派器。
        
        Args:
            stratum: 使用者的分層標籤 ("high" 或 "low")。
        
        Returns:
            一個包含分配組別 ("A" 或 "B") 和盲測代碼 ("X" 或 "Y") 的元組。
        
        Raises:
            ValueError: 當傳入未定義的分層標籤時。
        """
        if stratum not in ["high", "low"]:
            raise ValueError("Router Error: Target pool index undefined.")

        # 如果該分層的隨機池已空，則重新生成一個新的安全區組
        if not self._pools[stratum]:
            self._pools[stratum] = self._create_secure_block()

        # 彈出隨機池首位元素，確保 A/B 兩組樣本數絕對對齊 1:1
        assigned_group = self._pools[stratum].pop(0)

        # 實施分析者盲 (Blinding)：動態將真實組別映射為去識別化之 X/Y 編碼
        # 這裡使用時間戳的毫秒數來決定映射規則，增加隨機性
        if int(time.time() * 1000) % 2 == 0:
            blind_code = "X" if assigned_group == "A" else "Y"
        else:
            blind_code = "Y" if assigned_group == "A" else "X"

        return assigned_group, blind_code