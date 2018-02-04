from textblob import TextBlob
#Please Also Check the txt file with additional words/scores I have uploaded
#The txt file is called 'dict.txt'

#Primary Function (Call this function below to return the score and the stress level)
def evaluate(Input,External):
    slice_list = TextBlob(Input)
    Sum = 0
    for i in range(len(slice_list.words)):
        word = slice_list.words[i]
        score = TextBlob(word).sentiment.polarity
        if score:
            score -= 0.1
        Word = TextBlob(word).correct().lower()
        if Word in External:
            Sum += External[Word.lower()]
        Sum += score
        i += 1
    if Sum<=-0.75:
        return [Sum,'V']
    elif Sum<=-0.5:
        return [Sum,'IV']
    elif Sum<=-0.35:
        return [Sum,'III']
    elif Sum<=-0.2:
        return [Sum,'II']
    elif Sum<=0:
        return [Sum,'I']
    else:
        return [Sum,'N/A']

#Stress/Anxiety Level:
#Level N/A(OK): >0
#Level I(Slightly Worried):-0.2~0
#Level II(Worried,Concerned):-0.35~-0.2
#Level III(Anxious,Stressed):-0.35~-0.5
#Level IV(Very Anxious, Depressed):-0.5~-0.75
#Level V(Caution,Immediate Action/Intervention):<=-0.75

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
                 'tests':-0.25}

#Please use the string 'dict.txt' for the path argument
#Please use the variable 'calendar' for the add_on argument
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

#Sample Call Below: To Evaluate the description 'Studying for Test'
evaluate('Studying for Test',read_input_and_combine('dict.txt',calendar))
Output: [-0.45,'III']
