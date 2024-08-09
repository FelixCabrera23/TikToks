def spiralMatrixIII(rows,cols,rStart,cStart):
    # some variables
    cells = rows * cols
    stp = 1
    y = rStart
    x = cStart
    
    result = [[y,x]]
    
    d = 1
    i = 1
    
    while i < cells:
        # move in the x direction
        for j in range(stp):
            x += d
            if x>=0 and x<cols and y>=0 and y<rows:
                result.append([y,x])
                i+=1
        # move in the y direction
        for k in range(stp):
            y += d
            # chek if (y,x) is correct
            if x>=0 and x<cols and y>=0 and y<rows:
                result.append([y,x])
                i+=1
        
        # finaly increase step
        stp += 1
        # change direction
        d *= -1
    return result


        
        
        
        
        
        
        