from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  new_arr_1 = nums1[0:m]
  new_arr_2 = nums2[0:n]
  sorted_array = []
  if m>n:
    for x in range(len(new_arr_1)):
      if new_arr_1[x] < new_arr_2[x]:
        sorted_array.append(new_arr_1[x])
      else:
        sorted_array.append(new_arr_2[x])
  elif m>n:
    for x in range(len(new_arr_1)):
      if new_arr_1[x] < new_arr_2[x]:
        sorted_array.append(new_arr_1[x])
      else:
        sorted_array.append(new_arr_2[x])
       
# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
print(nums1)
