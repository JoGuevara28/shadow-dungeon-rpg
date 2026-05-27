class Game:

    def __init__(self):
        self.option = ""

    def show_menu(self):
        print("=========WELCOME TO THE SHADOW DUNGEON RPG=============")
        print("1. Start Game")
        print("2. How to Play")
        print("3. Exit")

    def start(self):
        while True:
            self.show_menu()
            self.option = input("Select one Option: ")

            match self.option:
                case "1":
                    self.start_game()

                case "2":
                    self.how_to_play()

                case "3":
                    print("Leaving the program")
                    break

                case _:
                    print("Opción inválida.")

    def start_game(self):
        print("Starting a new adventure...")

    def how_to_play(self):
        print("Explore rooms, fight enemies, collect gold, use potions, and defeat the final boss.")

