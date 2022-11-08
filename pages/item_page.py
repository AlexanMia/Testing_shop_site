class ItemPageObject:
    def __init__(self, section, loc_item, add_to_wishlist_button, item_name):
        self.section = section
        self.loc_item = loc_item
        self.add_to_wishlist_button = add_to_wishlist_button
        self.item_name = item_name

    def get_section(self):
        return self.section

    def get_loc_item(self):
        return self.loc_item

    def get_add_to_wishlist_button(self):
        return self.add_to_wishlist_button

    def get_item_name(self):
        return self.item_name
