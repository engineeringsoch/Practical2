import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("Information.csv")
df =pd.DataFrame(data)
print(df)
df['average']=df[['Math','Physics','Marathi']].mean(axis=1)
print(df)

plt.figure(figsize=(10,5))
plt.bar(df['Students'],df['average'] ,color=['skyblue'])
plt.xlabel('Students')
plt.ylabel('Average Score')
plt.title('Average Scores of Students')
plt.show()

plt.figure(figsize=(10,5))
plt.plot(df['Students'],df['Math'],marker='p',label='Math',color='r')
plt.plot(df['Students'],df['Physics'],marker='o',label='Physics',color='g')
plt.plot(df['Students'],df['Marathi'],marker='o',label='Marathi',color='b')
plt.xlabel('Students')
plt.ylabel('Scores')
plt.title('Scores of Students in Different Subjects')
plt.legend()
plt.show()
# Standard deviation of Physics
math_scores = np.array(df['Math'])
print("Mean Math Score:", np.std(math_scores))