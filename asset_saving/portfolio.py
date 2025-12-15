ALL_WEATHER = {
"Equity": 0.30,
"Long_Bond": 0.40,
"Mid_Bond": 0.15,
"Gold": 0.075,
"Commodity": 0.075,
}




def calculate_required_cash(predicted_expense, buffer_rate=0.1):
    return predicted_expense * (1 + buffer_rate)




def calculate_investable_asset(total_asset, required_cash):
    return max(total_asset - required_cash, 0)




def allocate_all_weather(investable_asset):
    allocation = {}
    for asset, ratio in ALL_WEATHER.items():
        allocation[asset] = investable_asset * ratio
    return allocation