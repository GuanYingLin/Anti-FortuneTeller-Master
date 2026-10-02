# -*- coding: utf-8 -*-
import random
import time

class StratifiedBlockRouter:
    """
    Step 2. 後端分流控制軌 (分層隨機池)
    實作臨床級 Stratified Block Randomization，並進行三盲隨機編碼，封死統計作弊(p-hacking)。
    """
    def __init__(self):
        # 記憶體動態隨機區組池，嚴格鎖定隨機分母
        self._pools = {
            "high": [],
            "low": []
        }

    def _create_secure_block(self) -> list:
        """生成一個 50% 真預報(A)與 50% 假話術(B)的雙盲安全區組"""
        block = ["A", "B"]
        random.shuffle(block)
        return block

    def allocate_target_arm(self, stratum: str) -> tuple:
        """
        門控路由分派器
        輸出: (assigned_group 'A'/'B', blind_code 'X'/'Y')
        """
        if stratum not in ["high", "low"]:
            raise ValueError("Router Error: Target pool index undefined.")

        if not self._pools[stratum]:
            self._pools[stratum] = self._create_secure_block()

        # 彈出當前隨機池最前排的元素，確保 1:1 剛性比例
        assigned_group = self._pools[stratum].pop(0)

        # 實施【分析者盲】：動態在後台將真實組別映射為無客觀期望的 X/Y 編碼
        if int(time.time() * 1000) % 2 == 0:
            blind_code = "X" if assigned_group == "A" else "Y"
        else:
            blind_code = "Y" if assigned_group == "A" else "X"

        return assigned_group, blind_code
