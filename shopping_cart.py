class ShoppingCart:
    # write your code here
    def __init__(self, total=0,employee_discount=None,items = []):
      self.total = total
      self.employee_discount = employee_discount
      self.items = items
    def add_item(self, name, price, quantity=1):
       self.items.append(self.name)
       self.total += quantity * price

    def mean_item_price(self):
       pass

    def median_item_price(self):
        pass

    def apply_discount(self):
       pass

    def void_last_item(self):
        pass
