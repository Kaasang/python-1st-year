import read
import write
import operation

def validate_customer_name(name):
    """Validates that the customer name is a proper string and not a number."""
    try:
        # Check if name is empty or only whitespace
        if not name or not name.strip():
            raise ValueError("Customer name cannot be empty.")
        
        # Check if name contains only numbers
        if name.replace(" ", "").isdigit():
            raise ValueError("Customer name cannot be a number. Please enter a proper name.")
        
        # Check if name contains any special characters
        special_chars = "!@#$%^&*()_+{}[]|\\:;\"'<>,.?/~`"
        if any(char in special_chars for char in name):
            raise ValueError("Customer name cannot contain special characters.")
        
        # Check if name contains any digits
        if any(char.isdigit() for char in name):
            raise ValueError("Customer name cannot contain numbers.")
        
        return True
    except ValueError as e:
        print(f"Error: {str(e)}")
        return False

def main():
    products = read.load_products()
    if not products:
        print("No products loaded. Exiting.")
        return

    while True:
        print("\nWelcome to WeCare Wholesale Skincare!")
        print("1. Sell Products")
        print("2. Restock Products")
        print("3. View Products")
        print("4. Add New Product")  
        print("5. Exit")  

        choice = input("Enter your choice: ")
        print(f"You entered: '{choice}'")  

        if choice == '1':
            operation.display_products(products)
            while True:
                try:
                    customer_name = input("Enter customer name (or 'exit' to return to main menu): ").strip()
                    if customer_name.lower() == 'exit':
                        break
                    
                    if validate_customer_name(customer_name):
                        purchased_items, total_amount = operation.process_transaction(products, customer_name)
                        if purchased_items:
                            write.generate_invoice(customer_name, purchased_items, total_amount)
                            write.save_products(products)
                        else:
                            print("No items purchased.")
                        break
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
                    print("Please try again with a valid customer name.")

        elif choice == '2':
            restocked_items, total_amount, vendor_name = operation.restock_products(products)
            if restocked_items:
                write.generate_restock_invoice(restocked_items, vendor_name, total_amount)
                write.save_products(products)
            else:
                print("No items restocked.")

        elif choice == '3':
            operation.display_products(products)

        elif choice == '4':
            new_product = operation.add_new_product(products)
            if new_product:
                write.generate_new_product_invoice(new_product)
                write.save_products(products)
            else:
                print("No new product added.")

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
