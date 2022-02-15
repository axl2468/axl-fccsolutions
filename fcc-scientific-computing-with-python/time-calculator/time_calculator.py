def add_time(start, duration, day=None):
	#Reading the input for calculation
	start_time = start.split()[0]
	start_period = start.split()[1]

	start_hour = start_time.split(":")[0]
	start_minute = start_time.split(":")[1]

	duration_hour = duration.split(":")[0]
	duration_hour = int(duration_hour) #needed for line 18
	duration_minute = duration.split(":")[1]
	
	#Adding the times
	days_passed = 0
	new_minute = int(start_minute) + int(duration_minute)

	if new_minute >= 60:
		duration_hour += int(new_minute/60)
		new_minute -= 60 * int(new_minute/60)
	
	if new_minute < 10:
		new_minute = "0" + str(new_minute)
	else:
		new_minute = str(new_minute)
	
	new_hour = int(start_hour) + int(duration_hour)

	if new_hour >= 12:
		change_period = int(new_hour/12)
		new_hour -= 12 * change_period
		for x in range(change_period):
			if start_period == "PM":
				start_period = "AM"
				days_passed += 1 #for additional checks
			else:
				start_period = "PM"
	
	if new_hour == 0:
		new_hour = 12 #in case hour turns into 0
	
	new_hour = str(new_hour)

	new_time = new_hour + ":" + new_minute + " " + start_period

	#Additional checks
	final_day = None
	days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	if day != None:
		day_index = days_of_the_week.index(day.title()) + (days_passed % 7)
		if day_index > 6:
			day_index -= 7 #modulo operation already ensures days_passed is =< 7, so -7 if index goes above what is expected
		final_day = days_of_the_week[int(day_index)]
		new_time = new_time + ", " + final_day
	
	if days_passed > 0:
		if days_passed == 1:
			new_time = new_time + " (next day)"
		else:
			new_time = new_time + " (" + str(days_passed) + " days later)"

	return new_time