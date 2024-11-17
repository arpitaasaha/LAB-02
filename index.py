def trading_agent(price, avg_price, stock_level):
    # Define thresholds
    discount_threshold = 0.20  # 20% discount
    critical_stock_level = 10  # Critical stock level
    minimum_order_quantity = 10  # Minimum quantity to order
    normal_order_quantity = 15  # Normal quantity to order

    # Calculate discounted price
    discounted_price = avg_price * (1 - discount_threshold)

    # Decision-making process
    if price < discounted_price and stock_level > critical_stock_level:
        tobuy = normal_order_quantity  # Buy more because of promotion
    elif stock_level <= critical_stock_level:
        tobuy = minimum_order_quantity  # Prioritize restocking
    else:
        tobuy = 0  # No need to order

    return tobuy


# Example usage
average_price = 60  # Average price of the smartphone
current_price = 500  # Current price of the smartphone
stock_level = 20  # Current stock level in the store

# Get the decision from the trading agent
order_quantity = trading_agent(current_price, average_price, stock_level)

# Print the result
if order_quantity > 0:
    print(f"The agent decides to order {order_quantity} units.")
else:
    print("The agent decides not to place an order.")
