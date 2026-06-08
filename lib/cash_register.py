class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    # DISCOUNT PROPERTY
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    # METHODS
    def add_item(self, item, price, quantity):
        item_total = price * quantity

        self.total += item_total

        self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)

        self.previous_transactions.pop()

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()

        self.total -= last["price"] * last["quantity"]

        if last["item"] in self.items:
            self.items.remove(last["item"])