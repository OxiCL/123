from random import randint

def is_valid(text):
     while not text.isdigit():
          print('А может быть все-таки введем целое число?')
          text=input()
     return int(text)
game=0
chall=True

while chall == True:
     attemp=1
     print('Добро пожаловать, в угадайку, введите границы отгадваемого числа')
     n=input()
     n=is_valid(n)
     quest = randint(1, int(n))
     print('Сыграем! Угадайте число загаданное компьютером!')
     s=input()
     s=is_valid(s)
     while s != quest:
          attemp += 1
          if s > quest:
               print('Ваше число больше загаданного, попробуйте еще разок')
          elif s < quest:
               print('Ваше число меньше загаданного, попробуйте еще разок')

          s = input()
          s = is_valid(s)
     print('Вы угадали, поздравляем!')
     game+=1
     print(f'Вы угадали с {attemp} раза! Вы сыграли {game} партий! Сыграем еще разок? Введите "да" для продолжения')
     i=input()
     if i=='да':
          chall=True
     else:
          chall=False