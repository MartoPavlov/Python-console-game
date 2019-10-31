from src.StoryObject import StoryObject
import abc
class Interactable(StoryObject):
    def __init__(self, name, info):
        StoryObject.__init__(self, info)
        self.__name = name
        self._active = True
    
    #getters
    @property
    def name(self):
        return self.__name

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, newValue):
        self._active = newValue


    @abc.abstractmethod
    def trigger(self, game):
        print(self._info)