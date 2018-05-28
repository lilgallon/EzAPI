import time

from EzProgressBar import EzProgressBar


def main():
    # Init the window
    my_progress_window = EzProgressBar('My progress window', 'Sleeping', 'zzz')

    # Do some tasks
    time.sleep(1)
    my_progress_window.set_progress(10, description='still sleeping')

    # Do some tasks
    time.sleep(1)
    my_progress_window.set_progress(20, description='waking up')

    # Do some tasks
    time.sleep(1)
    my_progress_window.set_progress(30, title='Going to work',
                                    description='Taking train...')

    time.sleep(1)
    my_progress_window.set_progress(100, title='Working', description='zzzz')

    time.sleep(0.5)
    my_progress_window.close()

if __name__ == '__main__':
    main()
