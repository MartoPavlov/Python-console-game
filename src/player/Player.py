class Player:
    def __init__(self):
        self.__inventory = {}
        self.__currRoom = 0
    
    #getters
    @property
    def inventory(self):
        return self.__inventory

    @property
    def currRoom(self):
        return self.__currRoom
    @currRoom.setter
    def currRoom(self, next):
        self.__currRoom = next

    def add_item(self, item):
        self.__inventory[item.name] = item;

    def find(self, itemName):
        try:
            self.__inventory[itemName].trigger();
        except KeyError:
            print("No such item in inventory.")
    
    def hasItem(self, itemName):
        return self.__inventory.get(itemName) != None