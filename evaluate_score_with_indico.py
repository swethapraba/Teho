#Import the Indicocio Library for Semantic Analysis
#Note: Make <=10,000 calls to the server per month for free
import indicoio
indicoio.config.api_key = '054351afd31d8f0fae1c30f0e1634742'

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
    if fear>=120:
        response.append('Fear:IV') #IV(very anxious)--> recommend user should immediately take a break or talk to someone
    elif fear>=90:
        response.append('Fear:III') #III(stressed)--> recommend user should take a break within 5 minutes
    elif fear>=70:
        response.append('Fear:II') #II(worried)--> recommend user should take a deep breath and do a little meditation
    elif fear>=35:
        response.append('Fear:I') #I(slightly concerned)--> recommend user should relax and focus on other activities
    else:
        response.append('Fear:OK') #O(Stable)--> recommend user to drink some water and keep up with the good state

    if anger>=110:
        response.append('Anger:IV') #IV(enraged)--> recommend user should immediately calm down, drink some water, and go outside for a walk
    elif anger>=80:
        response.append('Anger:III') #III(very angry)--> recommend user should go to the bathroom, take a quick shower or wash his/her face
    elif anger>=50:
        response.append('Anger:II') #II(mad)--> recommend user should take a deep breath and do a little meditation
    elif anger>=20:
        response.append('Anger:I') #I(irrated)--> recommend user should relax and focus on other activities
    else:
        response.append('Anger:OK') #O(Stable)--> recommend user to drink some water and keep up with the good state

    if sadness>=100:
        response.append('Sadness:IV') #IV(depressed)--> recommend user should immediately talk to someone else and seek assistance
    elif sadness>=80:
        response.append('Sadness:III') #III(sorrowful)--> recommend user should have a break, take a nap, or take a shower
    elif sadness>=60:
        response.append('Sadness:II') #II(upset)--> recommend user should go out for a walk, take a deep breath, and do some meditation
    elif sadness>=30:
        response.append('Sadness:I') #I(sad)--> recommend user should try to smile and do something for fun to distract him/herself
    else:
        response.append('Sadness:OK') #O(Stable)--> recommend user to drink some water and keep up with the good state

    return ['anger',anger,'fear',fear,'joy',joy,'sadness',sadness,'surprise',surprise]+response
