# ### 8 Question
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. / Учитывая целочисленный массив nums и целое число k, верните k наиболее часто встречающихся элементов. Вы можете вернуть ответ в любом порядке.

def coun_num(nums, k, cnt = 0, list_one = []):
    if len(nums) == 1:
        list_one.append(1)
        print(list_one)

    else:    
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                cnt += 1
                if cnt >= k:
                    list_one.append(nums[i])
    
        print(list_one)

b = input().split()
n = int(input())

coun_num(b, n)
