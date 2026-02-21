ch =input("enter the character :")
uppercase="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
lowercase="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
digits="0,1,2,3,4,5,6,7,8,9"

if ch in uppercase:       #membership
    print(F'Uppercase :')
elif ch in lowercase:
    print(F'Lowercase :')    
elif ch in digits:
    print(F'Digit :')
else:
    print(F'Special Character :')        
