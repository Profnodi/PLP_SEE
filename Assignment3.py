def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if applicable.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage
    
    Returns:
    float: Final price after discount (if discount is 20% or higher), otherwise original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Main program
def main():
    try:
        # Prompt user for input
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Calculate final price
        final_price = calculate_discount(original_price, discount_percentage)
        
        # Display results
        if discount_percentage >= 20:
            print(f"\nDiscount applied: {discount_percentage}%")
            print(f"Original price: ${original_price:.2f}")
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print(f"\nNo discount applied (discount must be 20% or higher)")
            print(f"Final price: ${final_price:.2f}")
            
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")

# Run the program
if __name__ == "__main__":
    main()