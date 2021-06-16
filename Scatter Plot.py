#!/usr/bin/env python
# coding: utf-8

# In[14]:


import csv
import matplotlib.pyplot as plt
features = []

with open ("IRIS.csv","r") as data:
    readData = csv.reader(data)
    for row in readData:
        features.append(row)

sepal_length_setosa = []
sepal_length_versilcolor = []
sepal_length_virginica = []

sepal_width_setosa = []
sepal_width_versilcolor = []
sepal_width_virginica = []

features.pop(0)

for everyItem in range(0,50):
    sepal_length_setosa.append(float(features[everyItem][0]))
for everyItem in range(50,100):
    sepal_length_versilcolor.append(float(features[everyItem][0]))
for everyItem in range(100,150):
    sepal_length_virginica.append(float(features[everyItem][0]))
    
for everyItem in range(0,50):
    sepal_width_setosa.append(float(features[everyItem][1]))
for everyItem in range(50,100):
    sepal_width_versilcolor.append(float(features[everyItem][1]))
for everyItem in range(100,150):
    sepal_width_virginica.append(float(features[everyItem][1]))
    
plt.scatter(sepal_length_setosa,sepal_width_setosa, label = 'Setosa',color = 'y' )
plt.scatter(sepal_length_versilcolor,sepal_width_versilcolor, label = 'Versilcolor',color = 'r' )
plt.scatter(sepal_length_virginica,sepal_width_virginica, label = 'Virginica',color = 'g' )
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal -> Length vs Width")
plt.legend()
plt.show()


# In[15]:


#petal length vs petal width
import csv
import matplotlib.pyplot as plt
features = []

with open ("IRIS.csv","r") as data:
    readData = csv.reader(data)
    for row in readData:
        features.append(row)

petal_length_setosa = []
petal_length_versilcolor = []
petal_length_virginica = []

petal_width_setosa = []
petal_width_versilcolor = []
petal_width_virginica = []

features.pop(0)

for everyItem in range(0,50):
    petal_length_setosa.append(float(features[everyItem][2]))
for everyItem in range(50,100):
    petal_length_versilcolor.append(float(features[everyItem][2]))
for everyItem in range(100,150):
    petal_length_virginica.append(float(features[everyItem][2]))
    
for everyItem in range(0,50):
    petal_width_setosa.append(float(features[everyItem][3]))
for everyItem in range(50,100):
    petal_width_versilcolor.append(float(features[everyItem][3]))
for everyItem in range(100,150):
    petal_width_virginica.append(float(features[everyItem][3]))
    
plt.scatter(petal_length_setosa,petal_width_setosa, label = 'Setosa',color = 'y' )
plt.scatter(petal_length_versilcolor,petal_width_versilcolor, label = 'Versilcolor',color = 'r' )
plt.scatter(petal_length_virginica,petal_width_virginica, label = 'Virginica',color = 'g' )
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Petal -> Length vs Width")
plt.legend()
plt.show()


# In[16]:


#sepal length vs petal width
import csv
import matplotlib.pyplot as plt
features = []

with open ("IRIS.csv","r") as data:
    readData = csv.reader(data)
    for row in readData:
        features.append(row)

sepal_length_setosa = []
sepal_length_versilcolor = []
sepal_length_virginica = []

petal_width_setosa = []
petal_width_versilcolor = []
petal_width_virginica = []

features.pop(0)

for everyItem in range(0,50):
    sepal_length_setosa.append(float(features[everyItem][0]))
for everyItem in range(50,100):
    sepal_length_versilcolor.append(float(features[everyItem][0]))
for everyItem in range(100,150):
    sepal_length_virginica.append(float(features[everyItem][0]))
    
for everyItem in range(0,50):
    petal_width_setosa.append(float(features[everyItem][3]))
for everyItem in range(50,100):
    petal_width_versilcolor.append(float(features[everyItem][3]))
for everyItem in range(100,150):
    petal_width_virginica.append(float(features[everyItem][3]))
    
plt.scatter(sepal_length_setosa,petal_width_setosa, label = 'Setosa',color = 'y' )
plt.scatter(sepal_length_versilcolor,petal_width_versilcolor, label = 'Versilcolor',color = 'r' )
plt.scatter(petal_width_virginica,sepal_length_virginica, label = 'Virginica',color = 'g' )
plt.xlabel("Sepal Length")
plt.ylabel("Petal Width")
plt.title("Sepal vs Petal -> Length vs Width")
plt.legend()
plt.show()


# In[4]:


#petal length vs sepal width
import csv
import matplotlib.pyplot as plt
features = []

with open ("IRIS.csv","r") as data:
    readData = csv.reader(data)
    for row in readData:
        features.append(row)

petal_length_setosa = []
petal_length_versilcolor = []
petal_length_virginica = []

sepal_width_setosa = []
sepal_width_versilcolor = []
sepal_width_virginica = []

features.pop(0)

for everyItem in range(0,50):
    petal_length_setosa.append(float(features[everyItem][2]))
for everyItem in range(50,100):
    petal_length_versilcolor.append(float(features[everyItem][2]))
for everyItem in range(100,150):
    petal_length_virginica.append(float(features[everyItem][2]))
    
for everyItem in range(0,50):
    sepal_width_setosa.append(float(features[everyItem][1]))
for everyItem in range(50,100):
    sepal_width_versilcolor.append(float(features[everyItem][1]))
for everyItem in range(100,150):
    sepal_width_virginica.append(float(features[everyItem][1]))
    
plt.scatter(petal_length_setosa,sepal_width_setosa, label = 'Setosa',color = 'y' )
plt.scatter(petal_length_versilcolor,sepal_width_versilcolor, label = 'Versilcolor',color = 'r' )
plt.scatter(petal_length_virginica,sepal_width_virginica, label = 'Virginica',color = 'g' )
plt.xlabel("Petal Length")
plt.ylabel("Sepal Width")
plt.title("Petal vs Sepal -> Length vs Width")
plt.legend()
plt.show()


# In[5]:


#sepal width vs sepal length
import csv
import matplotlib.pyplot as plt
features = []

with open ("IRIS.csv","r") as data:
    readData = csv.reader(data)
    for row in readData:
        features.append(row)

sepal_length_setosa = []
sepal_length_versilcolor = []
sepal_length_virginica = []

sepal_width_setosa = []
sepal_width_versilcolor = []
sepal_width_virginica = []

features.pop(0)

for everyItem in range(0,50):
    sepal_length_setosa.append(float(features[everyItem][0]))
for everyItem in range(50,100):
    sepal_length_versilcolor.append(float(features[everyItem][0]))
for everyItem in range(100,150):
    sepal_length_virginica.append(float(features[everyItem][0]))
    
for everyItem in range(0,50):
    sepal_width_setosa.append(float(features[everyItem][1]))
for everyItem in range(50,100):
    sepal_width_versilcolor.append(float(features[everyItem][1]))
for everyItem in range(100,150):
    sepal_width_virginica.append(float(features[everyItem][1]))
    
plt.scatter(sepal_width_setosa,sepal_length_setosa, label = 'Setosa',color = 'y' )
plt.scatter(sepal_width_versilcolor,sepal_length_versilcolor, label = 'Versilcolor',color = 'r' )
plt.scatter(sepal_width_virginica,sepal_length_virginica, label = 'Virginica',color = 'g' )
plt.ylabel("Sepal Length")
plt.xlabel("Sepal Width")
plt.title("Sepal -> Width vs Length")
plt.legend()
plt.show()


# In[10]:


#petal length vs petal width
import csv
import matplotlib.pyplot as plt
features = []

with open ("IRIS.csv","r") as data:
    readData = csv.reader(data)
    for row in readData:
        features.append(row)

petal_length_setosa = []
petal_length_versilcolor = []
petal_length_virginica = []

petal_width_setosa = []
petal_width_versilcolor = []
petal_width_virginica = []

features.pop(0)

for everyItem in range(0,50):
    petal_length_setosa.append(float(features[everyItem][2]))
for everyItem in range(50,100):
    petal_length_versilcolor.append(float(features[everyItem][2]))
for everyItem in range(100,150):
    petal_length_virginica.append(float(features[everyItem][2]))
    
for everyItem in range(0,50):
    petal_width_setosa.append(float(features[everyItem][3]))
for everyItem in range(50,100):
    petal_width_versilcolor.append(float(features[everyItem][3]))
for everyItem in range(100,150):
    petal_width_virginica.append(float(features[everyItem][3]))
    
plt.scatter(petal_width_setosa,petal_length_setosa, label = 'Setosa',color = 'y' )
plt.scatter(petal_width_versilcolor,petal_length_versilcolor, label = 'Versilcolor',color = 'r' )
plt.scatter(petal_width_virginica,petal_length_virginica, label = 'Virginica',color = 'g' )
plt.ylabel("Petal Length")
plt.xlabel("Petal Width")
plt.title("Petal -> Width vs Length")
plt.legend()
plt.show()


# In[19]:


import csv
import matplotlib.pyplot as plt
features = []

with open ("IRIS.csv","r") as data:
    readData = csv.reader(data)
    for row in readData:
        features.append(row)
features.pop(0)

for i in range(len(features)):
    for j in range(4):
        features[i][j]=float(features[i][j])
        
setosa = [[],[],[],[]]
versicolor = [[],[],[],[]]
virginica = [[],[],[],[]]
for i in range(150):
  if features[i][4] == 'Iris-setosa':
    for j in range(4):
        setosa[j].append(features[i][j])
  elif features[i][4] == 'Iris-virginica':
    for j in range(4):
        virginica[j].append(features[i][j])
  else:
    for j in range(4):
        versicolor[j].append(features[i][j])

    

plt.subplot(211)
plt.title("Sepal Length vs Width")
plt.scatter(setosa[0],setosa[1],label="setosa",color="r")
plt.scatter(versicolor[0],versicolor[1],label="versicolor",color="b")
plt.scatter(virginica[0],virginica[1],label="virginica",color="g")
plt.legend()
plt.subplot(212)
plt.title("Petal Length vs Width")
plt.scatter(setosa[2],setosa[3],label="setosa",color="r")
plt.scatter(versicolor[2],versicolor[3],label="versicolor",color="b")
plt.scatter(virginica[2],virginica[3],label="virginica",color="g")
plt.legend()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




