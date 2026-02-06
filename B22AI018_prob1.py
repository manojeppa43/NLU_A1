import re
from datetime import date

#we hardcode these so we can use them for the 
# spelling mistakes/ different formats in birthdate function
MONTHS= {
    "jan":1, "january":1,
    "feb":2, "february":2,
    "mar":3, "march":3,
    "apr":4, "april":4,
    "may":5,
    "jun":6, "june":6,
    "jul":7,"july":7,
    "aug":8, "august":8, "augst":8,
    "sep":9, "sept":9, "september":9,
    "oct":10,"octo":10,"october":10,
    "nov":11, "november":11,
    "dec":12, "december":12,
}

def full_name():
    '''
    Docstring for full_name
    this function takes the input of user name and detects the surname 
    Note: This takes input from user until user enters a valid and full name 
    '''
    name = input(">> ").strip() #This returns the user input with front and back space removed
    if re.match(r"^[A-Za-z]+(\s+[A-Za-z]+)+$",name):
        first_name= name.split()[0] #first name 
        surname= name.split()[-1]# assumes last names as surname (works for most of the cases)
        print(f"Reggy++: Nice to meet you {first_name}!!")
        print(f"Reggy++: I noticed your surname is {surname}!!")
        return first_name, surname
    else:
        print(f"Reggy++: I dont think that looks like a full name!!")
        print(f"Reggy++: Can you tell me your full name again??")
        return full_name()

def birthdate():
    day= month= year= None
    # we take the bday input and remove spaces and convert it to lowercase
    date_input = input(">> ").strip().lower()
    # we try to match the format of dd-mm-yyyy, dd-mm-yy, mm/dd/yyyy,dd.mm.yyyy, dd mm yyyy
    match_date_format = re.match(r"^(\d{1,2})[.\-/\s](\d{1,2})[.\-/\s](\d{2,4})$", date_input)
    if match_date_format:
        day, month, year= map(int, match_date_format.groups())

    else:
        #we try to match the format dd MONTH yyyy,dd/MONTH/yyyy, dd/MONTH/yy, dd.MONTH.yyyy
        match_date_format= re.match(r"^(\d{1,2})[.\-/\s]([a-z]+)[.\-/\s](\d{2,4})$", date_input)
        if match_date_format:
            day= int(match_date_format.group(1))
            month_name= match_date_format.group(2)
            year= int(match_date_format.group(3))

            if month_name in MONTHS:
                month= MONTHS[month_name]
            else:
                print(f"Reggy++: Invalid Month name.")
                return birthdate()
        # if no format matches we ask the input again 
        else:
            print(f"Reggy++: Invalid date format. Try again.")
            return birthdate()
        
    if year<100: # cause the ones born in 90's mostly enter last two digits
            # but some from 2000's also enter only 2 digits 
            # so we find remainder by diving with 100 and check with current year
            current_year= date.today().year %100
            if year<= current_year:
                year+= 2000
            else:
                year+= 1900
    today= date.today()
    age= today.year- year
    # if birthday has not occured in this year we do age -1
    if (today.month, today.day)< (month,day):
        age-=1
    
    print(f"Reggy++: You are {age} years old!!")

def mood(first_name):
    '''
    Docstring for mood
    
    :param first_name: Takes the first_name as input
    returns a response based on the user's mood
    it deals with some minor spelling mistakes
    '''
    #we take input here
    user_mood= input(">> ").strip().lower()
    #we try to match various patterns(handcoded ones)
    #first we check for negative phrases
    if re.search(r"\b(not\s+good|not\s+happy|not\s+okay|not\s+fine)\b",user_mood):
        print(f"Reggy++: I'm sorry to hear about that, {first_name}.")
        return

    #happy patterns
    if re.search(r"\b(hap+y+|great+|awesome+|joy+|excite+d*)\b|^good$",user_mood):
        print(f"Reggy++: That's great to hear {first_name}!!!")
        print("Reggy++: Keep Smiling!!")
        return 
    
    #sad patterns
    if re.search(r"\b(sad+|down+|low+|unhap+y*)\b",user_mood):
        print(f"Reggy++: I'm sorry that you are feeling this way, {first_name}!!")
        print(f"Reggy++: Don't Worry, Things will get better soon!! ")
        return  
    
    #angry patterns
    if re.search(r"\b(angr+y|angri+|mad+|furious+)\b",user_mood):
        print(f"Reggy++: Take a deep breath {first_name}!!")
        print(f"Reggy++: Slow down things for a moment!!")
        return 
    #tired patterns
    if re.search(r"\b(tired+|exhaust+ed*|sleep+y*)\b",user_mood):
        print(f"Reggy++: Sounds like you need some good rest ,{first_name}!!")
        print(f"Reggy++: Please take care of yourself ,{first_name}!!")
        return 
    
    #okay or kind of neutral cases
    if re.search(r"\b(ok+ay*|fine+|well+|normal+)\b",user_mood):
        print(f"Reggy++: Got it {first_name}, Hope today turns out even better!!")
        return 
    
    #stressed/depressed patterns
    if re.search(r"\b(stress+ed*|depress+ed*)\b",user_mood):
        print(f"Reggy++: That sounds tough, {first_name}.")
        print(f"Reggy++: You're not alone. Take things one at a time.")
        print(f"Reggy++: If this feeling continues, talking to a professional might help.")
        return
    
    #if nothing matches 
    print(f"Reggy++: Thanks for sharing, {first_name}. I'm here if you want to talk!!")

def main():
    #Basic Intro at the start of the bot
    print("Hi! Myself Reggy++ a chatbot designed By Manoj Eppa")
    print("Reggy++: What's your name, mate??")

    # call the full_name() function
    first_name,surname= full_name()
    print(f"Reggy++: When were you born {first_name}??")

    # call the birthdate function
    birthdate()
    print(f"Reggy++: How's Your mood today {first_name}??")

    #call the mood function
    mood(first_name)

    #saying thnaks at the end
    print(f"Reggy++: Thanks for chatting with me today, {first_name}!!")
    print(f"Reggy++: Have a great day ahead!!")
    print(f"Reggy++: cheers!!")

if __name__ == "__main__":
    main()# default call