# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    most = []
    highest_count = 0

    for num in numbers:
        count = numbers.count(num)
        if count > highest_count:
            highest_count = count
            most = [num]
        elif count == highest_count and num not in most:
            most.append(num)
    return most
    
test1 = [1, 3, 2, 3, 4, 1, 3]
print(most_frequent(test1))

test2 = [5, 6, 7, 8, 9, 5]
print(most_frequent(test2))

edge1 = [5, 6, 5, 7, 8, 6]
print(most_frequent(edge1))

edge2 = [1, 2, 3, 4, 5]
print(most_frequent(edge2))
"""
Time and Space Analysis for problem 1:
- Best-case: 0(n) - Running through each item would not be bad if the input of items is a short list.
- Worst-case: 0(n^2) - For each item, the .count() loops through the whole list. For big lists, this can take up a lot of time.
- Average-case: 0(n^2) - Usually, each item triggers a full scan of the whole list.
- Space complexity: 0(1) - Since you are taking a list, and ultimately reducing some of the variables into another list, this would be linear. No new data structure is being created.
- Why this approach? Every time a number is being checked, it has the chance to be the highest counted number. Checking every number and comparing it the current highest number best fits this coding problem.
- Could it be optimized? I believe it could be optimized using dictionaries or other forms of sorting and checking.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
"""
Time and Space Analysis for problem 2:
- Best-case: O(n) - No choice but to go through the entire list, even if there isn't any duplicates.
- Worst-case: 0(n) - Each item is checked and added into the set and the 'result' list.
- Average-case: 0(n) - Lookups and insertions for sets are 0(1), so this would be constant.
- Space complexity: The space complexity is 0(n) because each item is being stored into a new list and set.
- Why this approach? I chose this approach because we needed to filter out any duplicates. Adding the numbers into a new list
and then checking that list against the rest of the numbers ensures that no more duplicates will be added. If a number remaining is found within the 
'seen' set, then it will skip over it. 
- Could it be optimized? The only way it could be optimized is returning a list that uses the 'set' function to remove duplicates, 
but it would not preserve order.
"""

test1 = [4, 5, 4, 6, 5, 7]
print(remove_duplicates(test1))

edge1 = [1, 1, 1, 1, 1]
print(remove_duplicates(edge1))

edge2 = []
print(remove_duplicates(edge2))

edge3 = [1, 5 ,3, 3, 10000, 999, 1, 10000]
print(remove_duplicates(edge3))

# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((complement, num))))
        seen.add(num)
    return list(pairs)

"""
Time and Space Analysis for problem 3:
- Best-case: 0(n) - Must run through the whole list even if there is a pair that is found early. 
- Worst-case: 0(n) - Each element and pair is checked every time the loop runs.
- Average-case: 0(n) - Each lookup and insert in a set takes a constant time.
- Space complexity: 0(n) - the set and pairs can store up to however many n might equal.
- Why this approach? This approach is best because it ensures that duplicate pairs are not being added while checking for every possible pair.
- Could it be optimized? I think that this is the optimized version by using a set.
"""
test1 = [1, 2, 3, 4]
print(find_pairs(test1, 5))

test2 = [1, 6, 7, 3, 8]
print(find_pairs(test2, 8))

edge1 = [1,2,1,2,1,2]
print(find_pairs(edge1,3))


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1          
    size = 0              # how many items currently in list
    data = []             # simulated list

    for i in range(n):
        if size == capacity:
            print(f"Resizing from {capacity} → {capacity * 2}")
            # simulate copying items to a new, larger list
            new_data = data.copy()
            data = new_data
            capacity *= 2
        
        data.append(i)
        size += 1
        print(f"Added {i}, size={size}, capacity={capacity}")

    print("Final list:", data)

"""
Time and Space Analysis for problem 4:
- When do resizes happen? Resizes happen when the size and the capacity equal the same. When this happens, the capacity doubles in size.
- What is the worst-case for a single append? The worst case is that it must copy all the existing elements to a new, larger list creating O(n).
- What is the amortized time per append overall? Even though sometimes the complexity is O(n), most appends are just O(1).
- Space complexity: Space complexity is O(n) because it grows proportional to its size.
- Why does doubling reduce the cost overall? It reduces the cost because it only resizes very few times compared to the appending of items.
"""
add_n_items(6)

# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    running = []
    current_sum = 0
    for num in nums:
        current_sum += num
        running.append(current_sum)
    return running

#def running_total(nums):
#   for i in range(1, len(nums)):
#        nums[i] += nums[i -1]
#    return nums

"""This new running_total function improves space efficiency by modifying the list in place instead of creating a whole new one."""


"""
Time and Space Analysis for problem 5:
- Best-case: O(n) - We must go through the list completely, keeping a running total for each item.
- Worst-case: 0(n) - Because it has to go through the whole list.
- Average-case: O(n) - Usually with a running total, you have to run through the whole list to get the all the items.
- Space complexity: A list is built with the same size and using all the items, so it would be O(n).
- Why this approach? This approach is simple and clear and adds the sum one by one.
- Could it be optimized? It probably could be optimized but I'm not too sure how it could be.
"""

test1 = [1, 2, 3, 4]
print(running_total(test1))

test2 = [1, 36, 2, 50]
print(running_total(test2))

edge1 = [-2,-3,1,6]
print(running_total(edge1))