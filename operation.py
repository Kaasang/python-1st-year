def display_products(products):
    """Displays the available products in a formatted table."""
    if not products:
        print("No products to display.")
        return

    print("\nAvailable Products:")
    print("-" * 90)
    print(f"{'Product Name':<20} {'Brand':<15} {'Price':<10} {'Stock':<10}")
    print("-" * 90)

    for product in products:
        selling_price = product["cost_price"] * 2
        print(f"{product['name']:<20} {product['brand']:<15} {selling_price:<10.2f} {product['quantity']:<10}")

def add_new_product(products):
    """Adds a new product to the inventory."""
    name = input("Enter product name: ").strip()
    brand = input("Enter product brand: ").strip()

    if not name or not brand:  # Ensure valid input
        print("Product name and brand cannot be empty.")
        return None

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter a number.")

    while True:
        try:
            cost_price = float(input("Enter cost price: "))
            if cost_price < 0:
                print("Cost price cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid cost price. Please enter a number.")

    country = input("Enter country of origin: ").strip()

    # Create new product 
    new_product = {
        "name": name,
        "brand": brand,
        "quantity": quantity,
        "cost_price": cost_price,
        "country": country
    }

    products.append(new_product)
    print(f"Added new product: {new_product}")
    return new_product

def process_transaction(products, customer_name):
    """Processes a customer transaction, applying the 'buy three get one free' policy."""
    total_amount = 0
    purchased_items = []

    if not products:
        print("No products available.")
        return purchased_items, total_amount

    display_products(products)

    while True:
        item_name = input("\nEnter product name to purchase (or 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break

        product = next((p for p in products if p["name"].lower() == item_name.lower()), None)

        if not product:
            print("Product not found. Please try again.")
            continue

        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
                if product["quantity"] < quantity:
                    print(f"Insufficient stock. Only {product['quantity']} available.")
                    continue
                break
            except ValueError:
                print("Invalid quantity. Please enter a number.")

        free_quantity = quantity // 4  # Buy 3 get 1 free
        quantity_to_charge = quantity - free_quantity
        selling_price = product["cost_price"] * 2
        item_price = selling_price * quantity_to_charge

        total_amount += item_price
        product["quantity"] -= quantity

        purchased_items.append({
            "name": product["name"],
            "brand": product["brand"],
            "quantity": quantity,
            "selling_price": selling_price,
            "free_quantity": free_quantity
        })

        print(f"Added {quantity} {product['name']} to cart. {free_quantity} free. Price: {item_price:.2f}")

    return purchased_items, total_amount

def restock_products(products):
    """Processes a restock transaction."""
    restocked_items = []
    total_amount = 0

    display_products(products)

    while True:
        item_name = input("\nEnter product name to restock (or 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break

        product = next((p for p in products if p["name"].lower() == item_name.lower()), None)

        if not product:
            print("Product not found. Please try again.")
            continue

        while True:
            try:
                quantity = int(input("Enter quantity to restock: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
                break
            except ValueError:
                print("Invalid quantity. Please enter a number.")

        while True:
            try:
                cost_price = float(input("Enter the cost price per item: "))
                if cost_price <= 0:
                    print("Cost price must be positive.")
                    continue
                break
            except ValueError:
                print("Invalid cost price. Please enter a number.")

        vendor_name = input("Enter the vendor name: ").strip()

        item_price = cost_price * quantity
        total_amount += item_price

        product["quantity"] += quantity
        product["cost_price"] = cost_price  # Update cost price

        restocked_items.append({
            "name": product["name"],
            "brand": product["brand"],
            "quantity": quantity,
            "cost_price": cost_price
        })

        print(f"Restocked {quantity} {product['name']}. New stock: {product['quantity']}. New cost price: {cost_price:.2f}")

    return restocked_items, total_amount, vendor_name

if __name__ == "__main__":
    from main import main
    main()
