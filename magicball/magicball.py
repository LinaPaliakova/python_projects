import random 
answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
name = input('Как тебя зовут?')
print("Привет", name)

while True:
     question = input("Введите вопрос: ")
     print("Твой ответ: ", random.choice(answers))
     print("Хотите задать еще один вопрос? Да или Нет?")
     answer = input().lower()
     if answer == "да":
         continue
     else:
         print("Возвращайся, если возникнут вопросы!")
         break