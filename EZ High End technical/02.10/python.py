#print numbers from 1 to n using recursion
'''n=int(input())
def fun(n):
    if(n==0):
        return
    fun(n-1)
    print(n)
fun(n)'''
#print number from n to 1 using recursion
'''n=int(input())
def fun(n):
    if(n==0):
        return
    print(n)
fun(n-1)
fun(n)'''
#check whether string is palindrome or not
'''name=input()
rev=name[::-1]
if(name==rev):
    print("true")
else:
    print("false")'''
#check whether string is palidrome or not using loopss=input()
'''s=input()
i=0
j=len(s)-1
while i<=j:
    if(s[i]!=s[j]):
        print("not palindrome")
        break
    i+=1
    j-+1
else:
    print("palindrome")'''
#using recursion 
def fun(s,i,j):
    if i>j:
        return True
    if s[i]!=s[j]:
        return False
    return fun(s,i+1,j-1)
s=input()
print(fun(s,0,len(s)-1))


