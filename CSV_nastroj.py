import matplotlib.pyplot as plt 
import matplotlib
import numpy as np
from matplotlib.pyplot import axes
import csv
import pandas
from pickle import FALSE

 

try:
    pandas.read_csv("nastroj/text.csv")
    obsah = pandas.read_csv("nastroj/text.csv")
except:
    print("První soubor nebyl nazelezen, objeví se graf z druhého souboru.")
    try:        
        pandas.read_csv("nastroj/text1.csv")
        obsah1 = pandas.read_csv("nastroj/text1.csv")

    

        x = obsah["x"] 
        y = obsah["y"] 
        x1 = obsah1["x"] 
        y1 = obsah1["y"] 
        fig, axes = plt.subplots(2, 1, figsize=(8, 8), dpi=100 )

        bodx = x
        body = y
        bodx1= x1
        body1= y1 



        axes[0].plot(bodx, body, color="red", label="1st")
        axes[0].set_title("První graf")
        axes[0].legend()
        axes[1].plot(bodx1, body1, label="2nd")
        axes[1].set_title("Druhý graf") 
        axes[1].legend()

        axes[0].set(xlim=(None, None),
                ylim=(None, None), )
    
        axes[1].set(xlim=(None , None), 
                ylim=(None, None),)

        plt.show()
    except:
        x1 = obsah1["x"] 
        y1 = obsah1["y"]
        bodx1= x1
        body1= y1
        fig, ax = plt.subplots()

        ax.plot(bodx1, body1, linewidth=2.0)

        ax.set(xlim=(None, None), 
               ylim=(None, None),)

        plt.show()
try:
    pandas.read_csv("nastroj/text1.csv")
    obsah1 = pandas.read_csv("nastroj/text1.csv")
except:
    print("Druhý soubor nebyl nazelezen, objeví se graf z prvního souboru.")
    pandas.read_csv("nastroj/text.csv")
    obsah1 = pandas.read_csv("nastroj/text.csv")
    
    x = obsah["x"] 
    y = obsah["y"]
    bodx= x
    body= y
    fig, ax = plt.subplots()

    ax.plot(bodx, body, linewidth=2.0)

    ax.set(xlim=(None, None), 
            ylim=(None, None),)

    plt.show()
        
try:
    pandas.read_csv("nastroj/text.csv")
    obsah = pandas.read_csv("nastroj/text.csv")
  
    pandas.read_csv("nastroj/text1.csv")
    obsah1 = pandas.read_csv("nastroj/text1.csv")

    

    x = obsah["x"] 
    y = obsah["y"] 
    x1 = obsah1["x"] 
    y1 = obsah1["y"] 
    fig, axes = plt.subplots(2, 1, figsize=(8, 8), dpi=100 )
    
    
    bodx = x
    body = y
    bodx1= x1
    body1= y1 


 
    axes[0].plot(bodx, body, color="red", label="1st")
    axes[0].set_title("První graf")
    axes[0].legend()
    axes[1].plot(bodx1, body1, label="2nd")
    axes[1].set_title("Druhý graf") 
    axes[1].legend()
    
    
    axes[0].set(xlim=(None, None),
                ylim=(None, None), )
    
    axes[1].set(xlim=(None , None), 
                ylim=(None, None),)
    
    print("Graf z obou souborů")
    plt.show()
       
except:
    print("Chyba")