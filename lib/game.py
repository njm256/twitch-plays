import pyautogui
import time


class Game:

    base_keys = ['1','2','3','4','5','6','7','8','9','!','.',"'",'"',',','-',':',';','?','s','f']

    def get_valid_buttons(self):
        return self.base_keys

    def is_valid_button(self, button):
        return button in self.base_keys

    def button_to_key(self, button):
        return button

    def push_button(self, button):
        if button == 's':
            pyautogui.hotkey('alt', 'enter')
        elif button == 'f':
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            time.sleep(.05)
            pyautogui.hotkey('ctrl', 'end')
        else:
            pyautogui.keyDown(button)
            pyautogui.keyUp(button)
