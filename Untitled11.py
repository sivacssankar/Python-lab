ab=int(input("enter current year"))
bc=int(input("enter final year"))

if(ab%400==0 or ab%100 or ab%4==0):
    print("current year is a leap year",ab);
print("the leap years are")
for i in range(ab,bc):
    if(i%400==0 or ab%100 or i%4==0):
        print(i)

# In[ ]:




