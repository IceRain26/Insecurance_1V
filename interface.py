from prettytable import PrettyTable

class Interface:
    @staticmethod
    def display_menu():
        table = PrettyTable()
        table.border = True
        table.field_names = ["Menu","Evidence pojištěných"]
        table.add_row(["1", "Vytvořit nového pojištěného"])
        table.add_row(["2", "Zobrazit seznam pojištěných"])
        table.add_row(["3", "Hledat pojištěného"])
        table.add_row(["4", "Konec"])
        table.align = "l"
        table.align["Menu"] = "c"
        print(table)

    @staticmethod
    def get_choice():
        return input("Zadejte volbu: ")
