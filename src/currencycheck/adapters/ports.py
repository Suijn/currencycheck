import abc
import typing

import pandas as pd
import pendulum

from src.currencycheck.domain.models import CurrencyStock


class CurrencyAdapterInterface(typing.Protocol):
    @abc.abstractmethod
    def get_currency_hist(
        self,
        currency: CurrencyStock,
        start: pendulum.Date,
        end: pendulum.Date,
    ) -> pd.DataFrame:
        raise NotImplementedError
