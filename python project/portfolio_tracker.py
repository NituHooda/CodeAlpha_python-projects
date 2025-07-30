import csv

# Hardcoded stock prices (in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "MSFT": 330,
    "AMZN": 140,
}

portfolio = {}

print("Welcome to the Stock Portfolio Tracker!")

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print(f"Stock '{stock}' not found in price list. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid quantity. Please enter a number.")

# Calculate total investment
total_value = 0
print("\nYour Stock Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: Save to CSV
save = input("\nDo you want to save your portfolio to a CSV file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio.csv", mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            writer.writerow([stock, qty, price, value])
        writer.writerow(["Total", "", "", total_value])
    print("Portfolio saved to 'portfolio.csv'.")


