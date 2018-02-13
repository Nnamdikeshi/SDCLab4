# Created by Scott Kim
# Lab1 Part 4
# This program will retreive the latest USD to CAD exchange rate and user will be able to exchange either from USD to CAD or CAD to USD

import requests
import sys




# http://www.hashbangcode.com/blog/stopping-code-execution-python request exception
def setup():
    try:
        base_url = 'https://api.fixer.io/latest?base=USD'
        data = requests.get(base_url).json()
        return data
    except requests.exceptions.RequestException as e:
        print(e)
        raise fixer_exception
        sys.exit()


def get_cad(data):

    cad = data["rates"]["CAD"]
    print("The latest exchange rate is 1 USD to " +str(cad)+ " CAD\n")
    return cad


def conversion(cad):

        option = int(input("Please select an option\n"+
        "1. USD to CAD\n"+
        "2. CAD to USD\n"))


        if option == 1:
            while True:
                try:
                    xcFrom = float(input("\nEnter USD to exchange to CAD: $"))
                    xcTo = xcFrom * cad
                    print( str(round(xcFrom, 2)) + " USD is " + str(round(xcTo, 2)) + "CAD")
                    break
                except ValueError:
                    print("Please enter number only")

        elif option == 2:
            while True:
                try:
                    xcFrom = float(input("\nEnter CAD to exchange to USD: $"))
                    xcTo = xcFrom / cad
                    print( str(round(xcFrom, 2)) + " CAD is " + str(round(xcTo, 2)) + " USD")
                    break
                except ValueError:
                    print("Please enter number only")

def fixer_exception():
    pass


def main():
    data = setup()
    cad = get_cad(data)
    conversion(cad)

if __name__ == '__main__':
    main()
