n = int(input().strip())
for a0 in range(n):
    grade = int(input("Enter grade : ").strip())

    if grade >= 38:
        mod5 = grade % 5
        if mod5 >= 3:
            grade = grade + (5 - mod5)
    print('Expected grade:' , grade) 
    #print(grade)
    
    
    
    """
    [summary]:
    Test Cases : 
    38 -> 40
    23 -> 23
    123 -> 125
    67 -> 67
    
    """