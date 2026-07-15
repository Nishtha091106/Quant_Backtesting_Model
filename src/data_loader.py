import yfinance as yf
import pandas as pd

def download_stock_data(
        tickers,
        start_date,
        end_date
):
    """
    Downloads historical stock data
    Saves it as a CSV file
    returns a Dataframe
    
    """

    try:

        data=yf.download(
            tickers=tickers,
            start=start_date,
            end=end_date
        )

        if data.empty:
            print("Error: invalid ticker symbol")
            return None
        
        filename=f"data/raw/{tickers}_{start_date}_{end_date}.csv"
        data.to_csv(filename)

        return data

    except Exception as e :
        print(f"Error occured: {e}")
        return None
    
if __name__ == "__main__":
    df=download_stock_data(
        tickers="AAPL",
        start_date="2024-01-01",
        end_date="2025-01-01"
    )

    df["Daily_Retuns"]=df["Close"].pct_change()
    print(df.describe())
