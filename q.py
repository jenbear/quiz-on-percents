import os, random

count = 0
score = 0

file1 = open('q.txt', 'r')

f1content = file1.readlines()

while count < 10:
    os.system('clear')

    qnum = random.randint(0, len(f1content)/2-1)*2
    anum = qnum + 1

    print 'Question:', f1content[qnum], ''

    answer = input('\nYour answer: ')

    if str(answer).strip() == f1content[anum].strip():
        raw_input('\nCorrect! Hit enter...')
        score = score + 1
    else:
        print ('\nWrong! Hit enter...')
        print 'Answer', f1content[anum]
        raw_input('Press enter to Contuine')

    count = count + 1

print '\nYour score is:', score
