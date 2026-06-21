from colorama import Fore, Style, init
from banner import ngl_banner, author
from services import url, send_message

init(autoreset=True)


def view():
    print(Fore.RED + ngl_banner)
    print(Fore.BLUE + author)

    username = input(Fore.GREEN + "Enter Username: ")
    slug = input("Enter Slug [OPTIONAL]: ")
    question = input("Enter Question: ")
    count = int(input("Enter Count: " + Fore.RESET))

    send_message(username, slug, question, count)


