#age calculator 
print("AGE CALCULATOR")
print(" Assume all years have 365 days")

cur_day= int(input("put today's date = "))
if cur_day>0 and cur_day<=30 : 
    cur_month = int(input("put current month = ")) 
    if cur_month>0 and cur_month<=12:
        cur_year = int(input("put current year = "))
        if cur_year > 1:
            print("Input your bith date")
            birth_day= int(input("Birth day = "))
            if birth_day >0 and birth_day<=30:
                birth_month= int(input("Birth month = "))
                if birth_month>0 and birth_month<=12:
                    birth_year = int(input("Birth year = "))
                    if birth_year >0:
                        print("wait")
                    else:
                        print("Don't waste my time")
                else:
                    print("Don't waste my time")
            else:
                print("Don't waste my time")
        else:
            print("Don't waste my time")
    else:
        print("Don't waste my time")
else:
    print("Don't waste my time")
cur_date = ( cur_day , 'day', cur_month ,'month' , cur_year ,'year')
birth_date= ( birth_day , 'day', birth_month ,'month' , birth_year ,'year')
total_age_in_days= (30-birth_day)+(cur_day)+((cur_year-birth_year-1)*360)+(24-((cur_month+birth_month)*30))+((cur_year-birth_year)*15)
print("Total age in days = ", total_age_in_days)
age_day= (30-birth_day)+(cur_day)
age_month=(24-((cur_month+birth_month)))
age_year= (cur_year-birth_year-1)
age = age_day,'days', age_month, 'months', age_year, 'years'
print("your age is: ",age)

from gtts import gTTS
tts = gTTS(str(age))
tts.save("age.mp3") 
