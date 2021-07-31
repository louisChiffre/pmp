import requests
import datetime


def get_last_price(symbol="XBT"):
    p = requests.get(
        "https://www.bitmex.com/api/v1/quote/bucketed",
        params=dict(
            binSize="1m",
            symbol="XBT",
            reverse="false",
            startTime=(
                datetime.datetime.utcnow() - datetime.timedelta(seconds=10)
            ).strftime("%Y-%m-%dT%H:%M"),
            partial=True,
        ),
    ).json()[-1]
    return p


def format_price(x):
    return f'{x["bidPrice"]:,.2f}-{x["askPrice"]:,.2f} [UTC time: {x["timestamp"]}]'


def test_get_last_price():
    x = get_last_price()
    print(x)
    print(format_price(x))
