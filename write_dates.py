month_map = {
    "January": "01",
    "February" : "02",
    "March" : "03", 
    "April" : "04", 
    "May" : "05", 
    "June" : "06", 
    "July" : "07", 
    "August" : "08", 
    "September" : "09", 
    "October" : "10", 
    "November" : "11", 
    "December" : "12"
    }


dates_file_r = open("template.txt", "r")


dates = dates_file_r.readlines()

newDatesName = []
newDatesNumber = []
properDates = []


# Fixes format of dates and adds named month dates (January 1 - December 31) to newDatesName[]
for date in dates:
    if date[-1] == '\n':
        newDatesName.append(date[4:-1].strip())
    else:
        newDatesName.append(date.strip())

dates_file_r.close()

# Changes format of dates from newDatesName[] to numbered dates (0101 - 1231) and appends dates to newDatesNumber[]
# Also changes format of dates from newDatesName[] to proper date format (1/1 - 12/31) and appends dates to properDates[]
for i in range(len(newDatesName)):
    month = newDatesName[i].split(" ")

    if len(month[1]) == 1:
        newDatesNumber.append(month_map[month[0]] + "0" + month[1])
    
    else:
        newDatesNumber.append(month_map[month[0]] + month[1])

    if month_map[month[0]][0] == '0':    
        properDates.append(month_map[month[0]][1] + "/" + month[1])
    else:
        properDates.append(month_map[month[0]] + "/" + month[1])


dates_file_w = open("dates.txt", "w")

# Writes newDatesNumber[] values into dates.txt
for i in range(len(newDatesNumber)):
    dates_file_w.write(newDatesNumber[i] + "\n")

dates_file_w.close()

# properDates can be used to add to spreadsheet