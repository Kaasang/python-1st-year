
def load_products(filename='products.txt'):

    products = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    fields = [field.strip() for field in line.strip().split(',')]
                    if len(fields) != 5:
                        print(f"Skipping line with incorrect number of fields: {line.strip()}")
                        continue

                    name, brand, quantity, cost_price, country = fields
                    products.append({
                        "name": name,
                        "brand": brand,
                        "quantity": int(quantity),
                        "cost_price": float(cost_price),
                        "country": country
                    })
                except ValueError:
                    print(f"Skipping line due to invalid numeric data: {line.strip()}")
                except Exception as e:
                    print(f"Skipping line due to unexpected error: {e}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    return products

if __name__ == "__main__":
    from main import main
    main()
