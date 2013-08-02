"""
Search problems can be solve by sorting first. It becomes trivial.

Notations

collection to be sorted A[i] a(i) is the ith element of that collection.

Since the elements are being compared these three things need to be true for elements p and q in A[i]
p=q
p<q
p>q

Always think of best, worst and average cases

No algo in CS that sorts can be better than O(nlogn) in the average or worst case
"""

#Insertation sort
'''
Best with small number or nearly sorted

Best  O(n )
Average O(n^2)
Worst  O(n^2)

sort() keeps calling insert())

A is sorted in place (no divide and conquering here really)
can do with recursion
'''

def in_sort(a, i):
    """A - is a list"""
    if i == 0: return
    in_sort(a,i-1)
    j=i
    while j >0 and a[j-1]>a[j]:
        a[j-1],a[j] = a[j], a[j-1]
        print a
        j-=1


if __name__ == '__main__':
    a = [3,2,5,6,7,1]
    a =in_sort(a,5)
    print a
