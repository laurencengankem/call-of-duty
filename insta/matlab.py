from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt



def figure(input):
    plt.close('all')
    x = ['Min', 'Avg', 'Max']
    plt.figure(1)
    a = plt.gca()
    y=comp('comments',input)
    f1=plt.bar(x,y)
    autolabel(f1,y,a)
    plt.figure(2)
    b = plt.gca()
    y1=comp('likes',input)
    f2=plt.bar(x,y1)
    autolabel(f2, y1,b)
    plt.figure(3)
    c=plt.gca()
    #c.invert_yaxis()
    y2,y3= hash(input)
    c.set_yticks(y2)
    f3=plt.bar(y3,y2)
    autolabel(f3, y3, c)
    plt.figure(1)
    plt.title('comments')
    a.set_facecolor('#4c4c4c')
    a.figure.set_facecolor('#293149')
    a.set_yticklabels([])
    box1 = BoxLayout()
    box1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    box2 = BoxLayout()
    box3 = BoxLayout()
    plt.figure(2)
    plt.title('likes')
    b.set_yticklabels([])
    b.set_facecolor('#4c4c4c')
    b.figure.set_facecolor('#293149')
    box2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    plt.figure(3)
    plt.title('Hashtags')
    c.set_facecolor('#4c4c4c')
    c.figure.set_facecolor('#293149')
    c.set_xticklabels([])
    box3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    return [box1,box2,box3]

def comp(input1,input2):
    sum=[]
    s=0.0
    if(len(input2)>0):
        for i in range(len(input2)):
            sum.append(input2[i][input1])
            s=s+ input2[i][input1]
        return [min(sum),round(s/max(len(input2),1)),max(sum)]
    else:
        return [0,0,0]
def hash(input):
    s=set()
    for i in range(len(input)):
        for n in range(len(input[i]['hashtags'])):
            input[i]['hashtags'][n]= input[i]['hashtags'][n].split(" ")[0]
            s.add(input[i]['hashtags'][n])
    h=[]
    num=[]
    l=0
    for x in s:
        h.append(x)
        c=0
        for i in range(len(input)):
            for n in range(len(input[i]['hashtags'])):
                if(input[i]['hashtags'][n]==x):
                    c=c+1
        num.append(c)
        #print(str(h[l])+': '+ str(num[l]))
        l=l+1
    return (num,h)

def autolabel(bar_plot,bar_label,ax):
    for idx,rect in enumerate(bar_plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 0.5*height,
                bar_label[idx],
                ha='center', va='bottom', rotation=90)