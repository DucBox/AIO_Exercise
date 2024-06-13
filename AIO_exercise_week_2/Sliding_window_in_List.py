num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
max_list = []

for i in range(len(num_list) - k + 1):
    sub_max = 0
    for j in range(i, i+k):
        if num_list[j] > sub_max:
            sub_max = num_list[j]
    max_list.append(sub_max)

print(max_list) 