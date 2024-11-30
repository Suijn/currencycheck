import pandas as pd
import pendulum
import yfinance as yf

from src.currencycheck.adapters.ports import CurrencyAdapterInterface
from src.currencycheck.domain.models import CurrencyStock


class CurrencyYFinanceAdapter(CurrencyAdapterInterface):
    def get_currency_hist(
        self,
        currency: CurrencyStock,
        start: pendulum.Date,
        end: pendulum.Date,
    ) -> pd.DataFrame:
        """Get historical data for currency."""
        date_format = "YYYY-MM-DD"
        data = yf.download(
            currency, start=start.format(date_format), end=end.format(date_format)
        )
        return data
