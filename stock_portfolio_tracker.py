import os

print("Welcome to Stock Portfolio Tracker!")
print("Here are some available stocks:\n")

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

# Display available stocks
for stock, price in stock_prices.items():
    print(f"{stock} = ${price}")

print("\nType 'done' when you are finished.\n")

portfolio = {}

while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    elif stock not in stock_prices:
        print("Stock not found! Try one from the list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Quantity should be more than zero.")
            continue
    except ValueError:
        print("Enter a valid number for quantity.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print(f"Added {quantity} shares of {stock}.\n")

# Display summary
print("\n------ Portfolio Summary ------")
total_value = 0
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    print(f"{stock}: {quantity} shares @ ${price} each")
    total_value += price * quantity

print(f"\nTotal Investment Value = ${total_value}")

# Ask user to save
save = input("\nSave summary to file? (yes/no): ").lower()

if save == "yes" or save == "y":
    # File will be saved exactly in D:\Internship work\
    file_path = r"D:\Internship work\portfolio.txt"
    with open(file_path, "w") as file:
        file.write("Your Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            file.write(f"{stock}: {quantity} shares @ ${price} each\n")
        file.write(f"\nTotal = ${total_value}\n")

    print("\n✅ Portfolio saved successfully!")
    print("📂 File location:", file_path)
else:
    print("\nFile not saved.")

print("\nThanks for using this tracker!")
