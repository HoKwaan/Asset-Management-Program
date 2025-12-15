from asset_management.analysis import load_monthly_expense
from asset_management.expense_model import (
    predict_next_month_expense,
    get_latest_balance,
)
from asset_management.transaction_manager import add_transaction
from asset_saving.portfolio import (
    calculate_required_cash,
    calculate_investable_asset,
    allocate_all_weather,
)
from asset_management.transaction_manager import (
    add_transaction,
    show_account_status,
)

from asset_saving.investment import Investment, save_investments
import csv

TRANSACTION_CSV = "data/transactions.csv"
INVESTMENT_CSV = "data/investment_status.csv"


def change_investment_status():
    investments = []

    with open(INVESTMENT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            investments.append(
                Investment(
                    row["asset"],
                    int(row["amount"]),
                    row["completed"] == "True"
                )
            )

    print("\n투자 상태 변경 (y/n)")
    for inv in investments:
        while True:
            done = input(f"{inv.asset} 완료 여부 (y/n): ").strip().lower()
            if done in ("y", "n"):
                inv.completed = (done == "y")
                break
            print("y 또는 n만 입력하세요.")

    save_investments(INVESTMENT_CSV, investments)
    print("✅ 투자 상태가 업데이트되었습니다.")


def main_menu():
    while True:
        print("\n===== 자산관리 프로그램 =====")
        print("1. 계좌 상태 변경")
        print("2. 투자 상태 변경")
        print("3. 자산 분석 및 포트폴리오 실행")
        print("4. 자산 상태 확인")
        print("0. 종료")

        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            add_transaction()

        elif choice == "2":
            change_investment_status()

        elif choice == "3":
            monthly = load_monthly_expense(TRANSACTION_CSV)
            predicted = predict_next_month_expense(monthly)

            while True:
                try:
                    buffer_rate = float(
                        input("안전 여유금 비율 입력 (예: 0.1): ").strip()
                    )
                    if buffer_rate < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("0 이상의 숫자를 입력하세요.")

            total_asset = get_latest_balance()
            required_cash = calculate_required_cash(predicted, buffer_rate)
            investable = calculate_investable_asset(total_asset, required_cash)
            allocation = allocate_all_weather(investable)

            print("\n===== 결과 =====")
            print(f"현재 자산: {total_asset:,}원")
            print(f"예상 지출: {int(predicted):,}원")
            print(f"투자 가능 자산: {int(investable):,}원")

            for k, v in allocation.items():
                print(f"{k}: {int(v):,}원")

        elif choice == "4":
            show_account_status()

        elif choice == "0":
            print("프로그램 종료")
            break

        else:
            print("올바른 메뉴를 선택하세요.")


if __name__ == "__main__":
    main_menu()
