class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------

#run the code
if __name__ == "__main__":
    list = ShoppingList()
    list.add("bananas", 10)
    list.add("apples", 5)
    list.add("pineapple", 1)

    print(list.number_of_items())
    print(list.item(1))
    print(list.amount(1))
    print(list.item(2))
    print(list.amount(2))

    #print(total_units(my_list))

    for i in range(1, list.number_of_items()+1):
        item = list.item(i)
        amount = list.amount(i)
        print(f"{item}: {amount} units")