# WRITE YOUR FUNCTIONS HERE

# 1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# 2


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# 3 ,4


def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    return pet_shop["admin"]["total_cash"]

# 5


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# 6


def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] += num
    return pet_shop["admin"]["pets_sold"]

# 7


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


# 8 ,9
def get_pets_by_breed(pet_shop, br):
    pet = []
    for pets in pet_shop["pets"]:
        if pets["breed"] == br:
            pet.append(pets["breed"])

    return pet

# ** pathing:
# pet_Shop[“pet”][0][“name”] = “Sir Percy”


# 10,11
def find_pet_by_name(pet_shop, name):
    for pets in pet_shop["pets"]:
        if pets["name"] == name:
            return pets

# 12


def remove_pet_by_name(pet_shop, name):
    for pets in pet_shop["pets"]:
        if pets["name"] == name:
            return pet_shop["pets"].remove(pets)


# 13
def add_pet_to_stock(pet_shop, new_pet):
    pets = pet_shop["pets"].append(new_pet)
    return pets

# 13


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# 14


def get_customer_cash(customer):
    return customer["cash"]

# 15


def remove_customer_cash(customer, cash):
    customer["cash"] = customer["cash"] - cash
    return customer

# 16


def get_customer_pet_count(customer):
    return len(customer["pets"])

# 17


def add_pet_to_customer(customer, new_pet):
    return customer["pets"].append(new_pet)

# --- OPTIONAL ---

# 18 ,19 ,20


def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

# 21,22,23


def sell_pet_to_customer(pet_shop, pet, customer):


 
    # if get_customer_pet_count(customer) == len(customer["pets"]):
    #     pass

    # elif get_pets_sold(pet_shop) == pet_shop["admin"]["pets_sold"]:
    #     pass

    # elif get_customer_cash(customer) == customer["cash"]:
    #     pass

    # elif get_total_cash(pet_shop) == pet_shop["admin"]["total_cash"]:
    #     pass

    # correct answer as follow:
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)