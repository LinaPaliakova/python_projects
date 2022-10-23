import random
word_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие", "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница", "магазин", "председатель", "сотрудник", "республика", "личность"]

def get_word():
    word = random.choice(word_list).upper()
    return word 

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
 
def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print("Давайте играть в угадайку слов!")
    print(display_hangman(tries))
    print(word_completion)
    print()
    
import random
word_list = ["человек", "слово", "лицо"]

def get_word():
    word = random.choice(word_list).upper()
    return word  
            
def play(word):
     word_completion = '*' * len(word)  
     guessed = False                   
     guessed_letters = []               
     guessed_words = []                 
     tries = 6                          
     print("Давайте играть в угадайку слов!")
     
     print(word_completion)
     print()

     while not guessed and tries != 0:
         guess = input().upper()
                          
         if len(guess) == 1 and guess.isalpha():
             if guess in guessed_letters:
                 print("Это слово/буквы уже были названы. Попробуйте ввести другую букву или слово.")
             elif guess not in word:
                 tries -= 1
                 print("You are wrong!")
                 guessed_letters.append(guess)
             else:
                 guessed_letters.append(guess)
                 for i in range(len(word)):
                     if word[i] == letter:
                         word_completion = word_completion[:i] + guess + word_completion[i + 1:]
                 print(word_completion)
                 print("You guessed")            
                    if '*' not in word_completion:
                        print("Поздравляем, вы угадали слово! Вы победили!")
                        guessed_words.append(word)
                        guessed = True
             
         elif  len(guess) == len(word):
             if guess in guessed_words:
                 print("Это слово/буквы уже были названы. Попробуйте ввести другую букву или слово.") 
             elif guess != word:
                 print("You are wrong!")
                 guessed_words.append(guess)
                 tries -= 1
             else:
                 print("You guessed")
                 guessed = True
                 word_completion = word
               
             
         else:
            print('Введите букву или слово.')

     if guessed:
         print('Поздравляем, вы угадали слово! Вы победили!')
     else:
         print('Вы не угадали слово. Загаданным словом было ' + word')

play_again = 'да'         
while play_again.lower() == 'да':
   word = get_word()
   play(word)
   play_again = input("Вы хотите играть снова? Да или Нет").lower()