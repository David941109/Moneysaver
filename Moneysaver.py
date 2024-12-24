import speech_recognition as sr
import matplotlib.pyplot as plt
import numpy as np
import json
import os

# 資產與記錄初始化
assets = {
    "活存": 0,
    "定存": 0,
    "基金": 0,
    "股票": 0,
    "不動產": 0,
    "貸款": 0
}

records = {
    "收入": {"主動收入": 0, "被動收入": 0},
    "支出": {category: 0 for category in ["飲食", "住家", "交通", "學習", "娛樂", "購物", "醫療", "稅金", "其他"]}
}

# 支出上限
expense_limit = 0
expense_thresholds = [0.5, 0.7, 0.8, 0.9]

# 語音輸入
def speech_to_text(prompt):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(prompt)
        try:
            audio = recognizer.listen(source, timeout=5)
            return recognizer.recognize_google(audio, language="zh-TW")
        except Exception as e:
            print("語音輸入失敗:", e)
            return None

# 記帳功能
def add_income():
    income_type = input("輸入收入類型（主動收入/被動收入）：") or speech_to_text("請說明收入類型")
    if income_type is None:
        print("收入類型輸入失敗")
        return
    amount = input("輸入收入金額：") or speech_to_text("請說明收入金額")
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        print("收入金額輸入失敗")
        return
    if income_type in records["收入"]:
        records["收入"][income_type] += amount
        print(f"{income_type} 增加了 {amount} 元")
    else:
        print("無效的收入類型！")

def add_expense():
    category = input("輸入支出類型（飲食/住家/...）：") or speech_to_text("請說明支出類型")
    if category is None:
        print("支出類型輸入失敗")
        return
    amount = input("輸入支出金額：") or speech_to_text("請說明支出金額")
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        print("支出金額輸入失敗")
        return
    if category in records["支出"]:
        records["支出"][category] += amount
        check_expense_limit()
        print(f"{category} 增加了 {amount} 元")
    else:
        print("無效的支出類型！")

# 支出上限檢查
def set_expense_limit(limit):
    global expense_limit
    expense_limit = limit
    print(f"支出上限設定為 {limit} 元")

def check_expense_limit():
    total_expense = sum(records["支出"].values())
    for threshold in expense_thresholds:
        if total_expense >= expense_limit * threshold:
            print(f"注意！您的支出已達上限的 {int(threshold * 100)}%")
            break

# 圖表生成
def generate_pie_chart():
    labels = records["支出"].keys()
    sizes = records["支出"].values()
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("支出分布")
    plt.show()

def generate_bar_chart(last_month, this_month):
    labels = records["支出"].keys()
    last_values = [last_month.get(cat, 0) for cat in labels]
    this_values = [records["支出"][cat] for cat in labels]

    x = np.arange(len(labels))
    width = 0.35

    plt.bar(x - width / 2, last_values, width, label="上個月")
    plt.bar(x + width / 2, this_values, width, label="這個月")

    plt.xlabel("支出類型")
    plt.ylabel("金額")
    plt.title("支出比較")
    plt.xticks(x, labels, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# 儲存和讀取支出數據
def save_expense_data():
    with open("expense_data.json", "w") as f:
        json.dump(records["支出"], f)

def load_expense_data():
    if os.path.exists("expense_data.json"):
        with open("expense_data.json", "r") as f:
            return json.load(f)
    else:
        return {category: 0 for category in records["支出"]}

# 主程式
def main():
    global records
    last_month_expense = load_expense_data()
    while True:
        print("\n1. 新增收入\n2. 新增支出\n3. 設定支出上限\n4. 生成支出圓餅圖\n5. 生成支出柱狀圖\n6. 離開")
        choice = input("選擇功能：")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            limit = float(input("設定支出上限金額："))
            set_expense_limit(limit)
        elif choice == "4":
            generate_pie_chart()
        elif choice == "5":
            generate_bar_chart(last_month_expense, records)
        elif choice == "6":
            save_expense_data()
            print("感謝使用記帳程式！")
            break
        else:
            print("無效選擇，請重新輸入！")

if __name__ == "__main__":
    main()