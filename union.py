A={100,7,8}
B={200,7,8}
C={300,2,3}
D={100,200,300}
print(A.union(D))
print(B.union(D))
print(C.union(D))
print(A.union(B).union(C).union(D))