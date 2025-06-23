def most_frequent_smallest(nums):
    freq = {}
    
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    max_freq = 0
    for count in freq.values():
        if count > max_freq:
            max_freq = count

    answer = None
    for num in freq:
        if freq[num] == max_freq:
            if answer is None or num < answer:
                answer = num

    return answer

nums = [1, 3, 1, 3, 2, 1]
print(most_frequent_smallest(nums))  
