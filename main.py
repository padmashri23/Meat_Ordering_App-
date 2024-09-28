#code:
class MeatItem:
    def __init__(self,name,price_per_kg):
        self.name = name
        self.price_per_kg=price_per_kg
class Order:
    def __init__(self):
        self.cart = {}
    def add_to_cart(self,meat_item,quantity):
        if meat_item.name in self.cart:
            self.cart[meat_item.name]['quantity']+=quantity

        else:
            self.cart[meat_item.name]={'price_per_kg':meat_item.price_per_kg,'quantity':quantity}
    def view_cart(self):
        if not self.cart:
            print("\nYour cart is empty.\n")
            return
        print("\nYour cart contains:")
        total_cost=0
        for item,details in self.cart.items():
            item_total=details['price_per_kg']*details['quantity']
            total_cost += item_total
            print(f"{item}-{details['quantity']}kg @ {details['price_per_kg']}/kg={item_total}total")
        print(f"\nTotal amount:{total_cost}\n")
    def checkout(self):
        self.view_cart()
        confirm=input("Proceed to Checkout?(yes/no):").strip().lower()
        if confirm == "yes":
            print("\nOrder placed successfully! Thanks for shopping.\n")
            self.cart.clear()
        else:
            print("\nOrder Cancelled.\n")
meat_menu= [
    MeatItem("Chicken",200.50),
    MeatItem("Beef",300.50),
    MeatItem("Lamb",700.50)

]   
def display_menu():  
    print("\n--- Meat Menu ---")
    for index, meat_item in enumerate(meat_menu,start=1):
        print(f"{index}.{meat_item.name}-{meat_item.price_per_kg}/kg")
    print()
def main():  
    order = Order()
    while True:
        print("Welcome to the Meat Ordering App")
        print("1.View meat menu")
        print("2.Add to cart")
        print("3.View cart")
        print("4.Checkout")
        print("5.Exit")
        choice = input("\nEnter your choice(1-5): ").strip()
        if choice == "1":
            display_menu()
        elif choice == "2":
            display_menu()
            try:
                meat_choice=int(input("Select the meat number to add to cart: "))
                if 1<=meat_choice<= len(meat_menu):
                    quantity = float(input(f"Enter quantity of { meat_menu[meat_choice-1].name}(in kg):"))
                    order.add_to_cart(meat_menu[meat_choice-1],quantity)
                    print(f"{quantity}kg of {meat_menu[meat_choice-1].name}added to cart.\n")
                else:
                    print("Invalid choice.Please try again.\n")
            except ValueError:
                print("Invalid input.Please enter a valid number.\n")
        elif choice == "3":
            order.view_cart()
        elif choice == "4":
            order.checkout()
        elif choice == "5":
            print("Thank you for using the app.Bye!")
            break  
        else:
            print("Invalid choice.Please select an option between 1 and 5.\n")
if __name__=="__main__":
    main()
