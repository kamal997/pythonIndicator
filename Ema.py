import MetaTrader5 as mt5
import pandas as pd


def get_signal_EMA(symbol):
    bars = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M15, 1, 1000)
    df = pd.DataFrame(bars)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df['EMA200'] = df.close.ewm(span=200,adjust=False).mean()
    print(df)

initialized = mt5.initialize()
symbol = "SGDJPY"
get_signal_EMA(symbol)
