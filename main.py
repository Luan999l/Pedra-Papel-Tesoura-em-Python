import random

user_points = 0
computer_points = 0

options = ['r', 'p', 't']

while True:
  user_choice = input('R(Pedra)\nP(Papél)\nT(Tesoura)\nQ(Sair)\n- ').lower()
  
  if user_choice == 'q':
    break
  computer_choice = random.randint(0,2)
  
  computer_options = options[computer_choice]
  print('O computador escolheu ' + computer_options)
  
  if user_choice == computer_options:
    print('Empate!')
    
  elif user_choice == 'r' and computer_options == 't':
    print('Voçê ganhou!')
    user_points = user_points +1
        
  elif user_choice == 'p' and computer_options == 'r':
    print('Voçê ganhou!')
    user_points = user_points +1
        
  elif user_choice == 't' and computer_options == 'p':
    print('Voçê ganhou!')
    user_points = user_points +1

  else:
    print('Você perdeu!')
    computer_points = computer_points +1

print('Sua pontuação foi: {}'.format(user_points))
print('A pontuação do computador foi: {}'.format(computer_points))

if computer_points < user_points:
  print('Vitória completa')
elif computer_points == user_points:
  print('Empate!')
else:
  print('Derrota!')

print('Goodby')