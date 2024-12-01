import pandas as pd
import pendulum
import streamlit as st

from src.currencycheck.adapters.currency_yfinance_adapter import CurrencyYFinanceAdapter
from src.currencycheck.domain.models import OHLC, CurrencyStock
from src.currencycheck.services.currency_service import get_bollinger_bands

pd.options.plotting.backend = "plotly"


st.write("Bollinger Bands")

option = st.selectbox(
    "Choose currency.",
    (
        "EURUSD=X",
        "EURGBP=X",
        "EURJPY=X",
        "EURCAD=X",
        "EURSEK=X",
        "EURCHF=X",
        "EURHUF=X",
    ),
)


bollinger_bands = get_bollinger_bands(
    currency_adapter=CurrencyYFinanceAdapter(),
    currency=CurrencyStock(option),
    start=pendulum.today().date().subtract(months=3),
    end=pendulum.today().date(),
    sma_window=30,
    ohlc=OHLC.close,
)


data = pd.DataFrame(
    {
        "Timeline": bollinger_bands.timeline,
        "SMA30": bollinger_bands.sma,
        "UpperBand": bollinger_bands.upper_band,
        "LowerBand": bollinger_bands.lower_band,
    }
)
data.dropna(inplace=True)
data.set_index("Timeline", inplace=True)


fig = data.plot()

st.plotly_chart(fig)
