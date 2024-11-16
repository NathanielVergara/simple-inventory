from datetime import datetime

inventory = {}
transactions = []  # To track transactions

# Prices
dealer_price = 550
retail_price = 600

def add_item():
    item = input("Enter item name: ").capitalize()
    quantity = int(input("Enter item quantity: "))
    if item in inventory:
        inventory[item]['stock'] += quantity
    else:
        inventory[item] = {'stock': quantity, 'dealer_price': dealer_price, 'retail_price': retail_price}
    print(f"{quantity} {item}(s) added to inventory.\n")

def remove_item():
    item = input("Enter item name to remove: ").capitalize()
    if item in inventory:
        quantity = int(input("Enter quantity to remove: "))
        if quantity >= inventory[item]['stock']:
            del inventory[item]
            print(f"All {item}(s) removed from inventory.\n")
        else:
            inventory[item]['stock'] -= quantity
            print(f"{quantity} {item}(s) removed from inventory.\n")
    else:
        print(f"{item} is not in the inventory.\n")

def view_inventory():
    if inventory:
        print("\nInventory:")
        for item, data in inventory.items():
            print(f"{item}: {data['stock']} in stock | Dealer Price: {data['dealer_price']} | Retail Price: {data['retail_price']}")
        print()
    else:
        print("Inventory is empty.\n")

def update_item():
    item = input("Enter item name to update: ").capitalize()
    if item in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[item]['stock'] = quantity
        print(f"{item} quantity updated to {quantity}.\n")
    else:
        print(f"{item} is not in the inventory.\n")

def record_transaction():
    date_time = datetime.now()
    date = date_time.strftime("%b %d")
    time = date_time.strftime("%H:%M")
    order_name = input("Enter order name: ").capitalize()
    item = input("Enter item name: ").capitalize()
    
    if item not in inventory:
        print(f"{item} is not in inventory.")
        return

    in_quantity = int(input("Enter quantity coming in: "))
    out_quantity = int(input("Enter quantity going out: "))
    mode_of_payment = input("Enter mode of payment: ").capitalize()
    paid_status = input("Enter payment status (Paid/Not Paid): ").capitalize()
    
    # Calculate total cost based on the quantities
    dealer_out = out_quantity * dealer_price
    retail_out = out_quantity * retail_price
    not_paid_dealer = dealer_out if paid_status == "Not Paid" else 0
    not_paid_retail = retail_out if paid_status == "Not Paid" else 0

    # Update inventory
    inventory[item]['stock'] += in_quantity - out_quantity

    # Save transaction details
    transaction = {
        "date": date,
        "time": time,
        "order_name": order_name,
        "in": in_quantity,
        "out": out_quantity,
        "stock": inventory[item]['stock'],
        "mode_of_payment": mode_of_payment,
        "dealer_out": dealer_out,
        "retail_out": retail_out,
        "not_paid_dealer": not_paid_dealer,
        "not_paid_retail": not_paid_retail,
        "paid_status": paid_status,
        "total_dealer": dealer_out,
        "total_retail": retail_out,
        "total_stocks": inventory[item]['stock'],
        "total_in": in_quantity
    }

    transactions.append(transaction)
    print(f"Transaction recorded successfully: {order_name}, {item}, {in_quantity} in, {out_quantity} out.\n")

def view_transactions():
    if transactions:
        print("\nTransactions:")
        for t in transactions:
            print(f"DATE: {t['date']} | TIME: {t['time']} | ORDER NAME: {t['order_name']} | "
                  f"IN: {t['in']} | OUT: {t['out']} | STOCKS: {t['stock']} | "
                  f"DEALERS OUT: {t['dealer_out']} | RETAIL OUT: {t['retail_out']} | "
                  f"NOT PAID DEALER: {t['not_paid_dealer']} | NOT PAID RETAIL: {t['not_paid_retail']} | "
                  f"PAID STATUS: {t['paid_status']} | TOTAL DEALERS: {t['total_dealer']} | "
                  f"TOTAL RETAIL: {t['total_retail']} | TOTAL STOCKS: {t['total_stocks']} | TOTAL IN: {t['total_in']}")
        print()
    else:
        print("No transactions recorded.\n")

# Main loop
while True:
    print("Simple Inventory System")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Inventory")
    print("4. Update Item Quantity")
    print("5. Record Transaction")
    print("6. View Transactions")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_inventory()
    elif choice == '4':
        update_item()
    elif choice == '5':
        record_transaction()
    elif choice == '6':
        view_transactions()
    elif choice == '7':
        print("Exiting Inventory System.")
        break
    else:
        print("Invalid choice. Please try again.\n")
