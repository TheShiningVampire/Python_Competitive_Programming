# %%
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')

n = np.arange(-10,10,1)
v = np.linspace(-10 , 10 , 50)

l = n.size

imp = np.zeros(l)
imp[np.where(n==0)] = 1

plt.stem(n , imp)
plt.title('Impulse Signal');
plt.xlabel('Samples'); plt.ylabel('Amplitude');
plt.grid(True)
plt.show()

step = np.zeros(l)
ind = np.where(n>=0)
step[ind] = 1


plt.stem(n , step)
plt.title('Step Signal');
plt.xlabel('Samples'); plt.ylabel('Amplitude');
plt.grid(True)
plt.show()


# %%

n = 5
while n:
    print(n)
    n = n-1

# %%
a = 5
b = 1
print(a , b , sep = '-', end = '= ');print(a-b)
# %%
t = 8
for i in range(1,t):
    print(i)
# %%
a = list(map(int, input().split()))
# %%
