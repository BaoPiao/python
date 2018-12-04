def bubble_sort(collection):
	'''
	冒泡排序的实现，
	param collection:一个可比类型的数据
	return: 返回同一个经过排序的collection
	'''
	
	lenght=len(collection)
	for i in range(lenght-1):
		swapped=False
		for j in range(lenght-1-i):
			if collection[j]>collection[j+1]:
				swapped=True
				collection[j],collection[j+1]=collection[j+1],collection[j]
				yield  collection
		if not swapped:break#如果此次比较没有交换，则结束外层循环。
		
		
	
	
	
if __name__ == "__main__":
	user_input=input('Enter number separated by a comma:').strip()
	
	unsort = [int(i) for i in user_input.split(',')]
	print(*bubble_sort(unsorted,sep=","))