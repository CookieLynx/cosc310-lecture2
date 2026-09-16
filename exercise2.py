"""Exercise 2: A Cart class.

Implement Cart so the example at the bottom of this file behaves correctly.

  add_item(item, qty=1)  add an item; if it is already in the cart,
                         increase the quantity instead of adding a second line
  remove_item(item_id)   remove that item entirely
  clear()                empty the cart
  total()                sum of price * qty across all lines, rounded to 2dp
  __repr__()             something readable, e.g. <Cart 3 items, $27.75>

Store each line as a dictionary:
    {"item_id": 1, "name": "Tonkotsu Ramen", "price": 16.50, "qty": 2}
"""

from exercise1 import load_menu # what are we importing here? Food for thought.


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        # TODO
            
        #Check if in cart already
        for items in self.lines:
            if items["id"] == item["id"]:
                items["qty"] += qty
                return
        #is not in cart
        
        self.lines.append(item)
        #will always be last item since added to end
        self.lines[(len(self.lines) - 1)]["qty"] = qty
        




    def remove_item(self, item_id: int) -> None:
        # TODO
        
        #find item by id and -1 qty, if less then 0, remove
        for item in self.lines:
            if item["id"] == item_id:
                item["qty"] = item["qty"] - 1
                
                if item["qty"] <= 0:
                    self.lines.remove(item)
        
       
            
        
        

    def clear(self) -> None:
        # TODO
        self.lines.clear()

    def total(self) -> float:
        # TODO - round ONCE, at the end
        runningTotal: float = 0
        for item in self.lines:
            runningTotal = runningTotal + (item["price"] * item["qty"])
            
        runningTotal = round(runningTotal, 2)
        
        return runningTotal

    def __repr__(self) -> str:
        # TODO
        cartTotalItems: int = len(self.lines)
        return (f"<CART {(cartTotalItems)} ITEM(S), ${self.total()}>")


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]
    ramen = menu[0]

    cart = Cart()
    cart.add_item(gyoza, 2)
    cart.add_item(gyoza, 1)      # should become qty 3, NOT a second line
    cart.add_item(ramen, 1)

    print(cart)                  # <Cart 2 items, $40.50>
    print(len(cart.lines))       # 2
    print(cart.total())          # 40.5
