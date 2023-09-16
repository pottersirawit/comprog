def knows(R,x,y):
    if x in R:
        if y in R[x]:
            return True
    return False
def is_celeb(R,x): # return True if a is celeb, otherwise return False
 # return False if x knows someone who is not him/herself
 # return False if there exists someone in R who don't know x
 # otherwise return True 
    if x not in R:return False
    if len(R[x]) != 0 and not( len(R[x])==1 and x in R[x]):return False
    for i in R:
        if i == x:continue
        if x not in R[i]:return False
    return True
def find_celeb(R):
 # for each person x in the party
 # if x is celeb --> return x
 # if no celeb in the party --> return None
    for i in R:
        if is_celeb(R,i):return i
def read_relations() :
 # build a dictionary R from inputs 
 # whose structure is shown in the example
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1 : break
        if d[0] not in R:
            R[d[0]] = {d[1]}
        else:
            R[d[0]].add(d[1])
        if d[1] not in R:
            R[d[1]] = set()
    return R
def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)
exec(input().strip()) # do not remove this line