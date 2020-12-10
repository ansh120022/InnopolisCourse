state_options = {"Выбор фильма": "1", "Выбор зала": "2", "Назад": "3"}


class TgBot(object):
    def __init__(self, state):
        self.state = None

    def check_state(self, state):
        if state == "Выбор фильма":
            print("Выбор фильма")
        if state == "Выбор зала":
            print("Выбор зала")
        if state == "Назад":
            print("Выбор фильма")

    def cancel_state(self, state):
        state = state

    def process_message(self, user, message):
        answer = state_options[message]
        user.change_state(message)
        print(answer)
        pass


class User(object):
    user_name = None
    current_state = None
    old_state = 0

    def __init__(self, current_state, user_name):
        self.current_state = current_state
        self.user_name = user_name

    def change_state(self, state):
        self.current_state = state
        print(f"{self.user_name}, твоё текущее состояние - {state} ")


user1 = User(current_state="Выбор фильма", user_name="Маша")
user2 = User(current_state="Назад", user_name="Не Маша")

tbBot = TgBot(user1.current_state)
tbBot.process_message(user1, "Выбор зала")
tbBot.process_message(user2, "Выбор зала")
tbBot.process_message(user1, "Назад")
