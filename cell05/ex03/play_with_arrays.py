#!/usr/bin/env python3

ori_lst = [2, 8, 9, 48, 8, 22, -12, 2]
new_lst = []

for i in range(len(ori_lst)) :
    if (ori_lst[i] + 2) > 5 :
        new_lst.append(ori_lst[i] + 2)

print(ori_lst)
print(set(new_lst))