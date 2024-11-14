import art
from game_data import data
from random import randint

#def initial(a, b):
  
print(art.logo)
num_a = randint(0,len(data)+1)
num_b = randint(0,len(data)+1)

followers_a = data[num_a]['follower_count']
followers_b = data[num_b]['follower_count']


item_a = f"{data[num_a]['name']}, a {data[num_a]['description']}, from {data[num_a]['country']}."
item_b = f"{data[num_b]['name']}, a {data[num_b]['description']}, from {data[num_b]['country']}."

print(f"Compare A: {item_a}")
print(art.vs)
print(f'Against B: {item_b}')
vote = input("Who has more followers? Type 'A' or 'B': ").lower()



