def create_quiz(myfile):
    """ Creates dictionary where keys are linux commands
        and values are definitions

        args:
            myfile (file): file containing quiz items
    """

    quiz_file = open(myfile,'r')
    quiz = {}

    for line in quiz_file:
        temp = line.rstrip('\n').split(",") 
       
        if temp[0] not in quiz:         
            quiz[temp[0]]= [temp[1]]
        else:
            quiz[temp[0]].append(temp[1]) 
    quiz_file.close()   
    
    return quiz

def choices(quiz,choice):
    """ Takes differnt action based on user input

        args:
            quiz (dict) : contains quiz items
            choice (int) : represents choice user made
    """
    commands = quiz.keys()
    
    if choice == 1: # displays keys in quiz dictionary which are the commands
        commands.sort()
        for item in commands:
            print item
        
    elif choice == 2: # displays defintions of each command in quiz
                
        commands.sort()    
        for item in commands:
            print item , "|", quiz[item][0]      
        
    elif choice == 3: # calls function for matching commands to their definitions
                
        command_definitions = []
        for item in commands:
            command_definitions.append(quiz[item][0])            
        match_command_name(zip(commands,command_definitions))
    elif choice == 4:
        
        
        optional_commands = []
        for command in commands:
            for option in quiz[command]:
                              
                temp = option.split('.')                
                optional_commands.append((command,(temp[0],temp[1])))        
        match_options(optional_commands)

def match_command(pairs):
    """ Matches linux commands with their optional inputs

        args:
            pairs (tuple): tuple of len 2 containing the command with it's optional input

     """       
    done = False
    try_again = ['yes','Yes','YES','y','Y']
    not_try_again = ['no', 'n', 'No', 'N', 'NO']
    
    while not done:
        print "The optional command for %s is  %s. " %(pairs[0],pairs[1][1])
        choice = raw_input("What do you think the syntax for this option is? ")
        if choice == pairs[1][0]:
            print "Correct!!!"
            done = True
            finished = raw_input("Would you like to match another command? ")
        else:
            replay = raw_input("Sorry that is incorrect. Would you like to try again? ")
            if replay in not_try_again:
                done = True
                finished = raw_input("Would you like to match another command? ")
    if finished in try_again:
        return False
    else:
        return True


def match_options(optionPairs):
    """ Calls the function to match commands and their optional inputs
        until user matches all pairs or they decide to stop

        args:
            optionpairs (list): list containing tuples of options and their optional inputs
     """       
    finished = False    

    while not finished:
        for pair in optionPairs:            
                done = match_command(pair)
                if done:
                    finished = True
                    break
        if not done:
            finished = True
            print "You matched all the words! Congrats!"




def match_name(pairs):
    """ Matches commands to their command definitions

        args:
            pairs (tuple) : tuple of len 2 containing a command and it's definition
    """
    done = False
    try_again = ['yes','Yes','YES','y','Y']    
    
    while not done:
        print "The command definition is %s. " %(pairs[1])
        choice = raw_input("What do you think the linux command is? ")
        if choice == pairs[0]:
            print "Correct!!!"
            done = True
            finished = raw_input("Would you like to match another command? ")
        else:
            replay = raw_input("Sorry that is incorrect. Would you like to try again? ")
            if replay in try_again:
                hint = raw_input("Would you like a hint? ")
                if hint in try_again:
                    print "The first letter of the command is %s" %(pairs[0][0])
                    print "The last letter of the command is %s" %(pairs[0][len(pairs[0])-1])
            else:
                done = True
                finished = raw_input("Would you like to match another command? ")
    if finished in try_again:
        return False
    else:
        return True

def match_command_name(commandNamePairs):
    """ Calls function to match commands to command definitions
        until user matches all commands or decides to stop

        args:
            commandNamePairs (list) : list containing tuples of commands and their definitions
    """
        
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
    """ Prints options for user to pick from

        args:
            none
    """
    print "1. Display list of all commands in this quiz"
    print "2. Display list of all command with definition"
    print "3. Match command to command definition"
    print "4. Match command with optional input"
    print "5. Quit"
    
   

def main():


    quiz = create_quiz('linuxcommands.txt')
    quiz2 = create_quiz('optionalcommands.txt')
    print "Hello welcome to the linux command quiz"    
    options()    
    choice = input("Please pick an option: ")
    while choice != 5:
        if choice in [1,2,3]:
            choices(quiz,choice)
            print "=========================================================="
            options()
            choice = input("Please pick an option: ")
        elif choice == 4:
            choices(quiz2,choice)
            print "==========================================================="
            options()
            choice = input("Please pick an option: ")
        else:
            print "Please pick an option between 1 and 5."

if __name__ == "__main__":
    main()
    
        
