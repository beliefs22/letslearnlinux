def create_quiz(myfile):

    quiz_file = open(myfile,'r')
    quiz = {}

    for line in quiz_file:
        temp = line.rstrip('\n').split(",")
        quiz[temp[0]]= temp[1:]
    quiz_file.close()
    for key in quiz:
        temp = quiz[key]
        quiz[key] = []
        for item in temp:
            temp2 = item.split('.')            
            quiz[key].append((temp2[0],temp2[1]))            
    
    return quiz

def choices(quiz,choice):
    if choice == 1:
        a = quiz.keys()
        a.sort()
        for item in a:
            print item
        
    elif choice == 2:
        a = quiz.keys()
        a.sort()        
        for item in a:
            temp = quiz[item][0][0]            
            print item,"|",temp            
        
    elif choice == 3:
        a = quiz.keys()        
        b = []
        for item in a:
            temp = quiz[item][0][0]
            b.append(temp)
        match_command_name(zip(a,b))
    elif choice == 4:
        print "check back later"
        pass
          


def match_name(pairs):
    done = False
    again = ['yes','Yes','YES','y','Y']    
    print "The command definition is %s. " %(pairs[1])
    while not done:
        choice = raw_input("What do you think the linux command is? ")
        if choice == pairs[0]:
            print "Correct!!!"
            done = True
            finished = raw_input("Would you like to match another command? ")
        else:
            replay = raw_input("Sorry that is incorrect. Would you like to try again? ")
            if replay in again:
                hint = raw_input("Would you like a hint? ")
                if hint in again:
                    print "The first letter of the command is %s" %(pairs[0][0])
                    print "The last letter of the command is %s" %(pairs[0][len(pairs[0])-1])
            else:
                done = True
                finished = raw_input("Would you like to match another command? ")
    if finished in again:
        return False
    else:
        return True

def match_command_name(commandNamePairs):
        
    finished = False    

    while not finished:
        for pair in commandNamePairs:            
                done = match_name(pair)
                if done:
                    finished = True
                    break
        if not done:
            finished = True
            print "You matched all the words! Congrats!"
    

def options():
    print "1. Display list of all commands in this quiz"
    print "2. Display list of all command with definition"
    print "3. Match command to command definition"
    print "4. Match command with optional input"
    print "5. Quit"
    
   

def main():


    quiz = create_quiz('linuxcommands.txt')
    print "Hello welcome to the linux command quiz"    
    options()    
    choice = input("Please pick an option: ")
    while choice != 5:
        choices(quiz,choice)
        print "=========================================================="
        options()
        choice = input("Please pick an option: ")

    
main()
    
        
