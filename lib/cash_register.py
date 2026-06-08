class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

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

    def add_item(self, item, price, quantity=1):
        # update total
        self.total += price * quantity

        # store each item per quantity (IMPORTANT FOR TESTS)
        self.items.extend([item] * quantity)

        # store transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        self.total -= self.total * (self.discount / 100)

        self.previous_transactions.pop()

    def void_last_transaction(self):
        if not self.previous_transactions:
            return

        last = self.previous_transactions.pop()

        self.total -= last["price"] * last["quantity"]

        # remove items correctly per quantity
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])