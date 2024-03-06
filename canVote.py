
#1 GET NAME INPUTS
last_name = input('Enter your lastname: ')

first_name = input('Enter your firstname: ')

#2  WELCOME USER

print(f'Hi {first_name, last_name}, Welcome to our polling unit. Kindly enter your year of birth to confirm your eligibility status')

yearOfBirth = int(input('Enter your Year Of Birth: '))


#3 CHECK IF AGE IS UPTO VOTING AGE
def checkAge(age):
  
   if age < 18 : 
     
     return True
     
   else: 
     
      return False
      
#4 SAVE THE RESULT INTO A VARIABLE
checkAge = checkAge(yearOfBirth)


#5 PRINT OUT RESULT BASED ON CHECKAGE /TRUE OR FALSE
def result():
  if (checkAge): 
    print('Hello You are eligible to vote')
    
  if(not checkAge): 
     print('Hello You are eligible to vote')
     
     
# CALL THE RESULT
result()