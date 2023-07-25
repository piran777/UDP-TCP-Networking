import matplotlib.pyplot as plt
import csv
#function to determine whether a value is a string or a number
def is_float_try(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
#function to extract window size from a string
def findWin(str):
    newStr = next((s for s in str.split(" ") if "Win=" in s), None)
    if(newStr != None):
        thirdStr = newStr.replace('Win=', '')
    else:
        thirdStr = "xxx" 
    
    if(is_float_try(thirdStr)):
        return int(thirdStr)
    else:
        return False
def plotCSV(files,loss): #plot csv
    z=[]
    n=[]    
    with open(files, 'r') as csvfile: 
        plots = csv.reader(csvfile, delimiter=',')  
        for row in plots:
            if(is_float_try(row[1]) and findWin(row[6])):
                z.append(float(row[1])) 
                n.append(findWin(row[6]))
    plt.plot(z, n)  #plot
    plt.xlabel('time')  
    plt.ylabel('Window Size')
    plt.title('Window Size vs Time of a TCP Connection ('+ str(loss) +'% loss)') 
    plt.show()  
#plot the 2 csvs
plotCSV('h1.csv', 10)   
plotCSV('h3.csv', 1)