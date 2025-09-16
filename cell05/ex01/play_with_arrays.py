#!/usr/bin/env python3

ori_lst = [2, 8, 9, 48, 8, 22, -12, 2]
new_lst = []

for i in range(len(ori_lst)) :
    new_lst.append(ori_lst[i] + 2)

print(f"Original array: {ori_lst}")
print(f"New array: {new_lst}")