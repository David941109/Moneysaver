# Moneysaver: A Python help manage finances

## (1) 程式的功能 Features

Moneysaver provides the following functionalities:

- **TRecord Income**:Users can add active or passive income via text or voice input.
- **Record Expenses**: Users can add expenses by specifying the category and amount via text or voice input.
- **Set Spending Limit**: Users can set a spending limit, and the system will check and alert if the spending exceeds different thresholds.
- **Generate Charts**: Pie Chart: Displays the distribution of different types of expenses.
Bar Chart: Compares expenses from the previous month to the current month.
- **Save and Load Expense Data**: The program saves the current expense data when it closes and loads it the next time it starts, allowing users to continue using it.


## (2) 使用方式 Usage

啟動程式：
用戶啟動程式後，會看到功能選單，可以選擇要執行的操作。

新增收入：
用戶選擇新增收入，程式會要求輸入收入類型（主動收入或被動收入）和收入金額。

新增支出：
用戶選擇新增支出，程式會要求輸入支出類型（如飲食、住家等）和支出金額。若支出總額達到設定的上限，程式會提示用戶。

設定支出上限：
用戶可以設定一個支出上限，當支出總額達到一定比例時，程式會發出提示。

生成圖表：
用戶可以生成支出的圓餅圖，顯示不同類型支出的分布。
用戶可以生成支出比較的柱狀圖，顯示上個月和這個月的支出變化。

離開程式：
用戶選擇離開程式時，會保存當前的支出數據，以便下次使用時讀取。

## (3) 程式的架構 Program Architecture

The project is organized as follows:

```
FinanceTracker/
├── financetracker/
│   ├── __init__.py
│   ├── assets.py          # 資產管理功能
│   ├── records.py         # 收支記錄功能
│   ├── notifications.py   # 支出提醒功能
│   ├── charts.py          # 報表生成功能
│   ├── speech.py          # 語音輸入功能
│   ├── storage.py         # 資料儲存與讀取功能
├── examples/
│   ├── interactive_tracker.py  # 互動式記帳程式主入口
│   ├── monthly_analysis.py     # 分析和生成月度報表的範例
├── requirements.txt      # 依賴套件列表
└── README.md             # 使用說明文件
```


## (4) 開發過程 Development Process

1.設計和規劃
確定記帳程式的基本功能，包括收入、支出的記錄，支出上限提醒，以及圖表生成。規劃進階功能，例如語音輸入、支出對比圖，以及資料的儲存與讀取。
2.設置環境
安裝必要的庫，包括 speech_recognition（語音輸入）、matplotlib（圖表生成）、numpy（數據處理）和 json（資料儲存）。建立模組化的程式架構。
3.實現基本功能
實現收入和支出類型的互動式輸入功能。
增加檢查支出上限的功能，並根據設定的提醒閾值進行警告提示。
提供生成支出圓餅圖的功能，視覺化支出分布。
4.實現進階功能
添加語音輸入功能，讓使用者可以用語音輸入收入與支出類型及金額。
實現月度支出對比柱狀圖，用以比較本月和上月的支出差異。
提供資料的儲存與讀取功能，確保數據不會因為程式結束而丟失。
5.測試和調試
測試記帳程式的各個模組，包括數據輸入、語音辨識、圖表生成以及支出提醒功能。測試各種極端情況，例如無效輸入和支出上限接近時的反應，並修復錯誤。
6.部署
將應用包裝為可執行程式，或者部署到伺服器上，提供使用者下載或直接運行的途徑。例如，生成安裝檔案或使用 Flask 搭建一個基於 Web 的版本。

## (5) 參考資料來源 References

1. [Flask](https://flask.palletsprojects.com/en/stable/) - Assisted with  architectural structuring of the project.
2. ChatGPT - Assisted with documentation and architectural structuring of the project.

## (6) 程式修改或增強的內容 Enhancements and Contributions
在這個專案中，我參考並結合 ChatGPT 提供的架構，完成了以下幾個主要貢獻：

1.實現進階功能：
新增語音輸入功能，允許用戶使用語音進行收入與支出項目的記錄，增強程式的使用便捷性
實現了支出上限管理功能，用戶可隨時調整上限，並及時獲得對超支情況的提醒。
為未來功能擴展設計了模組化結構，便於添加其他資產分析與記錄功能（如投資回報率計算、年度財務報告等）。

2.測試和調試：
測試所有功能，修復錯誤debug，確保程式穩定運行。
如處理輸入語音時失敗的問題，和支出上限提示多次重複等問題
