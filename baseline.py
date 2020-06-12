"""
Authored by Nathan Eggers
As part of "Novel Blockchain VANET"
A research paper and student project
involving Edgar Bowlin, David Schmidt,
Timothy Muncy and myself
-------------------------------------
Inspired by zero-knowledge-proofs
This copy will have to be re-written
for use in an application,
so represents an unfinished prototype
-------------------------------------
"""
#TODO
"""
addition of assert method based validation
for unmask.
-------------------------------------------
Even though it's been checked,
changing the operations in relatively minor
ways could unhinge the whole thing.
-------------------------------------------
"""
#TODO
"""
possible use of event or exception code
to trigger the registration of peers outside of the
control of baseline function
-------------------------------------------
"""
#TODO
"""
network functionality,
testing in blockchain,
etc.
--------------------------------------------
"""
import uuid
from uuid import uuid4
import random
from random import randint
def baseline(addressofapplicant):
    """
    if Attempting to connect as new peer then
        Call Baseline(addressofapplicant)
    end if
    procedure BASELINE(addressofapplicant)
    Generate new UUID . via UUID4 or better
    Assign UUID to addressofapplicant
    a, m, d as new Array()
    for i = 0 to 30 do
    a[i] = Random(in range of 1 to 9999)
    m[i] = Mask(a[i])
    end for
    SendMessage(m)
    maskedpeernumber = SendMessage(m) of peer
    Call Derive(number, maskedpeernumber)
    Call Peek(applicant, originalhost)
    end procedure
    """
    peerid = uuid4() 
    newpeer = (peerid, addressofapplicant)
    a = []
    a2 = []
    m = []
    m2 = []
    d = []
    d2 = []
    df = []
    for i in range(0,30):
        a.append(randint(1, 9999))
        a2.append(randint(1, 9999))
        m.append(mask(a[i], i))
        m2.append(mask(a2[i], i))
        d.append(derive(m[i], m2[i], i))
        df.append(falsederive(m[i], m2[i], i))
        #print(f"Index: {i}")
        #print(f"Hidden 1: {a[i]}  Hidden 2: {a2[i]}")
        #print(f"Masked 1: {m[i]}  Masked 2: {m2[i]}")
        #print(f"Derived: {d[i]}")
        #print(f"Unmasked {unmask(m[i], i)}")
    randomindex = generateindexset()
    print(randomindex)
    d2 = d
    p1 = packpeeklist(d, randomindex)
    p2 = packpeeklist(d2, randomindex)
    p3 = packpeeklist(df, randomindex)
    peek(p1, p2, "citizen")
    peek(p1, p3, "hacker")
def mask(number, index):
    mnum = 540
    mn = number << 1
    mn = mn + (mnum - index % 5)
    mn = mn + (index % 3)
    return mn
def unmask(number, index):
    mnum = 540
    um = number - (index % 3)
    um = um - (mnum - index % 5)
    um = um >> 1
    return um
def derive(number1, number2, index):
    um1 = unmask(number1, index)
    um2 = unmask(number2, index)
    if um1 < um2:
        return (um2<<1) - (um1<<1) + 42
    elif um1 > um2:
        return um1 - (um2>>1) + 542
    else:
        return (um1%2) + (index%3) + 542
def falsederive(number1, number2, index):
    um1 = unmask(number1, index)
    um2 = unmask(number2, index)
    if um1 < um2:
        return (um2) - (um1) + 2
    elif um1 > um2:
        return um1 - um2
    else:
        return 542
def generateindexset():
    listr = []
    for i in range(0,5):
        r = randint(1, 15)
        listr.append(15 - r)
    return listr
def packpeeklist(list1, rs):
    return packpeeklist1(list1[rs[0]], list1[rs[1]], list1[rs[2]], list1[rs[3]], list1[rs[4]])
def packpeeklist1(n1, n2, n3, n4, n5):
    """
    Packs and returns 5 item list
    """
    listp = [n1, n2, n3, n4, n5]
    return listp
def comparelistitem(item1, item2):
    """
    Returns result of list comparison
    """
    return item1 == item2
def peek(listp1, listp2, peertoregister):
    bp = []
    rs = generateindexset()
    for k in range(0,5):
        bp.append(comparelistitem(listp1[k], listp2[k]))
    if bp[0] and bp[1] and bp[2] and bp[3] and bp[4]:
        print(f"{peertoregister} is registered")
    else:
        print(f"{peertoregister} has been denied")
if __name__ == "__main__":
    baseline("this is an address")
