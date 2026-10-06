# -*- coding: utf-8 -*-
from datetime import datetime

class InputInitializer:
    """
    Step 1. 前端資料觀測與信仰分層
    負責物理初始場數據特徵工程清洗 (Normalization) 與既有信仰程度干擾變數之分層隔離。
    """
    def __init__(self):
        pass

    def validate_initial_field(self, user_data: dict) -> dict:
        """
        驗證並標準化物理初始場參數，排除非預期雜訊代碼。
        
        Args:
            user_data: 包含使用者輸入資料的字典。
        
        Returns:
            標準化後的資料字典。
        
        Raises:
            ValueError: 當缺少必要欄位時。
        """
        required_fields = ["year", "month", "day", "hour", "minute", "birth_city", "gender"]
        for field in required_fields:
            if field not in user_data or not user_data[field]:
                raise ValueError(f"Data Error: Missing observational variable [{field}]")
        
        # 特徵清洗：將時間與性別控制流進行標準化轉換
        user_data["gender"] = "M" if user_data["gender"] in ["男", "M", "Male"] else "F"
        return user_data

    def calculate_belief_stratum(self, score: int) -> str:
        """
        將主觀信仰量表分數轉化為隨機控制流之分層標籤。
        0-5 分劃分為低信仰子母體 (low)，6-10 分劃分為高信仰子母體 (high)。
        
        Args:
            score: 使用者的信仰分數 (0-10)。
        
        Returns:
            分層標籤 ("low" 或 "high")。
        
        Raises:
            ValueError: 當分數不在 0-10 的範圍內時。
        """
        if not (0 <= score <= 10):
            raise ValueError("Control Flow Error: Stratification score out of range.")
        return "low" if score <= 5 else "high"