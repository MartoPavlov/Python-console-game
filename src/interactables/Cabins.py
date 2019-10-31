from src.interactables.Interactable import Interactable

class Cabins(Interactable):
    def __init__(self):
        Interactable.__init__(self, "cabin", "There are 4 cabins. Which one to enter?")
    
    def trigger(self, game):
        super().trigger(game)
        user = input("Enter action. Example: first ->")
        if user.__eq__("first"):
            print("You enter the first cabin. There you see the number 5 painted on the wall")
        elif user.__eq__("second"):
            print("You enter the first cabin. There you see the number 8 painted on the wall")
        elif user.__eq__("third"):
            print("You enter the first cabin. There you see the number 1 painted on the wall")
        elif user.__eq__("fourth"):
            print("You enter the first cabin. There you see the number 3 painted on the wall")
        elif user.__eq__("back"):
            print("Stepping back...")
        else:
            print("No effect.")