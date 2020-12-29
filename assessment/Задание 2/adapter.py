class Target:
    """
    Это Kafka.
    """

    def request(self) -> str:
        return "Я - кафка, жду сообщений"


class forestsTeam:
    """Одна из множества исследовательских команд, которая шлёт данные."""

    def specific_request(self) -> str:
        return "!акфаК ,тевирП"


class Adapter(Target):
    """
    Адаптер.
    """

    def __init__(self, forestsTeam: forestsTeam) -> None:
        self.forestsTeam = forestsTeam

    def request(self) -> str:
        return f"""Адаптер: Пока я только переворачиваю строки:
               {self.forestsTeam.specific_request()[::-1]}
                Позже меня научат работать с json"""



def client_code(target: Target) -> None:
        print(target.request(), end="")


if __name__ == "__main__":
    kafka= Target()
    client_code(kafka)
    print("\n")

    forestsTeam = forestsTeam()

    print(f"forestsTeam: {forestsTeam.specific_request()}", end="\n\n")

    print("kafka: Они прислали какую-то фигню. "
          "Я не понимаю\\n")


    print("Kafka: Попробую прочитать через адаптер:\n")
    adapter = Adapter(forestsTeam)
    client_code(adapter)