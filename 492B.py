n,l = input().strip().split()

n = int(n)
l = int(l)

lanterns = input().strip().split()

lanterns = [int(x) for x in lanterns]

lanterns = sorted(lanterns)

d = 0

for i in range(n-1):
    d = max(d,lanterns[i+1]-lanterns[i])


print (max(d/2,lanterns[0],l-lanterns[-1]))     
