questions=["Who is the prime minister of India?","What is the color of mango?","Which is the largest state of India?","What is the capital of India?"]


options=[["Narendra Modi","Amit Shah","Rahul Gandhi","Pranab Mukherjee"],["Pink","Maroon","White","Yellow"],["Haryana","Assam","Rajasthan","Telangana"],[" New Delhi","Ahemdabad","Chandigarh","Kolkata"]]

solutions=[1,4,3,1]
lifeline=[["Narendra Modi","Pranab Mukherjee"],["Maroon","Yellow"],["Assam","Rajasthan"],[" New Delhi","Kolkata"]]
lifesol=[1,2,2,1]


i=0
s=0
count=0
while(i<len(questions)):
    print(questions[i])
    j=0
    k=0
    while(j<len(options[i])):
        print(j+1,".",options[i][j])
        j+=1
    ans=int(input("choose your answer:-"))
    if ans==solutions[s]:
        print("Congrats this is the right answer.")
    elif ans==5050:
        if count!=0:
            print("5050 lifeline is used")
        else:
            while(k<len(lifeline[i])):
                print(k+1,".",lifeline[i][k])
                k+=1
        count+=1
        ans=int(input("choose your answer:-"))
        if ans==lifesol[i]:
            print("Congrats this is the right answer.")
        else:
            print("wrong answer")
            break       
    else:
        print("wrong answer")
        break
    s+=1
    i+=1