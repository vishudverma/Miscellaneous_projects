"""
using this api to fetch the current currency conversion rates:
    {https://app.exchangerate-api.com/dashboard/confirmed}
    This API requires the use of a base currency to fetch the relative data. Keep this in mind when calling the key.
"""

import requests

BASE_URL = "https://v6.exchangerate-api.com/"


def get_api_key() -> str:
    file = open("conversion_api.txt", "r")
    key_str = file.read()
    file.close()
    return key_str.rstrip()


API_KEY = get_api_key()


def get_currencies(base_currency="USD"):
    endpoint = f"v6/{API_KEY}/latest/{base_currency}"
    url = BASE_URL + endpoint
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return data["conversion_rates"]
    # Using the conversion rates key of the API key
    # This gives the individual rates for conversion


def exchange_rate(currency1: str, currency2: str) -> int:
    rates = get_currencies(currency1)
    rates = dict(rates)  # converting to dictionary for usage and reference
    if currency2 not in rates.keys():
        return 0

    exchange = rates[currency2]
    return exchange


def convert(currency1: str, currency2: str, amount: float) -> float | None:
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:  # noqa: E722
        print("Invalid amount.")
        return
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount:.2f} {currency2}.")

    return round(converted_amount, 2)


def main():
    _ = convert("INR", "USD", 123456.01)


if __name__ == "__main__":
    main()
