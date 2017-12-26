
# coding: utf-8

# In[3]:


"""wcount.py: count words from an Internet file.

__author__ = "Lvjiawen"
__pkuid__  = "1600012173"
__email__  = "1600012173@pku.edu.cn"
"""

import sys
import urllib.request
from urllib.request import urlopen




def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    my_socket = urllib.request.urlopen(lines)
    dta = my_socket.read().decode()
    my_socket.close()
    #get the text from url
    
    s=dta.replace(',',' ')
    b=s.replace('.',' ')
    c=b.replace('?',' ')
    d=c.replace('_',' ')
    e=d.replace(']',' ')
    f=e.replace('[',' ')
    g=f.replace('*',' ')
    h=g.replace('%',' ')
    i=h.replace('!',' ')
    j=i.replace('"',' ')
    k=j.replace(':',' ')
    l=k.replace(';',' ')
    m=l.replace('(',' ')
    n=m.replace(')',' ')
    o=n.replace('-',' ')
    p=o.replace('_',' ')
    q=p.replace('/','')
    q=q.lower()
    x=q.split()
    y=set(x)
    #Processed documents are converted into ordered strings
    
    lst={}
    for i in y:
        num=x.count(i)
        lst[i]=num
    
    r=list(lst.values())
    r.sort(reverse=True)
    for i in r[:topn]:
        print(list(lst.keys())[list(lst.values()).index(i)].ljust(15)+"         "+str(i))
    
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)

        

