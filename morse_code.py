print("=== MORSE CODE TRANSLATOR ===")
print('''
DISCLAIMER: Only valid morse code letter will be shown in the translation
''')
print('''
For translation of text to morse code, please choose 1
For translation of morse code to text, please choose 2
''')
exit = False

while exit == 'y' :
  while True:
    try:
      choice = int(input("Enter 1 or 2: "))
      if choice == 1 or choice == 2:
        break
      else:
        print("Invalid input. Please enter a number (1 or 2).")
  
    except ValueError:
      print("Invalid input. Please enter a number (1 or 2).")
  
  class ttom:
  
    def __init__(self, text):
      self.text = text
  
    def ttom(self):
      morse_ttom_dict = {
          ' ': '/',
          'a': '.-',
          'b': '-...',
          'c': '-.-.',
          'd': '-..',
          'e': '.',
          'f': '..-.',
          'g': '--.',
          'h': '....',
          'i': '..',
          'j': '.---',
          'k': '-.-',
          'l': '.-..',
          'm': '--',
          'n': '-.',
          'o': '---',
          'p': '.--.',
          'q': '--.-',
          'r': '.-.',
          's': '...',
          't': '-',
          'u': '..-',
          'v': '...-',
          'w': '.--',
          'x': '-..-',
          'y': '-.--',
          'z': '--..',
          '0': '-----',
          '1': '.----',
          '2': '..---',
          '3': '...--',
          '4': '....-',
          '5': '.....',
          '6': '-....',
          '7': '--...',
          '8': '---..',
          '9': '----.',
          '&': '.-...',
          "'": '.---.',
          '@': '.--.-.',
          ')': '-.--.-',
          '(': '-.--.',
          ':': '---...',
          ',': '--..--',
          '=': '-...-',
          '!': '-.-.--',
          '.': '.-.-.-',
          '-': '-....-',
          '%': '------..-.-----',
          '+': '.-.-.',
          '"': '-....-',
          '?': '..--..',
          '/': '-..-.'
      }
      rtext = ""
      for letter in self.text:
        if letter.lower() in morse_ttom_dict:
          rtext += morse_ttom_dict[letter.lower()] + ' '
      return rtext.strip()
  
  class mtot:
  
    def __init__(self, code):
      self.code = code
  
    def mtot(self):
      x = self.code.split(" ")
      morse_mtot_dict = {
          '.-': 'a',
          '-...': 'b',
          '-.-.': 'c',
          '-..': 'd',
          '.': 'e',
          '..-.': 'f',
          '--.': 'g',
          '....': 'h',
          '..': 'i',
          '.---': 'j',
          '-.-': 'k',
          '.-..': 'l',
          '--': 'm',
          '-.': 'n',
          '---': 'o',
          '.--.': 'p',
          '--.-': 'q',
          '.-.': 'r',
          '...': 's',
          '-': 't',
          '..-': 'u',
          '...-': 'v',
          '.--': 'w',
          '-..-': 'x',
          '-.--': 'y',
          '--..': 'z',
          '-----': '0',
          '.----': '1',
          '..---': '2',
          '...--': '3',
          '....-': '4',
          '.....': '5',
          '-....': '6',
          '--...': '7',
          '---..': '8',
          '----.': '9',
          '.-...': '&',
          '.---.': "'",
          '.--.-.': '@',
          '-.--.-': ')',
          '-.--.': '(',
          '---...': ':',
          '--..--': ',',
          '-...-': '=',
          '-.-.--': '!',
          '.-.-.-': '.',
          '-....-': '-',
          '------..-.-----': '%',
          '.-.-.': '+',
          '-....-': '"',
          '..--..': '?',
          '-..-.': '/',
          '/': " "
      }
  
      rtext = ""
      for i in range(0, len(x)):
        if x[i] in morse_mtot_dict:
          rtext += morse_mtot_dict[x[i]]
      return rtext.strip()
  
  if choice == 1:
    text = str(input("Please input or paste your text here: "))
    r_text = ttom(text)
    print("Code: " + r_text.ttom())
  elif choice == 2:
    code = str(input("Please input or paste your code here:"))
    r_code = mtot(code)
    print("Text: " + r_code.mtot())
  else:
    print(
        """Sorry, this number is not an option, please restart this code and try agian with a valid option. Good bye!"""
    )
  while True:
    exit = str(input("Do you want to continue? (y/n) "))
    if exit.lower() == 'y' or exit.lower() == 'n':
      break
    else:
      print("Invalid input. Please enter 'y' or 'n'.")
