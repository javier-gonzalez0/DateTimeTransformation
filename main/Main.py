#################################
#   Javier Gonzalez             #
#   UTSA ECE                    #
#   CS 5103                     #
#################################
from datetime import datetime, timedelta
import re #used for Day of the week filter

if __name__ == '__main__':


    TimeZones = \
    [['Name', 'Description', 'Relative to GMT', 'Delta'],
    ['GMT',	'Greenwich Mean Time', 'GMT', 0],
    ['UTC',	'Universal Coordinated Time', 'GMT', 0],
    ['ECT',	'European Central Time', 'GMT+1:00', 1],
    ['EET',	'Eastern European Time', 'GMT+2:00', 2],
    ['ART',	'(Arabic) Egypt Standard Time', 'GMT+2:00', 3],
    ['EAT',	'Eastern African Time', 'GMT+3:00', 3],
    ['MET',	'Middle East Time', 'GMT+3:30', 3],
    ['NET',	'Near East Time', 'GMT+4:00', 4],
    ['PLT',	'Pakistan Lahore Time', 'GMT+5:00', 5],
    ['BST',	'Bangladesh Standard Time', 'GMT+6:00', 6],
    ['VST',	'Vietnam Standard Time', 'GMT+7:00', 7],
    ['CTT',	'China Taiwan Time', 'GMT+8:00', 8],
    ['JST',	'Japan Standard Time', 'GMT+9:00', 9],
    ['AET',	'Australia Eastern Time', 'GMT+10:00', 10],
    ['SST',	'Solomon Standard Time', 'GMT+11:00', 11],
    ['NST',	'New Zealand Standard Time', 'GMT+12:00', 12],
    ['MIT',	'Midway Islands Time', 'GMT-11:00', -11],
    ['HST',	'Hawaii Standard Time', 'GMT-10:00', -10],
    ['AST',	'Alaska Standard Time', 'GMT-9:00', -9],
    ['PST',	'Pacific Standard Time', 'GMT-8:00', -8],
    ['PNT',	'Phoenix Standard Time', 'GMT-7:00', -7],
    ['MST',	'Mountain Standard Time', 'GMT-7:00', -7],
    ['CST',	'Central Standard Time', 'GMT-6:00', -6],
    ['EST',	'Eastern Standard Time', 'GMT-5:00', -5],
    ['IET',	'Indiana Eastern Standard Time', 'GMT-5:00', -5],
    ['PRT',	'Puerto Rico and US Virgin Islands Time', 'GMT-4:00', -4],
    ['AGT',	'Argentina Standard Time', 'GMT-3:00', -3],
    ['BET',	'Brazil Eastern Time', 'GMT-3:00', -3],
    ['CAT',	'Central African Time', 'GMT-1:00', -1]]


    ValidDate = False

    while(ValidDate == False):

        print("\n\nPlease enter date & time in the following format:")
        print("     mm/dd/yyyy <day of the Week> hh:mm  ")
        timestring = input("     mm/dd/yyyy <day of the Week> hh:mm")
        print("User Input: ", timestring)
        input_mon = int(timestring[0:2])
        input_day = int(timestring[3:5])
        input_year = int(timestring[6:10])
        #Day of the Week (DoW)
        input_DoW = re.sub("[^A-Za-z]","",timestring[11:21]).capitalize()
        input_hour = int(timestring[-5:-3]) #Change to make code more robust
        input_min = int(timestring[-2:])    #Change to make code more robust

        try:
            currentdate = datetime(year=input_year,month=input_mon,day=input_day,
                                            hour=input_hour,minute=input_min)
            
            ValidDate = True

            if input_DoW != currentdate.strftime("%A"):
                ValidDate = False
                print("In valid Week of the day input, please try again")

        except ValueError:
            ValidDate = False
            print("Time Format error please try again")

    ValidTimeZone = False
    while(ValidTimeZone == False):

        print("\n\nUser must enter the time zone they are in, for list of time zones")
        print("please refer to SRS and enter index value for time zone")
        print("Default (GMT Time Zone) please press enter without hitting a key")
        TZIndex_current = input("Please enter integer value from 1 to 28: ")
        print("User Input: ", TZIndex_current)
        
        if TZIndex_current == '':
            TZIndex_current = 1
            ValidTimeZone = True
        elif int(TZIndex_current) >= 1 and int(TZIndex_current) <= 28:
            TZIndex_current = int(TZIndex_current)
            ValidTimeZone = True
        else:
            ValidTimeZone = False




    ValidTimeZone = False
    while(ValidTimeZone == False):

        print("\n\nUser must enter new time zone.")
        TZIndexChange = input("Please enter integer value from 1 to 28: ")
        print("User Input: ", TZIndexChange)
        
        if TZIndexChange == '':
            TZIndexChange = 1
            ValidTimeZone = True
        elif int(TZIndexChange) >= 1 and int(TZIndexChange) <= 28:
            TZIndexChange = int(TZIndexChange)
            ValidTimeZone = True
        else:
            ValidTimeZone = False



    hour_delta = TimeZones[TZIndex_current][3] + TimeZones[TZIndexChange][3]
    newdate = currentdate + timedelta(hours=hour_delta)

    print("\n\nThe old date & time:", currentdate.strftime("%m/%d/%Y %A %H:%M"))
    print("The new date & time:", newdate.strftime("%m/%d/%Y %A %H:%M"))
    print("Time delta:", hour_delta, "hours")
    

