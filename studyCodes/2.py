### 동영이의 파이썬 과제 .... ###
class Product:

    def __init__(self, id, title, description, price, quantity_available):
        self._id = id
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def decrease_quantity(self):
        self._quantity_available -= 1

    def get_id(self):
        return self._id
    def get_title(self):
        return self._title
    def get_description(self):
        return self._description
    def get_price(self):
        return self._price
    def get_quantity_avialable(self):
        return self._quantity_available

class Customer:
    customer_cart = []

    def __init__(self, name, id, premium_member):
        self._name = name
        self._id = id
        self._premium_member = premium_member

    def is_premium_member(self):
        if(self._premium_member):
            return True
        else:
            return False

    def add_product_to_cart(self, id):
        self.customer_cart.append(id)
    
    def empty_cart(self):
        self.customer_cart.clear()

    def get_name(self):
        return self._name
    def get_customer_id(self):
        return self._id
    def get_customer_cart(self):
        return self.customer_cart

class Store:
    inventory = [] ### list of class Product ###
    membership = []

    def __init__(self):
        self.tmp = 1
    
    def add_product(self, product):
        self.inventory.append(product)
    def add_member(self, customer):
        self.inventory.append(customer)

    def lookup_product_from_id(self, id):
        for i in range(0, len(self.inventory)):
            if(self.inventory[i].get_id() == id):
                return self.inventory[i]

        return None

    def lookup_member_id(self, id):
        for i in range(0, len(self.membership)):
            if(self.membership[i].get_customer_id() == id):
                return self.membership[i]

        return None

    def product_search(self, keyword):
        res = []
        keyword = keyword.lower()
        for i in range(0, len(self.inventory)):
            title = self.inventory[i].get_title()
            title = title.lower()
            description = self.inventory[i].get_description()
            description = description.upper()

            if(keyword in title or keyword in description):
                tmp = self.inventory[i].get_id()
                res.append(tmp)

        return res

    def add_product_to_member_cart(self, p_id, c_id):
        product_idx = -1
        customer_idx = -1

        check = True
        for i in range(0, len(self.inventory)):
            if(self.inventory[i].get_id() == p_id):
                check = False
                product_idx = i
                break
        
        if(check):
            return "product ID not found"
        
        check = True
        for i in range(0, len(self.membership)):
            if(self.membership[i].get_customer_id() == c_id):
                check = False
                customer_idx = i
                break
        
        if(check):
            return "member ID not found"
        
        if(self.inventory[product_idx].get_quantity_avialable() <= 0):
            return "product out of stock"
        
        self.membership[customer_idx].add_product_to_cart(p_id)
        self.inventory[product_idx].decrease_quantity()