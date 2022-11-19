class Restaurent:
    
    def __init__(self, table, counter, chair, customer):
        self.table = table
        self.counter = counter
        self.chair = chair
        self.customer = customer

    def check_availability(self):
        """This function say's the Availability of chair"""
        try:
            no_of_chair = self.chair//self.table # this will give number of chair (2)
            check_table = self.customer//no_of_chair # this will give the number table remaiining"
            result = self.table - check_table
            if result > 0:
                return result
            else:
                return "Sorry wait for sometime till customer leave"
        except Exception as e:
            return f"{e}"

    def get_status_restaurent(self):
        return f"The Availability of Table in Restaurent {self.check_availability()}"