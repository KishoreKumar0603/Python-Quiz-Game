print("___Welcome T0 Quiz Game___")
in1=input("Do You Want To Play : ").lower()

if in1!="yes":
    print("Thank You...")
    quit()

score=0
#quiz 1
q1=input("1.Python is What Level of language : ").lower()
if q1=="high level" or q1=="high level language":
    print("Correct!!!")
    score+=1
else:
    print("InCorrect!!!")
#quiz 2 
q2=input("2.Who Designed Python : ").lower()
if q2=="guido van rossum":
    print("Correct!!!")
    score+=1
else:
    print("InCorrect!!!")
#quiz 3
q3=input("3.When Python Was Developed : ").lower()
if q3=="1991":
    print("Correct!!!")
    score+=1
else:
    print("InCorrect!!!")
#quiz 4 
q4=input("4.Is Python Case Sensitive : ").lower()
if q4=="yes":
    print("Correct!!!")
    score+=1
else:
    print("InCorrect!!!")
#quiz 5 
q5=input("5.FullForm for OOP: ").lower()
if q5=="object oriented programming":
    print("Correct!!!")
    score+=1
else:
    print("InCorrect!!!")
#quiz 6 
q6=input("6.Which Funtion is Used to find the string in Upper Case or Not: ").lower()
if q6=="isupper()" or q6==".isupper()" or q6=="isupper":
    print("Correct!!!")
    score+=1
else:
    print("InCorrect!!!")
#quiz 7 
q7=input("7.What keyword is make program come out from loop : ").lower()
if q7=="break":
    print("Correct!!!")
    score+=1
else:
    print("InCorrect!!!")
#quiz 8
q8=input("8.Which keyword is use to print : ").lower()
if q8=="print":
    print("Correct!!!")
    score+=1
else:
    print("InCorrect!!!")
#quiz 9 
q9=input("'192' convert this to string : ").lower()
if q9=="str(192)":
    print("Correct!!!")
    score+=1
else:
    print("InCorrect!!!")
#quiz 10 
q10=input("10.Is Python Hard To Learn : ").lower()
if q10=="no":
    print("Correct!!!")
    score+=1
else:
    print("InCorrect!!!")

print("You Answered ",str(score)," Questions Correctly ")
print("You Answered ",(score/10)*100,"%")
   
