import MetaTrader5 as mt5
import pandas as pd


def get_signal_SMA(symbol):
    bars = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H1, 1, 1000)
    df = pd.DataFrame(bars)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df['SMA'] = df.close.rolling(20).mean()
    print(df.tail(5))

initialized = mt5.initialize()
symbol = "BTCUSD"
get_signal_SMA(symbol)
