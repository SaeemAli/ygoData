import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def levelsPieChart(): # Pie chart of monster levels
    labels = '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'
    sizes = []
    for i in range (1, 13):
        sizes.append(df['level'].value_counts()[i])

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, radius=3600)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def monsterRaceBarChart(): # Bar chart of monster types
    x = np.array(df[df.level>0].race.unique())
    y = []
    for i in x:
        y.append(df['race'].value_counts()[i])

    plt.bar(x,y)
    plt.xticks(rotation=90, ha='right')
    plt.show()

def AttributePieChart(): # Pie chart of monster levels
    labels = ['light', 'dark', 'fire', 'earth', 'water', 'wind']
    colors = ['#Ebee14', '#42085e', '#Dc3407', '#5e4108', '#107ac3', '#0db324']
    sizes = []
    for i in labels:
        sizes.append(df['attribute'].value_counts()[i])

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, radius=3600, colors=colors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def levelsLineGragh(): # Line graph of average attack and defense for each level
    levels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    averageAtk = []
    averageDef = []
    for i in range(1,13):
        averageAtk.append(df['atk'][df['level'] == i].mean())
        averageDef.append(df['def'][df['level'] == i].mean())
    
    plt.plot(levels, averageAtk, label = "Attack")
    plt.plot(levels, averageDef, label = "Defense")
    plt.legend()
    plt.show()

def spellPieChart(): # Pie chart of spell types
    labels = df['race'][df['attribute'] == 'spell'].unique()
    sizes = []
    for i in labels:
        sizes.append(df['race'].value_counts()[i])
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, radius=3600)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def trapPieChart(): # Pie chart of trap types
    labels = df['race'][df['attribute'] == 'trap'].unique()
    sizes = []
    for i in labels:
        sizes.append(df['race'].value_counts()[i])

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, radius=3600)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def monsterTypePieChart(): # Pie chart of monster card types
    labels = ['Normal', 'Effect', 'Fusion', 'Synchro', 'XYZ', 'Ritual', 'Link']
    colors = ['#Ff9e0e', '#Ad6a07', '#9b0cbf', '#Bef5f4', '#0c0e25', '#3668aa', '#014298']
    sizes = []
    for i in labels:
        sizes.append(df['type'][df['type'].str.contains(i)].size)
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, radius=3600, colors=colors)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

def archetypeData(): # Displays the number of cards per archetype
    x = df['archetype'][df['archetype'] != "None"].unique()
    y = []
    for i in x:
        y.append(df['archetype'].value_counts()[i])

    d = {'Archtype': x, 'Cards':y}
    archtypeDF = pd.DataFrame(data = d)
    print(archtypeDF)
    
    return

df = pd.read_csv('cleanData.csv')
# levelsPieChart()
# monsterRaceBarChart()
# AttributePieChart()
# levelsLineGragh()
# spellPieChart()
# trapPieChart()
# monsterTypePieChart()
#archetypeData()