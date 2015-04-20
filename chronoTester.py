import random
import json

def repeatAndLearn(date):
    print 'Nope: ' + date
    repeat = True
    while(repeat):
        echo = input('Repeat it back to me: ')
        repeat = not (echo == int(date))
    print 'Yup: ' + date
        
def main():
    # testWith = '/Users/michaelsilver/Downloads/chronoQuiz2ThirdPart.json'
    testWith = 'chronoQuiz2Post1837.json' 
    with open(testWith, 'rb') as fp:
        chrono = json.load(fp)
        chronoFlat = {}
        for key in chrono.keys():
            for value in chrono[key]:
                chronoFlat[value] = key

        errorWindow = 2        # years
        quit = False
        
        print 'When was (0 to quit)...'
        while(not quit):
            event = random.choice(chronoFlat.keys())
            date  = chronoFlat[event]
            rawGuess = raw_input(event + ': ')
            guessIsString = False
            try:
                guess = int(rawGuess)
            except ValueError:
                guess = rawGuess
                guessIsString = True

            if guessIsString:
                repeatAndLearn(date)
            else:
                if guess == 0:
                    quit = True
                elif abs(int(date) - guess) <= errorWindow:
                    print 'Yup: ' + date
                else:
                    repeatAndLearn(date)

main()
