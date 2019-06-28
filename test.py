#!/usr/bin/python
# -*- coding: UTF-8 -*-

list_a = [3,1,5,8]
def get_answer(list_a):
	if len(list_a) == 3:
		min_number = min(list_a)
		min_index = list_a.index(min_number)
		if min_index == 0:
			return 1*list_a[0]*list_a[1]+1*list_a[1]*list_a[2]+1*list_a[2]*1
		elif min_index == 2:
			return list_a[1]*list_a[2]*1+list_a[0]*list_a[1]*1+1*list_a[0]*1
		else:
			list_a.pop(min_index)
			max_number = max(list_a)
			max_index = list_a.index(max_number)
			if max_index == 0:
				return list_a[0]*list_a[1]*list_a[2]+list_a[0]*list_a[2]*1+list_a[0]
			else:
				return list_a[0]*list_a[1]*list_a[2]+1*list_a[0]*list_a[2]+list_a[2]
	else:
		min_number = min(list_a)
		min_index = list_a.index(min_number)
		if min_index == 0:
			list_a.pop(min_index)
			return list_a[min_index-1]*list_a[min_index]*1+get_answer(list_a)
		elif min_index == len(list_a)-1:
			list_a.pop(min_index)
			return 1*list_a[min_index]*list_a[min_index+1]+get_answer(list_a)
		else:
			return list_a[min_index-1]*list_a[min_index]*list_a[min_index+1]+get_answer(list_a)
	
if __name__ == '__main__':
    print(get_answer(list_a))