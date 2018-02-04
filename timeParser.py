def parse_time(List):
    Modified = [int(x.split(':')[0])*60+int(x.split(':')[1]) for x in List]
    #Create a list with the time in string format parsed and converted into integers (in minutes)
    return Modified

def min_to_time(List):
    return [str(x//60)+":"+str(x%60)+("0:" if x%60<10 else ":")+"00" for x in List]
    #Create a list with time in integers(in minutes) converted back into the string format
    #Essentially the inverse of parse_time function

def concatenate(A,B):
    assert len(A)==len(B)
    C = []
    for i in range(len(A)):
        C.append(A[i]+'-'+B[i])
        i += 1
    return C
#Return a concatenated list with elements from A, B paired up individually

@app.route('/schedules', methods=['POST'])
def run():
    schedule(request['param1'], request['param2'])

def schedule(start,end):
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
    free_schedule = concatenate(final_free_start,final_free_end)
    #Concatenating all the start and end free time
    return json.dumps({'status':'OK','schedule':free_schedule});

def break_insert(frequency,preferred_time_range,free_interval):
    if frequency > len(free_interval):
        break_insert(len(free_interval),preferred_time_range, free_interval)
    #else:

#Test
#A = parse_time(["2:00:00","4:00:00","8:00:00","12:00:00"])
#A
#Test
#min_to_time(A)
#start = ['7:00:00','9:00:00','9:30:00','18:00:00']
#end = ['8:30:00','10:00:00','14:30:00','22:45:00']
#print(parse_time(start))
#print(parse_time(end))
#schedule(start,end)
