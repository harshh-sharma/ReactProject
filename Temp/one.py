# first we take string by a user
str=input('Enter a string  ')

#  after taking string we apply for loop beacuse string is a iterable
count=0   # initalize count variable with zero
for i in str:
    if i=='a':
        count+=1
    elif i=='e':
        count+=1
    elif i=='i':
        count+=1
    elif i=='o':
        count+=1
    elif i=='u':
        count+=1

# after it we print a result
print(count," vowels")