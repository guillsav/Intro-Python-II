# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        str = f"""
              \n----------------------------------
              \n{self.title}
              \n   {self.description}\n
              \n{self._getItem_string()}\n
              \n{self._get_exits_string()}\n"""
        return str

    def _getItem_string(self):
        return ", ".join([item.name for item in self.items])

    def _get_exits_string(self):
        exits = []
        if self.n_to is not None:
            exits.append('n')
        if self.s_to is not None:
            exits.append('s')
        if self.e_to is not None:
            exits.append('e')
        if self.w_to is not None:
            exits.append('w')
        return "Exits to the " + ", ".join(exits)

    def remove_item(self, item):
        for i in self.items:
            if i == item:
                self.items.remove(i)

    def add_item(self, item):
        for i in self.items:
            if i == item:
                print(f"This {item} is already in the room!")
            else:
                self.items.append(item)

    def open(self, item_name):
        item_to_open = None
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item_to_open = item
                break
        if item_to_open is None:
            print(f"Did not find {item_name}")
            return
        if item_to_open.can_open():
            print(f"You opened the {item_name}")
        else:
            print("You cannot open that!")
            return
