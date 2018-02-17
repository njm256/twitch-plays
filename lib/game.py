import pyautogui
import time

class Game:

    basekeys = ['1','2','3','4','5','6','7','8','9','!','.',"'",'"',',','-',':',';','?']

    def get_valid_buttons(self):
        return self.basekeys

    def is_valid_button(self, button):
        return button in self.basekeys

    def button_to_key(self, button):
        return button

    def push_button(self, button):
        pyautogui.keyDown(button)
        pyautogui.keyUp(button)
