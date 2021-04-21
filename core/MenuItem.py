
class MenuItem:
    def __init__(self, item_id, item_name, category, item_price):
        self._item_id = item_id
        self._item_name = item_name
        self._category = category
        self._item_price = item_price

    def get_item_id(self):
        return self._item_id

    def set_item_id(self, item_id):
        self._item_id = item_id

    def get_item_name(self):
        return self._item_name

    def set_item_name(self, item_name):
        self._item_name = item_name

    def get_category(self):
        return self._category

    def set_category(self, category):
        self._category = category

    def get_item_price(self):
        return self._item_price

    def set_item_price(self, item_price):
        self._item_price = item_price
