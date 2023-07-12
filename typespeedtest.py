import time

String="The quick brown fox jumps over the lazy dog."
wordcount=len(String.split())


while True:
    print(String)
    print("-------------------------")
    startTime=time.time()
    textInput=str(input("Type The Sentence:"))
    endTime=time.time()
    accuary=len(set(textInput.split())&set(String.split()))
    accuary=accuary/wordcount*100
    timeTaken=round(endTime-startTime,2)
    wpm=round(wordcount/timeTaken*60)
    print("-------------------------")


    print("your accuary is: ",accuary)
    print("Time taken:",timeTaken,"seconds")
    print("Your typing speed is",wpm,"word per minute")


    if accuary<50 or wpm<30:
        print("You need to practice typing more!")
    elif accuary<80 or wpm<60:
        print("You are doing great!")
    elif accuary<=100 or wpm<=100:
        print("You are a pro in typing!")
    else:
        print("You are a typing achine!!")

    
    tryagain=input("Do you want to try again? (y/n): ")
    
    if tryagain=='n':
        break
    elif tryagain=='y':
        continue


