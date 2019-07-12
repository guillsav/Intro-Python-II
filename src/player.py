# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.strength = 10
        self.items = []

    def travel(self, direction):
        # Check if there's a valid room in the direction
        if getattr(self.current_room, f"{direction}_to") is not None:
            # If so, update current_room to new room and print description
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            # Else print an error message
            print("Sorry! there's no room here.", "\n")

    def _get_item_string(self):
        if len(self.items) > 0:
            return "\n" + ", ".join([item.name for item in self.items]) + "\n"
        else:
            return ""

    def print_inventory(self):
        print(f"Your strength is: {self.strength}\n")
        print("You are carrying:\n  " +
              ", ".join([item.name for item in self.items]) + "\n")

    def eat(self, item_name):
        # Check if the item is in the player's inventory
        item_to_eat = None
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item_to_eat = item
                break
        if item_to_eat is None:
            print(f"Did not find {item_name}")
            return
            # If not, throw an error and return
        # Check if the item is food
        if item_to_eat.can_eat():
            self.strength += item_to_eat.calories // 100
            print(f"You eat {item_name}")
            self.items.remove(item_to_eat)
        else:
            print("You cannot eat that!")
            return

    def get(self, item_name):
        self.items.append(item_name)
        print(f"You just picked up the {item_name.name}", "\n")
        return

    def drop(self, item_name):
        self.items.remove(item_name)
        print(f"You just drop the {item_name.name}", "\n")
        return
