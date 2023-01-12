import MetaTrader5 as mt5
import pandas as pd

def get_signal_stochastic(symbol):
    bars = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M15, 1, 1000)
    df = pd.DataFrame(bars)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    # stochastic strategi
    n = 5
    low_14 = df['low'].copy()
    high_14 = df['high'].copy()
    df['low_14'] = low_14.rolling(window=n).min()
    df['high_14'] = high_14.rolling(window=n).max()
    price_live = mt5.symbol_info_tick(symbol).ask
    df['k_percent']  = 100 * ((df['close'] - df.low_14) / (df.high_14 - df.low_14))
    df['d_percent'] = k_percent.rolling(3).mean()
    df = df[['time', 'close', 'k_percent', 'd_percent', 'symbol']]
    d_percent = df.iloc[-1]['d_percent']
    k_percent = df.iloc[-1]['k_percent']
    print(df.tail(3))
    return d_percent, k_percent
  
initialized = mt5.initialize()
symbol = "SGDJPY"
get_signal_stochastic(symbol)
