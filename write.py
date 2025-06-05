import datetime

def save_products(products, filename='products.txt'):
    """Saves product data to a text file."""
    try:
        with open(filename, 'w') as file:
            for product in products:
                file.write(f"{product['name']}, {product['brand']}, {product['quantity']}, {product['cost_price']}, {product['country']}\n")
        print("Product data saved successfully.")
    except Exception as e:
        print(f"Error saving product data: {e}")

def generate_new_product_invoice(new_product, invoice_dir="invoices"):
    """Generates and saves an invoice for a new product addition."""
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    invoice_number = f"NP-{now.strftime('%Y%m%d')}-{now.strftime('%H%M%S')}"
    
    try:
        lines = []
        # Header
        lines.append("+--------------------------------------------------+\n")
        lines.append("|              WeCare Wholesale Skincare           |\n")
        lines.append("|              Buddha chowk,Dharan                 |\n")
        lines.append("|              Phone: 9800928901                   |\n")
        lines.append("|                     025 590987                   |\n")
        lines.append("|              Email: inventory@wecare.com         |\n")
        lines.append("+--------------------------------------------------+\n\n")
        
        # Invoice Details
        lines.append(f"New Product Addition Record: {invoice_number}\n")
        lines.append(f"Date: {timestamp}\n")
        lines.append("+--------------------------------------------------+\n")
        
        # Product Details Header
        lines.append("| Product Details                                |\n")
        lines.append("+--------------------------------------------------+\n")
        lines.append(f"| Name: {new_product['name']:<40} |\n")
        lines.append(f"| Brand: {new_product['brand']:<39} |\n")
        lines.append(f"| Country of Origin: {new_product['country']:<30} |\n")
        lines.append("+--------------------------------------------------+\n")
        
        # Inventory Details
        lines.append("| Inventory Details                              |\n")
        lines.append("+--------------------------------------------------+\n")
        lines.append(f"| Initial Quantity: {new_product['quantity']:<35} |\n")
        lines.append(f"| Cost Price per Unit: ${new_product['cost_price']:<33.2f} |\n")
        total_value = new_product['quantity'] * new_product['cost_price']
        lines.append(f"| Total Inventory Value: ${total_value:<30.2f} |\n")
        lines.append("+--------------------------------------------------+\n")
        
        # Notes
        lines.append("\nNotes:\n")
        lines.append("- This is a new product addition to inventory\n")
        lines.append("- Product has been added to the system\n")
        lines.append("- Initial stock has been recorded\n\n")
        
        # Footer
        lines.append("Thank you for updating our inventory!\n")
        lines.append("For any queries, please contact our inventory department.\n")
        lines.append("+--------------------------------------------------+\n")

        # Store the complete invoice content
        invoice_content = ''.join(lines)
        
        # Write to file and print to console
        with open(f"{invoice_dir}/{invoice_number}.txt", 'w') as file:
            file.write(invoice_content)
        
        print("\n" + "="*50)
        print("NEW PRODUCT INVOICE GENERATED")
        print("="*50)
        print(invoice_content)
        print("="*50)
        print(f"New product invoice saved as '{invoice_number}.txt'\n")
        
        return invoice_content
    except Exception as e:
        print(f"Error saving new product invoice: {e}")
        return None

def generate_invoice(customer_name, purchased_items, total_amount, invoice_dir="invoices"):
    """Generates and saves a sales invoice."""
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    invoice_number = f"INV-{now.strftime('%Y%m%d')}-{now.strftime('%H%M%S')}"
    
    try:
        lines = []
        # Header
        lines.append("+--------------------------------------------------+\n")
        lines.append("|              WeCare Wholesale Skincare           |\n")
        lines.append("|              Buddha chowk,Dharan                 |\n")
        lines.append("|              Phone: 9800928901                   |\n")
        lines.append("|                     025 590987                   |\n")
        lines.append("|              Email: inventory@wecare.com         |\n")
        lines.append("+--------------------------------------------------+\n\n")
        
        # Invoice Details
        lines.append(f"Invoice Number: {invoice_number}\n")
        lines.append(f"Date: {timestamp}\n")
        lines.append(f"Customer: {customer_name}\n")
        lines.append("+--------------------------------------------------+\n")
        
        # Items Header
        lines.append("| Product              | Qty  | Free | Price    | Total    |\n")
        lines.append("+----------------------+------+------+----------+----------+\n")

        # Items
        subtotal = 0
        for item in purchased_items:
            # Calculate free items (1 free for every 3 items)
            free_quantity = item['quantity'] // 3
            # Calculate price for paid items only
            paid_quantity = item['quantity'] - free_quantity
            price = item['selling_price'] * paid_quantity
            subtotal += price
            
            # Add item to invoice
            lines.append(f"| {item['name']:<20} | {item['quantity']:<4} | {free_quantity:<4} | ${item['selling_price']:<8.2f} | ${price:<8.2f} |\n")

        # Calculate tax (assuming 20% VAT)
        tax_rate = 0.20
        tax_amount = subtotal * tax_rate
        total_with_tax = subtotal + tax_amount

        # Summary
        lines.append("+----------------------+------+------+----------+----------+\n")
        lines.append(f"| Subtotal: {'':<30} | ${subtotal:<8.2f} |\n")
        lines.append(f"| VAT (20%): {'':<30} | ${tax_amount:<8.2f} |\n")
        lines.append(f"| Total Amount: {'':<27} | ${total_with_tax:<8.2f} |\n")
        lines.append("+--------------------------------------------------+\n")
        
        # Payment Terms
        lines.append("\nPayment Terms:\n")
        lines.append("- Payment is due within 10 days\n")
        lines.append("- Please include invoice number in your payment reference\n")
        lines.append("- Bank details will be provided separately\n\n")
        
        # Promotion Details
        lines.append("\nPromotion Applied:\n")
        lines.append("- Buy 3 Get 1 Free on all products\n")
        lines.append("- Free items are automatically calculated\n\n")
        
        # Footer
        lines.append("Thank you for shopping with WeCare!\n")
        lines.append("For any queries, please contact our customer service.\n")
        lines.append("+--------------------------------------------------+\n")

        # Store the complete invoice content
        invoice_content = ''.join(lines)
        
        # Write to file and print to console
        with open(f"{invoice_dir}/{invoice_number}.txt", 'w') as file:
            file.write(invoice_content)
        
        print("\n" + "="*50)
        print("SALES INVOICE GENERATED")
        print("="*50)
        print(invoice_content)
        print("="*50)
        print(f"Invoice saved as '{invoice_number}.txt'\n")
        
        return invoice_content
    except Exception as e:
        print(f"Error saving invoice: {e}")
        return None

def generate_restock_invoice(restocked_items, vendor_name, total_amount, invoice_dir="invoices"):
    """Generates and saves a restock invoice."""
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    invoice_number = f"PO-{now.strftime('%Y%m%d')}-{now.strftime('%H%M%S')}"
    
    try:
        lines = []
        # Header
        lines.append("+--------------------------------------------------+\n")
        lines.append("|              WeCare Wholesale Skincare           |\n")
        lines.append("|              Buddha chowk,Dharan                 |\n")
        lines.append("|              Phone: 9800928901                   |\n")
        lines.append("|                     025 590987                   |\n")
        lines.append("|              Email: inventory@wecare.com         |\n")
        lines.append("+--------------------------------------------------+\n\n")
        
        # Invoice Details
        lines.append(f"Purchase Order Number: {invoice_number}\n")
        lines.append(f"Date: {timestamp}\n")
        lines.append(f"Vendor: {vendor_name}\n")
        lines.append("+--------------------------------------------------+\n")
        
        # Items Header
        lines.append("| Product              | Qty  | Cost      | Total    |\n")
        lines.append("+----------------------+------+-----------+----------+\n")

        # Items
        subtotal = 0
        for item in restocked_items:
            item_total = item['quantity'] * item['cost_price']
            subtotal += item_total
            lines.append(f"| {item['name']:<20} | {item['quantity']:<4} | ${item['cost_price']:<9.2f} | ${item_total:<8.2f} |\n")

        # Summary
        lines.append("+----------------------+------+-----------+----------+\n")
        lines.append(f"| Subtotal: {'':<30} | ${subtotal:<8.2f} |\n")
        lines.append(f"| Total Amount: {'':<27} | ${total_amount:<8.2f} |\n")
        lines.append("+--------------------------------------------------+\n")
        
        # Terms
        lines.append("\nTerms and Conditions:\n")
        lines.append("- All items must be in new condition\n")
        lines.append("- Delivery expected within 7 business days\n")
        lines.append("- Payment terms: Net 10\n\n")
        
        # Footer
        lines.append(f"Thank you for your supply, {vendor_name}!\n")
        lines.append("For any queries, please contact our procurement department.\n")
        lines.append("+--------------------------------------------------+\n")

        # Store the complete invoice content
        invoice_content = ''.join(lines)
        
        # Write to file and print to console
        with open(f"{invoice_dir}/{invoice_number}.txt", 'w') as file:
            file.write(invoice_content)
        
        print("\n" + "="*50)
        print("RESTOCK INVOICE GENERATED")
        print("="*50)
        print(invoice_content)
        print("="*50)
        print(f"Restock invoice saved as '{invoice_number}.txt'\n")
        
        return invoice_content
    except Exception as e:
        print(f"Error saving restock invoice: {e}")
        return None
    
if __name__ == "__main__":
    from main import main
    main()
