# automatedAlarm.py
# by _______

def automatedAlarm(day, noSchool):
	weekends = ["saturday","sunday"]
	weekdays = ["monday","tuesday","wednesday","thursday","friday"]
	if day.lower() in weekends:
		return "9:00"
	elif day.lower() in weekdays and noSchool:
		return "9:30" if day.lower() == "monday" else "8:30"
	else:
		return "7:30" if day.lower() == "wednesday" else "7:00"



# Make sure it returns a value

if __name__ == '__main__':
    x = automatedAlarm("wednesday",True)
    print (x)
