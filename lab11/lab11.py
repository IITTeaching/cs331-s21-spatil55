
from unittest import TestCase
import random

def quicksort(lst,pivot_fn):
    qsort(lst,0,len(lst) - 1,pivot_fn)

def qsort(lst,low,high,pivot_fn):
    ### BEGIN SOLUTION
    if low<high:
      func = pivot_fn(lst, low, high)
      turner = lst[func]
      h = high+1
      l = low-1
      while l<h:
        h=h-1
        while h>0 and lst[h]>turner:
          h=h-1
        l=l+1
        
        while l<high and lst[l]<turner:
          l=l+1
        
        if l<h:
          temp = lst[l]
          lst[l] = lst[h]
          lst[h] = temp
         
      qsort(lst, low, h, pivot_fn)
      qsort(lst, h+1, high, pivot_fn)
        

    ### END SOLUTION

def pivot_first(lst,low,high):
    ### BEGIN SOLUTION
    return low
    ### END SOLUTION

def pivot_random(lst,low,high):
    ### BEGIN SOLUTION
    return random.randint(low, high)
    ### END SOLUTION

def pivot_median_of_three(lst,low,high):
    ### BEGIN SOLUTION
    mean = (low+high)//2
    quicksort([lst[low], lst[mean], lst[high]], pivot_first)
    if [lst[low], lst[mean], lst[high]][1]==lst[low]:
      return low
    if [lst[low], lst[mean], lst[high]][1]==lst[mean]:
      return mean
    if [lst[low], lst[mean], lst[high]][1]==lst[high]:
      return high
    ### END SOLUTION

################################################################################
# TEST CASES
################################################################################
def randomize_list(size):
    lst = list(range(0,size))
    for i in range(0,size):
        l = random.randrange(0,size)
        r = random.randrange(0,size)
        lst[l], lst[r] = lst[r], lst[l]
    return lst

def test_lists_with_pfn(pfn):
    lstsize = 20
    tc = TestCase()
    exp = list(range(0,lstsize))

    lst = list(range(0,lstsize))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    lst = list(reversed(range(0,lstsize)))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    for i in range(0,100):
        lst = randomize_list(lstsize)
        quicksort(lst, pfn)
        tc.assertEqual(lst,exp)

# 30 points
def test_first():
    test_lists_with_pfn(pivot_first)

# 30 points
def test_random():
    test_lists_with_pfn(pivot_random)

# 40 points
def test_median():
    test_lists_with_pfn(pivot_median_of_three)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_first,
              test_random,
              test_median]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
