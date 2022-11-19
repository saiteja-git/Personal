from demonew import Restaurent

# table, counter, chair, customer
customer_entry  = int(input("Enter No of customer = "))
required_table = int(input("Enter the Table you want = "))
customer_order = input("Enter the order = ").split()

lst_menu = ["French Fries", "Chilli Cheese Toast", "Chilli Cheese Gralic Toast", "Garlic Bread", "Garlic Bread with Cheese"]

class Saiteja_Rest(Restaurent):

    def __init__(self, table, counter, chair, customer, food):
        super().__init__(table, counter, chair, customer)
        self.food = food

    def booking(self, coustomer_requirement):
        try:
            var = self.check_availability() - coustomer_requirement
            return var
        except Exception as e:
            return f"Sorry the avalabily of Table is Zero"
    
    def order_food(self, order_food):
        accept_order = []
        for i in range(len(order_food)):
            for k in range(len(lst_menu)):
                if order_food[i] in lst_menu[k]:
                    accept_order.append(lst_menu[k])
        return ",".join(([i for i in set(accept_order)]))

    def order_status(self, booking, order_food):
        table, order_s = self.booking(booking), self.order_food(order_food)
        if isinstance(self.booking(booking), int) and isinstance(self.order_food(order_food), str):
            if table <= -1:
                return f"The Table is not ready"
            return f"TABLE : {table} the order is ready {order_s}"
        else:
            return f"Sorry either Table or food is not ready"


objsaiteja = Saiteja_Rest(5, 1, 10, customer_entry, lst_menu)

print(objsaiteja.order_status(required_table, customer_order))

