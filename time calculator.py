import datetime

now = datetime.datetime.now()
print
print ("Current date and time")
print (now.strftime("%H:%M"))


# 1 hour = Rs 800
a=int(input(" Enter your hour="))
b=int(input("Enter your minute="))
if a<24 and b<60:
# Converting Hours and Minutes into Second
    if a<24:
        s=a*3600
        print (s)
    else:
        print(error)
    if b<60:
        m=b*60
        print(m)
    else:
        print(Error)
# Calculating Rs per second as [(Rs800/Sec3600)=Rs 0.22222222 per Sec]
    sum=(s+m)*0.22222222
    print (sum)

else:
    print(Error)




