

def comp(input1,input2):
    sum=[]
    s=0.0
    if(len(input2)>0):
        for i in range(len(input2)):
            sum.append(input2[i][input1])
            s=s+ input2[i][input1]
        if(max(sum)>20):
            return [min(sum),round(s/max(len(input2),1)),max(sum),max(sum)+20]
        else:
            return [min(sum),round(s/max(len(input2),1)),max(sum),max(sum)+3]
    else:
        return [0,0,0,1]

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

        c=0
        for i in range(len(input)):
            for n in range(len(input[i]['hashtags'])):
                if(input[i]['hashtags'][n]==x):
                    c=c+1
        x = "#" + x
        h.append(x)
        num.append(c)
        #print(str(h[l])+': '+ str(num[l]))
        l=l+1
    return (h,num)

