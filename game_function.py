# write a function will be update the current score with the new score. the file might be blank as well 

def game():  # game function is defined which will return 64 as score
    return 10

score = game() # score variable will call game function 
with open("highscore.txt", "r") as f:
    highscore = f.read()  # this will read the previos highscore in the file

if highscore=="": # if the earlier score is blank
    with open("highscore.txt", "w") as f:
        f.write(str(score))

elif int(highscore)<score: # if logic, highscore is less than score it will write the new highscore in the file
    with open("highscore.txt", "w") as f:
        f.write(str(score))