# Burger shop assignment - Csilla Tepliczky, 30.10.2023 
class Burger():
    def __init__(self, amount):
        self.price = 10
        self.amount = amount

class Drink():
    def __init__(self, amount):
        self.small_price = 3
        self.large_price = 5
        self.amount = amount

class Side():
    def __init__(self, amount):
        self.fries_price = 5
        self.onion_price = 7
        self.amount = amount
    
class Combo():
    def __init__(self, amount):
        self.price = 22
        self.amount = amount
    
class Order:
    def __init__(self, name):
        self.total_price = 0
        self.order_items = []
        self.name = name
    
 
def take_order():
    name = input('Please enter your name: ')
    order = Order(name) 

    print(f"Welcome to Burger Shop, dear {order.name}!")
    
    while True:
        ans = input('Would you like to continue ordering? yes/no/cancel ')

        if ans == 'no':
            print(f'Your current order details are {order.order_items} and the total price is {order.total_price}$. Thank you for choosing Burger Shop!')
            break

        elif ans == 'cancel':
            print(f'Thank you for choosing Burger Shop, dear {order.name}, see you soon!')
            break

        elif ans == 'yes':
            choice = input("What would you like to order, burger, drink, side dish or a combo? ").lower()
            amount = int(input('Please enter required amount: '))

            if choice == 'burger':
                b = Burger(amount)
                order.total_price += b.price * b.amount
                order.order_items.append(f'Burger x {b.amount}, price: {b.price}$')

            elif choice == 'drink':
                d = Drink(amount)
                size = input('Would you like small or large? small/large ')
                if size == 'small':
                    order.total_price += d.small_price * d.amount
                    order.order_items.append(f'Small drinks x {d.amount}, price: {d.small_price}$')
                elif size == 'large':
                    order.total_price += d.large_price * d.amount
                    order.order_items.append(f'Large drinks x {d.amount}, price: {d.large_price}$')
                else:
                    print('Please input a valid choice.')

            elif choice == 'side dish':
                s = Side(amount)
                selection = input('Would you like onion rings or french fries? onion/fries ')
                if selection == 'onion':
                    order.total_price += s.onion_price * s.amount
                    order.order_items.append(f'Onion rings x {s.amount}, price: {s.onion_price}$')
                elif selection == 'fries':
                    order.total_price += s.fries_price * s.amount
                    order.order_items.append(f'French fries x {s.amount}, price: {s.fries_price}$')
                else:
                    print('Please input a valid choice.')

            elif choice == 'combo':
                c = Combo(amount)
                order.total_price += c.price * c.amount
                order.order_items.append(f'Side dish x {c.amount}, price: {c.price}$')

            else:
                print('Please input a valid choice.')

        else:
            print('Please input a valid choice.')


take_order()