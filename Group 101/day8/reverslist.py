# student = ["nika","ana","beka","mamuka","dachi","iva","farna"]

# new_list = []

# for char in student:
#     new_list = [char] + new_list

# print(new_list)


student = ["nika","ana","beka","mamuka","dachi","iva","farna"]




newlist = []
i = len(student)
while i > 0:
    newlist.append(student[i -1])
    i -= 1
print(newlist)