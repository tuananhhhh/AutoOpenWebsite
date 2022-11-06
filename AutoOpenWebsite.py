import webbrowser
import time
from pykeyboard import PyKeyboard

lst = list(range(1,100))

k = PyKeyboard()

for i in lst:
    webbrowser.open('https://www.youtube.com/watch?v=b47y7Yr-hgA', new=1)
    time.sleep(30)
    k.press_keys([k.control_key,'w'])
else:
    pass
