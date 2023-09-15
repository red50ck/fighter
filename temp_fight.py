import random
import time

class User_interaction:
    #проверка ввода на заданный тип
    def check_type(type, type_name, hint):
        while True:
            try:
                return type(input(hint))
                break
            except:
                print("Какая-то ошибка! Введите", type_name)

#класс с методом создания персонажа      
class Character:
    
    #создание персонажа
    def __init__(self, id):
        self.id = id
        self.damage_per_second = random.randint(1, 10)
        self.start_health = random.randint(1, 100)
        self.health = self.start_health
        
    #создание списка персонажей
    def create_characters():
        character_count = User_interaction.check_type(int, "целое число", "Укажите количество генерируемых персонажей: ")
        characters = []
        for id in range(1, character_count+1):
            characters.append(Character(id))
        return characters
     
    #метод, выводящий на консоль всех персонажей и их характеристики  
    def print_details(characters):
        for Character in characters:
            print(f"\n**ID персонажа: {Character.id}**,\nУрон в секунду: {Character.damage_per_second},\
                    \nСтартовое здоровье: {Character.start_health},\nОставшееся здоровье: {Character.health}.")

class Fight:
    #метод, в котором противник выбирает персонажа
    def bot_choose(characters):
        random_character = random.choice(characters)
        characters.remove(random_character)
        print(f"\nПерсонаж противника: {random_character.id}.\nУрон в секунду: {random_character.damage_per_second},\
             \nСтартовое здоровье: {random_character.start_health}.\n")
        return characters, random_character
    
    #создание листов персонажей
    winners = []
    losers = []
    equals = []
    
    #метод, проверяющий, жив ли персонаж
    def is_alive(Character):
        return Character.health >= 0

    #метод, восстанавливающий характеристики персонажа
    def restart(Character):
        Character.health = Character.start_health

    #метод с алгоритмом боя
    def fight(characters, random_character):
        for Character in characters:
            input("\nНажмите Enter, чтобы продолжить.")
            if not Fight.is_alive(random_character):
                Fight.restart(random_character)
                print(f"Персонаж {random_character.id} был воскрешен. Его здоровье снова {random_character.health}!")
            print(f"\nБой с персонажем {Character.id}:")
            while Fight.is_alive(Character) and Fight.is_alive(random_character):
                Character.health -=  random_character.damage_per_second
                print(f"Персонаж {Character.id} получает {random_character.damage_per_second} урона. Оставшееся здоровье: {Character.health}.")
                random_character.health -= Character.damage_per_second
                print(f"Персонаж {random_character.id} получает {Character.damage_per_second} урона. Оставшееся здоровье: {random_character.health}")
                if not Fight.is_alive(Character) and Fight.is_alive(random_character):
                    Fight.losers.append(Character)                    
                    Fight.restart(random_character)
                    print(f"Персонаж {Character.id} выбыл. Компьютер победил.")
                    break
                elif not Fight.is_alive(random_character) and Fight.is_alive(Character):
                    print(f"Персонаж {random_character.id} выбыл. Компьютер проиграл.")
                    Fight.winners.append(Character)
                    break
                elif not Fight.is_alive(Character) and not Fight.is_alive(random_character):
                    Fight.equals.append(Character)
                    print(f"Оба персонажа погибли.")
                    Fight.winners.append(Character)
                    break
        print("\nПобедители: " + ", ".join(str(Character.id) for Character in Fight.winners))  
        print("Проигравшие: " + ", ".join(str(Character.id) for Character in Fight.losers)) 
        print("Ничья: " + ", ".join(str(Character.id) for Character in Fight.equals)) 
             
characters = Character.create_characters()
input("Персонажи сгенерированы. Нажмите Enter, чтобы начать бой.\n")
characters, random_character = Fight.bot_choose(characters)
Fight.fight(characters, random_character)