# Teho

Please Use #ScheduleRec+SentimentAnalysis.py and #dict.txt file for integration of functionality

(From Paul): WHEN INTEGRATING,

Please use the two files I give above (make sure #dict.txt is in the same directory as the .py file).
To Run the Functions, simply call the method like below:
        break_insert(pref,start,end,descriptions)(duration)
        
        #For Demonstration, let's say the user have the following schedule on google calendar today:
            START                    END                     TITLE/DESCRIPTION
            7:00                     11:00                   Meeting
            14:00                    19:00                   Studying For Qualification Exams
            
        pref is the input preference time blocks.
        #For example, If the user chooses the time blocks 5-11(morning) and 11-17(afternoon),
        pref = ['5:00:00','11:00:00','11:00:00','17:00:00']
        
        start/end is the input starting/ending time for all the events in the GOOGLE CALENDAR.
        #In this case, start=['7:00:00','11:00:00']
                       end=['14:00:00','19:00:00']
                       descriptions=['Meeting','Studying For Qualification Exams']
        
        #If the user chooses a duration of 10 minutes for breaks,
                       duration = 10
        
        Sample INPUT:
        break_insert(pref,start,end,descriptions)(duration)
        
        Sample OUTPUT:
        #Three Lists Will be Returned:
        
        ['6:20:00','6:30:00','11:00:00','11:10:00'] #Recommended Time Frames For Breaks 
          start       end       start       end
               Break 1               Break 2
        
        ['Take a quick nap or break. Relax. You can do this!','Try to go out for a walk, take a deep breath, and do some meditation. Try to smile a bit more. Do Something For Fun!']#Suggested Activities For Each Break
        
        [[43,24,10],[32,22,12]]#Recorded Negative Emotion Intensities Surrounding Each Break
        [Fear, Anger, Sadness]
        
