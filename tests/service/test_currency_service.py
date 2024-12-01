import pandas as pd
import pendulum
from pandas import DatetimeIndex

from src.currencycheck.domain.models import OHLC, CurrencyStock
from src.currencycheck.services.currency_service import get_bollinger_bands
from src.currencycheck.services.models import BollingerBandsData
from tests.factories import get_test_currency_data, get_test_index
from tests.fakes import FakeCurrencyAdapter


def test_get_bollinger_bands():
    test_index = get_test_index(
        [
            "2024-09-01",
            "2024-09-02",
            "2024-09-03",
            "2024-09-04",
            "2024-09-05",
            "2024-09-06",
            "2024-09-07",
            "2024-09-08",
            "2024-09-09",
            "2024-09-10",
            "2024-09-11",
            "2024-09-12",
            "2024-09-13",
            "2024-09-14",
            "2024-09-15",
            "2024-09-16",
            "2024-09-17",
            "2024-09-18",
            "2024-09-19",
            "2024-09-20",
            "2024-09-21",
            "2024-09-22",
            "2024-09-23",
            "2024-09-24",
            "2024-09-25",
            "2024-09-26",
            "2024-09-27",
            "2024-09-28",
            "2024-09-29",
            "2024-09-30",
            "2024-10-01",
            "2024-10-02",
            "2024-10-03",
            "2024-10-04",
            "2024-10-05",
            "2024-10-06",
            "2024-10-07",
            "2024-10-08",
            "2024-10-09",
            "2024-10-10",
            "2024-10-11",
            "2024-10-12",
            "2024-10-13",
            "2024-10-14",
            "2024-10-15",
            "2024-10-16",
            "2024-10-17",
            "2024-10-18",
            "2024-10-19",
            "2024-10-20",
            "2024-10-21",
            "2024-10-22",
            "2024-10-23",
            "2024-10-24",
            "2024-10-25",
            "2024-10-26",
            "2024-10-27",
            "2024-10-28",
            "2024-10-29",
            "2024-10-30",
            "2024-10-31",
            "2024-11-01",
            "2024-11-02",
            "2024-11-03",
            "2024-11-04",
            "2024-11-05",
            "2024-11-06",
            "2024-11-07",
            "2024-11-08",
            "2024-11-09",
            "2024-11-10",
            "2024-11-11",
            "2024-11-12",
            "2024-11-13",
            "2024-11-14",
            "2024-11-15",
            "2024-11-16",
            "2024-11-17",
            "2024-11-18",
            "2024-11-19",
            "2024-11-20",
            "2024-11-21",
            "2024-11-22",
            "2024-11-23",
            "2024-11-24",
            "2024-11-25",
            "2024-11-26",
            "2024-11-27",
            "2024-11-28",
            "2024-11-29",
            "2024-11-30",
            "2024-12-01",
        ],
        freq="D",
    )
    test_currency_data = get_test_currency_data(
        [
            1.6373403582449255,
            1.6163650224382693,
            1.7233279319062715,
            1.1180380318315306,
            1.254456741427385,
            1.602419662001673,
            1.6109544351038605,
            1.449494317312653,
            1.0260196163176483,
            1.3849596220713725,
            1.810919614928451,
            1.7767589088611573,
            1.0953562041354226,
            1.8864008582116187,
            1.7243215148008089,
            1.231730651767093,
            1.0526313812855683,
            1.795995638225791,
            1.6316272910369305,
            1.7162332645143135,
            1.2962884490010231,
            1.088317567605426,
            1.8457509526855498,
            1.6612913685163884,
            1.0505282772200404,
            1.2184088612101471,
            1.9424128223854198,
            1.1100086889491676,
            1.6108611324411028,
            1.933037813825882,
            1.4488728741665813,
            1.064059099444558,
            1.859982428023005,
            1.7114819454011156,
            1.2970991234735807,
            1.1041398616335014,
            1.6096379860464727,
            1.9053788199188286,
            1.3598961628967328,
            1.9024265979488209,
            1.8648254671918396,
            1.6139295867357955,
            1.247888547470362,
            1.3425085740596745,
            1.1163331627140831,
            1.600311178837102,
            1.784611184363135,
            1.739100193286009,
            1.8050399274959261,
            1.9692221045330407,
            1.118069674262609,
            1.6726860981494234,
            1.5489753555830483,
            1.78620324036178,
            1.4853459828390863,
            1.784397571656163,
            1.423431947798839,
            1.787619480009112,
            1.8629893208178476,
            1.0790248909307927,
            1.051215851621807,
            1.5561994935024814,
            1.6216356309434556,
            1.0592966794392782,
            1.3610184224096389,
            1.2843035102122249,
            1.4281468811530913,
            1.4939347532557457,
            1.9666213750749395,
            1.252006358398308,
            1.9659651266321156,
            1.589059662438458,
            1.0485419487350192,
            1.7336229206702471,
            1.4908856766154097,
            1.7851354719259638,
            1.0345703708696825,
            1.5173019608644949,
            1.041435225884217,
            1.9624926776495326,
            1.5905005811005624,
            1.499207206948741,
            1.0082074019569012,
            1.605564017719175,
            1.966690192247892,
            1.1659373918164007,
            1.1938096960545428,
            1.4864856049347361,
            1.4506440550594846,
            1.4036700975680416,
            1.6227093889808133,
            1.851653268157246,
        ]
    )
    test_currency_data = pd.DataFrame(
        {(OHLC.close, CurrencyStock.eurusd): test_currency_data}, index=test_index
    )
    bb_data = get_bollinger_bands(
        currency_adapter=FakeCurrencyAdapter(currency_data=test_currency_data),
        currency=CurrencyStock.eurusd,
        start=pendulum.Date(year=2023, month=9, day=1),
        end=pendulum.Date(year=2023, month=11, day=29),
        sma_window=30,
        ohlc=OHLC.close,
    )

    expected_bb_timeline = DatetimeIndex(
        [
            "2024-11-02",
            "2024-11-03",
            "2024-11-04",
            "2024-11-05",
            "2024-11-06",
            "2024-11-07",
            "2024-11-08",
            "2024-11-09",
            "2024-11-10",
            "2024-11-11",
            "2024-11-12",
            "2024-11-13",
            "2024-11-14",
            "2024-11-15",
            "2024-11-16",
            "2024-11-17",
            "2024-11-18",
            "2024-11-19",
            "2024-11-20",
            "2024-11-21",
            "2024-11-22",
            "2024-11-23",
            "2024-11-24",
            "2024-11-25",
            "2024-11-26",
            "2024-11-27",
            "2024-11-28",
            "2024-11-29",
            "2024-11-30",
            "2024-12-01",
        ],
        dtype="datetime64[ns]",
        freq="D",
    )
    expected_bb_sma = [
        1.5583874987494155,
        1.5366479898840208,
        1.5387786331818896,
        1.5447840881345138,
        1.5387343846380677,
        1.525019582415965,
        1.5452437561552383,
        1.5235630815035546,
        1.526934403484897,
        1.5261054060083192,
        1.519460519383808,
        1.532497664270827,
        1.544982748067538,
        1.5511435578371666,
        1.526142197387385,
        1.5187489229733344,
        1.4932954329196106,
        1.4930711186901604,
        1.508818815584759,
        1.5030361858780694,
        1.4850105874238646,
        1.4789892800024445,
        1.4950340869827379,
        1.4744187476547457,
        1.4667646725966026,
        1.45672687676079,
        1.4429820345688447,
        1.453803541456753,
        1.4728533260353864,
        1.4827017851905453,
    ]
    expected_bb_upper_band = [
        2.1215531826821783,
        2.1251415147373773,
        2.1241378750868463,
        2.1151976364704197,
        2.110150587746004,
        2.0795222114403606,
        2.1187575877614426,
        2.090340222336402,
        2.1032343676113965,
        2.101958922046147,
        2.112929610037051,
        2.127064426286763,
        2.118755164289025,
        2.131307699169284,
        2.1288795517578825,
        2.116094376612671,
        2.105063470559286,
        2.104121577051912,
        2.1040239117824777,
        2.0950156537126925,
        2.1035388971535323,
        2.0888410017347345,
        2.1303729686261046,
        2.1110397822629423,
        2.111393431570348,
        2.0899592636807514,
        2.0573444808364894,
        2.0528851704787634,
        2.0550704671524107,
        2.08053867262253,
    ]
    expected_bb_lower_band = [
        0.9952218148166527,
        0.9481544650306646,
        0.9534193912769329,
        0.9743705397986082,
        0.9673181815301314,
        0.9705169533915693,
        0.9717299245490343,
        0.9567859406707073,
        0.9506344393583978,
        0.9502518899704911,
        0.9259914287305652,
        0.9379309022548912,
        0.9712103318460509,
        0.9709794165050495,
        0.9234048430168874,
        0.9214034693339975,
        0.8815273952799353,
        0.8820206603284085,
        0.9136137193870405,
        0.9110567180434463,
        0.866482277694197,
        0.8691375582701546,
        0.8596952053393712,
        0.8377977130465488,
        0.822135913622857,
        0.8234944898408284,
        0.8286195883012001,
        0.8547219124347426,
        0.890636184918362,
        0.8848648977585608,
    ]

    expected_bb_sma_series = pd.Series(data=expected_bb_sma, index=expected_bb_timeline)
    expected_bb_upper_band_series = pd.Series(
        data=expected_bb_upper_band, index=expected_bb_timeline
    )
    expected_bb_lower_band_series = pd.Series(
        data=expected_bb_lower_band, index=expected_bb_timeline
    )

    expected_bb_data = BollingerBandsData(
        timeline=expected_bb_timeline,
        sma=expected_bb_sma_series,
        upper_band=expected_bb_upper_band_series,
        lower_band=expected_bb_lower_band_series,
    )
    assert expected_bb_data.timeline.equals(bb_data.timeline)
    assert expected_bb_data.sma.equals(bb_data.sma)
    assert expected_bb_data.upper_band.equals(bb_data.upper_band)
    assert expected_bb_data.lower_band.equals(bb_data.lower_band)
