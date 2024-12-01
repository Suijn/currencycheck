import pandas as pd
import pendulum

from src.currencycheck.adapters.ports import CurrencyAdapterInterface
from src.currencycheck.domain.models import OHLC, CurrencyStock
from tests.factories import get_test_currency_data, get_test_index


class FakeCurrencyAdapter(CurrencyAdapterInterface):
    def __init__(self, currency_data: pd.DataFrame | None = None):
        if currency_data is None:
            self._currency_data = pd.DataFrame(
                {(OHLC.close, CurrencyStock.eurusd): get_test_currency_data()},
                index=get_test_index(),
            )
        else:
            self._currency_data = currency_data

    def get_currency_hist(
        self,
        currency: CurrencyStock,
        start: pendulum.Date,
        end: pendulum.Date,
    ) -> pd.DataFrame:
        return self._currency_data
