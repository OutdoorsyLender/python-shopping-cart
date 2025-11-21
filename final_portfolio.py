# Step 1
#Build Build the ItemToPurchase class with the following specifications:
class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")
# Step 2
# Build the ShoppingCart class with the following data attributes and related methods.
class ShoppingCart:
    # Parameterized constructor, which takes the customer name and date as parameters
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # Attributes
        # customer_name (string) - Initialized in default constructor to "none"
        self.customer_name = customer_name
        # current_date (string) - Initialized in default constructor to "January 1, 2020"
        self.current_date = current_date
        # cart_items (list)
        self.cart_items = []

    # Methods
    # add_item()
    # Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    def add_item(self, item):
        self.cart_items.append(item)

    # remove_item()
    # Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        # If item name cannot be found, output this message: Item not found in cart. Nothing removed.
        print("Item not found in cart. Nothing removed.")

    # modify_item()
    # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    def modify_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                # If item can be found (by name) in cart, check if parameter has default values for description, price, and quantity. If not, modify item in cart.
                if item.item_description != "none":
                    cart_item.item_description = item.item_description
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                return
        # If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
        print("Item not found in cart. Nothing modified.")

    # get_num_items_in_cart()
    # Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    # get_cost_of_cart()
    # Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    # print_total()
    # Outputs total of objects in cart.
    def print_total(self):
        # If cart is empty, output this message: SHOPPING CART IS EMPTY
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            print()
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart():.2f}")

    # print_descriptions()
    # Outputs each item's description.
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("\nItem Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

# Step 5: In the main section of your code, implement the print_menu() function.
# print_menu() has a ShoppingCart parameter and outputs a menu of options to manipulate the shopping cart.
def print_menu(cart):
    while True:
        # Each option is represented by a single character. Build and output the menu within the function.
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        # If an invalid character is entered, continue to prompt for a valid choice.
        choice = input("Choose an option: ")

        if choice == 'a':
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(name, description, price, quantity)
            cart.add_item(item)

        elif choice == 'r':
            name = input("Enter name of item to remove: ")
            cart.remove_item(name)

        elif choice == 'c':
            name = input("Enter the item name: ")
            quantity = int(input("Enter the new quantity: "))
            item = ItemToPurchase(name, "none", 0, quantity)
            cart.modify_item(item)

        # Step 6: Implement Output item's description menu option.
        elif choice == 'i':
            cart.print_descriptions()

        # Implement Output shopping cart menu option.
        elif choice == 'o':
            cart.print_total()

        elif choice == 'q':
            break

def main():
   
    # Step 7:
    # In the main section of your code, 
    # prompt the user for a customer's name and today's date. 
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    # Output the name and date. 
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    # Create an object of type ShoppingCart.
    cart = ShoppingCart(customer_name, current_date)
    # Call print_menu() in the main() function.
    print_menu(cart)

if __name__ == "__main__":
    main()