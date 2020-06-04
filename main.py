"""Moduł main"""
import tkinter as tk
import mygame
import mygui


def main():
    """Główna funkcja main"""
    game = mygame.MyGame()
    root = tk.Tk()
    mygui.MyGUI(root, game)
    root.mainloop()


if __name__ == '__main__':
    main()
