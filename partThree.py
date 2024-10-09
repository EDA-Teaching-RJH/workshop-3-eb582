score = int(input("What presentige did the student score in this unit? 100 - 0? "))
if score > 100 or score < 0: print("Invalid Input")
else:
    if score <= 100 and score >= 90: print("They scored" , score , "whitch is between 100-90 their result is A")
    if score <= 89 and score >= 80: print("They scored" , score , "whitch is between 89-80 their result is B")
    if score <= 79 and score >= 70: print("They scored" , score , "whitch is between 79-70 their result is C")
    if score <= 69 and score >= 60: print("They scored" , score , "whitch is between 69-60 their result is D")
    elif score <= 59 and score >= 0: print("They scored" , score , "whitch is below 60 their result is F")