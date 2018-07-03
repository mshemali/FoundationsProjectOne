####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750,
  

}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Zain Cupcakes"
signature_flavors = ['Zain','Coffee','jameel']
order_list = ['tea','coffee']


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    for i in menu:
        print (" - %s KWD %s " % ( i ,menu[i]))



def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for i in original_flavors:
        print (i)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for i in signature_flavors:
        print (i)
    # your code goes here!


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in signature_flavors: 
        return True
    elif order in original_flavors:
        return True
    elif order in menu:
        return True
    else:
        False
        



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    user_input = input ("What would you like to order? \n")

    while user_input.lower() != "exit":
        if is_valid_order(user_input):
            order_list.append(user_input)
        else:
            print("this is not a valid order")
        user_input = input("Anything else ?")

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return True
    else:
        return False


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for order in order_list:
        # if order in original_flavors:
        #     total += 2
        # elif order in signature_flavors:
        #     total += signature_price
        # elif order in menu:
        #     if order == "tea":
        #         total += 0.900
        #     elif order == "coffee":
        #         total += 1.00
        #     elif order == "bottled_water":
        #         total += 0.750
        for item in order_list:
            total += menu.get(item)
            print(item)
        print ("Your total is %s " % total)
    


    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
