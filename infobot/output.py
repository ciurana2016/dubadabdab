from colorama import Fore, Style



def output(text, color, nostar=False):
    front = '[*] ' if nostar == False else ''
    text_output = front + text
    c = Fore.GREEN if color == 'verde' else Fore.RED
    print(c + text_output + Style.RESET_ALL)
