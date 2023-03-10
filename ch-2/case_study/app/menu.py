import sys
from notebook import NoteBook


class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self) -> None:
        self.notebook = NoteBook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def display_menu(self):
        print(
            """
            Notebook Menu
            1. Show all Notes
            2. Search Notes
            3. Add Note
            4. Modify Note
            5. Quit
            """
        )

    def run(self):
        """
        Display menu and respond to choices
        """
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)

            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes

        print(f"""
            Notes
            _________________________________________ \n
            """)
        for note in notes:
            print(f"{note.id} : {note.memo} \n {note.tags}")

    def search_notes(self):
        filter = input("Search in memo or tags: ...")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter your memo text : ")
        self.notebook.new_note(memo)
        print("your Note has been added")

    def modify_note(self):
        id = input("Enter a note id : ")
        memo = input("Enter a note memo : ")
        tags = input("Enter a note tag[s] : ")

        if memo:
            self.notebook.modify_memo(id, memo)

        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
