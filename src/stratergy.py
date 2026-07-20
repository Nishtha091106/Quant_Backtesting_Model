import pandas as pd

#generate signal
def generate_ma_signals(
        df,
        window
):
    """    """

    try:

        signals=[]

        if window<=0:
            raise ValueError("Window size must be greater than zero.")

        if f"MA_{window}" not in df.columns:
            raise ValueError("The window size is not in the Dataframe.")
        
        else:
            for i in range(len(df)):
                if df["Close"][i]>df[f"MA_{window}"][i]:
                    signals.append("BUY")

                else:
                    signals.append("SELL")
                
            df["Signal"]=signals

            return df
    
    except Exception as e:
        print(f"Error occured: {e}")
        return None