import art
from game_data import data
from replit import clear
import  random

def compare(first, second):
  """
  input two option name, return a if first's followers is more, b if second
  """
  for i in data:
      if(i['name'] == first ):
        first_num = i['follower_count']
      if(i['name'] == second):
        second_num = i['follower_count']
  if first_num > second_num:
    return 'a'
  else:
    return 'b'
    
clear()
answer_right = False
game_continue = True
right = 0
option2 = random.choice(data)

while game_continue:
  print(art.logo)
  if(answer_right):
    print(f"You're right! Current score : {right}")
  if(answer_right == False): #first
    option1 = random.choice(data)
  else:
    option1 = option2
  option2 = random.choice(data)
  print(f"Compare A : {option1['name']}, {option1['description']},  from {option1['country']}")
  print(art.vs)
  print(f"Compare B : {option2['name']}, {option2['description']},  from {option2['country']}")
  reply = input("Who has more follers? Type 'a' or 'b' : ")
  if reply == compare(option1['name'], option2['name']):
    right+=1
    answer_right = True
  else:
    game_continue = False
  clear()

print(f"Sorry, that's wrong. Final score : {right}")