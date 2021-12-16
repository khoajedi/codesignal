def solution(image):
    box = []
    width = len(image[0])
    height = len(image)
    
    for i in range(1, height - 1):
        row = []
        for j in range(1, width - 1):
            top = image[i-1][j-1] + image[i-1][ j ] + image[i-1][j+1]
            mid = image[ i ][j-1] + image[ i ][ j ] + image[ i ][j+1]
            bot = image[i+1][j-1] + image[i+1][ j ] + image[i+1][j+1]
            row.append((top + mid + bot) // 9)
        box.append(row)
    
    return box