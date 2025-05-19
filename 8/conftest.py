import pytest

@pytest.fixture(scope="function")
def dabe_uzytkownika():
    return({"imie": "jan", "nazwisko", "nowak")