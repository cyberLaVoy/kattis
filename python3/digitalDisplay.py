
# used to create translation dictionary
"""
translation = {}

for i in range(11):
    digit = []
    for j in range(7):
        digit.append(input())
    translation[i] = digit

print(translation)
"""

translation = {0: ['+---+', '|   |', '|   |', '+   +', '|   |', '|   |', '+---+'], 1: ['    +', '    |', '    |', '    +', '    |', '    |', '    +'], 2: ['+---+', '    |', '    |', '+---+', '|    ', '|    ', '+---+'], 3: ['+---+', '    |', '    |', '+---+', '    |', '    |', '+---+'], 4: ['+   +', '|   |', '|   |', '+---+', '    |', '    |', '    +'], 5: ['+---+', '|    ', '|    ', '+---+', '    |', '    |', '+---+'], 6: ['+---+', '|    ', '|    ', '+---+', '|   |', '|   |', '+---+'], 7: ['+---+', '    |', '    |', '    +', '    |', '    |', '    +'], 8: ['+---+', '|   |', '|   |', '+---+', '|   |', '|   |', '+---+'], 9: ['+---+', '|   |', '|   |', '+---+', '    |', '    |', '+---+'], 10: [' ', ' ', 'o', ' ', 'o', ' ', ' ']}

def showTime(display): 
    for j in range(len(display[0])):
        row = ""
        for i in range(len(display)):
             row += display[i][j] + '  '
        print(row[0:-2])

def solve():
    time = input()
    while time != "end":
        time = [c for c in time]
        display = []
        for c in time:
            if c == ':':
                display.append(translation[10])
            else:
                display.append(translation[int(c)])
        showTime(display)
        time = input()
        print()
        print()
    print("end")
solve()



"""
+---+
|   |
|   |
+   +
|   |
|   |
+---+
    +
    |
    |
    +
    |
    |
    +
+---+
    |
    |
+---+
|    
|    
+---+
+---+
    |
    |
+---+
    |
    |
+---+
+   +
|   |
|   |
+---+
    |
    |
    +
+---+
|    
|    
+---+
    |
    |
+---+
+---+
|    
|    
+---+
|   |
|   |
+---+
+---+
    |
    |
    +
    |
    |
    +
+---+
|   |
|   |
+---+
|   |
|   |
+---+
+---+
|   |
|   |
+---+
    |
    |
+---+
     
     
  o  
     
  o  
     
     
"""