"""
It allows you to create and update a progress bar in a very simple way.
It is made to be used in a non-object oriented programming context. You
won't have to handle threads or anything. It is a simple as this :

0. Import
    from EzProgressBar import EzProgressBar

1. Create a progress bar window :
    progress_window = EzProgressBar('My progressbar window',
                                    'Reading data',
                                    'First part done')

2. Update the progression at any time :
    progress_window.set_progress(10)

3. Close the window
    progress_window.close()

This API is built over the tkinter lib. http://tkinter.fdex.eu/

Author : Lilian Gallon (N3ROO) 28/05/18
"""

import os
import warnings
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class EzProgressBar:
    def __init__(self, win_title, title, description, icon_path=None):
        """ It inits the window and its components.

        Arguments:
        ----------
            win_title {str} -- Title of the window,
            title {str} -- Title of the progress,
            description {str} -- Description of the progress,

        Keyword Arguments:
        ------------------
            icon_path {str} -- The path of the icon : it can be either
                relative or absolute (default: {'none'}).
        """

        # Used to prevent updates when we don't need
        self.update_allowed = False

        # Everything dealing with the window :
        # ---
        # Size
        WIDTH, HEIGHT = 350, 150

        # Init window
        self.root = tk.Tk()

        # Set the title of the window
        self.root.title(win_title)

        # Fix the size of the window
        self.root.maxsize(width=WIDTH, height=HEIGHT)
        self.root.minsize(width=WIDTH, height=HEIGHT)
        self.root.resizable(0, 0)

        # Make the components of the grid fill the window width
        self.root.grid_columnconfigure(1, weight=1)

        # Change the icon
        self.set_icon(icon_path)

        # Center the window
        self.center_window()

        # Font for the labels
        font_title = Font(root=self.root, family='DejaVu Sans', size=14)
        font_description = Font(root=self.root, family='DejaVu Sans', size=12)

        # Everything dealing with the title :
        # ---
        self.title = tk.Label(self.root, font=font_title, fg='blue',
                              anchor='w')
        self.title.grid(row=1, column=1, sticky=tk.W, pady=5, padx=5)
        self.set_title(title)

        # Everything dealing with the description :
        # ---
        self.description = tk.Label(self.root, font=font_description,
                                    anchor='w')
        self.description.grid(row=2, column=1, sticky=tk.W, pady=5, padx=5)
        self.set_description(description)

        # Everything dealing with the progress bar :
        # ---
        self.progressbar = ttk.Progressbar(self.root, orient="horizontal",
                                           length=200, mode="determinate")
        self.progressbar.grid(row=3, column=1, pady=20, padx=5, sticky='nsew')
        self.progressbar["maximum"] = 100
        self.set_progress(0)

        # Now we can update the window !
        self.update_allowed = True
        self.__update__()

    def set_progress(self, progress, title='', description=''):
        """ It changes the information of the progress window :
        - Progress : 0<x<100,
        - Title : if "" then it won't change,
        - Description : if "" then it won't change.

        Arguments:
        ----------
            progress {int} -- Progression in % (between 0 and 100
                included).

        Keyword Arguments:
        ------------------
            title {str} -- Title of the progress (default: {''})
            description {str} -- Description of the progress
                (default: {''})
        """

        if progress > 100:
            progress = 100
            warnings.warn('The progress has been set to %s whereas the max ' +
                          'is set to 100', progress)
        elif progress < 0:
            progress = 0
            warnings.warn('The progress has been set to %s whereas the min ' +
                          'is set to 0', progress)

        if title != '':
            self.update_allowed = False
            self.set_title(title)
            self.update_allowed = True

        if description != '':
            self.update_allowed = False
            self.set_description(description)
            self.update_allowed = True

        self.progressbar['value'] = progress
        self.__update__()

    def set_icon(self, icon_path):
        """ It changes the window icon.

        Arguments:
        ----------
            icon_path {str} -- The path of the icon : it can be either
                relative or absolute (default: {'none'}).
        """
        if icon_path is not None:
            self.root.iconbitmap(os.path.abspath(icon))
            self.__update__()

    def set_title(self, title):
        """ It changes the progress title.

        Arguments:
        ----------
            description {str} -- The new title.
        """

        self.title.configure(text=title)
        self.__update__()

    def set_description(self, description):
        """ It changes the progress description.

        Arguments:
        ----------
            description {str} -- The new description.
        """

        self.description.configure(text=description)
        self.__update__()

    def center_window(self):
        """ It centers the window.
        """

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        x = (screen_width/2) - (window_width/2)
        y = (screen_height/2) - (window_height/2)

        self.root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

        self.__update__()

    def __update__(self):
        """ It updates the window.
        """

        if self.update_allowed:
            self.root.update_idletasks()
            self.root.update()

    def close(self):
        """ It closes the window.
        """

        self.root.destroy()
