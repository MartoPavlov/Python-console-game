from src.StoryObject import StoryObject
class Room(StoryObject):
    def __init__(self, info, door):
        StoryObject.__init__(self, info)
        self.__interactables = {}
        self.__door = door;
    #getters
    @property
    def interactables(self):
        return self.__interactables
    
    @property
    def door(self):
        return self.__door

    def add_interactable(self, inter):
        self.__interactables[inter.name] = inter;

    def trigger(self, key, game):
        try:
            return self.__interactables[key].trigger(game)
        except KeyError:
            print("No such object in the room.")

    def open_door(self, game):
        self.__door.trigger(game);