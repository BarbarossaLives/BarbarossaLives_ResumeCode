#FizzBuzz divisible by 3 and 5
#Fizz by 3
#Buzz by 5
#the number if not divisible by either 

#no line breaks 

def fizzBuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        answer = "FizzBuzz"
    
    elif number % 3 == 0:
        answer = "Fizz"
    
    elif number % 5 == 0:
        answer = "Buzz"
        
    else:
        answer = str(number)
    
    print(answer)    
    return answer

print("what number would you like to test?")
number = input(">>")
number = int(number)
print(number)
sentence = ""
answer = ""
for i in range (1, number+1):
    print(i)
    answer = fizzBuzz(i)
    sentence = sentence + answer
    print(sentence)

print(sentence)