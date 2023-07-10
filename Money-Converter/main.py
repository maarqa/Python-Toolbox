import requests

API_KEY = "39d3bf720982f44839e9a954"  # Replace with your API key

def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    return data.get("conversion_rate")

def format_currency(amount, currency):
    symbols = {
        "USD": "$",
        "PKR": "₨",
        "GBP": "£",
        "INR": "₹",
        "CNY": "¥"
    }
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:.2f}"

def main():
    print("Currency Converter 💵")
    print("------------------")

    # Fetch latest exchange rates
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    response = requests.get(url)
    data = response.json()
    exchange_rates = data.get("conversion_rates")

    print("Real Time Currency Rates:")
    print(f"USD TO PKR: {exchange_rates.get('PKR')}")
    print(f"USD to GBP: {exchange_rates.get('GBP')}")
    print(f"USD TO INR: {exchange_rates.get('INR')}")
    print(f"USD TO CNY: {exchange_rates.get('CNY')}")
    print("------------------")

    choice = input("Choose the currency rates:\n"
                   "1. USD TO PKR\n"
                   "2. PKR TO USD\n"
                   "3. USD TO INR\n"
                   "4. INR TO USD\n"
                   "5. USD TO CNY\n"
                   "6. CNY TO USD\n"
                   "7. GBP TO USD\n"
                   "8. USD TO GBP\n"
                   "9. Other Rates\n"
                   "Enter your choice: ")

    if choice == "1":
        rate = exchange_rates.get("PKR")
        print("USD TO PKR:", format_currency(1, "USD"), "=", format_currency(rate, "PKR"))
    elif choice == "2":
        rate = get_exchange_rate("PKR", "USD")
        print("PKR TO USD:", format_currency(1, "PKR"), "=", format_currency(rate, "USD"))
    elif choice == "3":
        rate = exchange_rates.get("INR")
        print("USD TO INR:", format_currency(1, "USD"), "=", format_currency(rate, "INR"))
    elif choice == "4":
        rate = get_exchange_rate("INR", "USD")
        print("INR TO USD:", format_currency(1, "INR"), "=", format_currency(rate, "USD"))
    elif choice == "5":
        rate = exchange_rates.get("CNY")
        print("USD TO CNY:", format_currency(1, "USD"), "=", format_currency(rate, "CNY"))
    elif choice == "6":
        rate = get_exchange_rate("CNY", "USD")
        print("CNY TO USD:", format_currency(1, "CNY"), "=", format_currency(rate, "USD"))
    elif choice == "7":
        rate = get_exchange_rate("GBP", "USD")
        print("GBP TO USD:", format_currency(1, "GBP"), "=", format_currency(rate, "USD"))
    elif choice == "8":
        rate = get_exchange_rate("USD", "GBP")
        print("USD TO GBP:", format_currency(1, "USD"), "=", format_currency(rate, "GBP"))
    elif choice == "9":
        base_currency = input("Enter the base currency: ").upper()
        target_currency = input("Enter the target currency: ").upper()
        rate = get_exchange_rate(base_currency, target_currency)
        print(f"{base_currency} TO {target_currency}:", format_currency(1, base_currency), "=", format_currency(rate, target_currency))
    else:
        print("Invalid choice. Please try again.")


main()
