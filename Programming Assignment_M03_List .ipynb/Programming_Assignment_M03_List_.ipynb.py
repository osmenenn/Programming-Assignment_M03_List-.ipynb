
#Ismoil Boboev 
#M03 Programming Assignment 
#List and Functions 
#Last updated: 9/27


years_list = [1999, 2000, 2001, 2002, 2003, 2004, 2005]


print(*years_list)

print("I was three years old at " )

print(years_list[3])

print("I was the oldest in year of, ")

print(years_list[6])


#creating list of things 

things_list = ["CINDERALL", "Mozzerella ", "Salmonella"]

print(*things_list)

everything_list = ["Anything ", "litrally ", "let me tell you ", "about it hehe"]
print(*everything_list)


disease_list = ["Cancer", " Headache", "Childbirth", "COVID-19"] 


print(("The Nobel Price is going to person that has demenishing the disease of ") + str(disease_list[2]))



#this is the 9.1 - 9-2
#9.1 Define a function called good() that returns the following list: 
#['Harry', 'Ron', 'Hermione'].

def good():
    return ['Harry', 'Ron', 'Hermione']
print(*good())

#9.2 Define a generator function called get_odds() that returns the odd numbers from range(10). 
#Use a for loop to find and print the third value returned.


limit = 10
get_odds = (num for num in range(limit) if not num % 2 == 0)
count = 0
for num in get_odds:
    if count == 2:
        print(num)
        break
    count += 1


def get_odds():
        for number in range(1, 10, 2):

               yield number

count = 1
for number in get_odds():
  if count == 3:
    print("The third odd number is", number)
    break
count += 1
