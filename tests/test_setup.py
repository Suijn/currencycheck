from src.currencycheck.entrypoints.dummy import dummy_entrypoint


def test_ok():
    assert dummy_entrypoint() is True
