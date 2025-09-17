import yfinance as yf

def get_stock_data(ticker, period = "1mo", interval = "1d"):
    
    """
    Fetch historical stock data for a given ticker symbol.

    Args:
        ticker (str): Stock symbol, e.g. "AAPL".
        period (str, optional): How far back to fetch data (e.g., "1mo", "6mo", "1y"). Defaults to "1mo".
        interval (str, optional): Data granularity (e.g., "1d" for daily, "1h" for hourly). Defaults to "1d".

    Returns:
        pd.DataFrame: Stock price history with Open, High, Low, Close, Adj Close, Volume.
    """
    
    data = yf.download(ticker, period = period, interval = interval)
    return data

df = get_stock_data("AAPL", period="1mo")
print(df.head())
