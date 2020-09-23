import math
#read dimension
dim = int(input())

#read vector
vec = list(map(float, input().split()))
if len(vec) != dim:
    print('Incorrect dimension!')
    exit()

#calculate length
length = len(vec)

#scale by input constant
def scale(vec, c):
    ans = [el*c for el in vec]
    return ans

scaled_vector = scale(vec, 2)

#rotate vector by a given angle
def make_rot_mtx2(angle):
    sin = math.sin(angle)
    cos = math.cos(angle)
    mtx = [[cos, -sin],[sin,cos]]
    return mtx

def make_rot_mtx3(angle, axes):
    sin = math.sin(angle)
    cos = math.cos(angle)
    if axes == 'x':
        return [[1,0,0],[0,cos,-sin],[0,sin,cos]]
    elif axes == 'y':
        return [[cos,0,sin],[0,1,0],[-sin,0,cos]]
    elif axes == 'z':
        return [[1,cos,-sin],[sin,cos,0],[0,0,1]]

def mult_mtxs(A,B):
    X = []
    for row in range(len(A)):
        new_row = []
        for col in range(len(B[0])):
            a = 0
            for i in range(len(A[0])):
                a += A[row][i]*B[i][col]
            new_row.append(a)
        X.append(new_row)
    return X
            
    


def rotate(vec, angle, axes = None):
    vec = [vec[:]]
    if not axes:
        rot_mtx = make_rot_mtx2(angle)
    elif axes:
        rot_mtx = make_rot_mtx3(angle, axes)
    new_vector = mult_mtxs(vec, rot_mtx)
    return new_vector

#test
if dim == 2:
    rotated_vector = rotate(vec,3.14)
else:
    rotated_vector = rotate(vec, 3.14, 'x')

print(rotated_vector)
