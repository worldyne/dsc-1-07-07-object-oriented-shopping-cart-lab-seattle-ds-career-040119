class ShoppingCart:
    # write your code here
    def __init__(self, total=0,employee_discount=None,items = [],prices = []):
        self.total = total
        self.employee_discount = employee_discount
        self.items = items
    def add_item(self, name, price, quantity=1):
        self.items.append(name)
        self.total += quantity * price
        self.prices = []
        self.prices.append(price)
        return self.total
    def mean_item_price(self):
        return (self.total / len(self.items))

    def median_item_price(self):
        n = len(self.prices)
        if n < 1:
            return None
        elif n % 2 == 1:
            return sorted(self.prices)[n//2]
        else:
            return sum(sorted(self.prices)[n//2-1:n//2+1])/2.0

    def apply_discount(self):
        pass

    def void_last_item(self):
        pass
