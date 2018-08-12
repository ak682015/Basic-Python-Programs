# import datetime
# import time

# command = "set a reminder of 10 minutes "
# while True:
# 	now=datetime.datetime.now()
# 	n=str(now.time())
# 	n=n[:5]
# 	#print(n)

# 	#time.sleep(10)
# 	if n == '22:09':
# 		print("Pick up the kids!")
# 		break

def check_reminder():
    """
    Checks if you have any reminder set for today.
    """
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c_year = current_date[0:4]
    c_month = current_date[5:7]
    c_date = current_date[8:10]
    to_del = ''
    reminder_path = os.getcwd() + "/Text_Files/reminder.txt"
    f_reminder = open(reminder_path, "r+")  
    for line in f_reminder:
        r_date = line[0:2]
        if r_date == c_date:
            r_month = line[3:5]
            if r_month == c_month:
                r_year = line[6:10]
                if r_year == c_year:
                    speak("You have a reminder set for today." \
                        "This is what it says: \n" + line[11:])
                    speak("Would you like me to delete the reminder now?")
                    reply = raw_input('\033[1m'+'Username '+'\033[0m')  #modify
                    if confirm(reply) == 1:
                        to_del = line
                        #TO FINISH
    f_reminder.close()