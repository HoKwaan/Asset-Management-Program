import csv
from datetime import datetime

TRANSACTION_CSV = "data/transactions.csv"
FIELDNAMES = ["date", "category", "amount", "type", "balance"]


def get_last_balance():
    try:
        with open(TRANSACTION_CSV, "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
            if not rows:
                return 0
            return int(rows[-1]["balance"])
    except FileNotFoundError:
        return 0


def add_transaction():
    """계좌 상태 변경 (수입 / 지출 추가)"""

    date = input("날짜 입력 (YYYY-MM-DD, 엔터 시 오늘): ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    category = input("카테고리 입력: ").strip()

    # 금액 입력
    while True:
        try:
            amount = int(input("금액 입력 (숫자만): ").replace(",", ""))
            break
        except ValueError:
            print("숫자만 입력하세요.")

    # 타입 입력
    while True:
        t_type = input("유형 입력 (income / expense): ").strip().lower()
        if t_type in ("income", "expense"):
            break
        print("income 또는 expense 만 입력 가능")

    # 지출은 음수로 강제
    if t_type == "expense" and amount > 0:
        amount = -amount

    last_balance = get_last_balance()
    new_balance = last_balance + amount

    with open(TRANSACTION_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({
            "date": date,
            "category": category,
            "amount": amount,
            "type": t_type,
            "balance": new_balance
        })

    print(f"✅ 거래 완료 | 현재 잔액: {new_balance:,}원")

def show_account_status(recent_n=5):
    """현재 잔액 및 최근 거래 출력"""

    try:
        with open(TRANSACTION_CSV, "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))

        if not rows:
            print("거래 내역이 없습니다.")
            return

        latest = rows[-1]
        balance = int(latest["balance"])

        print("\n===== 자산 상태 =====")
        print(f"현재 잔액: {balance:,}원")

        print(f"\n최근 거래 {min(recent_n, len(rows))}건:")
        for row in rows[-recent_n:]:
            print(
                f'{row["date"]} | {row["category"]:<15} '
                f'{int(row["amount"]):>10,} | 잔액 {int(row["balance"]):,}'
            )

    except FileNotFoundError:
        print("transactions.csv 파일이 없습니다.")