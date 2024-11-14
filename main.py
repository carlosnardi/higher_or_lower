import art
from game_data import data
from random import randint

def compare_screen(num_a, num_b):
  print(art.logo)
  item_a = f"{data[num_a]['name']}, a {data[num_a]['description']}, from {data[num_a]['country']}."
  item_b = f"{data[num_b]['name']}, a {data[num_b]['description']}, from {data[num_b]['country']}."
  print(f"Compare A: {item_a}")
  print(art.vs)
  print(f'Against B: {item_b}')
  vote = input("Who has more followers? Type 'A' or 'B': ").lower()
  return vote

def compare_vote(num_a):  
  vote = compare_screen(num_a, num_b)
  global score
  if vote == 'a' and followers_a > followers_b:
    a_or_b = 'a'
    score += 1
    print(f"You're right. Current score: {score}")
  elif vote == 'b' and followers_b > followers_a:
    a_or_b = 'b'
    score += 1
    print(f"You're right. Current score: {score}")
  else:
    a_or_b = 'c'
    print(f"Sorry. That's wrong. Final score: {score}")
  return a_or_b

score = 0
a_or_b = 0
game_over = False
while not game_over:
  num_a = randint(0,len(data))
  num_b = randint(0,len(data))
  followers_a = data[num_a]['follower_count']
  followers_b = data[num_b]['follower_count']
  if compare_vote(num_a) == 'c':
    game_over = True

    
 