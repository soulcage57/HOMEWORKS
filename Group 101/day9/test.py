def point_calculator():
    numbers = [int(input("type player 1 point: ")), int(input("type player 2 pont: "))]
    sxvaoba = numbers [0] - numbers [1]
    if sxvaoba < 0:
        sxvaoba = sxvaoba * -1

    if numbers [0] > numbers [1]:
        print("player 1 has {} more point ".format(sxvaoba))
    elif numbers [0] < numbers [1]:
        print("player 2 has {} more point".format(sxvaoba))  
point_calculator()































