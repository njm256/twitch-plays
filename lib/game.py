import win32api
import win32con
import time

class Game:

    keymap = {
        '1':0x61,
        '2':0x62,
        '3':0x63,
        '4':0x64,
        '5':0x65,
        '6':0x66,
        '7':0x67,
        '8':0x68,
        '9':0x69,
		'.':0xBE,
		',':0xBC,
		'?':0xBF,
		'-':0xBD,
		'\'':0xDE,
		';':0xBA
    }

    def get_valid_buttons(self):
        return [button for button in self.keymap.keys()]

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, button):
        win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
        time.sleep(.15)
        win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
