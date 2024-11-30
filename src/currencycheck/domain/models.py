import enum


class CurrencyStock(enum.StrEnum):
    eurusd = "EURUSD=X"


class OHLC(enum.StrEnum):
    open = "Open"
    high = "High"
    low = "Low"
    close = "Close"
