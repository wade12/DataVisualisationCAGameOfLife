print "              ,_   .  ._. _.  ."
print "          , _-\','|~\~      ~/      ;-'_   _-'     ,;_;_,    ~~-"
print "/~~-\_/-'~'--' \~~| ',    ,'      /  / ~|-_\_/~/~      ~~--~~~~'--_"
print "/              ,/'-/~ '\ ,' _  , '|,'|~                   ._/-, /~"
print "~/-'~\_,       '-,| '|. '   ~  ,\ /'~                /    /_  /~"
print"-~      '|        '',\~|\       _\~     ,_  ,               /|"
print "         '\        /'~          |_/~\\,-,~  \          ,_,/ |"
print "          |       /            ._-~'\_ _~|              \ ) /"
print "           \   __-\           '/      ~ |\  \_          /  ~"
print ".,         '\ |,  ~-_      - |          \\_' ~|  /\  \~ ,"
print "             ~-_'  _;       '\           '-,   \,' /\/  |"
print "               '\_,~'\_       \_ _,       /'    '  |, /"
print "                  /     \_       ~ |      /         \  ~'; -,_."
print "                  |       ~\        |    |  ,        '-_, ,; ~ ~\ "
print "                   \,      /        \    / /|            ,-, ,   "
print "                    |    ,/          |  |' |/          ,-   ~ \   '."
print "                   ,|   ,/           \ ,/              \       |"
print "                   /    |             ~                 -~~-, /   _"
print "                   |  ,-'                                    ~    / "
print "                   / ,'                                      ~ "
print "                   ',|  ~"
print  





import random
from userSpecs import UserSpecs

class GameOfLifeApp(object):
    
    ## create user object
    global userSpecs
    userSpecs = UserSpecs()
    
    def userInfo():

        ## print quit message
        print 'Type "q" to quit this program at anytime.'
   
        ## obtain input form user
        while True:
            name = raw_input('Please enter your name: ')
            ## cover to lower case
            name = name.lower()
            ## check for quit option
            if name == 'q':
                quit()
            ## check user did not just press return button
            ## and all characters are alphabetic
            ## note: unfortunately the isalpha method will not work in cases
            ## whereby some african names contain an exclamation mark
            if name.isalpha() == False:
                print 'Sorry, name not recognised.  Please try again.'
                continue
            break
        userSpecs.setName(name)

        while True:
            print '(Type "f" for female or "m" for male)'
            gender = raw_input('Please enter your gender: ')
            ## cover to lower case
            gender = gender.lower()
            ## check for quit option
            if gender == 'q':
                quit()
            if (gender != 'f') and (gender != 'm'):
                print 'Sorry, gender not recognised.  Please try again.'
                continue
            break
        userSpecs.setGender(gender)
    
        while True:
            age = raw_input('Please enter your age (in years): ')
            ## cover to lower case
            age = age.lower()
            ## check for quit option
            if gender == 'q':
                quit()
            ## parse string input to integer
            try:
                age = int(age)
            except:
                print 'Invalid input.  Only integers are accepted.'
                continue
            break
        userSpecs.setAge(age)

    ## method call
    userInfo()

    print 'Thanks %s' %(userSpecs.getName())
    print 'We are rolling the dice of life for you now ... good luck!'
    dice = random.randrange(1, 100, 1)
    userSpecs.setDice(dice)
    print 'Your game of life number is %.0f' %(userSpecs.getDice())
    
    print "               (( _______"
    print "     _______     /\O    O\ "
    print "    /O     /\   /  \      \ "
    print "   /   O  /O \ / O  \O____O\ ))"
    print "((/_____O/    \\    /O     /"
    print "  \O    O\    / \  /   O  /"
    print "   \O    O\ O/   \/_____O/"
    print "    \O____O\/ ))         ))"
    print "  (("
    
    
    ## assign country, status and check less than 2 dollars per day
    if (userSpecs.getDice() <= 32):
        userSpecs.setCountry('China')
        userSpecs.setLess2Dollars(0)
        if userSpecs.getGender() == 'f':
            if userSpecs.getAge() <= 24:
                status = 'single'
            else:
                status = 'married'
        if userSpecs.getGender() == 'm':
            if userSpecs.getAge() <= 26:
                status = 'single'
            else:
                status = 'married'
    elif userSpecs.getDice() <= 62:
        userSpecs.setCountry('India')
        userSpecs.setLess2Dollars(1)
        if userSpecs.getGender() == 'f':
            if userSpecs.getAge() <= 22:
                status = 'single'
            else:
                status = 'married'
        if userSpecs.getGender() == 'm':
            if userSpecs.getAge() <= 28:
                status = 'single'
            else:
                status = 'married'
    elif userSpecs.getDice() <= 70:
        userSpecs.setCountry('USA')
        userSpecs.setLess2Dollars(0)
        if userSpecs.getGender() == 'f':
            if userSpecs.getAge() <= 27:
                status = 'single'
            else:
                status = 'married'
        if userSpecs.getGender() == 'm':
            if userSpecs.getAge() <= 29:
                status = 'single'
            else:
                status = 'married'
    elif userSpecs.getDice() <= 76:
        userSpecs.setCountry('Indonesia')
        userSpecs.setLess2Dollars(1)
        if userSpecs.getGender() == 'f':
            if userSpecs.getAge() <= 22:
                status = 'single'
            else:
                status = 'married'
        if userSpecs.getGender() == 'm':
            if userSpecs.getAge() <= 26:
                status = 'single'
            else:
                status = 'married'
    elif userSpecs.getDice() <= 81:
        userSpecs.setCountry('Brazil')
        userSpecs.setLess2Dollars(0)
        if userSpecs.getGender() == 'f':
            if userSpecs.getAge() <= 26:
                status = 'single'
            else:
                status = 'married'
        if userSpecs.getGender() == 'm':
            if userSpecs.getAge() <= 28:
                status = 'single'
            else:
                status = 'married'
    elif userSpecs.getDice() <= 85:
        userSpecs.setCountry('Pakistan')
        userSpecs.setLess2Dollars(1)
        if userSpecs.getGender() == 'f':
            if userSpecs.getAge() <= 20:
                status = 'single'
            else:
                status = 'married'
        if userSpecs.getGender() == 'm':
            if userSpecs.getAge() <= 25:
                status = 'single'
            else:
                status = 'married'
    elif userSpecs.getDice() <= 90:
        userSpecs.setCountry('Nigeria')
        userSpecs.setLess2Dollars(1)
        if userSpecs.getGender() == 'f':
            if userSpecs.getAge() <= 18:
                status = 'single'
            else:
                status = 'married'
        if userSpecs.getGender() == 'm':
            if userSpecs.getAge() <= 27:
                status = 'single'
            else:
                status = 'married'
    elif userSpecs.getDice() <= 94:
        userSpecs.setCountry('Bangladesh')
        userSpecs.setLess2Dollars(1)
        if userSpecs.getGender() == 'f':
            if userSpecs.getAge() <= 16:
                status = 'single'
            else:
                status = 'married'
        if userSpecs.getGender() == 'm':
            if userSpecs.getAge() <= 21:
                status = 'single'
            else:
                status = 'married'
    elif userSpecs.getDice() <= 97:
        userSpecs.setCountry('Russia')
        userSpecs.setLess2Dollars(0)
        if userSpecs.getGender() == 'f':
            if userSpecs.getAge() <= 25:
                status = 'single'
            else:
                status = 'married'
        if userSpecs.getGender() == 'm':
            if userSpecs.getAge() <= 27:
                status = 'single'
            else:
                status = 'married'
    elif userSpecs.getDice() <= 100:
        userSpecs.setCountry('Japan')
        userSpecs.setLess2Dollars(0)
        if userSpecs.getGender() == 'f':
            if userSpecs.getAge() <= 29:
                status = 'single'
            else:
                status = 'married'
        if userSpecs.getGender() == 'm':
            if userSpecs.getAge() <= 31:
                status = 'single'
            else:
                status = 'married'
    else:
        ## debug comment
        print('\nThe early bird might get the worm, but the second mouse gets the cheese!\n')

    userSpecs.setStatus(status)
    
    ## check electricity
    if (userSpecs.getDice() <= 85) or (95 <= userSpecs.getDice()):
        userSpecs.setElectricity(1)
    elif (86 <= userSpecs.getDice()) and (userSpecs.getDice() <= 94):
        userSpecs.setElectricity(0)
    else:
        ## debug comment
        print('\nThere is a loose connection somewhere Sammy!')
    
    ## check water
    if (userSpecs.getDice() <= 85) or (91 <= userSpecs.getDice()):
        userSpecs.setWater(1)
    elif (86 <= userSpecs.getDice()) and (userSpecs.getDice() <= 94):
        userSpecs.setWater(0)
    else:
        ## debug comment
        print('\nThere is a leaking tap somewhere Jimmy!')
    
    
    print 'You are now living in ' + userSpecs.getCountry()
    print 'and you are currently ' + userSpecs.getStatus()
    
    if userSpecs.getElectricity() == 1:
        print 'Great news, you have electricity!'
    elif userSpecs.getElectricity() == 0:
        print 'There is a 50/50 chance you might have electricity'
    else:
        ## debug comment
        print('\nWe should not be here Freddy!')
        
    if userSpecs.getWater() == 1:
        print 'Wow!, you have access to clean drinking water!'
    elif userSpecs.getWater() == 0:
        print 'Oh No!, you do not have access to clean drinking water!'
    else:
        ## debug comment
        print('\nOops!  Something wrong with the pipework!')
        
    if userSpecs.getLess2Dollars() == 0:
        print 'Super!, you are earning more than 2 dollars per day.'
    elif userSpecs.getLess2Dollars() == 1:
        print 'Woops!  You are living in poverty, earning less than 2 dollars per day.'
    else:
        ## debug comment
        print('\nHells Bells!  There is a payment missing somewhere!')    
        
        
        
        
        
    