import os, random

chosen_file = random.choice(os.listdir("./sgfs/"))[:-4]
command = "./sgfutils-0.25/sgftopng ./parsed_sgfs/" + chosen_file + ".png < ./sgfs/" + chosen_file + ".sgf"
print(command)
os.system(command)
