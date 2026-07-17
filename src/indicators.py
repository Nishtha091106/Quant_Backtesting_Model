import pandas as pd

#function for moving average
def calculate_moving_average(
        df,
        window
):
    """     """

    try:

        if window<=0:
            print("Error: Invalid window size")
            return None
        
        df["MA_{window}"]=df["Close"].window(window).mean()
        return df
    
    except Exception as e:
        print(f"Error occured: {e}")
        return None
    

if __name__ == "__main__":
    data_ma=calculate_moving_average(
        df="AAPL_2024-01-01_2025-01-01.csv",
        window=3
    )

    data_ma



