# Write a program to count uppercase and lowercase letters in a string.
"""
Method 1

S = "EnvirOnmEnT"

uppercase = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
upper_count = 0


lower_count = 0

for i in S:
    if i in uppercase:
        upper_count += 1

    else:
        lower_count += 1    


print("uppercase",upper_count)  
print("lowercase",lower_count)      



S = "EnvirOnmEnT"


# method 2

uppercase = 0

lowercase = 0

for i in S:
    if i.isupper():
        uppercase += 1

    else:
        lowercase += 1

print("uppercase",uppercase)
print("lowercase",lowercase)            

"""

#######################################################################################
"""
# Write a program to count digits present in a string.

A = "NKNJ27hkj67KK"


digits_count = 0

for i in A:
    if i.isdigit():
        digits_count += 1

print("digits_count",digits_count)   
"""
######################################################################################

# Write a program to count special characters in a string.

"""
S = "hjgf#jv@hvgc$"

count = 0


for i in S:
    if not (i.isalnum()):
        count += 1

print("S_symbols_counts",count)        

"""

###################################################################################################
#Write a program to remove all spaces from a string.
"""
S = "  India is my country   "

A = S.replace(" ", "")

print(A)
"""

################################################################################################

# Write a program to find the frequency of each character in a string.
"""
S = "  India is my country   "

freq = {}

for i in S:
    if i in freq:
        freq[i] += 1

    else:
        freq[i] = 1

print(freq)                

"""

#################################################################################################

#Write a program to find the first non-repeated character in a string.
"""
S = "my name is om gore"

freq = {}

for i in S:
    if i in freq:
        freq[i] += 1

    else:
        freq[i] = 1


for i in S:
    if freq[i] == 1:
        print("first repeated chracter is :",i)
        break;        

"""

#######################################################################################

# Write a program to count the number of words in a string without using split().
"""
s = "india is my country all indians are my brothers and sisters"

count = 0

for i in s:
   if i == " ":
      count += 1

words = count + 1

print(words)

"""
#######################################################################################

# Write a program to find the longest word in a sentence.
"""
s = "india is my country all indians are my brothers and sisters"

A = s.split()

longest = ""

B = 0

for i in A:
    if len(i) > B:
        B = len(i)

for j in A:
    if len(j) == B:
        print(j)       

"""

#########################################################################################
"""
#Write a program to check whether two strings are anagrams.

A = "Listen"

B = "Silent"

freq_A = {}

freq_B = {}

lower_A = (A.lower())
lower_B = (B.lower())

len(lower_A) == len(lower_B)

for i in lower_A:
    if i in freq_A:
        freq_A[i] += 1

    else:
        freq_A[i] = 1


for j in lower_B:
    if j in freq_B:
        freq_B[j] += 1

    else:
        freq_B[j] = 1  

if freq_A == freq_B:
    print("Anagrams")

else:
    print("Not Anagrams")  
"""
########################################################################################                 
"""
# Write a program to find the second-largest number in a list without using sort() or max().

N = [23,60,10,4,90,100]

largest = N[0]

S_largest = float('-inf')

for i in N:
    if i > largest:
        S_largest = largest
        largest = i

    elif i < largest and i > S_largest:
        i = S_largest
print(S_largest)        

"""
#################################################################################################

# Write a program to separate positive and negative numbers from a list.
"""
L = [2,3,-4,5,-6,3,-8,7,2,-1]


p_tive = [ ]

n_tive = [ ]

for i in L:
    if i > 0:
        p_tive.append(i)
        
for j in L:
    if j < 0:
        n_tive.append(j)

print("positive No",p_tive)
print("negative No",n_tive)

"""
###################################################################################################

# Write a program to find common elements between two lists.
"""
L1 = ["a","b","c","d","e","f","g","h"]

L2 = ["c","z","e","i","j","k","a"]

comman_words = [ ]


for i in L1:
    if i in L2:
        comman_words.append(i)
print(comman_words)        

"""
##################################################################################################

# Write a program to merge two lists without using the + operator.
"""
L1 = ["ram","mohan","om","shyam"]

L2 = ["mauli","suraj","sumit","ketan"]

N_l1 = [ ]

for i in L1:
    N_l1.append(i)

for j in L2:
    N_l1.append(j)

print(N_l1)  

"""
##################################################################################################

# Write a program to find the frequency of each element in a list.
"""
L1 = ["a","b","c","a","g","c","m","k","b","a","i","b"]

freq = {}

for i in L1:
    if i in freq:
        freq[i] += 1

    else:
        freq[i] = 1

print(freq)

"""
##################################################################################################

# Write a program to move all zeros to the end of a list.
"""
L1 = [1,2,3,0,6,9,3,6,1,9,0,4,5,7,0,4,6,79,0,0,5,8]

N_List = [ ]

Z_list = [ ]

for i in L1:
    if i != 0:
        N_List.append(i)

    else:
        Z_list.append(i)

result = N_List + Z_list 

print(result)

"""
####################################################################################################

# Write a program to rotate a list by one position to the right.
"""
L1 = [1,2,3,4,5,6,7,8,9,0]

result = [L1[-1]] + L1[:-1]

print(result)

"""
######################################################################################################

# Write a program to find the missing number from a list of consecutive numbers.
"""
L1 = [1,3,4,5,6,7,8]

S = min(L1)

L = max(L1)

expected_sum = L * (L + 1) // 2 

Actual_sum = sum(L1)

missing_no = expected_sum - Actual_sum

print(missing_no)

"""
#####################################################################################################

# Write a program to remove all negative numbers from a list.
"""
L1 = [1,3,7,-2,8,4,-5,8,-10]

for i in L1:
    if i < 0:
        L1.remove(i)

print(L1)        

"""
####################################################################################################

# Write a program to find the sum of elements at even and odd indexes separately.
"""
L1 = [ 1,2,3,4,5,6,7,8,9,10]

even = [ ]

odd = [ ]

for i in L1:
    if i % 2 == 0:
        even.append(i)

    else:
        odd.append(i)


S_E = sum(even)

S_O = sum(odd)


print("sum of even numbers",S_E)
print("sum of odd numbers",S_O)

"""

#######################################################################################################

# Write a program to find the second-largest element in a tuple.
"""
T = (10,23,13,5,57,34,90,14,99)

A = list(T)

A.sort()

print(A[-2])

"""
#####################################################################################################

# Write a program to find the frequency of each element in a tuple.
"""
T = ("a","b","c","a","c","k","a","b")

freq = { }

for i in T:
    if i in freq:
        freq[i] += 1

    else:
        freq[i] = 1


print(freq)        
"""
####################################################################################################

# Write a program to find the index of a particular element without using index().

# T = (10,23,13,5,57,34,90,14,99)

# for i in range(0,len(T)):
#     print(i,"is Index of-->",T[i])

#####################################################################################################

# Write a program to separate positive and negative numbers from a tuple.
"""
T = (10,-23,13,-5,57,34,90,-14,99)

p_tive = [ ]

n_tive = [ ]

for i in T:
    if i > 0:
        p_tive.append(i)

    else:
        n_tive.append(i)

print("positive no's",p_tive)
print("negative no's",n_tive)            

"""
###################################################################################################

# Write a program to create a new tuple containing only numbers divisible by 3.
"""
T = (1,2,3,12,56,9,4,18,27,23,30,21)

D = [ ]

N_D = [ ]



for i in T:
    if i % 3 == 0:
        D.append(i)

    else:
        N_D.append(i)

print(D)        

"""
########################################################################################################

# Write a program to swap the first and last elements of a tuple.
"""
T = (10,23,13,5,57,34,90,14,99)

L = list(T)

L[0] , L[8] = L[8] , L[0]

T = tuple(L)

print(T)

"""
######################################################################################################

# Write a program to find common elements between two tuples.
"""
T1 = (1,2,3,4,5,11,16,2,9,3,10,5)

T2 = (61,62,1,68,4,89,11,4,10,3,16)

common_num = [ ]

for i in T1:
    if i in T2:
        common_num.append(i)

print("common numbers: ",common_num)

T_C_num = tuple(common_num)

print(T_C_num)

"""
################################################################################################

# Write a program to convert a nested tuple into a single tuple.
"""
T = (1,2,3,4,5,(6,7,8,9,10))

A = T[:4]

B = T[5]

new_tuple = A + B

print(new_tuple)

"""

##############################################################################################

# Write a program to check whether all elements in a tuple are unique.
"""
T1 = (1,2,3,4,5,11,16,2,9,3,10,5)



for i in T1:
    T = T1.count(i)
    
    if T < 2:
        print("unique",i)

    else:
        print("common",i)

"""
######################################################################################################

# Write a program to create a tuple containing only strings from a mixed tuple.
"""
T1 = (1,"rr",3,4,"om",11,16.43,2,"ram",[3,10],5)

S_T = [ ]

for i in T1:
    if type(i) == str :
        S_T.append(i)

Tuplestring = tuple(S_T)       

print(Tuplestring)

"""
#######################################################################################################

# Write a program to find the student with the lowest marks.
"""
students = {"om" : 90 , "ketan" : 98 , "sumit" : 85 , "rohan" : 60 , "sonya" : 75}

Low_m = min(students, key=students.get)

print("students with lowest marks:",Low_m)
print("Lowest marks",students[Low_m])

"""
#######################################################################################################

# Write a program to calculate the average marks of all students.
"""
students = {"om" : 90 , "ketan" : 98 , "sumit" : 85 , "rohan" : 60 , "sonya" : 75}

avg_marks = sum(students.values()) / len(students)

print("Average marks of all students: ",avg_marks)

"""
###################################################################################################

# Write a program to find students who scored more than the average marks.
"""
students = {"om" : 90 , "ketan" : 98 , "sumit" : 85 , "rohan" : 60 , "sonya" : 75}

avg_marks = sum(students.values()) / len(students)

marks = students.values()

for i,j in students.items():
    if j > avg_marks:
        print(i,j)
"""
###################################################################################################

# Write a program to find the employee with the highest salary.
"""
D = {"om" : 45000 , "ketan" : 50000 , "sumit" : 35000 , "rohan" : 25000}

highest_salary = max(D.values())

for i,j in D.items():
    if j == highest_salary:
        print(i,j)
        
"""
#######################################################################################################

# Write a program to increase every employee's salary by 10%.
"""
D = {"om" : 45000 , "ketan" : 50000 , "sumit" : 35000 , "rohan" : 25000}

for i,j in D.items():
    I = j * 10 / 100
    print(i,j+I)
       """
##################################################################################################

# Write a program to merge two dictionaries without using the update() method. 
"""
D = {"om" : 45000 , "ketan" : 50000 , "sumit" : 35000 , "rohan" : 25000}

D2 = {"suraj" : 10000 , "miraj" : 30000 , "sharayu" : 20000}

result = { }

for i,j in D2.items():
    D[i] = j

print(D)

"""

###################################################################################################

# Write a program to find common keys between two dictionaries.
"""
D = {"om" : 45000 , "ketan" : 50000 , "sumit" : 35000 , "rohan" : 25000}

D2 = {"suraj" : 10000 , "om" : 30000 , "ketan" : 20000}


c = [ ]

for i,j in D.items():
    if i in D2:
        print("common keys",i)

"""
###################################################################################################

# Write a program to create a new dictionary containing only values greater than 50.
"""
N = 61

D = { }


if N > 50:
   D["number"] = N

print(D)       

"""
#####################################################################################

# Write a program to swap keys and values in a dictionary.

D = {"om" : 45000 , "ketan" : 50000 , "sumit" : 35000 , "rohan" : 25000}
"""
S_num = { }

for i,j in D.items():
    S_num[j] = i

print(S_num)    

"""

######################################################################################################

# Write a program to find the frequency of each character in a string using a dictionary.

D = "abcdeakiobjjgcjaa"
D1 = { }

for i in D:
    if i in D1:
        D1[i] += 1

       
    else:
        D1[i] = 1

print(D1)    

####################################################################################################