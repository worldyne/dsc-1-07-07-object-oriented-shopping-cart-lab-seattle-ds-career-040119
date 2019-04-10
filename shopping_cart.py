class ShoppingCart:
    # write your code here
    def __init__(self, total=0,employee_discount=None,items = [],prices = []):
      self.total = total
      self.employee_discount = employee_discount
      self.items = items
    def add_item(self, name, price, quantity=1):
       self.items.append(name)
       self.total += quantity * price
       self.prices = prices
       return self.total
    def mean_item_price(self):
        return total / len(items)

    def median_item_price(self):
        self.prices.median()

    def apply_discount(self):
        pass

    def void_last_item(self):
        pass
