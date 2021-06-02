try:
    import pygame
    import sys
    import math
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    import os
except:
    import install_requirements  # install packages

    import pygame
    import sys
    import math
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    import os

screen = pygame.display.set_mode((800, 800))