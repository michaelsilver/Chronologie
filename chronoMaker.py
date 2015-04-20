import json

def saveToFile(fp, dct):
    for key in dct.keys():
        dct[key] = list(set(dct[key]))
    fp.seek(0)  # rewind
    fp.write(json.dumps(dct, sort_keys=True))
    fp.truncate()
    
def main():
    useChronology = 'chronoMerge.json'
    # useChronology = 'chronoQuiz2Full.json'
    with open(useChronology, 'r+b') as fp:
        chrono = json.load(fp)

        quit = False
    
        try:
            while(not quit):
                date = raw_input("Enter a date (-1 to quit): ")
                if(date == '-1'):
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
