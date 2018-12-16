5 / 3
5 % 3
5.0 / 3
5/3.0
5.2 % 3
2000.3 ** 200
1.0 + 1.0 - 1.0
1.0 + 1.0e20 - 1.0e20
1.0e20
5**2
float(123)
float('123')
float('123.23')
int(123.23)
# THROWS VALUE ERROR
# int('123.23')
int(float('123.23'))
str(12)
str(12.2)
bool('a')
bool(0)
bool(0.1)
range(5)

for i in range(5):
    print(i)

numberFound = 0
x = 11
while numberFound < 20:
    if x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
        print(x)
        numberFound = numberFound + 1
    x = x + 1


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    #from 2 to x?
    #x//2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


print(is_prime(17))

print(is_prime(14))


17 ** 0.5

myList = [1, 2, 3, 4, 5, 6]


def printList(aList):
    for item in aList:
        print(item)


def reverseAList(aList):
    print(aList[::-1])


printList(myList)
reverseAList(myList)


def myLenFunct(aList):
    length = 0
    aListAsString = str(aList)
    for i in aListAsString:
        length += 1
    return length


myLenFunct(myList)


aList = [23, 43, 12, 54, 0]
printList(aList)
bList = aList

bList[1] = 777
print("\n")
printList(aList)


cList = aList[:]
cList[2] = 888
print("\n")
printList(aList)


def set_first_elem_to_zero(l):
    l[0] = 0
    return l


set_first_elem_to_zero(aList)


#consider having a list with lists as elements [[1,3],[3,6]]
#write a function that takes such a list, and returns a list with as elements the elements of the sublists
list_of_lists = [[1, 3], [3, 6]]
# print(len(list_of_lists[0]))


def list_merger(list_to_merge):
    # remember to read from right to left with list comps
    #so, for item in sublist for which sublist is in list get the item and store in newlist
    returnable_list = [item for sublist in list_to_merge for item in sublist]
    return returnable_list


list_merger(list_of_lists)


#input of the funct is list w nums the funct returns the product of the numbers in the list
def iteration_version_prod(l):
        x = 1
        for i in range(0, len(l)):
            x = x * l[i]
        return x


print(iteration_version_prod([10, 20, 30]))

# def recursive_version_prod(item, l):
#     if l is None or l is 0:
#         return 0
#     else:
#         iteration_version_prod(l)


def recursive_version_prod(x, l):
    if not l:
        return x
    else:
        element = l.pop()
        x *= element
        returnableList = l
        return recursive_version_prod(x, returnableList)


print(recursive_version_prod(1, [10, 20, 30]))
