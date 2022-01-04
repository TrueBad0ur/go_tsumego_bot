import os

files_in_folder = os.listdir("./sgfs/right_answers/")
for filename in files_in_folder:
    print(filename)
    #os.system("cat ./sgfs/right_answers/" + filename + " | rev | cut -c7- | rev > ./sgfs/incomplete/" + filename)
    #os.system("echo ')' >> ./sgfs/incomplete/" + filename)

    os.system("./sgfutils-0.25/sgftopng -nonrs ./sgfs/parsed_right_answers/" + filename[:-4] + ".png < ./sgfs/right_answers/" + filename[:-4] + ".sgf")
    os.system("./sgfutils-0.25/sgftopng -nonrs ./sgfs/parsed_incomplete/" + filename[:-4] + ".png < ./sgfs/incomplete/" + filename[:-4] + ".sgf")
