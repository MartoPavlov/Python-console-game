from enum import Enum
import os
import platform
from src.player.Player import Player
from src.scripts import Scripts
#-------------------------------------
class GameState(Enum):
    MENU = 0
    PLAY = 1
    HELP = 2
    ABOUT = 3
    EXIT = 4
#-------------------------------------
class Game:
    def __init__(self):
        self.game_state = GameState.MENU
        self.last_state = GameState.MENU
        self.player = Player()
        self.rooms = [];
    def start(self):
        while self.game_state != GameState.EXIT:
            self.clear_screen()
            if self.game_state == GameState.MENU:
                print(Scripts.menu)
                user = input("Enter menu: ")
                if user.__eq__("P") or user.__eq__("p"):
                    self.game_state = GameState.PLAY
                elif user.__eq__("H") or user.__eq__("h"):
                    self.game_state = GameState.HELP
                elif user.__eq__("A") or user.__eq__("a"):
                    self.game_state = GameState.ABOUT
                elif user.__eq__("E") or user.__eq__("e"):
                    self.game_state = GameState.EXIT
                else:
                    print("Invalid input")
            elif self.game_state == GameState.PLAY:
                self.clear_screen()
                print(self.rooms[self.player.currRoom].info)
                user = input("What to do? ")
                words = user.split();
                if words[0].__eq__("use"):
                    self.rooms[self.player.currRoom].trigger(words[1], self)
                elif (words[0].__eq__("open") and
                 words[1].__eq__(self.rooms[self.player.currRoom].door.name)):
                    self.rooms[self.player.currRoom].open_door(self)
                elif words[0].__eq__("back"):
                    if self.player.currRoom == 0:
                        print("There is no previous room.")
                    elif self.player.currRoom > 0:
                        self.player.currRoom-=1
                        print("You go back.")
                elif words[0].__eq__("take") and words[1].__eq__("out"):
                    self.player.find(words[2])
                elif words[0].__eq__("inventory"):
                    for item in self.player.inventory.values():
                        print(f"Item: {item.name}")
                        print(item.info)
                elif words[0].__eq__("help"):
                    self.last_state = GameState.PLAY
                    self.game_state = GameState.HELP
                elif words[0].__eq__("exit"):
                    self.game_state = GameState.EXIT
                else:
                    print(f"Command {words[0]} not found! Enter \'help\' to see the\n"+
                          "command list.")
                input("Press enter to continue...")
                    
            elif self.game_state == GameState.HELP:
                self.clear_screen()
                print(Scripts.help_menu)
                input("Press enter to go back..")
                self.game_state = self.last_state
            elif self.game_state == GameState.ABOUT:
                self.clear_screen()
                print(Scripts.about_menu)
                input("Press enter to go back..")
                self.game_state = GameState.MENU
    
    def add_room(self, room):
        self.rooms.append(room);

    def clear_screen(self):
        if platform.system().__eq__("Linux"):
            os.system("clear")
        elif platform.system().__eq__("Windows"):
            os.system("cls")
        else:
            print("Error. You OS is not supported!")
            exit(self, 69)
