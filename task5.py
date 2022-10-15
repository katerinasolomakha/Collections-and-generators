N=int(input())
pupils={}
MARKS_COUNT=3
marks=[0]*MARKS_COUNT

for i in range(N):
    pupil=input().split()
    last_name=pupil[0]
    pupils[pupil[0]]=[int(i) for i in pupil[1:]]
    for i in range(MARKS_COUNT):
        marks[i]+=pupils[last_name][i]

print('-'*20)
avg_marks=(str('%.2f' % (marks[i]/N)) for i in range(MARKS_COUNT))
print(' '.join(avg_marks))
