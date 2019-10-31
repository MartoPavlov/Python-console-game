class StoryObject:
    def __init__(self, info):
        self._info = info
    
    #getter
    @property
    def info(self):
        return self._info