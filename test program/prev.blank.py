def getNonBlankInput(message, error_message):

    x = input(message)
    while len(x.strip()) == 0:
        x = input(error_message)

    return x

def getValidIntegerInput(message, error_message):

    msg = message
    while(True):
        try: 
            x = int(input(msg))
            break
        except ValueError:
            msg = error_message

    return x

def orderFunction(): # The function which allows the customer to choose delivery or pickup
    global deliveryPickup
    global customerName
    global customerAddress
    global customerPhnum

    deliveryPickup = input("Please input delivery or pickup: d for delivery p for pickup")

    if deliveryPickup == "d": 
        customerName = getNonBlankInput("Please input your name: ", "Please input a valid name: ")
        customerAddress = getNonBlankInput("Please input your address: ", "Please input a valid address: ")
        customerPhnum = getValidIntegerInput("Please input your phone number: ", "Please input a valid phone number: ")
        print("There will also be a $3 delivery surcharge")
    elif deliveryPickup == "p": 
        customerName = getNonBlankInput("Please input your name: ", "Please input a valid name: ")
    else:
        print("Please ensure that you have chosen d for Delivery or p for Pickup")
        orderFunction()

orderFunction() 