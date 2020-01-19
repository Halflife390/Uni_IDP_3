"""
IDP 3 Group 9 - Tidal Lagoon Mathematical Model
Module: 3D Model of Lagoon
Gianluca Cantone 2019
"""

#Libraries ====================================================================
import math as m
import matplotlib.pyplot as plt
import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d

#Variables ==================================================================== 

#Main Program =================================================================

'''
Precision to 2 dp
Constant = 0.01590579
Constant for last 3 rows = 0.007458374278
'''

Contour_Map_X = np.array([[322.52,385.39,415.57,591.61,733.07,726.15,707.29,685.29,662.02,629.96,587.21,566.46,552.63],
                          [322.52,331.33,395.45,586.58,699.75,716.72,692.83,678.37,653.85,606.70,575.26,552.00,523.71],
                          [299.26,307.44,356.47,431.92,506.73,572.75,576.52,579.03,581.55,547.60,513.02,500.45,502.96],
                          [267.83,283.54,282.92,355.22,372.19,399.23,408.66,417.46,413.69,395.45,364.02,418.08,468.38],
                          [183.58,194.90,216.27,230.73,244.57,256.51,269.08,277.26,283.54,294.23,346.41,392.31,449.52],
                          [146.49,155.29,217.53,237.02,243.94,254.62,266.57,276.00,284.80,322.52,352.70,396.71,431.92],
                          [098.08,111.91,228.85,233.88,243.31,251.48,262.17,274.74,284.80,299.89,313.09,328.81,406.14],
                          [075.44,086.13,124.48,147.74,174.15,192.38,217.53,231.99,244.57,260.28,300.52,325.04,360.25],
                          [040.87,064.76,099.33,142.09,155.29,174.15,186.72,201.18,215.02,228.85,242.05,255.25,264.68],
                          [066.01,110.02,132.66,137.69,151.52,176.04,196.15,212.50,230.73,246.45,257.14,263.43,267.20],
                          [067.90,091.79,116.31,134.54,148.37,177.92,202.44,216.90,238.28,255.25,298.63,290.46,281.03],
                          [059.98,083.62,101.85,131.40,145.23,178.55,207.47,220.67,242.05,301.15,335.10,350.19,331.33],
                          [-00.63,013.83,062.87,128.88,143.34,179.18,211.87,225.70,249.59,352.07,390.42,401.11,385.39],
                          [-23.26,-01.26,055.95,127.63,142.09,179.81,215.64,228.22,273.49,366.53,438.83,422.49,478.44],
                          [-22.00,-03.77,050.30,125.74,141.46,179.81,221.30,233.88,316.87,400.48,491.64,485.36,519.94],
                          [-11.32,-02.51,089.90,123.85,139.57,181.07,226.33,262.17,360.25,411.17,549.49,528.74,534.40],
                          [54.07,78.59,107.51,120.71,135.17,182.32,229.48,276.63,397.34,510.51,571.49,635.62,638.76],
                          [00.00,011.95,033.95,098.08,115.05,247.71,365.28,470.90,542.57,604.81,670.82,709.18,718.61],
                          [-34.58,-18.86,031.44,128.26,196.78,279.14,369.68,465.24,526.23,608.58,699.75,753.18,759.47],
                          [-46.52,-29.55,-20.12,125.11,201.81,295.49,376.59,463.98,528.74,609.84,740.61,760.73,768.90],
                          [-459.89,-458.89,-457.89,-135.42,-25.47,95.20,207.82,343.24,482.68,604.69,953.97,954.97,955.97],
                          [-459.89,-458.89,-457.89,-135.42,-25.47,95.20,207.82,343.24,482.68,604.69,953.97,954.97,955.97],
                          [-459.89,-458.89,-457.89,-135.42,-25.47,95.20,207.82,343.24,482.68,604.69,953.97,954.97,955.97]])

Contour_Map_Y = np.array([[844.35,864.47,857.55,795.94,741.24,712.95,649.45,601.039,529.37,492.90,474.04,472.78,460.21],
                          [802.22,794.05,835.54,786.51,738.72,710.43,656.99,602.30,541.94,494.79,485.99,478.44,457.69],
                          [787.76,778.33,756.96,753.81,728.04,699.75,672.08,645.05,618.01,593.49,568.35,540.05,458.32],
                          [789.65,768.90,724.89,726.15,711.06,706.03,695.97,682.14,660.77,643.79,633.73,602.30,452.04],
                          [709.80,699.75,681.51,668.94,656.99,648.82,640.02,635.62,631.22,624.30,587.84,576.52,450.15],
                          [653.22,641.28,647.56,630.59,628.07,619.27,612.36,605.45,599.78,572.75,555.14,539.43,440.09],
                          [598.52,594.12,616.76,608.58,597.27,587.21,576.52,562.69,550.74,533.77,517.42,510.51,433.18],
                          [589.09,570.23,570.23,552.00,533.77,519.94,499.82,487.87,479.07,468.38,436.95,420.60,418.72],
                          [501.08,489.13,507.36,474.04,466.50,453.92,445.75,435.69,428.77,417.46,409.28,403.63,399.85],
                          [465.24,422.49,420.60,417.46,411.17,400.48,392.31,387.28,376.59,370.31,364.02,377.85,389.17],
                          [389.17,377.85,368.42,366.53,362.76,358.99,355.85,353.96,350.82,347.67,383.51,391.68,396.71],
                          [332.58,323.15,319.38,321.90,323.78,326.92,330.70,331.95,334.47,342.01,390.42,397.97,407.40],
                          [293.60,277.89,285.43,294.23,295.49,301.78,306.81,308.06,312.46,327.55,363.39,388.54,405.51],
                          [264.68,257.14,263.43,275.37,279.77,284.17,290.46,291.72,300.52,316.24,325.67,358.99,344.53],
                          [189.87,227.59,243.31,252.11,254.62,260.28,264.68,267.20,277.89,290.46,246.45,330.70,338.87],
                          [165.98,183.58,212.50,217.53,220.67,226.96,235.13,240.79,257.14,265.31,193.01,281.66,300.52],
                          [172.89,120.71,189.87,182.95,166.61,201.81,216.90,230.73,240.79,178.55,163.46,104.99,125.74],
                          [00.00,-06.29,-72.30,-08.80,056.58,098.08,089.28,053.44,014.46,042.12,-88.65,-69.79,-60.36],
                          [-84.25,-71.67,-94.31,-76.07,60.-98,-56.58,-50.92,-90.53,-116.31,-118.82,-121.97,-114.42,-88.02],
                          [-114.42,-120.08,-122.60,-122.60,-123.85,-125.74,-127.00,-129.51,-130.14,-132.03,-136.43,-134.54,-133.91],
                          [-1030.40,-1030.40,-1030.40,-1236.88,-1313.30,-1391.06,-1470.17,-1340.12,-1222.13,-1108.16,-795.76,-795.76,-795.76],
                          [-1031.40,-1031.40,-1031.40,-1237.88,-1314.30,-1392.06,-1471.17,-1341.12,-1223.13,-1109.16,-796.76,-796.76,-796.76],
                          [-1032.40,-1032.40,-1032.40,-1238.88,-1315.30,-1393.06,-1472.17,-1342.12,-1224.13,-1110.16,-797.76,-797.76,-797.76]])

Contour_Map_Z = np.array([[13.00,13.00,13.00,13.00,13.00,13.00,13.00,13.00,13.00,13.00,13.00,13.00,13.00],
                          [13.00,12.00,12.00,12.00,12.00,12.00,12.00,12.00,12.00,12.00,12.00,12.00,13.00],
                          [13.00,12.00,10.00,10.00,10.00,10.00,10.00,10.00,10.00,10.00,10.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,05.00,12.00,13.00],
                          [13.00,12.00,02.70,02.70,02.70,02.70,02.70,02.70,02.70,02.70,02.70,12.00,13.00],
                          [13.00,12.00,00.00,00.00,00.00,00.00,00.00,00.00,00.00,00.00,00.00,12.00,13.00],
                          [13.00,12.00,00.00,00.00,00.00,00.00,00.00,00.00,00.00,00.00,00.00,12.00,13.00],
                          [13.00,12.00,00.00,00.00,00.00,00.00,00.00,00.00,00.00,00.00,00.00,12.00,13.00],
                          [13.00,12.00,12.00,12.00,12.00,12.00,12.00,12.00,12.00,12.00,12.00,12.00,13.00],
                          [13.00,13.00,13.00,13.00,13.00,13.00,13.00,13.00,13.00,13.00,13.00,13.00,13.00]])

Ocean_X = np.array([[-600,1000],
                   [-600,1000]])
Ocean_Y = np.array([[1500,1500],
                   [-1500,-1500]])
Ocean_Z = np.array([[4,4],
                   [4,4]])

fig = plt.figure(figsize=plt.figaspect(1)*2)
ax = plt.axes(projection='3d') #proj_type = 'ortho'

plt.title("Barry Harbour Surface Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

ax.set_xlim3d(-1500,1500)
ax.set_ylim3d(-1500,1500)
ax.set_zlim3d(-1500,1500)

#plt.axis('scaled')

#ax.plot_wireframe(Ocean_X, Ocean_Y, Ocean_Z, color='blue', edgecolor="black", alpha=0.5)
ax.plot_surface(Contour_Map_X, Contour_Map_Y, Contour_Map_Z, cmap='Greens', edgecolor="black")


def Integrate_Volume(Height):
    Total = 0
    #loop through coordinate arrays to get 4, pass them to integration function
    for Count_Verticle in range(22):
        for Count_Horizontal in range(12):
            print("Current surface coordinate: (" + str(Count_Verticle) + "," + str(Count_Horizontal))
            Coords_1 = [Contour_Map_X[Count_Verticle][Count_Horizontal], Contour_Map_Y[Count_Verticle][Count_Horizontal], Contour_Map_Z[Count_Verticle][Count_Horizontal]]
            Coords_2 = [Contour_Map_X[Count_Verticle][Count_Horizontal+1], Contour_Map_Y[Count_Verticle][Count_Horizontal+1], Contour_Map_Z[Count_Verticle][Count_Horizontal+1]]
            Coords_3 = [Contour_Map_X[Count_Verticle+1][Count_Horizontal+1], Contour_Map_Y[Count_Verticle+1][Count_Horizontal+1], Contour_Map_Z[Count_Verticle+1][Count_Horizontal]+1]
            Coords_4 = [Contour_Map_X[Count_Verticle+1][Count_Horizontal], Contour_Map_Y[Count_Verticle+1][Count_Horizontal], Contour_Map_Z[Count_Verticle+1][Count_Horizontal]]
            Total += Integrate_Element([Coords_1, Coords_2, Coords_3, Coords_4], Height, "", "")

    print(Total)
    return Total

def Volume_Vs_Height(Step):
    
    Max_Iteration = int(13/Step)+1
    Heights = [0]
    Volumes = [0]
    
    for Iteration in range(Max_Iteration):
        Volumes.append(Integrate_Volume(Heights[Iteration]))
        Heights.append(Heights[Iteration]+Step)

    fig = plt.figure(figsize=plt.figaspect(1)*2)
    ax = plt.axes()
    plt.title("Volume vs Ocean Height of Lagoon")
    ax.set_xlabel("Height (m)")
    ax.set_ylabel("Volume (m^3)")
    ax.plot(Heights, Volumes)
    #ax.plot([0,13], [0, 18465417])
    
    return [Heights, Volumes]


def test():
    
    fig = plt.figure(figsize=plt.figaspect(1)*2)
    ax = plt.axes() #proj_type = 'ortho'
    plt.title("Volume vs Ocean Height of Lagoon")
    ax.set_xlabel("Height (m)")
    ax.set_ylabel(r'Volume ($m^3$)')
    ax.plot(Heights, Volumes)
    plt.minorticks_on()
    ax.grid(which='major', color='black', linestyle='-', linewidth=1)
    ax.grid(which='minor', color='black', linestyle='--', linewidth=0.5)
    #ax.plot([0,13], [0, 18465417])
    
#[Heights, Volumes] = Volume_Vs_Height(0.1)






