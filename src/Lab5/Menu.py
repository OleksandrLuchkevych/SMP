class Menu:
    def __init__(self, options):
        self.options = options

    def show(self):
        print("\nMenu:")
        for key, desc in self.options.items():
            print(f"{key}: {desc[0]}")
        choice = input("> ")
        if choice in self.options:
            self.options[choice][1]()
        else:
            print("Invalid choice, please try again.")