# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_dictionary):
    return pet_shop_dictionary["name"]


def get_total_cash(sum_of_cash):
    return sum_of_cash["admin"]["total_cash"]


def add_or_remove_cash(total, num1):
    total["admin"]["total_cash"] += num1


def get_pets_sold(sold_pets):
    return sold_pets["admin"]["pets_sold"]


#def get_stock_count(number_of_pets):
#    return len["cc_pet_shop"]

#def remove_pet_by_name(list, name_of_pet):
#  names_of_pets = []
#  for name in list:
#    if name["pets"]["name"] == name_of_pet:
#      names_of_pets.del(name)
#      print(names_of_pets)

