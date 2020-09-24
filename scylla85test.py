import timeit
from matplotlib import pyplot as plt
import random
firstrun1 = True
firstrun2 = True
firstrun3 = True
firstrun4 = True
firstrun5 = True
initial_value = 7
runcount = 0
summary = 0
nodesum = 1
nodesum2 = 0
prv = 0
isRSU = False
s85 = 0
s65 = 0
e = 0
sr = random.SystemRandom()
def pagerankv(ro, ri):
    #global nodesum
    #global nodesum2
    global firstrun5
    global prv
    global isRSU #should be based on %secret% which is encrypted on RSU instead of boolean
    
    d1 = .65
    d2 = .85
    d3 = .1
    #nodesum = nodesum + 1
    #nodesum2 = nodesum2 + 1
    if firstrun5:
        prv = .334
        firstrun5 = False
    elif isRSU and not firstrun5:
        prv = (1-d3) + d3 * ((prv*ri)/(ri*ro))
    else:
        #prv = (1-d1) + d1 * (prv*nodesum)/(nodesum2*nodesum)
        prv = (1-d1) + d1 * ((prv*ri)/(ri*ro))
        #where d2 is .85 dampening value and ri is links in and ro is links out
    return prv
def smamean(now):
    global runcount
    global summary
    runcount = runcount + 1
    summary = summary + now
    sm = summary/runcount
    return sm
def scylla65(now):
    global firstrun1
    global s65
    global initial_value
    
    if firstrun1:
        s65 = initial_value
        firstrun1 = False 
    else:
        s65 = (now *.65) + (s65 * .35)
    return s65
def scylla85(now):
    global firstrun2
    global s85
    global initial_value
    
    if firstrun2:
        s85 = initial_value
        firstrun2 = False 
    else:
        s85 = (now *.85) + (s85 * .15)
    return s85
def ema(now):
    global firstrun3
    global runcount
    global e
    global initial_value
    runcount = runcount + 1
    smoothing = 2/runcount
    if firstrun3:
        e = initial_value
        firstrun3 = False
    else:
        e = (now * smoothing) + (e * (1-smoothing))
    return e
def main():
    global isRSU
    sma = []
    sr = random.SystemRandom()
    
    #print(pagerankv(6,32))
    #print(pagerankv(6,32))
    #isRSU = True
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    xx = []
    
    for x in range(0, 10):
        xx.append(x)
        #print(pagerankv(6,32))
        now = sr.randint(2, 14)
        y1.append(now)
        y2.append(scylla85(now))
        y3.append(scylla65(now))
        y4.append(ema(now))
        
        #rvi = sr.randint(3, 32)
        #rvo = sr.randint(3, 32)
        #print("current value:")
        #print(now)
        #print("exponential moving average:")
        #print(ema(now))
        #print("scylla65:")
        #print(scylla65(now))
        #print("scylla85:")
        #print(scylla85(now))
        #print(smamean(now))
        #print(pagerankv(rvo,rvi))
    plt.subplot(2,1,1)
    plt.plot(xx,y1,'--',color='m')
    plt.title('Current Trust')
    #plt.xlabel('transactions')
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10],['','','','','','','','','',''])
    plt.ylabel('trust value')
    plt.yticks([2,4,6,8,10,12,14])
    #85
    plt.subplot(2,1,2)
    plt.plot(xx,y2,'-.',color='c')
    plt.title('Scylla85')
    plt.xlabel('transactions')
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
    plt.ylabel('trust value')
    plt.yticks([2,4,6,8,10,12,14])
    plt.show()
    #65
    plt.subplot(2,1,1)
    plt.plot(xx,y3,'-',color='r')
    plt.title('Scylla65')
    #plt.xlabel('transactions')
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10],['','','','','','','','','',''])
    plt.ylabel('trust value')
    plt.yticks([2,4,6,8,10,12,14])
    #ema
    plt.subplot(2,1,2)
    plt.plot(xx,y4,':',color='g')
    plt.title('EMA')
    plt.xlabel('transactions')
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
    plt.ylabel('trust value')
    plt.yticks([2,4,6,8,10,12,14])
    plt.show()
if __name__ == "__main__":
    main()
