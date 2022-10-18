import random 
print("Добро пожаловать в числовую угадайку")
print("Введите правую границу диапозона")
n = int(input())

 
num1 = random.randint(1, n) 



def is_valid(num): 
    
    if num.isdigit():
        if 1 <= int(num) <= n:
            return True
    return False

counter = 1
while True:
     num = input()
     
     if  is_valid(num) == False:
         print("А может быть все-таки введем целое число от 1 до границы вы указали?")
         counter += 1
         continue 
     else:
         num = int(num) 
     if num > num1:
         counter += 1
         print("Ваше число больше загаданного, попробуйте еще разок")
     elif num < num1:
         counter += 1
         print("Ваше число меньше загаданного, попробуйте еще разок")
     else:
         print("Вы угадали, поздравляем!","Количество попыток :", counter)
         print("Хотите сыграть еще раз? Да или Нет?")
         responce = input().lower()
         if responce == "да":
            num1 = random.randint(1, n)
         else:     
             break  
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")