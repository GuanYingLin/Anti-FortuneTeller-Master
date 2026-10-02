# -*- coding: utf-8 -*-
import streamlit as st
import os
import csv
from datetime import date
from core.stratification import InputInitializer
from core.randomization import StratifiedBlockRouter
from core.gate_control import UnifiedGateController

if "initializer" not in st.session_state:
    st.session_state.initializer = InputInitializer()
if "router" not in st.session_state:
    st.session_state.router = StratifiedBlockRouter()
if "gate_controller" not in st.session_state:
    st.session_state.gate_controller = UnifiedGateController()

st.set_page_config(page_title="反算命大師", page_icon="📡", layout="centered")

st.title("📡 反算命大師 (Anti-FortuneTeller Master)")
st.caption("「若天氣預報是一門科學，那東方命理能否走向數值分析模型？」")
st.write("---")

st.header("📋 Step 1. 前端資料觀測與信仰分層 (初始場輸入)")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**【時間初始場觀測】**")
    # 🛡️ 隱私防禦：預設生日全面歸零為中立白紙
    birth_date_ui = st.date_input(
        "西元出生年月日",
        value=date(2000, 1, 1),
        min_value=date(1900, 1, 1),
        max_value=date(2026, 12, 31)
    )
    st.write(" ")
    st.caption("出生精確時間設定 (時 / 分)：")
    time_col_h, time_col_m = st.columns(2)
    with time_col_h:
        hours_options = [f"{h:02d}" for h in range(24)]
        selected_hour = st.selectbox("時 (Hour)", hours_options, index=0)
    with time_col_m:
        minutes_options = [f"{m:02d}" for m in range(60)]
        selected_minute = st.selectbox("分 (Minute)", minutes_options, index=0)

with col2:
    st.markdown("**【身分與地理初始場觀測】**")
    # 🛡️ 隱私防禦：將姓名與城市完全中立化，不帶任何個人特徵
    name_ui = st.text_input("受測者姓名", placeholder="例如：張三 (可填匿名)")
    gender_ui = st.selectbox("生理性別 (決定大運順逆分支)", ["男", "女"])
    st.write(" ")
    st.caption("出生地理初始場校準：")
    birth_city_ui = st.text_input("出生城市 (進行真太陽時校正)", placeholder="例如：台灣台中市")

st.write(" ")
st.markdown("**🛡️ 信仰體質控制變數校準：**")
st.caption("【量表定義】 0 ~ 4 分：科學理性派（不信玄學）｜ 5 分：中立並尊重 ｜ 6 ~ 10 分：玄學感性派（深信引指）")
belief_score = st.slider("請客觀評估你目前對命理玄學的「真實信仰程度」：", 0, 10, 0)

st.write("---")

if st.button("🚀 啟動數值分析與動態慰問門控組裝", type="primary"):
    b_hour = int(selected_hour)
    b_minute = int(selected_minute)
        
    raw_user_data = {
        "year": birth_date_ui.year, "month": birth_date_ui.month, "day": birth_date_ui.day,
        "hour": b_hour, "minute": b_minute,
        "birth_city": birth_city_ui if birth_city_ui else "台灣台北市", 
        "gender": gender_ui
    }
    
    try:
        normalized_data = st.session_state.initializer.validate_initial_field(raw_user_data)
        stratum = st.session_state.initializer.calculate_belief_stratum(belief_score)
        assigned_group, blind_code = st.session_state.router.allocate_target_arm(stratum)
        report = st.session_state.gate_controller.compile_unified_template(normalized_data, assigned_group)
        
        st.session_state.current_experiment = {
            "belief_level": stratum,
            "assigned_group": assigned_group,
            "blind_code": blind_code,
            "belief_score": belief_score
        }
        
        st.success("✨ 雙軌資料流同化完畢！報告結構已鎖定，以下為雙盲即時預覽：")
        
        st.markdown(f"# {report['title']}")
        st.write("---")
        
        st.markdown("### 📊 【數據校準基線】 觀測初始場對齊數據")
        st.info(f"**【真太陽時校正】** {report['part_one_charts']['solar_time_calibrated']}\n\n"
                f"**【真實八字四柱】** {report['part_one_charts']['bazi_matrix']}\n\n"
                f"**【真實紫微宮位】** {report['part_one_charts']['ziwei_matrix']}")
        
        st.markdown("## 壹、 八字命局結構與氣息精確定位")
        st.markdown(report['part_one_text'].replace("\n\n", "\n\n***\n\n"))
        st.write("---")
        
        st.markdown("## 貳、 紫微斗數空間結構與心理動能追蹤")
        st.markdown(report['part_two_text'].replace("\n\n", "\n\n***\n\n"))
        st.write("---")
        
        st.markdown("## 參、 歲運交互作用的動態觸發點")
        st.markdown(report['part_three_text'].replace("\n\n", "\n\n***\n\n"))
        st.write("---")

        st.markdown("## 肆、 易經動態決策矩陣與時位應對")
        st.markdown(report['part_four_text'].replace("\n\n", "\n\n***\n\n"))
        
        st.write(" ")
        st.caption(report['footer_signature'])
        st.write("---")
        
    except Exception as e:
        st.error(f"系統運行異常 (Runtime Exception): {str(e)}")

if "current_experiment" in st.session_state:
    st.header("📥 數據去識別化自動回收模組")
    st.caption("請以你真實的人生遭遇，客觀評定上方『壹、貳、參、肆部分』的描述與你現狀的吻合度：")
    
    score = st.feedback("stars")
    feedback_text = st.text_area("是否有任何意見回饋書想提交給後台分析？（選填）")
    
    if st.button("💾 鎖定並匿名送出硬數據"):
        if score is None:
            st.error("請先點選星星進行評分再送出！")
        else:
            os.makedirs("data", exist_ok=True)
            csv_path = "data/results.csv"
            file_exists = os.path.isfile(csv_path)
            
            with open(csv_path, mode="a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["belief_score", "belief_level", "assigned_group", "blind_code", "score", "feedback"])
                
                exp = st.session_state.current_experiment
                writer.writerow([exp["belief_score"], exp["belief_level"], exp["assigned_group"], exp["blind_code"], score + 1, feedback_text])
                
            st.balloons()
            st.success("🎉 數據已成功寫入 data/results.csv！你已成功為本科學實驗增加了一筆去識別化高純淨度硬數據！")
            del st.session_state.current_experiment
            
    st.write(" ")
    if "current_experiment" in st.session_state:
        exp = st.session_state.current_experiment
        st.text(f"[⚙️ DEVELOPER DEBUG MODE] 系統即時監控：控制軌 = {exp['assigned_group']} 組 ｜ 後台匿名編碼 = {exp['blind_code']}")
