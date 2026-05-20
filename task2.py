# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 145
}

portfolio = {}
total_investment = 0

print(" Welcome to Stock Portfolio Tracker")
print("Available Stocks and Prices:")

# Display stock prices
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# Number of stocks user wants to enter
n = int(input("\nHow many different stocks do you want to add? "))

# Taking user input
for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()

    # Check if stock exists
    if stock_name in stock_prices:

        quantity = int(input(f"Enter quantity of {stock_name}: "))

        # Calculate investment
        investment = stock_prices[stock_name] * quantity

        # Store in portfolio
        portfolio[stock_name] = {
            "quantity": quantity,
            "price": stock_prices[stock_name],
            "investment": investment
        }

        # Add to total
        total_investment += investment

    else:
        print(" Stock not available in tracker.")

# Display Portfolio Summary
print("\n Portfolio Summary ")

for stock, details in portfolio.items():
    print(f"\nStock: {stock}")
    print(f"Price per Share: ${details['price']}")
    print(f"Quantity: {details['quantity']}")
    print(f"Investment Value: ${details['investment']}")

print("\n")
print(f" Total Investment Value: ${total_investment}")

# Optional: Save result to a text file
save = input("\nDo you want to save the report to a file? (yes/no): ").lower()

if save == "yes":

    with open("portfolio_report.txt", "w") as file:

        file.write(" STOCK PORTFOLIO REPORT\n\n")

        for stock, details in portfolio.items():
            file.write(f"Stock: {stock}\n")
            file.write(f"Price: ${details['price']}\n")
            file.write(f"Quantity: {details['quantity']}\n")
            file.write(f"Investment: ${details['investment']}\n\n")

        file.write(f"Total Investment Value: ${total_investment}")

    print(" Report saved as 'portfolio_report.txt'")

else:
    print(" Report not saved.")