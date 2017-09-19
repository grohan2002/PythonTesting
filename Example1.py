import datetime
now = datetime.datetime.now()
curr_year = now.year
#print curr_year
name = raw_input("Enter your name\t");
age = int(raw_input("Enter your age\t"));
#print "The year you will be 100 yrs old is "
x = 100
yrs_to_hundred = x - age
yrs_when_hundred = curr_year +  yrs_to_hundred

print  "The year you will turn 100 yrs old is %d" %yrs_when_hundred
