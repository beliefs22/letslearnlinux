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
        return a
    elif choice == 2:
        a = quiz.keys()
        a.sort()
        b = []
        for item in a:
            temp = quiz[item][0][0]
            b.append(temp)
            print temp            
        return b
    

def options():    
    print "Please pick one of the following options"
    print "1. Display list of all commands in this quiz"
    print "2. Display list of names of all commands in this quiz"
    print "3. Match command to command name"
    print "4. Match command to command definition"
    print "5. Quit"
    
   

def main():

    quiz = create_quiz('linuxcommands.txt')
    print "Hello welcome to the linux command quiz"
    options()    
    choice = input("pick an option: ")
    while choice != 5:
        a = choices(quiz,choice)        
        options()
        choice = input("pick an option: ")

main()
    
        
