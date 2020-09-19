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
def make_rot_mtx(angle, dim = 2):
    sin = math.sin(angle)
    cos = math.cos(angle)
    if dim == 2:
        mtx = [[cos, -sin],[sin,cos]]
        return mtx
    if dim == 3:
        print('Sorry, don\'t know how to make that yet')
        
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
            
    


def rotate(vec, angle):
    vec = [vec[:]]
    rot_mtx = make_rot_mtx(angle, dim)
    new_vector = mult_mtxs(vec, rot_mtx)
    return new_vector

rotated_vector = rotate(vec, 3.14)

print(rotated_vector)
