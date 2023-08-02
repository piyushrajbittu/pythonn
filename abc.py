from forex_python.converter import CurrencyRates

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the source currency: ").upper()
        to_currency = input("Enter the target currency: ").upper()

        converted_amount = currency_converter(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

    except ValueError:
        print("Please enter a valid amount.")
    except Exception as e:
        print("An error occurred:", e)
