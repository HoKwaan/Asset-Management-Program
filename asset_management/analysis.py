import pandas as pd

def load_monthly_expense(csv_path):
    df = pd.read_csv(csv_path)

    # date 강제 datetime 변환
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # 지출만 필터
    df = df[df["type"] == "expense"]

    # amount 숫자 강제 변환
    df["amount"] = (
        df["amount"]
        .astype(str)
        .str.replace(",", "")
        .astype(float)
        .abs()
    )

    # 날짜 변환 실패한 행 제거
    df = df.dropna(subset=["date"])

    # 월별 집계
    monthly = (
        df.groupby(df["date"].dt.to_period("M"))["amount"]
        .sum()
        .reset_index()
    )

    monthly.columns = ["month", "total_expense"]
    monthly["month"] = monthly["month"].astype(str)

    return monthly
