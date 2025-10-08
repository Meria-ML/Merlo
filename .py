def calculate_discount(price, discount_percent):
    """
    Calculate final price after applying discount if discount >= 20%.
    Otherwise, return original price.
    """
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price


def calculate_discount_prompt():
    """
    Prompt user to enter original price and discount percentage,
    then calculate and print final price or original price based on discount.
    """
    price = float(input("Enter original price: "))
    discount_percent = float(input("Enter discount percentage: "))
    
    final_price = calculate_discount(price, discount_percent)
    
    if discount_percent >= 20:
        print(f"Final price after applying discount: {final_price}")
    else:
        print(f"No discount applied. Original price: {price}")

# Example of running the prompt function
calculate_discount_prompt()