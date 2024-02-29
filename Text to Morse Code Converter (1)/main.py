MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': " "}

class StringToMorse:
    def __init__(self) -> None:
        self.str_english = None
        self.str_converted = None
        self.isvalid=True
        self.splitter=""


    def get_input(self):
        self.str_english = input('Please provide a string to convert to Morse code:\n').upper()

    def convert_morse(self):
        self.str_converted= ''
        for ch in self.str_english:
            try:
                if not (ch == ' ' and self.splitter==" "):
                    self.str_converted+= MORSE_CODE_DICT[ch]+ self.splitter
            except:
                self.isvalid = False
                self.str_converted+= '?'
    
class MainLoop:
    def __init__(self) -> None:
        self.isContinue = True

    def main_loop(self):
        print('Hello! This is a program to convert an English string (including 0-9 and ".,?/-()")')
        while self.isContinue:
            user_reply=input('Type "w" to convert to Morse code without spaces between letters, "s" to convert with spaces only between words or "n" to exit: ')
            if user_reply.lower()=='n':
                self.isContinue=False
            elif user_reply.lower()=='s' or user_reply.lower()=='w':
                string_input = StringToMorse()
                string_input.get_input()
                if user_reply.lower()=='w':
                    string_input.splitter=" "
                string_input.convert_morse()
                if not string_input.isvalid:
                    print ("You have an unconvertable character in your string, there will be a ? instead")
                print(f"Converted String: {string_input.str_converted}")
            else:
                print('Your input was incorrect!')
        print("Have a nice day!")

if __name__=="__main__":
    pg = MainLoop()
    pg.main_loop()

                