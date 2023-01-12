import MetaTrader5 as mt5
import pandas as pd


def get_signal_MACD(symbol):
    bars = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M15, 1, 1000)
    df = pd.DataFrame(bars)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df['EMA12'] = df.close.ewm(span=12,adjust=False).mean()
    df['EMA26'] = df.close.ewm(span=26,adjust=False).mean()
    df['MACD'] = df.EMA12 - df.EMA26
    df['signal'] = df.MACD.ewm(span=9,adjust=False).mean()
    df = df[['time', 'close', 'EMA12', 'EMA26', 'MACD', 'signal']]
    print(df.tail(5))

initialized = mt5.initialize()
symbol = "SGDJPY"
get_signal_MACD(symbol)
