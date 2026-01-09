
N1, N2, N3, N4 = map(float, input().split())

average = ( N1*2 + N2*3 + N3*4 + N4*1 ) / 10

print(f"Media: {average:.1f}")

if average >= 7.0 :
    print("Aluno aprovado.")
elif average < 5.0 :
    print("Aluno reprovado.")    
else:
    print("Aluno em exame." )  
    #In case of exam, read one more score. 
    nextScore = float(input())
    #Print the message "Nota do exame: "
    print(f"Nota do exame: {nextScore:.1f}")
    #Recalculate the average
    finalAverage = (average + nextScore) / 2
    #in case of average 5.0 or more
    if finalAverage >= 5.0 :
        print("Aluno aprovado.")
    #in case of average 4.9 or less.
    elif finalAverage <= 4.9:
        print("Aluno reprovado.")
        
    #approved or reproved after the exam)   
    print(f"Media final: {finalAverage:.1f}")
        
    
    