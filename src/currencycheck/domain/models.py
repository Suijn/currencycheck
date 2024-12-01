import enum
import functools

import pandas as pd


class CurrencyStock(enum.StrEnum):
    eurusd = "EURUSD=X"
    eurgpb = "EURGBP=X"
    eurjpy = "EURJPY=X"
    eurcad = "EURCAD=X"
    eursek = "EURSEK=X"
    eurchf = "EURCHF=X"
    eurhuf = "EURHUF=X"


class OHLC(enum.StrEnum):
    open = "Open"
    high = "High"
    low = "Low"
    close = "Close"


class BollingerBands:
    """
    Calculate Bollinger Bands.

    Assumptions:
    - Stocks don't operate on weekends.
    - Because of that there are gaps in the timeline (
        the days when the Stock doesn't operate are just not present in the dataset
    ).

    This class behaves that way:
    For sma_window=30 it returns Bollinger Bands
    for precisely 30 "registered" days when the Stock operated.
    """

    def __init__(
        self,
        currency_hist_data: pd.DataFrame,
        sma_window: int,
        ohlc: OHLC,
        currency: CurrencyStock,
    ) -> None:
        self._data = currency_hist_data
        self._sma_window = sma_window
        self._ohlc = ohlc
        self._currency = currency

    @property
    def timeline(self) -> pd.DatetimeIndex:
        """Get Bollinger Bands timeline for selected SMA Window."""
        return self._data.tail(self._sma_window).index

    @property
    def sma(self) -> pd.Series:
        """Get Bollinger Bands SMA for selected SMA Window."""
        return self._get_sma().tail(self._sma_window)

    @property
    def upper_band(self) -> pd.Series:
        """Get Bollinger Bands Upper Band for selected SMA Window."""
        return (self._get_sma() + 2 * self._get_std()).tail(self._sma_window)

    @property
    def lower_band(self) -> pd.Series:
        """Get Bollinger Bands Lower Band for selected SMA Window."""
        return (self._get_sma() - 2 * self._get_std()).tail(self._sma_window)

    @functools.cache
    def _get_sma(self) -> pd.Series:
        return (
            self._data[self._ohlc][self._currency]
            .rolling(window=self._sma_window)
            .mean()
        )

    @functools.cache
    def _get_std(self) -> pd.Series:
        return (
            self._data[self._ohlc][self._currency]
            .rolling(window=self._sma_window)
            .std()
        )
