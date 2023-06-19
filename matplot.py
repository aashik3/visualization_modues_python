import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from mpl_toolkits import mplot3d

#1 plotting
''' x= np.arange(-100,101,1)
y= 0.5 *x**2 +2*x

#you can also plot two or more graph in one graph
y1 =np.sin(x) *2000
plt.plot(x,y,ls='dashed',c='c')
plt.plot(x,y1,lw='12')
plt.show()'''

#2 marker
'''#You can use the keyword argument marker to emphasize each point
ypoints = np.array([3, 8, 1, 10])
#plt.plot(ypoints, marker = 'o')
#This parameter is also called fmt, and is written with this syntax:marker|line|color
#there are many colors , linestyle available

plt.plot(ypoints,'o--r')
plt.show()'''

#3 marker properties and grid
'''
ypoints = np.array([3, 8, 1, 10])
#markersize 'ms' to set the size of the markers
#markeredgecolor or the shorter mec to set the color of the edge of the markers:
#markerfacecolor or the shorter mfc to set the color inside the edge of the markers
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
#grid() function to add grid lines to the plot.
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()'''

#4 subplots
'''x=np.arange(0,100,1)
y1=np.sin(x)
y2= x**2 +2*x
y3=np.cos(x)
y4= np.tan(x)
y5=np.sin(x) *1.5
#The subplot() function takes three arguments that describes the layout of the figure.
#first one detemines the no.of rows and second one determines columns and
# third define the index of the current plot

x1=plt.subplot(3, 2 ,1)
x1.plot(x,y1)
x1.plot(x,y3)
#we can also multiple plot in single plot example is x1,x2
x2=plt.subplot(3,2,2)
x2.plot(x,y2)
x2.plot(x,y4)

x3=plt.subplot(3,2,3)
x3.plot(x,y3)

x4=plt.subplot(3,2,4)
x4.plot(x, y4, c='hotpink', marker='o', mec='r', mfc='r', ms= 7)

x5=plt.subplot(3,2,5)
x5.plot(x,y5,'o-r')

#plt.tight_layout() makes our all plots arranged
plt.tight_layout()
plt.show()
'''
#5 multiple windows and subplot
'''x=np.arange(0,100,1)
y1=np.sin(x)
y2= x**2 +2*x
y3=np.cos(x)
y4= np.tan(x)

plt.figure(1)
x1=plt.subplot(2, 1 ,1)
x1.plot(x,y1)
x1.plot(x,y3)

plt.figure(2)
x2=plt.subplot(2,2,2)
x2.plot(x,y2)
x2.plot(x,y4)

plt.figure(3)
plt.plot(x,y4)

plt.show()'''

#6 inbuild styling design

'''#search in browser 'matplotlib stylesheet reference' you can see different stylesheet
x=np.arange(0,30,1)
y=np.sin(x)
y2= x**2 +2*x
y3=np.tan(x)

plt.figure(1)
style.use('bmh')
plt.plot(x,y)
plt.plot(x,y2)

plt.figure(2)
style.use('dark_background')
plt.plot(x,y3)

plt.show()'''

#7 labels
'''#xlabel() and ylabel() functions to set a label for the x- and y-axis.
# you can use the title() function to set a title for the plot.
x=np.arange(0,100,1)
y1=np.sin(x)
y2= x**2 +2*x
y3=np.cos(x)
y4= np.tan(x)
y5=np.sin(x) *1.5


x1=plt.subplot(3, 2 ,1)
#plt.legend() function allow you to define label for multiple ploting in a single graph
x1.plot(x,y1,label="today")
x1.plot(x,y3,label="yesterday")
plt.legend(loc='upper left')
plt.title("sales")

x2=plt.subplot(3,2,2)
x2.plot(x,y2)
x2.plot(x,y4)
plt.title("orders")

x3=plt.subplot(3,2,3)
x3.plot(x,y3)
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.title("balance_stock")

x4=plt.subplot(3,2,4)
x4.plot(x, y4, c='k', marker='o', mec='r', mfc='r', ms= 7)
#You can use the loc parameter in title() to position the title.('left', 'right', and 'center')
plt.title("revenue",loc='left')

x5=plt.subplot(3,2,5)
x5.plot(x,y5,'o-r')
plt.title("purchases",loc='right')

#You can add a title to the entire figure with the suptitle() function
plt.suptitle("MY SHOP",color='r')
plt.tight_layout()
plt.show() '''

#8 bar charts
#we gonna make a barchart that shows marks of students in computer languages
index=np.arange(4)
python=(80,60,70,30)
java=(50,80,30,90)
networking=(60,20,50,60)
machine_learning=(55,77,77,66)
people=["aashik","dhina","manic","ganesh"]

plt.subplot(1,2,1)
plt.bar(index,python,width=0.2,label="python")
#we add index by 0.2 because to view results in a ordered way
plt.bar(index+0.2,networking,width=0.2,label="networking")
plt.bar(index+0.4,machine_learning,width=0.2,label="machine learning")
plt.bar(index+0.6,java,width=0.2,label="java")
plt.title('IT skill level')
plt.xlabel("persons")
plt.ylabel("skill level")
plt.legend(loc='upper right')
plt.xticks(index+0.4,people)
#plt.ylim() function will set a limit in chart
plt.ylim(0,120)

plt.subplot(1,2,2)
plt.bar(people,[75,66,26,80])
plt.title('disciplinary record')
plt.suptitle("student record")
plt.show()

#9 pie charts
'''nationalities= ['japanese','korean','indian','french']
students=[36,93,58,71]
#zip function is very usefull so learn it
#zip function first blend student and natio.. and we sorting it infavour of students
#then we again seperating the sorted stu.. and natio.. back now we get the result in asc order
pairs= zip(students,nationalities)
pairs=sorted(list(pairs))
student,national= zip(*pairs)
print(student,national)
#autopct'%.2f%% -- calculates the percentage
#explode=myexplode this will seperte and show the japanese part

myexplode=[0.2,0,0,0]
plt.pie(student,labels= national,autopct='%.2f%%',explode=myexplode,counterclock=False,startangle=90)
plt.title("students nationality")
plt.legend(title='nationalities')
plt.show()
#you can also specify colours you want in the piechart'''

#10 Histograms

'''#A histogram is a graph showing frequency distributions.
#It is a graph showing the number of observations within each given interval
x= np.random.normal(170,10,250)
plt.hist(x,facecolor='r',density=True)
plt.xlabel('heights of students')
plt.ylabel('percentage')
plt.grid()
plt.show()'''

#11 scattter plots

'''x= np.random.randint(100,size=(100))
y= np.random.randint(100,size=(100))
colors=np.random.randint(100,size=(100))
size=5* np.random.randint(100,size=(100))
#c means colors of the dots , alpha denotes the transparency of each dots
#cmap= '---' , there are many colormap available you can specify what you want
plt.scatter(x,y,marker='*',c=colors,cmap='nipy_spectral',alpha= 0.5,s=size)
plt.colorbar()
plt.grid(c='k',lw=1,ls='--')
#t=plt.colormaps()
#print(t)
plt.show()'''

#12 3-D plotting
'''#for 3D plotting you should import this library first mpl_toolkits
ax= plt.axes(projection='3d')
z= np.linspace(0,40,100)
x= np.sin(z)
y= np.cos(z)
ax.plot3D(x,y,z)

plt.show()'''






