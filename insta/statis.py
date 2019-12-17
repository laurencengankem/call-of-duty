lol

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
