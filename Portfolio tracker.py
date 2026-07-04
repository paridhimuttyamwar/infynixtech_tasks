# -------------------------------
# Stock Portfolio Tracker
# -------------------------------

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 150
}

portfolio = {}
total_value = 0

print("========== Stock Portfolio Tracker ==========\n")

# Number of different stocks
n = int(input("How many different stocks do you own? "))

# Input stock details
for i in range(n):
    print(f"\nStock {i + 1}")

    stock = input("Enter Stock Name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter Quantity Purchased: "))
        portfolio[stock] = quantity
    else:
        print("This stock is not available in the price list.")

print("\n========== Portfolio Summary ==========\n")

# Display portfolio
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value

    print(f"Stock : {stock}")
    print(f"Price : ₹{price}")
    print(f"Quantity : {quantity}")
    print(f"Value : ₹{value}")
    print("-" * 30)

print(f"\nTotal Investment Value = ₹{total_value}")

# Save to file
choice = input("\nDo you want to save the portfolio? (yes/no): ").lower()

if choice == "yes":

    filename = input("Enter filename (example: portfolio.txt or portfolio.csv): ")

    with open(filename, "w", encoding="utf-8") as file:

        if filename.endswith(".csv"):
            file.write("Stock,Quantity,Price,Value\n")

            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity
                file.write(f"{stock},{quantity},{price},{value}\n")

            file.write(f"\nTotal Investment Value,{total_value}")

        else:
            file.write("========== Portfolio Summary ==========\n\n")

            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                value = price * quantity

                file.write(f"Stock : {stock}\n")
                file.write(f"Price : ₹{price}\n")
                file.write(f"Quantity : {quantity}\n")
                file.write(f"Value : ₹{value}\n")
                file.write("-" * 30 + "\n")

            file.write(f"\nTotal Investment Value = ₹{total_value}")

    print("\nPortfolio saved successfully!")

else:
    print("\nPortfolio was not saved.")