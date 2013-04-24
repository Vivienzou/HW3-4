4X4
=====
%time
def f(b,c,d,e,f,h,i,j,k,l,m,n,o,p,q,s):
    R = PolynomialRing(QQ,16,'x')
    a = matrix(R,4,4,R.gens())
    a[0,0] = b
    a[0,1] = c
    a[0,2] = d
    a[0,3] = e
    a[1,0] = f
    a[1,1] = h
    a[1,2] = i
    a[1,3] = j
    a[2,0] = k
    a[2,1] = l
    a[2,2] = m
    a[2,3] = n
    a[3,0] = o
    a[3,1] = p
    a[3,2] = q
    a[3,3] = s
    a.det()

%time
%cython
def f(b,c,d,e,f,h,i,j,k,l,m,n,o,p,q,s):
    R = PolynomialRing(QQ,16,'x')
    a = matrix(R,4,4,R.gens())
    a[0,0] = b
    a[0,1] = c
    a[0,2] = d
    a[0,3] = e
    a[1,0] = f
    a[1,1] = h
    a[1,2] = i
    a[1,3] = j
    a[2,0] = k
    a[2,1] = l
    a[2,2] = m
    a[2,3] = n
    a[3,0] = o
    a[3,1] = p
    a[3,2] = q
    a[3,3] = s
    a.det()
