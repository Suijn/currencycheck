import dataclasses

import pandas as pd


@dataclasses.dataclass(frozen=True)
class BollingerBandsData:
    timeline: pd.DatetimeIndex
    sma: pd.Series
    upper_band: pd.Series
    lower_band: pd.Series
