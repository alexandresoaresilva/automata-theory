
# coding: utf-8

# In[19]:


import numbers, fractions
#ECE, Texas Tech
#theory of automata HW#1
#fall 2018, Dr. Nelson Rushton


#ex. 13 implementation (assumed inputs: natural numbers or 2-tuples)
def f(x):
    if isinstance(x,numbers.Number) and x >= 0: return x+1
    return x[0]-1
print()	
print("|||||  N U{(1,1)} -> N  |||||")
print("for (1,1), " + str(f((1,1))) )
print("for 10, " + str(f(10)) )


# In[2]:


#ex. 14 implementation (Dr. Rushton's)
def f(x):
    if isinstance(x,int) and x >= 0: return x+20
    return x[1]-1
print()
print("|||||  N U{(1,1),...,(1,20)} -> N")
print("for (1,1), " + str(f((1,1))) )
print("for 20, " + str( f(20) ) )


# In[5]:


#ex. 15 implementation
def f(x):
    if x>=0: return 2*x
    return -(2*x+1)
print()
print("|||||  Z -> N  |||||")
print("for 0, " + str(f(0)) )
print("for 20, " + str( f(20) ) )


# In[17]:


#ex. 16 implementation
def f(*x):
    return (3**x[0]*5**x[1])
    #if isinstance(x,tuple) and len(x,2): 
print()
print("|||||  N x N -> N  |||||")
print("for (0,0), " + str(f(0,0)) )
print("for (2,0), " + str(f(2,0)) )


# In[16]:
# N x N x N -> N
def f(*x):
    return (3**x[0]*5**x[1]*7**x[2])
    #if isinstance(x,tuple) and len(x,3):
    
print()
print("|||||  N x N x N -> N  |||||")
print("for (0,0,0), " + str(f(0,0,0)) )
print("for (2,0,1), " + str(f(2,0,1)) )


# In[20]:


# Q -> N



#fract.numerator
def f(x):
  #  if isinstance(x,fractions.Fraction) and fractions.gcd(x.numerator, x.denominator) == denominator: #fraction's lowest form
	if x.numerator is 0: return 0
	elif x > 0 : return (2**x.numerator*3**x.denominator)
	else: return (5**x.numerator * 7**x.denominator)
    
    #if isinstance(x,tuple) and len(x,3):
    
fract1 = fractions.Fraction('2/3')
fract2 = fractions.Fraction('-3/2')
#fractions.gcd(a, b)
print()
print("|||||  Q -> N  |||||")
print("for 2/3, "+str(f(fract1) ))
print("for 3/2, "+ str(f(fract2) ))

# The set of all finite strings of ascii characters. (Godel numbering is one way to do this)
