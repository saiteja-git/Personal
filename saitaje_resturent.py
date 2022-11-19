from demonew import Restaurent

# table, counter, chair, customer
customer_entry  = int(input("Enter No of customer = "))
required_table = int(input("Enter the Table you want = "))

class Saiteja_Rest(Restaurent):
    
    def booking(self, coustomer_requirement):
        try:
            var = self.check_availability() - coustomer_requirement
            return f"The remaining Table : {var}"
        except Exception as e:
            return f"Sorry the avalabily of Table is Zero"
            
objsaiteja = Saiteja_Rest(5, 1, 10, customer_entry)
print(objsaiteja.booking(required_table))
