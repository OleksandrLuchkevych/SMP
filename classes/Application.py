from UI.UserInterface import *

class Application:

    def __init__(self):
        self.ui = UserInterface()

    def run(self):

        try:
            choice = self.ui.get_user_input()
            if choice == 'posts':
                data = self.ui.repository.get_posts()
            else:
                data = self.ui.repository.get_users()

            self.ui.display_data(data)
            
            save_choice = input("Бажаєте зберегти дані? (y/n): ").strip().lower()
            if save_choice == 'y':
                self.ui.save_data(data)

            self.ui.log_history(f"Запит {choice} завершено успішно.")

            history_choice = input("Бажаєте переглянути історію запитів? (y/n): ").strip().lower()
            if history_choice == 'y':
                self.ui.view_history()

        except requests.exceptions.RequestException as e:
            print("Помилка під час виконання запиту до API:", e)
        except Exception as e:
            print("Виникла помилка:", e)