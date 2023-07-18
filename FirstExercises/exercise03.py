rows = int(input("How many rows do you want? "))
def printPascalsTriangle(rows):
    triangle = []
    
    for row in range(rows):
        currentRow = [1]
        if triangle:
            lastRow = triangle[-1]
            currentRow.extend([sum(pair) for pair in zip(lastRow, lastRow[1:])])
            currentRow.append(1)
        
        triangle.append(currentRow)
    
    for row in triangle:
        print(" ".join(str(num) for num in row))

printPascalsTriangle(rows)