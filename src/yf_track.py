from functools import lru_cache, reduce

import yfinance as yf


def dict_to_markdown(d: dict[str, float]) -> str:
    """Fromats a dict to a markdown compatible string

    Args:
        d (dict[str, float]): _description_

    Returns:
        str: _description_
    """
    result = "```\n"
    max_key_len: int = reduce(max, map(len, d.keys()))
    for k, v in d.items():
        result += f"{k:{max_key_len+2}} {v:.1f}\n".replace(".", ",")
    result += "```"
    return result


@lru_cache
def get_cached_tracker_info(ticker: str) -> dict[str, float]:
    return get_tracker_info(ticker)


def get_tracker_info(ticker_str: str) -> dict[str, float]:
    ticker = yf.Ticker(ticker_str)

    # initialize history
    ticker.history()

    keys_as_pretty_names = {
        "fiftyDayAverage": "50 Day Average",
        "twoHundredDayAverage": "200 Day Average",
        "fiftyTwoWeekLow": "52 Week Low",
        "fiftyTwoWeekHigh": "52 Week High",
    }

    selected_info = {
        pretty_name: ticker.info[key]
        for key, pretty_name in keys_as_pretty_names.items()
    }

    # Add info from "basic info" as well
    selected_info["Last Price"] = ticker.basic_info["lastPrice"]

    return selected_info
