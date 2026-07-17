import pandas as pd

#function for moving average
def calculate_moving_average(
        df,
        window
):
    """ 
    Calculates the moving average for a given window.

    Parameters:
        df (DataFrame): Stock price data.
        window (int): Moving average window size.

    Returns:
        DataFrame: Updated DataFrame with a new MA column.
    """

    try:

        if window<=0:
            raise ValueError("Window size must be greater than zero.")
        
        df[f"MA_{window}"]=df["Close"].rolling(window=window).mean()
        return df
    
    except Exception as e:
        print(f"Error occured: {e}")
        return None

