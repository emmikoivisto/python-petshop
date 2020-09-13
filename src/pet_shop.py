# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_dictionary):
    return pet_shop_dictionary["name"]


def get_total_cash(sum_of_cash):
    return sum_of_cash["admin"]["total_cash"]


def add_or_remove_cash(total, num1):
    total["admin"]["total_cash"] += num1


def get_pets_sold(sold_pets):
    return sold_pets["admin"]["pets_sold"]


def increase_pets_sold(current_number, sold_pets):
    current_number["admin"]["pets_sold"] += sold_pets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pet_list = []
    for pet_breed in pet_shop["pets"]:
        if pet_breed["breed"] == breed:
            pet_list.append(pet_breed)
    return pet_list


def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

#doesn't work
def remove_pet_by_name(pet_shop, name):
    pet_list = []
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_list.remove(name)

def add_pet_to_stock(pet_shop, new_pet):
    pet_list = []
    for pet in pet_shop["pet"]:
        pet_list.append(new_pet)