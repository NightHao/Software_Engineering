import show
from PIL import Image, ImageOps
screen = show.ShowOnMonitor()
def print_screen():
    print("test-text:",screen.text)
    print("test-img:",screen.img)
    print("test-bg:",screen.bg)
    print("test-label_bg:",screen.label_bg)
    print("test-fg:",screen.fg)
    print("test-font:",screen.font)
def test_modify_show(): #測試修改函式和顯示結果的函式是否正常
    Input = Image.open("test_pic.png")
    screen.show(0,Input)
    screen.modify_text("Test Success!")
    screen.modify_bg("Test Success!")
    screen.modify_label_bg("Test Success!")
    screen.modify_fg("Test Success!")
    screen.modify_font("Test Success!")
    print_screen()
def test_setting(): #測試setting GUI更改後是否正常
    while screen.setting():
        continue
Input = Image.open("test_pic.png")
screen.show(0,Input)
print_screen()
print("更改後")
test_setting()
screen.show(0,Input)
print_screen()