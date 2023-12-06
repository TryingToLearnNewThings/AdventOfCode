import re
from collections import defaultdict
# wir haben: 12 red cubes, 13 green cubes, 14 blue cubes
red = 12
green = 13
blue = 14

with open("day2.txt", 'r') as games:
    game = games.read().strip().split("\n")
# sorgt dafür dass alles als list von strings aka lines eingelesen wird. Darüber kann mann dann mit Loop arbeiten

    # gameString = games.join("")
  
valid_games = 0
# oder total oder so. Das wir nachher geprinted

# iterates over each game
for line in game:
    # init dictionary
    cube = defaultdict(int)
    
    #loop over each round in each game
    for round_data in line['rounds']:
        for color, count in round_data.items():
            #set the max color count
            cube[color] = max(cube[color], count)

    # condition
    if cube["red"] <= 12 and cube["green"] <= 13 and cube["blue"] <= 14:
        valid_games += line['game']
        print(valid_games)


# filtered = []
# for line in games:
#     if not (red > 12 or green > 13 or blue > 14):
#         filtered.append(line)
#         print(filtered)


# def word_before(text, target_word):
#     pattern = re.compile(r'\b(\w+)\s+' + re.escape(target_word))
#     match = re.search(pattern, text)
#     if match:
#         return match.group(1)
#     else:
#         return None


# target = "red"
# text = gameString

# result = word_before(text, target)
# print(result)