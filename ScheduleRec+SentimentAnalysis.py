#Preliminary DataSet 1
#Break_type and Recommendations for Reference
break_type = ['Breathing','Meditation','Walking','Napping']
suggestions = ['Drink some water and take a deep breath. Keep up with what you are doing, and enjoy a good day!',
              'Try to smile a bit more. Do Something For Fun!',
              'Try to go out for a walk, take a deep breath, and do some meditation. ',
              'Take a quick nap or break. Relax. You can do this!',
              'Take a quick shower or wash your face. Chill.',
              'Talk to a friend and don\'t hold all the stress to yourself. You\'re doing great!']

#Primary Backend Functionality: Sentiment Analysis Portion
import indicoio
indicoio.config.api_key = '054351afd31d8f0fae1c30f0e1634742'

#Preliminary DataSet 2
#Additional Dictionaries with Scores For Reference
calendar = {'class':-0.2,
                 'test':-0.25,
                 'quiz':-0.15,
                 'exam':-0.25,
            'conference':-0.2,
            'conferences':-0.3,
                 'meeting':-0.2,
                 'company':-0.1,
                 'homework':-0.15,
                 'lab':-0.1,
                 'application':-0.15,
                 'interview':-0.1,
                 'presentation':-0.1,
                 'speech':-0.15,
                 'call':-0.15,
                 'public':-0.15,
                 'funeral':-0.2,
                 'memorial':-0.2,
                 'lawyer':-0.15,
                 'legal':-0.15,
                 'appointment':-0.1,
                 'review':-0.15,
                 'court':-0.2,
                 'jury':-0.15,
                 'jail':-0.2,
                 'placement':-0.15,
                 'final':-0.2,
                 'dates':-0.4,
                 'breakup':-0.2,
                 'doctor':-0.15,
                 'paper':-0.15,
                 'due':-0.15,
                 'deadline':-0.15,
                 'business':-0.1,
                 'divorce':-0.35,
                 'wedding':-0.1,
                 'flight':-0.2,
                 'delay':-0.2,
                  'probation':-0.25,
                  'violation':-0.2,
                  'ticket':-0.1,
                  'traffic':-0.15,
                  'jam':-0.15,
                  'cram':-0.2,
                  'grind':-0.2,
                  'cramming':-0.2,
                  'grinding':-0.4,
                  'study':-0.2,
                  'late':-0.25,
                  'studying':-0.2,
                 'cs':-0.2,
                 'computer science':-0.2,
                 'math':-0.2,
                 'physics':-0.3,
                 'make':-0.3,
                 'preparing':-0.2,
                 'prepare':-0.2,
                 'rehearsal':-0.2,
                 'studying':-0.2}

#Please USE the string 'dict.txt' for the path argument
#Please USE the variable 'calendar' for the add_on argument
def read_input_and_combine(path,add_on):
    with open(path) as my_file:
        dictionary = my_file.readlines()
    #Formatting the input lines from the txt file
    def split(L):
        Lf = {}
        for i in range(len(L)):
            temp = L[i].split(',')
            left = temp[0]
            right = round(int(temp[1].split('\n')[0])*0.1,1)
            Lf[left]=right
            i += 1
        return Lf

    library = split(dictionary)
    library.update(add_on)
    return library

def percentage(x):
    return round(x*100,2)
#The method below evaluates the emotions

def evaluate_emotions(Input,External):
    Emotions = indicoio.emotion(Input)
    anger = percentage(Emotions['anger'])
    fear = percentage(Emotions['fear'])
    joy = percentage(Emotions['joy'])
    sadness = percentage(Emotions['sadness'])
    surprise = percentage(Emotions['surprise'])
    #Extract and convert the emotions output by the server to rounded two-decima-place percentages
    words = Input.split(' ')
    for i in range(len(words)):
        word = words[i].lower()
        #If the current word exists in the existing additional dictionary, the negative feeling
        #values are further augmented with adjustments
        if word in External:
            key = External[word]
            fear += abs(percentage(key)+5)
            anger += abs(percentage(key)+7)
            sadness += abs(percentage(key)+10)
        i += 1
    #returning a list containing all the 5 emotions, along with the percentage values
    #showing the magnitude
    response = []
    if fear>=90:
        response.append('IV') #IV(very anxious)--> recommend user should immediately take a break or talk to someone
    elif fear>=65:
        response.append('III') #III(stressed)--> recommend user should take a break within 5 minutes
    elif fear>=30:
        response.append('II') #II(worried)--> recommend user should take a deep breath and do a little meditation
    elif fear>=20:
        response.append('I') #I(slightly concerned)--> recommend user should relax and focus on other activities
    else:
        response.append('OK') #O(Stable)--> recommend user to drink some water and keep up with the good state

    if anger>=90:
        response.append('IV') #IV(enraged)--> recommend user should immediately calm down, drink some water, and go outside for a walk
    elif anger>=60:
        response.append('III') #III(very angry)--> recommend user should go to the bathroom, take a quick shower or wash his/her face
    elif anger>=30:
        response.append('II') #II(mad)--> recommend user should take a deep breath and do a little meditation
    elif anger>=20:
        response.append('I') #I(irrated)--> recommend user should relax and focus on other activities
    else:
        response.append('OK') #O(Stable)--> recommend user to drink some water and keep up with the good state

    if sadness>=80:
        response.append('IV') #IV(depressed)--> recommend user should immediately talk to someone else and seek assistance
    elif sadness>=60:
        response.append('III') #III(sorrowful)--> recommend user should have a break, take a nap, or take a shower
    elif sadness>=30:
        response.append('II') #II(upset)--> recommend user should go out for a walk, take a deep breath, and do some meditation
    elif sadness>=20:
        response.append('I') #I(sad)--> recommend user should try to smile and do something for fun to distract him/herself
    else:
        response.append('OK') #O(Stable)--> recommend user to drink some water and keep up with the good state

    return ['anger',anger,'fear',fear,'joy',joy,'sadness',sadness,'surprise',surprise]+response

#Preliminary Function 1
def parse_time(List):
#Create a list with the time in string format parsed and converted into integers (in minutes)
    Modified = [int(x.split(':')[0])*60+int(x.split(':')[1]) for x in List]
    return Modified

#Preliminary Function 2
def min_to_time(List):
#Create a list with time in integers(in minutes) converted back into the string format
#Essentially the inverse of parse_time function
    return [str(x//60)+":"+("0"+str(x%60)+":" if x%60<10 else str(x%60)+":")+"00" for x in List]

#Preliminary Function(Optional)
#Return a concatenated list with elements from A, B paired up individually (for DateTime Purposes)
def concatenate(A,B):
    assert len(A)==len(B)
    C = []
    for i in range(len(A)):
        C.append(A[i]+'-'+B[i])
        i += 1
    return C

#PRIMARY FUNCTION 1
def schedule(start,end,description):
#return two lists containing the starting and ending time of free-time interval
    start,end = parse_time(start),parse_time(end)
    #Parse the start and end lists
    first_start = start[0]
    #Locate the first starting time of the day
    free_start,free_end,free_interval,recs,emotion_state = [],[],[],[],[]

    if first_start > 0:
        free_start.append(0)
        free_end.append(first_start)
        rec, emo = evaluate_indico(description[0])
        #Evaluate sentiments from the closest events and return the recommendations and negative emotion intensities
        recs.append(rec)
        emotion_state.append(emo)
        #Record these values

    #Check if there is free time interval before the first time slot of the day
    i = 0
    while i<len(start)-1:
        last_end = end[i]
        next_start = start[i+1]
        if next_start > last_end:
            #The condition above checks for overlaps
            rec,emo = evaluate_indico(description[i])
            #Evaluate sentiments from the closest events and return the recommendations and negative emotion intensities
            recs.append(rec)
            emotion_state.append(emo)
            #Record these values
            free_start.append(last_end)
            free_end.append(next_start)

        i += 1
    #Loop through and append the new free time interval; check for overlaps
    if end[len(end)-1]<23*60+59:
        free_start.append(end[len(end)-1])
        free_end.append(23*60+59)
        rec, emp = evaluate_indico(description[len(description)-1])
        recs.append(rec)
        emotion_state.append(emo)
    #Check if there is free time interval after the last time slot of the day

    final_free_start = min_to_time(free_start)
    final_free_end = min_to_time(free_end)
    #free_schedule = concatenate(final_free_start,final_free_end)
    #Concatennating all the start and end free time
    return free_start,free_end, recs, emotion_state

#Preliminary function 3
def reverse_nested(NList):
#Return an one-level list containing all the elements de-nested.
    List = []
    for i in range(len(NList)):
        temp = len(NList[i])
        for j in range(temp):
            List.append(NList[i][j])
            j+=1
        i+=1
    return List

#Preliminary Function 4
def intersect(T1,T2):
#Return the intersection of two time intervals (if it exists)
#Otherwise, None is returned.
    if max(T1[0],T2[0])<min(T1[1],T2[1]):
        return [max(T1[0],T2[0]),min(T1[1],T2[1])]

#Preliminary Function 5
def pair(L1,L2):
#Return a two-level nested lists containig paired up elements from two separate lists
    Lf=[]
    for i in range(len(L1)):
        Lf.append([L1[i],L2[i]])
    return Lf

#Preliminary Function 6
def pair_wise(L):
#Return a nested list containing adjacent elements as a pair from a list with an even number of elements
    Lf,i = [],0
    while i<len(L):
        Lf.append([L[i],L[i+1]])
        i += 2
    return Lf

#PRIMARY FUNCTION 2
def break_insert(preferred_time_range,start,end,descriptions):
    #A higher order function that takes in the following parameters:
    #For the outer Level:
    #         1. Preferred Time Blocks Selected By the User
    #            Format(dtype = str): [start_1, end_1, start_2, end_2, ...]
    #         2. All the Starting Time of the Events in the User's Google Calendar
    #            Format(dtype = str): [start_1,start_2,...]
    #         3. All the Ending Time of the Events in the User's Google Calendar
    #            Format(dtype = str): [end_1,end_2,...]
    #         4. Descriptions of events for each time frame in the user's original Google calendar
    #            Format(dtype = str):[description_1,description_2,...]
    #For the inner level:
    #         1. Duration of the Break Selected By the User
    #            Format(dtype = int)
    #A sample call should look like: break_insert(.., .., ..)(..)
    assert len(preferred_time_range)>=2
    frequency = len(preferred_time_range)//2
    free_start,free_end,recs,emotion_state = schedule(start,end,descriptions)
    final_rec, final_emo_state = [],[]
    #returns the processed free time block
    merge = pair(free_start,free_end)
    #merge the time blocks together into a nested list
    time_int = parse_time(preferred_time_range)
    pref = pair_wise(time_int)
    #split the preferred time range into a nested list
    result = []
    for i in range(len(pref)):
        x = 0
        for j in range(len(merge)):
            if intersect(merge[j],pref[i]) and x<1:
                #If the intersection between these two time intervals exists, we will append it
                #to our resulting list. x<1 ensures that only the first valid time interval within the
                #the current time preferrence block is selected.
                if j<len(recs):
                    final_rec.append(recs[j])
                if j<len(emotion_state):
                    final_emo_state.append(emotion_state[j])
                result.append(intersect(merge[j],pref[i]))
                x+=1
            j += 1
        i += 1
        #The above for loop iterates through the nested lists to determine a match time block using the
        #preference time range and the free time range.
    simplified = reverse_nested(result)

    def recommendation(duration):
        #This method will use the duration for break determined by the user to give the recommended time range
        i = 2
        simplified[0]=simplified[1]-30-duration
        simplified[1]=simplified[1]-30
        while i<len(simplified):
            simplified[i+1] = simplified[i]+duration
            i += 2
        return min_to_time(simplified),final_rec,final_emo_state
    return recommendation

#Sample Run:
Input:
start = ['7:00:00','9:30:00','10:00:00','11:15:00','12:00:00','13:00:00','14:15:00','15:30:00','16:30:00','18:30:00']
end = ['8:30:00','10:00:00','11:00:00','12:00:00','13:00:00','14:00:00','15:30:00','16:30:00','17:00:00','20:30:00']
pref = ['5:00:00','11:00:00','11:00:00','17:00:00','17:00:00','23:00:00']
descriptions = ['Spin Class','Performance Review with Boss','Call With Team','Team StandUp','Lunch with Roommates','Meet with Investors','Mentor Junior Staff','Write Report','Drive Home','Date Night']

Output:
['6:20:00', '6:30:00', '11:00:00', '11:10:00', '17:00:00', '17:10:00']#Recommended Time Frames for Breaks,
['Take a quick nap or break. Relax. You can do this!',
  'Take a quick nap or break. Relax. You can do this!',
  'Try to go out for a walk, take a deep breath, and do some meditation. Try to smile a bit more. Do Something For Fun!']#Suggestions,
[[38.0, 32.2, 25.73], [44.72, 24.82, 21.65], [23.74, 18.55, 17.28]]#Predicted Emotion Intensities Surrounding Breaks
