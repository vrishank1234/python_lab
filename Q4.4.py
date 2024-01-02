#1. wap that has a class Store which keeps a record of code and price of each product. display the menu of all products to the user and prompt him to enter the quantity of each item required.and generate a bill and display total amount. 
class Store:
    def __init__(self):
        self.products = {} 

    def add_product(self, code, price):
        self.products[code] = price

    def display_menu(self):
        print("Product Menu:")
        for code, price in self.products.items():
            print(f"{code}: ${price}")

    def generate_bill(self, quantities):
        total_amount = 0
        print("\nYour Bill:")
        for code, quantity in quantities.items():
            if code in self.products:
                price = self.products[code]
                subtotal = price * quantity
                total_amount += subtotal
                print(f"{code}: {quantity} x Rs{price} = Rs{subtotal}")
            else:
                print(f"Invalid product code: {code}")
        print(f"\nTotal Amount: Rs{total_amount}")
def main():
    store = Store()
    store.add_product("001", 10.0)
    store.add_product("002", 20.0)
    store.add_product("003", 15.0)

    store.display_menu()

    quantities = {}
    print(""" PRODUCT CODE               PRICE
        001                Rs 10.0
        002                Rs 20.0
        003                Rs 15.0""")
    while True:
        code = input("Enter product code (or 'done' to finish): ")
        if code.lower() == 'done':
            break
        quantity = int(input(f"Enter quantity for product {code}: "))
        quantities[code] = quantity

    store.generate_bill(quantities)


if __name__ == "__main__":
    main()
