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
def schedule(start,end):
#return two lists containing the starting and ending time of free-time interval
    start,end = parse_time(start),parse_time(end)
    #Parse the start and end lists
    first_start = start[0]
    #Locate the first starting time of the day
    free_start,free_end,free_interval = [],[],[]

    if first_start > 0:
        free_start.append(0)
        free_end.append(first_start)
    #Check if there is free time interval before the first time slot of the day
    i = 0
    while i<len(start)-1:
        last_end = end[i]
        next_start = start[i+1]
        if next_start > last_end:
            #The condition above checks for overlaps
            free_start.append(last_end)
            free_end.append(next_start)
        i += 1
    #Loop through and append the new free time interval; check for overlaps
    if end[len(end)-1]<23*60+59:
        free_start.append(end[len(end)-1])
        free_end.append(23*60+59)
    #Check if there is free time interval after the last time slot of the day

    final_free_start = min_to_time(free_start)
    final_free_end = min_to_time(free_end)
    #free_schedule = concatenate(final_free_start,final_free_end)
    #Concatennating all the start and end free time
    return free_start,free_end

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
def break_insert(preferred_time_range,start,end):
    #A higher order function that takes in the following parameters:
    #For the outer Level:
    #         1. Preferred Time Blocks Selected By the User
    #            Format(dtype = str): [start_1, end_1, start_2, end_2, ...]
    #         2. All the Starting Time of the Events in the User's Google Calendar
    #            Format(dtype = str): [start_1,start_2,...]
    #         3. All the Ending Time of the Events in the User's Google Calendar
    #            Format(dtype = str): [end_1,end_2,...]
    #For the inner level:
    #         1. Duration of the Break Selected By the User
    #            Format(dtype = int)
    #A sample call should look like: break_insert(.., .., ..)(..)
    assert len(preferred_time_range)>=2
    frequency = len(preferred_time_range)//2
    free_start,free_end = schedule(start,end)
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
                result.append(intersect(merge[j],pref[i]))
                x+=1
            j += 1
        i += 1
        #The above for loop iterates through the nested lists to determine a match time block using the
        #preference time range and the free time range.
    simplified = reverse_nested(result)
    def recommendation(duration):
        #This method will use the duration for break determined by the user to give the recommended time range
        i = 0
        while i<len(simplified):
            simplified[i+1] = simplified[i]+duration
            i += 2
        return min_to_time(simplified)
    return recommendation
