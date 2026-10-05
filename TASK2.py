# Simple Stock Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

total_investment = 0
portfolio = []

print("===== STOCK TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    portfolio.append(
        f"{stock} - Quantity: {quantity}, "
        f"Price: ${price}, Investment: ${investment}"
    )

    print(f"Investment for {stock}: ${investment}")

# Display results
print("\n===== PORTFOLIO =====")

for item in portfolio:
    print(item)

print("----------------------")
print(f"Total Investment: ${total_investment}")

# Optional: Save result to a text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("stock_tracker.txt", "w") as file:
        file.write("===== STOCK TRACKER =====\n")

        for item in portfolio:
            file.write(item + "\n")

        file.write("----------------------\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("Result saved to stock_tracker.txt")