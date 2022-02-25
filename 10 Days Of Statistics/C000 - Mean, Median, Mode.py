import statistics as st

# Enter your code here. Read input from STDIN. Print output to STDOUT
total = int(input())
data = input()
arr_data = [int(i) for i in list(data.split(' '))]

# print(arr_data)

# Mean
mean = sum(arr_data) / total
print(mean)

# Median
arr_sort = arr_data.sort()
mid = total // 2
median = (arr_data[mid] + arr_data[~mid]) / 2
print(median)

# Modus
print(st.mode(arr_data))