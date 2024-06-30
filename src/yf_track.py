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
        result += f"{k +':':{max_key_len+2}} {v:.1f}\n".replace(".", ",")
    result += "```"
    return result


@lru_cache
def get_cached_tracker_info(ticker: str) -> dict[str, float]:
    return get_tracker_info(ticker)


def get_tracker_info(ticker_str: str) -> dict[str, float]:
    ticker = yf.Ticker(ticker_str)

    # initialize history
    ticker.history()

    selected_keys = (
        "fiftyDayAverage",
        "twoHundredDayAverage",
        "fiftyTwoWeekLow",
        "fiftyTwoWeekHigh",
    )

    selected_info = {key: ticker.info[key] for key in selected_keys}
    selected_info["lastPrice"] = ticker.basic_info["lastPrice"]

    return selected_info
