import yfinance as yf

def basic_info(ticker_str: str) -> dict[str, float]:
    ticker = yf.Ticker(ticker_str)

    # initialize history
    ticker.history()

    ticker.basic_info['lastPrice']

    selected_keys = (
        'fiftyDayAverage',
        'twoHundredDayAverage',
        'fiftyTwoWeekLow',
        'fiftyTwoWeekHigh'
    )

    selected_info =  {key: ticker.info[key] for key in selected_keys}
    selected_info['lastPrice'] = ticker.basic_info['lastPrice']

    return selected_info
