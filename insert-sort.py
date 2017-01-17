#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import time

def insert_sort(input_list):
	for i in range(1, len(input_list)):
		j = i - 1
		while (j >= 0) and (input_list[j] > input_list[i]):
			j = j - 1
		input_list.insert(j + 1, input_list.pop(i))
	return input_list

def insert_sort_reverse(input_list):
	for i in range(1, len(input_list)):
		j = i - 1
		while (j >= 0) and (input_list[j] < input_list[i]):
			j = j - 1
		input_list.insert(j + 1, input_list.pop(i))
	return input_list

def get_time(list):
	timeStart = time.time()
	after_sort = insert_sort(list)
	timeEnd = time.time()
	return round(1000 * (timeEnd - timeStart))

def check():
	size_lists = [100, 1000, 2000]
	list_items=[]

	max_range = 10

	for size in size_lists:
		sum_time = 0;
		for x in range(1, max_range):
			list_items = [int(1000*random.random()) for i in range(size)]
			sum_time += get_time(list_items)
		print("ms for counting", len(list_items), "by", max_range, "iterations -", sum_time / max_range)


check()

