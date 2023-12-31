import datetime, random

def getBirthdays(numberOfBirthdays):
     # retuns a list of birthdays
     birthdays = []
     for i in range (numberOfBirthdays):
         # the year is not important for the program, as long
         # as they all have the same year
         startOfYear = datetime.date(2000,1,1)
         
         # get a ramdaom day into the date
         randomNumberOfDays = datetime.timedelta(random.randint(0,364))
         birthday = startOfYear + randomNumberOfDays
         birthdays.append(birthday)
     return getBirthdays

def getMatch(birthdays):
    '''return the birthday object that occurs more than once
    in the birsthdays list '''
    if len(birthdays) == len(set(birthdays)):
        return None # all birthdays are unique so the answer is none
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA # returns the matching birthdays
            
            
# Display the intro:

print(''' Birthday Paradox - lesson from The Big Book of Small Python Projects''')

print('''The birthday paradox show us that in a group of N people, the odds 
      that two of them have matching birthdays is suprisingly large. 
      This program does a Monte Carlo simulation(that is, repeated random
      simulations) to explore this concept. It's not actully a paradox, its just a
      suprising result''' )


# Sets up a tuple of month names in order:
MONTHS = ('Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Mov','Dec')

while True:  # Keep asking until the user enters a valid amount.
    print("How many birthdays shall i generate? (max of 100)")
    response = input('>')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break #User has entered a valid amount
print()

# Generate and display the birthdays
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
print(type(birthdays))
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday
        print(',',end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName,birthday.day)
    print(dateText, end='')
print()
print()

# Determine if there are two birthday that match
match = getMatch(birthdays)

# Display the results
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{}{}'.format(monthName, match.day)
    print('multiple people have a birthday on'. dateText)
else:
    print('ther are no matching birthdays.')
print()

# Run through 100,000 simulation
print("Generating", numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations')
simMatch = 0 # How may simulations had matching birthday in them.add
for i in range(100000):
    #Report on the progress every 10,000 simulations:
    if i % 10000 == 0:
        print(i, 'simulation run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

#Display simulation results:
probability = round(simMatch / 100000 * 100, 2)
print('Out of 100,000 simulations of ', numBDays, 'people there was a ')
print('matching birthday in that group', simMatch, 'times.  This means')
print('that', numBDays, 'people have a ', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probaaly more that you would think!')