scores = [20, 30, 73, 98, 333, 44, 777, 22, 56, 78, 89, 34]

# max_num = scores[0]

# for score in scores:
#     if score > max_num:
#         max_num = score

# print(max_num)

i = 0

max_num = scores[0]
while i < len(scores):
    if scores[i] > max_num:
        max_num = scores[i]
    i += 1

print(max_num)