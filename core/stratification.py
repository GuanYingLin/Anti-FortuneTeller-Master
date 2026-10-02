# -*- coding: utf-8 -*-
from datetime import datetime

class InputInitializer:
    """
    Step 1. 前端資料觀測與信仰分層
    負責五維初始場數據的清洗（Normalization）與隔離「迷信體質」干擾變數。
    """
    def __init__(self):
        pass

    def validate_initial_field(self, user_data: dict) -> dict:
        """驗證並標準化五維氣象初始場，防止雜訊代碼傳入後端"""
        required_fields = ["year", "month", "day", "hour", "minute", "birth_city", "gender"]
        for field in required_fields:
            if field not in user_data or not user_data[field]:
                raise ValueError(f"Data Error: Missing weather variable [{field}]")
        
        # 數據清洗：將時間與性別控制流進行標準化轉換
        user_data["gender"] = "M" if user_data["gender"] in ["男", "M", "Male"] else "F"
        return user_data

    def calculate_belief_stratum(self, score: int) -> str:
        """
        將信仰量表分數轉化為控制流標籤
        0-5分為低信仰子母體(low)，6-10分為高信仰子母體(high)
        """
        if not (0 <= score <= 10):
            raise ValueError("Control Flow Error: Stratification score out of range.")
        return "low" if score <= 5 else "high"
