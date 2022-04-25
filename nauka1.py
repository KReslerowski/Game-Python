class User:

    def __init__(self, age, name):
        print(
            "jestem inicjalizatorem który wywoluje sie zawsze podczas konstrukcji obiektu")
        self.age = age
        self.name = name
    def print_age(self, message):
        print(message, "wiek: ", self.age, self.name)
        
user1 = User(30, "Arek")
user2 = User(24, "Mirek")

user1.print_age("dodatkowy tekst całkowicie inny")

user2.print_age("dodatkowy tekst")