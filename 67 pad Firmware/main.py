import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

# Enable macros
macros = Macros()
keyboard.modules.append(macros)

# 4 physical keys
PINS = [board.D3, board.D4, board.D2, board.D1]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Key layout
keyboard.keymap = [
    [
        KC.Macro(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)),  # Copy
        KC.Macro(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)),  # Paste
        KC.Macro(Press(KC.LCTRL), Tap(KC.Z), Release(KC.LCTRL)),  # Undo
        KC.Macro(Press(KC.LCTRL), Tap(KC.Y), Release(KC.LCTRL)),  # Redo
    ]
]

if __name__ == '__main__':
    keyboard.go()
