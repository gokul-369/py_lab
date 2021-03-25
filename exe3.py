import random #import the random module
print(random.getstate())#Returns an object capturing the current internal state of the generator
print("\n")
print("*****RANDOM INTEGER*****")
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
print("the random values are",random.randint(a,b)) #Returns a random integer between a and b inclusive
print("\n")
print("*****RANDOM INTEGER*****")
seq=input("enter the value of sequence:")
print("the random values are",random.choice(seq)) #Return a random element from the non-empty sequence
print("\n")
print("*****SHUFFLE THE SEQUENCE*****")
list = [20, 16, 10, 5];
random.shuffle(list) #Shuffle the sequence
print ("Reshuffled list : ",  list)

print("\n")
print("*****PRINTING RANDOM INTEGER*****")
print("the random values are",random.random()) #Return the next random floating point number in the range [0.0, 1.0)
print("\n")
print("*****FLOATING NUMBER*****")
c=int(input("enter the value of c:"))
d=int(input("enter the value of d:"))
print("the random values are",random.uniform(c,d)) #Return a random floating point number between a and b inclusive
print("\n")
print("*****NORMAL DISTRIBUTION*****")
mu=int(input("enter the value of mu:"))
sigma=int(input("enter the value of sigma:"))
print("the random values are",random.normalvariate(mu,sigma)) #Normal distribution
print("\n")
print("*****RANDOM INTEGER*****")
k=int(input("enter the value of sequence:"))
print("the random values are",random.getrandbits(k)) #Returns a Python integer with k random bits
print("\n")
print("*****BETA DISTRIBUTION*****")
alpha=int(input("enter the value of alpha:"))
beta=int(input("enter the value of beta:"))
print("the random values are",random.betavariate(alpha,beta)) #beta distribution
print("\n")
print("*****GAMMA DISTRIBUTION*****")
alpha1=int(input("enter the value of alpha:"))
beta1=int(input("enter the value of beta:"))
print("the random values are",random.betavariate(alpha1,beta1)) #gamma distribution
