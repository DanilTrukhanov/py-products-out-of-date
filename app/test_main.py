import pytest
import datetime
from unittest import mock
from typing import Any

from app.main import outdated_products


@pytest.fixture()
def groceries() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@mock.patch("app.main.datetime")
def test_outdated_products_calls_datetime(
        mocked_today: Any,
        groceries: list[dict]
) -> None:
    mocked_today.date.today.return_value = datetime.date(2022, 2, 14)
    outdated_products(groceries)
    mocked_today.date.today.assert_called()


@mock.patch("app.main.datetime")
def test_all_products_expired(
        mocked_today: Any,
        groceries: list[dict]
) -> None:
    mocked_today.date.today.return_value = datetime.date(2022, 2, 14)
    result = outdated_products(groceries)
    assert result == ["salmon", "chicken", "duck"]


@mock.patch("app.main.datetime")
def test_one_product_expired(
        mocked_today: Any,
        groceries: list[dict]
) -> None:
    mocked_today.date.today.return_value = datetime.date(2022, 2, 4)
    result = outdated_products(groceries)
    assert result == ["duck"]
