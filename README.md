# EzAPI
A compilation of useful and VERY simple python APIs maintained by N3ROO. Those are made to be used in a non-object oriented programming context and can be used by beginners.

## 1. EzProgressBar ![Version 1](https://img.shields.io/badge/Version-1-green.svg)
It allows you to create and update a progress bar in a very simple way.
It is made to be used in a non-object oriented programming context. You
won't have to handle threads or anything.

This API is built over the [tkinter](http://tkinter.fdex.eu/) lib. 

### 1.1 How to use it
It is a simple as this :

- 0. Import
```
from EzProgressBar import EzProgressBar
```

- 1. Create the window
```
progress_window = EzProgressBar('My progressbar window',
                                'Sleeping',
                                'still sleeping')
```

- 2. Update the progression at any time :
```
progress_window.set_progress(10)
```

- 3. Close the window once it's done :
```
progress_window.close()
```

### 1.2 What does it looks like

![EzProgressBar_Preview](images/EzProgressBar_preview1.png)

You can change the title or the description in the same time as the progression with :
```
progress_window.set_progress({progression}, title={title}, description={description})
```

Or one by one with :
```
progress_window.set_title({title})
progress_window.set_description({description})
```

You can change the icon too with :
```
progress_window.set_icon({icon path})
```

Or directly when creating the window with :
```
progress_window = EzProgressBar({window title},
                                {progress title},
                                {progress description},
                                icon={icon path})
```

### 1.3 How to use it in your projects

Get the file from the github page and put it in your project directory.

### 1.4 Contributing

If you want to contribute, make sure to respect PEP8 and python coding conventions. And please remind that the goal of this API is to be very easy to use in a non-object oriented programming context.

## 2. EzWebScraping
Work in progress ...