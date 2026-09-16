"""Exercise 3: Enforce a business rule.

Extend your Cart so invalid operations are rejected by the CART.

  ValueError        when qty < 1
  OutOfStockError   when the item's "available" field is False
  KeyError          when removing an item that is not in the cart

Then demonstrate each one with try/except.
"""

from exercise1 import load_menu


class OutOfStockError(Exception):
    """Raised when a customer tries to order an item that is unavailable."""
    pass

class ValueError(Exception):
    """Raised when a customer tries to add <= 0 items of type to their cart"""
    pass

class KeyError(Exception):
    """"Raised when a customer tries to remove an item that is not in their cart"""
    pass


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int = 1) -> None:
        # TODO: validate FIRST, then mutate.
        #   if qty < 1:                 raise ValueError(...)
        
        if qty < 1: raise ValueError()
        
        
        #   if not item["available"]:   raise OutOfStockError(...)
        
        if not item["available"]: raise OutOfStockError()     
        
        #Check if in cart already
        for items in self.lines:
            try:
                if items["id"] == item["id"]:
                    items["qty"] += qty
                    return
            except:
                raise KeyError
                
        #is not in cart
                
        self.lines.append(item)
        #will always be last item since added to end
        self.lines[(len(self.lines) - 1)]["qty"] = qty   
        

    def remove_item(self, item_id: int) -> None:
        # TODO: raise KeyError if the item is not in the cart
        
        foundItem : bool = False
        
        for item in self.lines:
            if item["id"] != str(item_id):
                foundItem = True
        
        if(not foundItem):
            raise KeyError
         #find item by id and -1 qty, if less then 0, remove
        for item in self.lines:
            if item["id"] == item_id:
                item["qty"] = item["qty"] - 1
                        
                if item["qty"] <= 0:
                    self.lines.remove(item)

    def total(self) -> float:
        return round(sum(line["price"] * line["qty"] for line in self.lines), 2)

    def __repr__(self) -> str:
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]           # available
    miso = menu[3]            # NOT available

    cart = Cart()

    # TODO: demonstrate each rejection with try/except and a readable message.
    # Example:
    # try:
    #     cart.add_item(gyoza, 0)
    # except ValueError as e:
    #     print(f"Rejected: {e}")
    
    #out of stock
    try:
        cart.add_item(miso, 1)
    except OutOfStockError as e:
        print(f"Item was out of stock! {e}")
       
    #quantity error    
    try:
        cart.add_item(gyoza, 0)
    except ValueError as e:
        print(f"Item quantity was <= 0! {e}")
        
    #key error   
    try:
        cart.remove_item(25)
    except KeyError as e:
            print(f"Key was not found in dict! {e}")
            
            
    
    #in stock and qty > 0, so should work
    try:
        cart.add_item(gyoza, 50)
    except OutOfStockError as e:
            print(f"Item was out of stock! {e}")
    
    
    
    print(cart)                  # <Cart 1 items, $400>
    print(len(cart.lines))       # 1
    print(cart.total())  
    
    #removing a single gyoza added above
    try:
        cart.remove_item(2)
    except KeyError as e:
            print(f"Key was not found in dict! {e}")
            
    
    print(cart)                  # <Cart 1 items, $392.00>
    print(len(cart.lines))       # 1
    print(cart.total())  