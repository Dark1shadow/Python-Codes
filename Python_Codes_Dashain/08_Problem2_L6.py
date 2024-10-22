ms1 = int(input("Enter the marks of first subject: "))
ms2 = int(input("Enter the marks of second subject: " ))
ms3 = int(input("Enter the marks of third subject: "))
Tmark = int(input("Enter the total marks"))
perc = ((ms1+ms2+ms3)/Tmark)*100
if(perc>40 and ms1>33 and ms2>33 and ms3>33):
    print("You Passed with", perc , "Percentage")
else:
     print("You Failed")