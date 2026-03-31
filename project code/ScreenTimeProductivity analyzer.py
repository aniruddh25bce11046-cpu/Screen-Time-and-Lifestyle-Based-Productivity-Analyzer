#Viyarthi project screentime vs Productivity
#“Screen Time and Lifestyle Based Productivity Analyzer”
def ValidOutput():
    while True:
        print("\nenter your daily hours (dont go above 24 hours to get valid output)")

        try:
            screentime = float(input("screen hrs: "))
            sleeptime = float(input("sleep hrs: "))
            studytime = float(input("study hrs: "))
            exercisetime = float(input("exercise hrs: "))
            mealtime = float(input("meal time hrs: "))
        except:
            print("invalid input try numbers only")
            continue

        total_hours = screentime + sleeptime + studytime + exercisetime + mealtime

        # checking if total exceeds a day
        if total_hours > 24:
            print("uhh total > 24... doesn't make sense, enter again\n")
        else:
            break

    return screentime, sleeptime, studytime, exercisetime, mealtime


def totalTime(screentime, sleeptime, studytime, exercisetime, mealtime):
    score = 0

    # screen logic
    if screentime <= 3:
        score += 2
    elif screentime <= 6:
        score += 1
    else:
        score -= 2   # too much screen

    # sleep logic
    if sleeptime >= 7:
        score += 2
    elif sleeptime >= 5:
        score += 1
    else:
        score -= 1   # not enough sleep

    # study
    if studytime >= 5:
        score += 2
    elif studytime >= 3:
        score += 1
    else:
        score -= 1

    # exercise
    if exercisetime >= 1:
        score += 1
    else:
        score -= 1

    # meals
    if 1 <= mealtime <= 2:
        score += 1
    elif mealtime > 3:
        score -= 1   # too much time eating 

    return score


def productivity(score):
    # deciding level based on score
    if score >= 5:
        level = "High"
    elif score >= 2:
        level = "Medium"
    else:
        level = "Low"

    return level


def suggestion(screentime, sleeptime, studytime, exercisetime, mealtime, score):
    print("\n     Suggestions ")

    if screentime > 7:
        print("reduce screen time ")

    if sleeptime < 6:
        print("sleep needed, your body is tired")

    if studytime < 3:
        print("study more")

    if exercisetime < 1:
        print("add some physical activity")

    if mealtime > 3:
        print("too much time on meals")

    if score >= 5:
        print("overall good routine ")


# main program starts here
print("productivity checker (basic version)\n")
data = ValidOutput()

# unpacking tuple 
sc, sl, st, ex, ml = data
score = totalTime(sc, sl, st, ex, ml)
level = productivity(score)
used = sc + sl + st + ex + ml
left = 24 - used

print("\nresult")
print("productivity", level)
print("score =", score)
print("\ntime usage ")
print("used hours ", used)
print("remaining ", left)

if left > 0:
    print("you still have some free time utilize or relax")
suggestion(sc, sl, st, ex, ml, score)
print("\n closing system end of program.., ")