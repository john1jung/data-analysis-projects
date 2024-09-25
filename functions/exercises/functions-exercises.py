# Part 1 A -- Make a Line

def make_line2(size):
    return '#'* size

def make_line(size):
   line = ""
   for i in range(size):
      line += "#"
   return line


# Part 1 B -- Make a Square
# create a function using your make_line function to code a square

def make_square(size):
    square = ''
    for i in range(size):
        square += (make_line(size) + "\n")
    return square
    
print(make_square(5))

# Part 1 C -- Make a Rectangle

def make_rect(height, width):
    rect = ''
    for i in range(height):
        rect += (make_line(width) + "\n")
    return rect
print(make_rect(10, 15))



# Part 2 A -- Make a Stairs

def make_stairs(steps):
    stairs = ''
    for i in range(steps):
        stairs += (make_line(i) + "\n")
    return stairs
print(make_stairs(14))


# Part 2 B -- Make Space-Line 
def make_space_line(numSpaces, numChar):
    return numSpaces * ' '+ numChar*'#' + numSpaces * ' '
print(make_space_line(90, 14))
    

# Part 2 C -- Make Isosceles Triangle

def make_isosceles_triangle(height):
    isosceles_triangle = ''
    for i in range(height):
        isosceles_triangle += (make_space_line(height - i - 1 , 1 + (i*2)) + "\n")
    return isosceles_triangle
print(make_isosceles_triangle(9))




# def make_isosceles_triangle(height):
#     isosceles_triangle = ''
#     for i in range(height):
#         isosceles_triangle += (make_space_line(0+i, (height-1)*2 -(1+i*2)) + "\n")
#     return isosceles_triangle
# print(make_isosceles_triangle(9))
# Part 3 -- Make a Diamond
def make_isosceles_triangle(height):
    isosceles_triangle = ''
    for i in range(height):
        isosceles_triangle += ( "\n"+  make_space_line(height - i - 1 , 1 + (i*2)) )
    return isosceles_triangle
print(make_isosceles_triangle(9))

def make_isosceles_triangle(height):
    isosceles_triangle = ''
    for i in range(height-1, -1, -1):
        isosceles_triangle += (make_space_line(height - i - 1 , 1 + (i*2)) + "\n")
    return isosceles_triangle
print(make_isosceles_triangle(9))

# def make_diamond(height):
#     diamond = ''
    
#     def make_isoceles_triange(height):



# class solution below
# def make_diamond(height):
#    diamond = ""
#    triangle = make_isosceles_triangle(height)
#    diamond += triangle[:-1]
#    for i in range(len(triangle)-1, -1, -1):
#       diamond += triangle[i]
#    return diamond

# print(make_diamond(5))
        



