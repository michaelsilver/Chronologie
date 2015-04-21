import json

def merge_dols(dol1, dol2):
    keys = set(dol1).union(dol2)
    no = []
    return dict((k, dol1.get(k, no) + dol2.get(k, no)) for k in keys)

def main():
    file1 = 'chronoQuiz2Full.json'
    file2 = 'chronoFinal.json'

    with open(file1, 'rb') as fp1:
        chrono1 = json.load(fp1)
        with open(file2, 'rb') as fp2:
            chrono2 = json.load(fp2)
            chronoMerge = merge_dols(chrono1, chrono2)

            print 'Writing to disk...'
            with open('chronoMerge.json', 'wb') as fpMerge:
                json.dump(chronoMerge, fpMerge)

    print 'DONE.'

main()
