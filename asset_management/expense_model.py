import pandas as pd
from sklearn.linear_model import LinearRegression

TRANSACTION_CSV = "data/transactions.csv"


# 🔹 최신 balance 가져오기
def get_latest_balance(csv_path=TRANSACTION_CSV):
    df = pd.read_csv(csv_path)

    if df.empty:
        return 0

    return int(df.iloc[-1]["balance"])


# 🔹 다음 달 지출 예측
def predict_next_month_expense(monthly_df):
    df = monthly_df.copy()

    # 1️⃣ 데이터 부족 방어
    if len(df) < 3:
        return df["total_expense"].mean()

    df["month_index"] = range(len(df))
    df["prev_1"] = df["total_expense"].shift(1)
    df["prev_2"] = df["total_expense"].shift(2)
    df = df.dropna()

    # 2️⃣ shift 후 데이터 부족 방어
    if len(df) < 1:
        return monthly_df["total_expense"].mean()

    X = df[["month_index", "prev_1", "prev_2"]]
    y = df["total_expense"]

    model = LinearRegression()
    model.fit(X, y)

    last = df.iloc[-1]

    next_X = [[
        last["month_index"] + 1,
        last["prev_1"],
        last["prev_2"],
    ]]

    prediction = model.predict(next_X)[0]

    return max(prediction, 0)
