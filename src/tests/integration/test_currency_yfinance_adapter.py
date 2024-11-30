import numpy as np
import pendulum
import vcr

from src.currencycheck.adapters.currency_yfinance_adapter import CurrencyYFinanceAdapter
from src.currencycheck.domain.models import CurrencyStock


@vcr.use_cassette("fixtures/yfinance_eur.yaml")
def test_get_currency_hist__eur():
    currency_adapter = CurrencyYFinanceAdapter()
    result = currency_adapter.get_currency_hist(
        currency=CurrencyStock.eurusd,
        start=pendulum.Date(year=2023, month=9, day=1),
        end=pendulum.Date(year=2023, month=11, day=29),
    )

    # Based on recorded API response.
    expected_data = [
        np.float64(1.0844104290008545),
        np.float64(1.07758629322052),
        np.float64(1.0794472694396973),
        np.float64(1.0726161003112793),
        np.float64(1.0724204778671265),
        np.float64(1.0697818994522095),
        np.float64(1.071811318397522),
        np.float64(1.0750375986099243),
        np.float64(1.075326681137085),
        np.float64(1.0734220743179321),
        np.float64(1.0637166500091553),
        np.float64(1.0668259859085083),
        np.float64(1.0692671537399292),
        np.float64(1.0682048797607422),
        np.float64(1.065303087234497),
        np.float64(1.0661548376083374),
        np.float64(1.0648492574691772),
        np.float64(1.0591648817062378),
        np.float64(1.0569483041763306),
        np.float64(1.0505305528640747),
        np.float64(1.0562450885772705),
        np.float64(1.0565240383148193),
        np.float64(1.0480751991271973),
        np.float64(1.0472300052642822),
        np.float64(1.0507071018218994),
        np.float64(1.0546631813049316),
        np.float64(1.056747317314148),
        np.float64(1.0578875541687012),
        np.float64(1.0604791641235352),
        np.float64(1.0624282360076904),
        np.float64(1.0536741018295288),
        np.float64(1.0521553754806519),
        np.float64(1.0554312467575073),
        np.float64(1.057305932044983),
        np.float64(1.053851842880249),
        np.float64(1.0586491823196411),
        np.float64(1.0589966773986816),
        np.float64(1.0669853687286377),
        np.float64(1.059535264968872),
        np.float64(1.056725025177002),
        np.float64(1.0564459562301636),
        np.float64(1.0562450885772705),
        np.float64(1.061503529548645),
        np.float64(1.0579099655151367),
        np.float64(1.05870521068573),
        np.float64(1.0619093179702759),
        np.float64(1.0732147693634033),
        np.float64(1.0721560716629028),
        np.float64(1.0696102380752563),
        np.float64(1.0710422992706299),
        np.float64(1.0667576789855957),
        np.float64(1.069015622138977),
        np.float64(1.0701825618743896),
        np.float64(1.0878314971923828),
        np.float64(1.0854581594467163),
        np.float64(1.0853756666183472),
        np.float64(1.090702772140503),
        np.float64(1.0945948362350464),
        np.float64(1.0918222665786743),
        np.float64(1.0890873670578003),
        np.float64(1.0906314849853516),
        np.float64(1.0940439701080322),
        np.float64(1.0958423614501953),
    ]
    returned_data = [val for val in result["Close"].values.flatten()]
    assert expected_data == returned_data
