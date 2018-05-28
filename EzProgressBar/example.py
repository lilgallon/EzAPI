#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

""" Run this script to get a preview of EzProgressBar.
"""

import time

from EzProgressBar import EzProgressBar


def main():
    # Init the window
    my_progress_window = EzProgressBar('My progress window', 'Sleeping', 'zzz')

    time.sleep(1)  # Do some tasks
    my_progress_window.set_progress(10, description='still sleeping')

    time.sleep(1)  # Do some tasks
    my_progress_window.set_progress(20, description='waking up')

    time.sleep(1)  # Do some tasks
    my_progress_window.set_progress(30, title='Going to work',
                                    description='Taking train...')

    time.sleep(1)  # Do some tasks
    my_progress_window.set_progress(100, title='Working', description='zzzz')

    time.sleep(0.5)  # Do some tasks
    my_progress_window.close()

if __name__ == '__main__':
    main()
