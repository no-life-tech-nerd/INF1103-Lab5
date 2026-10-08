from logging import warning
from os import environ, getcwd

errorCount = int(0)

dataFile = f"{str(environ.get('DATA_PATH') or getcwd())}/inventory.json"

inventory: list[dict] = []

def warnUser(message: str) -> None:
    global errorCount
    warning(message)
    errorCount += 1

def int_input(message: str) -> int:
    while True:
        try:
            return int(input(message))
        except ValueError:
            warnUser("\nInput must be an integer, try again!\n")

def display_all() -> None:
    print("Current Inventory")
    print("-----------------")

    # try:
    for product in inventory:
        print(f"ID: {product["prodId"]} | Name: {product["name"]} | Price: ${round(product["price"], 2)} | Stock: {product["stock"]}")
    # except:
    #     print("No products in inventory to display!")

    print("-----------------")

def add_product() -> None:
    print("Add New Product")
    print("---------------")
    prodId = int_input("Enter product ID: ")
    name = input("Enter product name: ")
    try:
        price = round(float(input("Enter product price: ")), 2)
    except ValueError:
        warnUser("\nInput must be a float of up to 2 decimal places, try again!\n")
        return
    stock = int_input("Enter stock quantity: ")

    for product in inventory:
        if prodId == product["prodId"]:
            warnUser("\nThis product ID already exists, try again!\n")
            return
        elif name == product["name"]:
            warnUser("\nThis product name already exists, try again!\n")
            return

    try:
        inventory.append({"prodId": prodId, "name": name, "price": price, "stock": stock})
        print("\nProduct added successfully!\n")
        return
    except:
        print("\nUnknown error adding new product to inventory, try again!\n")
        return

def update_stock() -> None:
    print("Update Stock")
    print("------------")
    prodId = int_input("Enter product ID: ")
    for product in inventory:
        if prodId == product["prodId"]:
            print(f"\nProduct found:\nName: {product["name"]}\nCurrent Stock: {product["stock"]}\n")
            new_stock = int_input("New Stock Quantity: ")
            product["stock"] = new_stock
            return
    print("Product not found.")

def search_product() -> None:
    print("Search Product")
    print("--------------")
    prodId = int_input("Enter product ID: ")
    for product in inventory:
        if prodId == product["prodId"]:
            print(f"\nProduct found:\nID: {product["prodId"]}\nName: {product["name"]}\nPrice: {product["price"]}\nCurrent Stock: {product["stock"]}\n")
            return
    print("Product not found.")

