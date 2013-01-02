import Tkinter
from Tkinter import *
master = Tk()
import urllib2
import os
url="http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/juno/SR1/eclipse-java-juno-SR1-win32-x86_64.zip&url=http://eclipse.saplabs.bg//technology/epp/downloads/release/juno/SR1/eclipse-java-juno-SR1-win32-x86_64.zip&mirror_id=501"
url2="http://rs5.rodfile.com:8182/d/3cam6fv776zxn5yb343hhzrbkico4gs2hirwbzwzmt2j223nsxcy36i4/jdk-7u10-windows-x64.exe"
url3="http://download.oracle.com/otn-pub/java/jdk/7u9-b05/jdk-7u9-windows-x64.exe"
url4="http://www.mozilla.org/products/download.html?product=firefox-17.0.1&os=win&lang=en-US"
def var_states():
    print("Eclipse: %d,\: %d, \JDK, \Java, \mozilla" % (var1.get(), var2.get(), var3.get(), var4.get()))
    
 
def downinstall():
    if var1.get()==1:
        file_name = url.split('/')[-1]
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz) #@ReservedAssignment
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status
        f.close()
        
    if var2.get()==1:
        file_name = url2.split('/')[-1]
        u = urllib2.urlopen(url2)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz) #@ReservedAssignment
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status
        f.close()
        
    if var3.get()==1:
        file_name = url3.split('/')[-1]
        u = urllib2.urlopen(url3)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz) #@ReservedAssignment
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status
        f.close()
        
    if var4.get()==1:
        file_name = url4.split('/')[-1]
        u = urllib2.urlopen(url4)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz) #@ReservedAssignment
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status
        f.close()
    

     
Label(master, text="Your programs:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Eclipse for Java", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Java SDK", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Java ", variable=var3).grid(row=3, sticky=W)
var4 = IntVar()
Checkbutton(master, text="Mozzila Firefox", variable=var4).grid(row=4, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=6, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=7, sticky=W, pady=4)
Button(master, text='Download', command=downinstall).grid(row=8, sticky=W, pady=4)
mainloop()
os.startfile("C:\Users\Andrei\workspace\Tehnologytemplate\jdk-7u10-windows-x64.exe")
os.startfile("C:\Users\Andrei\workspace\Tehnologytemplate\jxpiinstall.exe")
os.startfile("C:\Users\Andrei\workspace\Tehnologytemplate\Firefox%20Setup%206.0.exe")
