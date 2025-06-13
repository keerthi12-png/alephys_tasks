import json

#so i have taken my file name as mytest.json
with open('mytest.json','r') as files:
    send=json.load(files)

print('if u want to enter all the expences and salary and find the amount saved please enter word called "user"')
print('if u want to take the data from the json please enter word called "file"')
a1=input('enter at 1 from the above:')
if(a1=='user'):
    n=int(input('enter the salary:'))
    p=int(input('enter the number of expenses like 2 or 3  or 1:  '))
    s=0
    for o in range(0,p):
        q=input("enter the expenses such as food ,rent,travels: ")
        if(q=='rent' or q=='food' or q=="travels"):
            r=int(input('enter the amount :'))
            s=s+r
        else:
            print('please the valid expences and run the program again ')
    print("--------------------------------")
    print("Monthly Expense Summary Tool")
    print("--------------------------------")
    print("Total monthly Income ===> ",n)
    print("Total expenses    ======>",s)
    print('Remaining balance ======>' ,n-s)
elif(a1=="file"):
    for k in send:
        l=0

        l=l+k["Travel"]+k["rent"]+k["Food"]
        print("So monthly saved amount for user",k["id"],"is",k["salary"]-l)
else:
    print("Please enter the proper choice and start again")

    