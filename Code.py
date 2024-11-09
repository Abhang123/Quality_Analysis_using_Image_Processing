import numpy as np
import cv2

def quality_analysis():

    print("\n")
    n = input("Enter 'a' for apple analysis or 'b' for banana and 'd' daal analysis : ")
    print("\n")

    if n == "b":

        image = cv2.imread("Banana.png",1)
        image = cv2.resize(image,(400,400))

        cv2.imshow("Original Image",image)

        # HSV Range
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

        ripe_lower = np.array([20,100,100])
        ripe_upper = np.array([30,255,255])

        overripe_lower = np.array([20,30,50])
        overripe_upper = np.array([50,100,80])

        unripe_lower = np.array([40,100,255])
        unripe_upper = np.array([85,80,150])

        # Mask
        ripe_mask = cv2.inRange(hsv,ripe_lower,ripe_upper)
        overripe_mask = cv2.inRange(hsv,overripe_lower,overripe_upper)
        unripe_mask = cv2.inRange(hsv,unripe_lower,unripe_upper)

        # Visualization
        cv2.imshow("Ripe_area",ripe_mask)
        cv2.imshow("Overripe_area",overripe_mask)
        cv2.imshow(u"Unripe_area",unripe_mask)

        # Percentage Calculation
        ripe_area = cv2.countNonZero(ripe_mask)
        overripe_area = cv2.countNonZero(overripe_mask)
        unripe_area = cv2.countNonZero(unripe_mask)
        total_area = ripe_area + overripe_area + unripe_area

        ripe_percent = (ripe_area / total_area) * 100
        overripe_percent = (overripe_area / total_area) * 100
        unripe_percent = (unripe_area / total_area) * 100

        print("\n")
        print("Ripe Percentage = ",ripe_percent)
        print("\n")
        print("Overripe Percentage = ",overripe_percent)
        print("\n")
        print("Unripe Percentage = ",unripe_percent)
        print("\n")

    elif n == "a":

        color = cv2.imread("Apple.png")
        cv2.imshow("Original_Image",color)
        color = cv2.resize(color,(400,400))

        hsv = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV",hsv)

        # Range 
        redripe_lower = np.array([0,100,100])
        redripe_upper = np.array([10,255,255])

        yellowripe_lower = np.array([20,100,100])
        yellowripe_upper = np.array([30,255,255])


        overripe_lower = np.array([5,100,50])
        overripe_upper = np.array([15,255,200])

        unripe_lower = np.array([36,100,100])
        unripe_upper = np.array([85,255,255])


        # Mask Creation
        redripe_mask = cv2.inRange(hsv,redripe_lower,redripe_upper)
        yellowripe_mask = cv2.inRange(hsv,yellowripe_lower,yellowripe_upper)
        overripe_mask = cv2.inRange(hsv,overripe_lower,overripe_upper)
        unripe_mask = cv2.inRange(hsv,unripe_lower,unripe_upper)
        ripe_mask = redripe_mask + yellowripe_mask

        # PErcentage calculationṇ
        ripe_area = cv2.countNonZero(ripe_mask)
        overripe_area = cv2.countNonZero(overripe_mask)
        unripe_area = cv2.countNonZero(unripe_mask)
        total_area = ripe_area + overripe_area + unripe_area

        print('\n')
        print("Ripe Precentage  = ",(ripe_area / total_area) * 100)
        print('\n')
        print("Overripe Percentage - ",(overripe_area / total_area) * 100)
        print('\n')
        print("Unripe Percentage = ",(unripe_area / total_area) * 100)
        print('\n')

        print("Total Ripe Area -> ",ripe_area)
        print("Unripe Area -> ",total_area)
        print('\n')

        # Result Display
        cv2.imshow("RED_RIPE",redripe_mask)
        cv2.imshow("YELLOW_RIPE",yellowripe_mask)
        cv2.imshow("OVERRIPE",overripe_mask)
        cv2.imshow("UNRIPE",unripe_mask)
        cv2.imshow("Ripe_area",ripe_mask)

    elif n == "d":

        image = cv2.imread("Daal.png",1)
        image = cv2.resize(image,(400,400))

        cv2.imshow("Original Image",image)

        # HSV Range
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

        ripe_lower = np.array([25, 80, 80])
        ripe_upper = np.array([35, 255, 255])


        overripe_lower = np.array([20, 70, 70]) 
        overripe_upper = np.array([30, 200, 150])

        unripe_lower = np.array([35, 100, 100])  
        unripe_upper = np.array([50, 255, 255])


        # Mask
        ripe_mask = cv2.inRange(hsv,ripe_lower,ripe_upper)
        overripe_mask = cv2.inRange(hsv,overripe_lower,overripe_upper)
        unripe_mask = cv2.inRange(hsv,unripe_lower,unripe_upper)

        # Visualization
        cv2.imshow("Ripe_area",ripe_mask)
        cv2.imshow("Overripe_area",overripe_mask)
        cv2.imshow("Unripe_area",unripe_mask)

        # Percentage Calculation
        ripe_area = cv2.countNonZero(ripe_mask)
        overripe_area = cv2.countNonZero(overripe_mask)
        unripe_area = cv2.countNonZero(unripe_mask)
        total_area = ripe_area + overripe_area + unripe_area

        if total_area == 0:
            print("No relevant areas detected.")
        else:
            ripe_percent = (ripe_area / total_area) * 100
            overripe_percent = (overripe_area / total_area) * 100
            unripe_percent = (unripe_area / total_area) * 100

        print("\n")
        print("Clean Daal Percentage = ",ripe_percent)
        print("\n")
        print("Average Percentage = ",overripe_percent)
        print("\n")
        print("Bad quality Percentage = ",unripe_percent)
        print("\n")

    else:
        print("Sorry, your input is wrong, please try again.")


quality_analysis()


cv2.waitKey(0)
cv2.destroyAllWindows()






























































