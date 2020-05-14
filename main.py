from mygame import *
from mygui import *


def main():
    game = MyGame()
    root = Tk()
    Window = MyGUI(root, game)
    root.mainloop()


main()



