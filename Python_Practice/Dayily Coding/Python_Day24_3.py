def Hackjum(score) :
    for i in range(7) :
        index = score // 0.5
        grades = ['F', 'F', 'F', 'F', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']
        return grades[index]

print(Hackjum(int(input("학점을 입력하세요. :"))))
print(Hackjum())
