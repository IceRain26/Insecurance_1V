import sqlite3
from prettytable import PrettyTable


class Insured:
    def __init__(self, name, surname, age, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Phone Number: {self.phone_number}"

class Management:
    def __init__(self):
        self.conn = sqlite3.connect("evidence.db")
        self.cur = self.conn.cursor()

    def create_evidence(self, name, surname, age, phone_number):
        """Register person into evidence"""
        self.cur.execute('''INSERT INTO evidence (name, surname, age, phone_number) 
                            VALUES (?, ?, ?, ?)''', (name, surname, age, phone_number))
        self.conn.commit()
        return f"Pojištěný {name} {surname} byl úspěšně vytvořen"

    def view_evidence(self):
        """Let you view registered people from evidence in SQL"""
        self.cur.execute('''SELECT name, surname, age, phone_number FROM evidence''')
        rows = self.cur.fetchall()
        table = PrettyTable(["Name", "Surname", "Age", "Phone Number"])
        for row in rows:
            table.add_row(row)
        return table

    def search_for_person(self, name, surname):
        """Will find if person is in Evidence databse and return printed name and surname"""
        self.cur.execute('''SELECT * FROM evidence WHERE name = ? AND surname = ?''', (name, surname))
        row = self.cur.fetchone()
        if row:
            column_names = [description[0] for description in self.cur.description]
            table = PrettyTable(column_names)
            table.add_row(row)
            return table
        else:
            return "Pojištěný s daným jménem a příjmením nebyl nalezen."
