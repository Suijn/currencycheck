import pendulum

from src.currencycheck.adapters.ports import CurrencyAdapterInterface
from src.currencycheck.domain.models import OHLC, BollingerBands, CurrencyStock
from src.currencycheck.services.models import BollingerBandsData


def get_bollinger_bands(
    currency_adapter: CurrencyAdapterInterface,
    currency: CurrencyStock,
    start: pendulum.Date,
    end: pendulum.Date,
    sma_window: int,
    ohlc: OHLC,
) -> BollingerBandsData:
    currency_hist_data = currency_adapter.get_currency_hist(
        currency=currency,
        start=start,
        end=end,
    )
    bollinger_bands = BollingerBands(
        currency_hist_data=currency_hist_data,
        sma_window=sma_window,
        ohlc=ohlc,
        currency=currency,
    )
    return BollingerBandsData(
        timeline=bollinger_bands.timeline,
        sma=bollinger_bands.sma,
        upper_band=bollinger_bands.upper_band,
        lower_band=bollinger_bands.lower_band,
    )
