from colorama import Fore, Style, init
def get_colored_text(text):
    init(autoreset=True)
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
