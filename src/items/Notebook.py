from src.items.Item import Item
class Notebook(Item):
    def __init__(self):
        super().__init__("notebook", "Type \'take out notebook\' to write in me.")
    
    def trigger(self):
        print(self._info)
        write = input()
        if len(write) > 0:
            self._info += '\n'
            self._info += write