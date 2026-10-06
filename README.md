# 📡 反算命大師 (Anti-FortuneTeller Master)
> 傳統命理模型的實證科學壓力測試：基於分層隨機抽樣之雙盲 A/B 測試全端系統

**📜 License:** MIT | **💻 Platform:** Streamlit Cloud | **📊 Data Engine:** Python (Pure) + GCP Google Sheets API

---

### 專案結論 (TL;DR)
本獨立開發作品採用純 Python 實作一套全端實驗系統，探討傳統玄學演算法（八字/紫微）能否走向類似「數值天氣預報」之數學分析模型，或本質上屬於心理學巴納姆效應（Barnum Effect）。系統於前端導入「信仰體質控制變數」進行子母體分層，後端以「分層區組隨機池演算法」強制維持實驗組與對照組 1:1 之盲性分配，並內建數據去識別化實時回收模組，直接靜默拋轉至外部 Google 試算表，為下階段 p-value 假設檢定提供高純淨度之匿名硬數據。

👉 **如果您想直接參與本科學實驗的盲測壓力測試，請點擊跳轉至：[全自動雙盲測試公開網址](https://anti-fortuneteller-master-6cnypwpkjuww38fjeiw2v8.streamlit.app/)。請在收到反饋後填寫下方表單，感謝！**

---

## 1. 核心動機與科學痛點 (Project Motivation & Pain Points)

### 1.1 哲學思辨：科學盡頭與未解科學的邊界
「科學的盡頭是玄學」是常見的觀察假說。本作品試圖進一步解構此命題：若該假說成立，則目前定義上的玄學，本質上應屬於「尚未被現代科學解碼的規律」。若要將其推向科學範疇，必須採用嚴謹的演算法逆向工程（Reverse Engineering）與統計學方法進行證偽（Falsification）。

### 1.2 數值大氣預報類比假說
在中世紀，精準預測氣象常被視為神祕主義；而在現代，隨著流體動力學、物理初始場輸入與資料同化（Data Assimilation）的加入，天氣預報已成為數學與電腦科學的常態。本作品旨在探尋八字四柱矩陣與紫微斗數坐標映射，是否具備走向「數值預報模型」之潛力，亦或僅為精密的文字重組遊戲。

### 1.3 傳統命理實驗之統計偏誤
傳統命理學天生具備「無法證偽」的容錯機制。同時，一般的 A/B 測試若未在源頭控制受測者的「既有信仰程度（干擾變數）」，極易因樣本隨機分配不均（例如迷信體質高頻分配至實驗組），導致實驗結果遭受統計污染。

---

## 2. 全系統雙軌架構設計 (System Dual-Pipeline Design)

本系統架構捨棄龐雜框架，採用純 Python 實作。當使用者前端提交數據後，後端將啟動多執行緒處理，由「隨機分流控制軌」與「核心運算資料軌」並行交織。

### 📌 全系統多執行緒資料流向圖

```mermaid
graph TD
    %% 節點樣式定義
    classDef input fill:#2d3748,stroke:#3b82f6,stroke-width:2px,color:#fff;
    classDef control fill:#2d3748,stroke:#ec4899,stroke-width:2px,color:#fff;
    classDef data fill:#2d3748,stroke:#10b981,stroke-width:2px,color:#fff;
    classDef template fill:#1a202c,stroke:#a855f7,stroke-width:2px,color:#fff;
    classDef gate fill:#1a202c,stroke:#f59e0b,stroke-width:2px,color:#fff;
    classDef output fill:#2d3748,stroke:#64748b,stroke-width:1px,color:#fff;

    USER["使用者前端提交 (Step 1)"]:::input -->|信仰量表| CTRL["隨機分流控制軌 (Step 2)"]:::control
    USER -->|五維初始場| DATA["核心運算資料軌"]:::data

    CTRL --> POOL["分層隨機池分配組別"]:::control
    DATA -->|真太陽時校正| BLOCK["建立大一統報告骨架模板"]:::template

    POOL --> GATE["解盤動態門控閘道 (Step 3)"]:::gate
    
    BLOCK --> T1["一、個人命盤解析 (A/B組皆真實)"]:::template
    BLOCK --> T2["二、個人四維分析與建議 (內容分流)"]:::template
    BLOCK --> T3["三、明年的運勢分析與建議 (內容分流)"]:::template

    T1 --> GATE
    T2 --> GATE
    T3 --> GATE

    GATE -->|A 組 放行| REAL["雙幾何同化 ──► 實算文本注入二、三"]:::data
    GATE -->|B 組 阻斷| BARNUM["巴納姆組裝 ──► 話術文本注入二、三"]:::control

    REAL --> SCORE["雙盲評分 1~5 星 ──► GCP Google 試算表"]:::output
    BARNUM --> SCORE
```

*   **Step 1. 前端資料觀測與信仰分層 (初始場輸入)**：
    *   **五維物理初始場**：強制要求受測者輸入標準化參數（西元出生年、月、日、時、分、出生地理位置、生理性別），進行真太陽時精確校正。
    *   **控制變數隔離**：填寫「命理信仰程度量表」（0-4分：科學理性派｜5分：中立派｜6-10分：玄學感性派），在初始場源頭鎖定並隔離干擾變數。
*   **Step 2. 後端分流控制軌 (分層隨機池)**：
    *   **動態分層區組隨機演算法（Stratified Block Randomization）**：後端針對高、低信仰子母體分別建立獨立的隨機區組（Block Pool），強制確保其被分配到 A 組（實驗組）與 B 組（對照組）的分母比例絕對對齊 1:1。
    *   **三盲實驗思維**：受測者盲、分析者盲（後台實時映射為 X/Y 去識別化編碼）。內建「開發者專屬監控後門」，確保開發者的主觀期待不污染數據。
*   **Step 3. 核心運算資料軌與大一統外殼骨架 (排盤與門控注入)**：
    *   導入設計模式中的「模板方法模式（Template Method Pattern）」，制定了結構嚴格的「大一統報告骨架模板」。不論受測者最終被分流至哪一組，其拿到的報告排版、小標題、字數長度完全一致：
        *   **【一、個人命盤解析】區塊 (全體 100% 真實排盤 — 信度初始場)**：不論 A/B 組，皆執行八字四柱代數矩陣計算與紫微十二宮坐標幾何排盤，建立強烈的心理信度暗示。
        *   **【內容動態注入解盤閘道】**：
            *   **⚙️ A 組（實驗組文本）**：進行八字與紫微的跨模型資料同化（Data Assimilation），抓取交集（Ensemble Consensus），將實算結果注入骨架。
            *   **🧠 B 組（對照組文本）**：全面隔離資料軌。改調用後端「高級巴納姆心理學偽裝庫」，1:1 複製 A 組的四大章節小標題與星曜術語外殼，測試人類大腦的代償與對號入座邊界。

---

## 3. 統計假說驗證矩陣 (Data Matrix & Hypothesis Testing)

收集完受測者匿名數據後，本作品將使用 Python `scipy.stats` 模組進行獨立樣本 T 檢定（Independent t-test）。我們以科學界公認的 p-value < 0.05 作為具備統計顯著性（Statistical Significance）的唯一判準：

*   **情境一：證偽成功 (\(A_{\text{mean}} \approx B_{\text{mean}}\) 且均拿下高分)**：成功證明玄學本質為高明的巴納姆效應。人類大腦會主動代償並對號入座，底層玄學公式不具備顯著的統計學意義。
*   **情境二：支持假說 (\(A_{\text{mean}} > B_{\text{mean}}\) 且 p-value < 0.05)**：證實真實報告顯著優於對照組話術。高度支持「數值分析模型」類比假說，證明玄學具備資料科學的規規律性。
*   **情境三：反向反饋 (\(A_{\text{mean}} < B_{\text{mean}}\) 且 p-value < 0.05)**：傳統公式效能失靈，心理學話術大獲全勝。證明傳統命理產業高度依賴冷讀術與心理暗示。
*   **情境四：系統雜訊過大 (兩組評分無顯著差異 且 p-value ≥ 0.05)**：統計效能（Statistical Power）不足。可能源於 UI 易用性、報告文案辨識度，或受限於小樣本分母。

---

## 4. 開發者自我審查與權限承諾 (Limitations & Topology)

專案結尾附上嚴謹的科學盲點反思：若結果走向情境一或情境四，仍須聲明潛在的系統性偏誤——開發者本身對古典八字與紫微斗數古籍代碼的詮釋深度，可能在演算法降維轉換過程中產生了資訊遺失（Information Loss），無法 100% 還原人工解盤的複雜權重。

📁 **專案工程依賴與目錄拓樸 (Project Topology)**
```text
Anti-FortuneTeller-Master/
│
├── README.md               # 獨立作品開發計畫書 (本文件)
├── main.py                 # 全系統多執行緒主控制流程 (指揮官)
├── requirements.txt        # 雲端 Linux 相依套件清單 (純文字環境配置)
│
├── core/                   # 100% 原創編寫的核心 A/B 測試門控組件
│   ├── stratification.py   # Step 1. 前端信仰量表計分與初始場驗證
│   ├── randomization.py    # Step 2. 記憶體動態分層區組隨機池演算法
│   └── gate_control.py     # Step 3. 大一統報告模板與門控解盤填充機
│
└── vendor/                 # 源碼嵌入（Vendoring）基礎排盤底層輪子
    ├── lunar_python/       # 負責真實公農曆二十四節氣與真太陽時計算
    └── iztro_py/           # 負責真實紫微斗數十四主星二維空間矩陣映射
```

---

## License
MIT License
