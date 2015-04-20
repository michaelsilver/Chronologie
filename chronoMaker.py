import json

def saveToFile(fp, dct):
    fp.seek(0)  # rewind
    fp.write(json.dumps(dct, sort_keys=True))
    fp.truncate()
    
def main():
    with open('chronoQuiz2.json', 'r+b') as fp:
        chrono = json.load(fp)

        quit = False
    
        try:
            while(not quit):
                date = input("Enter a date (-1 to quit): ")
                if(date == -1):
                    print("quitting...")
                    saveToFile(fp, chrono)
                    quit = True
                else:
                    event = raw_input("Event (blank to quit): ")
                    if(event == ''):
                        print("quitting...")
                        saveToFile(fp, chrono)
                        quit = True
                    else:
                        if date not in chrono:
                            chrono[date] = [event]
                        else:
                            chrono[date].append(event)
        finally:
            saveToFile(fp, chrono)

main()
