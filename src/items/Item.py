from src.StoryObject import StoryObject
class Item(StoryObject):
    def __init__(self, name, info):


        StoryObject.__init__(self, info)
        self.__name = name
    
    #getters
    @property
    def name(self):
        return self.__name
    
    def trigger(self):
        print(self._info)