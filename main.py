from mygame import *
from mygui import *
# from myexception import *


def main():
    game = MyGame()
    root = Tk()
    MyGUI(root, game)
    root.mainloop()


if __name__ == '__main__':
    main()
