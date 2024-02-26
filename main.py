from evidence import Management
from interface import Interface
import re


def validate_input(input_str):
    """ Will check if input contains only letter and is not longer than 20 characters """
    if re.match(r'^[a-zA-ZščřžŠČŘŽěĚýáíéóúůÝÁÍÉÓÚŮ]{1,20}$', input_str):
        return True
    else:
        return False


management = Management()
interface = Interface()

keep_going = True

while keep_going:

    interface.display_menu()
    choice = interface.get_choice()

    if choice == "1":
        name = input("Zadejte jméno:\n")
        surname = input("Zadejte své příjmení:\n")
        if not validate_input(name) or not validate_input(surname):
            print("Neplatný vstup. Použijte pouze písmena a maximální počet 20 znaků.")
            continue
        age = int(input("Zadejte věk:\n"))
        phone_number = int(input("Zadejte telefonní číslo:\n"))
        result = management.create_evidence(name, surname, age, phone_number)
        print(result)

        again = input("Chcete pokračovat v zadávání dalších osob do evidence? (ano/ne):\n").lower()
        if again != "ano":
            keep_going = False

    elif choice == "2":
        print(management.view_evidence())

    elif choice == "3":
        name = input("Zadejte jméno:\n")
        surname = input("Zadejte příjmení:\n")
        print(management.search_for_person(name, surname))

    elif choice == "4":
        keep_going = False

    else:
        print("Neplatná volba. Zadejte znovu:\n")

