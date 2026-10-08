from logging import warning
from os import environ, getcwd

errorCount = int(0)

dataFile = f"{str(environ.get('DATA_PATH') or getcwd())}/inventory.txt"

def load_inventory() -> list[list]:
    try:
        with open(dataFile, 'r') as file:
            return [line.strip().split(',') for line in file]
    except FileNotFoundError:
        return []

def save_inventory(newItem: list) -> None:
    with open(dataFile, 'a') as file:
        file.write(','.join(str(i) for i in newItem) + "\n")

def warnUser(message: str) -> None:
    global errorCount
    warning(message)
    errorCount += 1

def get_value_input(idCurrent) -> list:
    userNameInput = input("Enter product name: ")
    if userNameInput == "quit":
        return [0, "quit", int(0)]
    if "," in userNameInput:
        warnUser(f"\nName cannot have a comma ',' in it, try again!\n")
        return[0, str(""), int(0)]
    userQuantityInput = input("Enter a stock quantity: ")
    if userQuantityInput == "quit":
        return [0, "quit", int(0)]
    try:
        addedInventory = int(userQuantityInput)
        if addedInventory <= 0:
            warnUser("\nNegative number not accepted, try again!\n")
            return [0, str(""), int(0)]
        else:
            return [int(idCurrent)+1, str(userNameInput), int(addedInventory)]
    except:
        warnUser(f"Input of type {str(type(userQuantityInput))} not accepted, try again!")
        return [0, str(""), int(0)]

def process_delivery(current_total, new_value: int) -> int:
    new_total = int(sum(current_total)) + int(new_value)
    return new_total

def calculate_tax(amount: int) -> float:
    return (float(0.1) * amount)

def generate_report(total_units, failed_attempts: int) -> None:
    print(f"Total Units Processed: {str(total_units)}")
    print(f"Number of Failed/Rejected Entries: {str(failed_attempts)}")

inventory = load_inventory()
newInventory = []
print("Current Orders:")
print("")
for i in inventory:
    print(i)
print("")

userData = ""
while userData != "quit":
    try:
        currentId = max([i[0] for i in inventory])
    except ValueError:
        currentId = 1000
    try:
        currentId = max([i[0] for i in newInventory])
    except:
        currentId = currentId
    userData = get_value_input(currentId)
    if userData[1] == "quit":
        print("Goodbye!")
        break
    if int(userData[2]) > 0:
        # inventory = process_delivery([i[2] for i in inventory if len(i)>2 and i[1]==userData[1]], int(userData[2]))
        print(f"\nTax for delivery amount {int(userData[2])}: {calculate_tax(int(userData[2]))}\n")
        newInventory.append(userData)
        print("New Order Added:")
        print(str(userData))
        print("")
        save_inventory(userData)
        print("Order successfully saved to inventory.txt\n")
    # it doesn't make sense that the program should be blocked if the inventory is more than 500, especially since history is now persistent. if persistent inventory is forever above 500, the program will always quit after 1 user prompt.
    # if inventory > 500:
    #     print("Inventory has overstocked!")
    #     break
generate_report(inventory+newInventory, errorCount)
