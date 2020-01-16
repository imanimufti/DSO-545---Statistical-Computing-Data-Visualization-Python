# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %%
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'pre_score': [4, 24, 31, 2, 3],
        'mid_score': [25, 94, 57, 62, 70],
        'post_score': [5, 43, 23, 23, 51]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'pre_score', 'mid_score', 'post_score'])
df


# %%
plt.figure(figsize = (5,4))
pos = np.arange(len(df.first_name))
width = 0.3

plt.bar(pos,
       df.pre_score,
       width,
       color = 'red',
       alpha = 0.3,
       label= 'pre score')

plt.bar(pos + width,
       df.mid_score,
       width,
       color = 'orange',
       alpha = 0.3,
       label = 'mid score')

plt.bar(pos + width*2,
       df.post_score,
       width,
       color = 'yellow',
       alpha = 0.3,
       label = 'post score')

ax = plt.gca()
plt.xticks(pos)
ax.set_xticks([p + width for p in pos])
ax.set_xticklabels(df.first_name)
plt.yticks(np.arange(0,161,20))
ax.yaxis.grid(which = 'major', linestyle= ':')
ax.xaxis.grid(which = 'major', linestyle= ':')
#plt.xlim(min(pos)-width, max(pos)+width*4)

plt.title('Test Subject Scores')
plt.legend(loc = 'upper left')
plt.show()

# %%
X = ['A','B','C']
Y = [1,2,3]
Z = [2,3,4]

df = pd.DataFrame(np.c_[Y,Z,Y], index=X)
df.plot.bar()

plt.show()

# %%
