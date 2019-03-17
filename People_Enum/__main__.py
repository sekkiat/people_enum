from googlesearch.googlesearch import GoogleSearch
from pyfiglet import Figlet
from termcolor import cprint
from pyfiglet import figlet_format
from hyperlink import URL
def main():
    text="People Enum"
    cprint(figlet_format(text, font="standard"), "green")
    name=input("Enter a name : ")
    gs=GoogleSearch()
    response=gs.search(name)
    gs.print_one_by_one(response)



if __name__ == '__main__':
    main()
