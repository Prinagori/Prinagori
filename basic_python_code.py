##########################################################################
##############################  Question-1  ##############################
##########################################################################

#importing datetime package
import datetime; 

#Getting the current date time!
currentTime = datetime.datetime.now(); 

#future date
futureTime = datetime.datetime(2030, 12, 1);  

#time period calculations
diffTime = futureTime - currentTime; 
wholeYears = (diffTime.days//365); 

#Using Compound intrest formula
finalBalance = (1.05**wholeYears)*10000;
print("Your Final account balance on December 1, 2030 would be \t"+ str(finalBalance));


##########################################################################
##############################  Question-2  ##############################
##########################################################################

#------------------------------------------------------------------------#
#-----------------------------  PART-A  ---------------------------------# 
#------------------------------------------------------------------------#

#importing random package 
import random;

#Setting initial balance to 3
balance = 3; 
coinFlip =0; 
while (balance > 0):  
    flipResult = random.randint(0, 1) # flipResult=0 -> loss ||||| flipResult=1 -> win
    if(flipResult == 0): #Reduce balance on flip loss        
        balance -= 1; # 0 is for loss so we will subtract 1 from balance.
        coinFlip += 1; # increasing number of coinFlip by one.
       
    else:  #Increase balance on flip win        
        balance += 1; # 1 is for win so we will add 1 in balance.
        coinFlip += 1; # increasing number of coinFlip by one.
        
print("Number of times coin was flipped was :\t"+str(coinFlip));

#------------------------------------------------------------------------#
#-----------------------------  PART-B  ---------------------------------# 
#------------------------------------------------------------------------#

y = []; 
# creating a loop for 100 counts.
for x in range(100):
    import random;
    balance = 3;
    coinFlip =0;
    while (balance > 0):
        flipResult = random.randint(0, 1) 
        if(flipResult == 0):
            balance -= 1;
            coinFlip += 1;
        else:
                balance += 1;
                coinFlip += 1;
    print("Number of times coin was flipped was :\t"+str(coinFlip));
    y.append(int(coinFlip)); #Inserting the coinFlips in a list og y[].
    
print("Maximum  number of coin flips until the gambler wentbroke was :\t" + str(max(y)));
print("Minimum  number of coin flips until the gambler wentbroke was :\t" + str(min(y)));
