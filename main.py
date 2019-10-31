from src.items.Notebook import Notebook
from src.interactables.LockedDoor import LockedDoor
from src.interactables.Skeleton import Skeleton
from src.rooms.Room import Room
from src.interactables.Door import Door
from src.interactables.Drawer import Drawer
from src.interactables.Radio import Radio
from src.interactables.LockBox import LockBox
from src.interactables.KeyDoor import KeyDoor
from src.interactables.Couch import Couch
from src.interactables.LampTable import LampTable
from src.interactables.Chair import Chair
from src.interactables.Bookshelf import Bookshelf
from src.interactables.ToyHouse import ToyHouse
from src.interactables.Bed import Bed
from src.interactables.Desk import Desk
from src.interactables.SpecialDrawer import SpecialDrawer
from src.interactables.Cabins import Cabins
from src.interactables.RustyDoor import RustyDoor
from src.interactables.Note import Note
from src.interactables.Window import Window
from src.Game import Game
from src.scripts import Scripts
#----------------Items-----------------
notebook = Notebook()
#----------------Rooms-----------------

#----------------Basement--------------
locked_door = LockedDoor("1000", "1130")
skeleton = Skeleton()
starting_room = Room(Scripts.basement, locked_door)
starting_room.add_interactable(skeleton)
#---------------F1R1-------------------
radioTape1 = (Scripts.radio_tape1)
door1 = Door()
drawer1 = Drawer()
radio1 = Radio(radioTape1)
room1 = Room(Scripts.bright_room, door1)
room1.add_interactable(drawer1)
room1.add_interactable(radio1)
#-----------------F1R2------------------
door2 = KeyDoor("brown")
box1 = LockBox("brown", "0130")
table = LampTable()
couch1 = Couch()
room2 = Room(Scripts.shady_room, door2)
room2.add_interactable(box1)
room2.add_interactable(table)
room2.add_interactable(couch1)
#-----------------F1R3------------------
door3 = KeyDoor("green")
box2 = LockBox("green", "9217")
table = LampTable()
bookshelf = Bookshelf()
chair1 = Chair()
room3 = Room(Scripts.library_room, door3)
room3.add_interactable(box2)
room3.add_interactable(table)
room3.add_interactable(bookshelf)
room3.add_interactable(chair1)
#-----------------F1R4------------------
door4 = LockedDoor("2265", "1121")
drawer2 = Drawer()
toy = ToyHouse()
bed = Bed()
room4 = Room(Scripts.barby_girl_room, door4)
room4.add_interactable(drawer2)
room4.add_interactable(toy)
room4.add_interactable(bed)
#-----------------F2R1------------------
door5 = KeyDoor("grey")
couch2 = Couch()
chair2 = Chair()
drawer3 = SpecialDrawer()
desk1 = Desk()
room5 = Room(Scripts.office_room, door5)
room5.add_interactable(couch2)
room5.add_interactable(chair2)
room5.add_interactable(drawer3)
room5.add_interactable(desk1)
#-----------------F2R2------------------
door6 = KeyDoor("white")
box3 = LockBox("white", "5813")
cabins = Cabins()
room6 = Room(Scripts.toilet_room, door6)
room6.add_interactable(box3)
room6.add_interactable(cabins)
#-----------------F2R3------------------)
door7 = RustyDoor()
note = Note()
couch3 = Couch()
box4 = LockBox("red", "3546")
room7 = Room(Scripts.bizarre_room, door7)
room7.add_interactable(note)
room7.add_interactable(box4)
#-----------------F2R4------------------
radioTape2 = (Scripts.radio_tape2)
bed2 = Bed()
desk2 = Desk()
desk2.active = False
door8 = LockedDoor("6708", "8067")
drawer4 = Drawer()
radio2 = Radio(radioTape2)
room8 = Room(Scripts.bedroom, door8)
room8.add_interactable(desk2)
room8.add_interactable(drawer4)
room8.add_interactable(radio2)
room8.add_interactable(bed2)
#---------------ceiling----------------
window = Window()
couch4 = Couch()
drawer5 = Drawer()
room9 = Room(Scripts.seiling, window)
room9.add_interactable(couch4)
room9.add_interactable(drawer5)

#--------------Game Launch-------------
game = Game()
game.add_room(starting_room)
game.add_room(room1)
game.add_room(room2)
game.add_room(room3)
game.add_room(room4)
game.add_room(room5)
game.add_room(room6)
game.add_room(room7)
game.add_room(room8)
game.add_room(room9)
game.player.add_item(notebook)
game.start()
exit()
