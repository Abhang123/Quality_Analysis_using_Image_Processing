import cv2
import numpy as np


def quality_analysis():

    print("\n")
    print("Two items are taken for quality analysis i.e., Tooth brush and Blade")
    print("\n")

    while True:

        n = input("Enter which image's do you want to analyse ('t' -> tooth_brush) OR ('b' -> blade) :  ")
        print("\n")
        

        if n == 't':

            nt = int(input("Enter which tooth brush image do you want to analyse (1) OR (2) :  "))

            if nt == 1:
                
                print("\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\n")
                print("The first crux behind analysing quality of a tooth brush is observing the bristles of the tooth brush.")
                print("\n")
                print("The bristles may be finely distributed (weak edge pixels) or densely distributed (strong edge pixels).")
                print("\n")
                print("For this Canny algorithm is implemented to classify strong, weak and non-edge pixels")
                print("\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                print("\n")
                print("Second crux behind analysing quality of tooth brush is finding the number of contours")
                print("\n")
                print("Contours are the boundaries of the image (in this case boundaries")
                print("     of the each and every bristle of the tooth brush).")
                print("A minimum threshold contour value is decided (here it is decided as 200).")
                print("If a tooth brush has lower number boundaries (contours drawn and by canny algorithm) than the minimum threshold contour value")
                print("     then that tooth brush will be considered as a good quality tooth brush")
                print("otherwise it is a bad quality tooth brush.")
                print("\n")


                image = cv2.imread("Image1.jpeg")
                cv2.imshow("Original Image",image)
                image = cv2.resize(image,(600,600))

                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


                edges = cv2.Canny(gray, 50, 150)


                contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                    
                image1 = image.copy()
                image1 = cv2.resize(image1,(600,600))  
                cv2.drawContours(image1, contours, -1, (0,255,0), 1)


                cv2.imshow("Original Image",image)


                cv2.imshow("Analysed Image",image1)


                minimum_threshold = 200
                print("\n")
                print("Number of perfect bristles -> {}".format(len(contours)))
                print("\n")

                if len(contours) < minimum_threshold:
                    print("Bad quality toothbrush beacuse number of perfect bristles are not greater than minimum threshold value.")
                else:
                    print("Good quality tooth brush")
                print("\n")
                break


            elif nt == 2:

                print("\n")
                print("The first crux behind analysing quality of a tooth brush is observing the bristles of the tooth brush.")
                print("\n")
                print("The bristles may be finely distributed (weak edge pixels) or densely distributed (strong edge pixels).")
                print("\n")
                print("For this Canny algorithm is implemented to classify strong, weak and non-edge pixels")      
                print("\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                print("\n")
                print("Second crux behind analysing quality of tooth brush is finding the number of contours")
                print("\n")
                print("Contours are the boundaries of the image (in this case boundaries")
                print("     of the each and every bristle of the tooth brush).")
                print("A minimum threshold contour value is decided (here it is decided as 200).")
                print("If a tooth brush has lower number boundaries (contours drawn and by canny algorithm) than the minimum threshold contour value")
                print("     then that tooth brush will be considered as a good quality tooth brush")
                print("otherwise it is a bad quality tooth brush.")
                print("\n")

                image = cv2.imread("Image2.png")
                cv2.imshow("Original Image",image)
                image = cv2.resize(image,(500,500))

                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


                edges = cv2.Canny(gray, 50, 100)


                contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                    
                image1 = image.copy()

                image1 = cv2.resize(image1,(500,500))  
                cv2.drawContours(image1, contours, -1, (0, 0, 255), 1)


                cv2.imshow("Original Image",image)


                cv2.imshow("Bri",image1)


                minimum_threshold = 200
                print("\n")
                print("Number of perfect bristles -> {}".format(len(contours)))
                print("\n")

                if len(contours) < minimum_threshold:
                    print("Bad quality toothbrush, beacuse number of perfect bristles are not greater than minimum threshold value.")
                else:
                    print("Good quality tooth brush")
                print("\n")

                break

            else:

                print("Please enter 1 OR 2")
                print("\n")

        elif n == 'b':

            print("\n")
            nb = int(input("Enter which blade image you want to analyse (1) OR (2) :  "))
            print("\n")

            if nb == 1:

                print("\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\n")
                print("The first crux factor behind blade's quality analysis is of implementing 'HSV'")
                print("\n")
                print("H -> Hue (dominant/primary color of the given image)")
                print("\n")
                print("S -> Saturation (purity value of the color)")
                print("\n")
                print("V -> Value (Brightness/intensity of the color)")
                print("\n")
                print("Hue includes range of color pixels. Example - 0 to 255")
                print("\n")
                print("'Saturation' and 'Value' also has the same range as of Hue i.e., 0 to 255")
                print("\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\n")
                print("Second crux behind this is implmentation of mask")
                print("\n")
                print("Mask is the process of creating range of the hsv pixels")
                print("With the help of this we can calucalte the nice area and expired(rusted) area of the blade image.")
                print("\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\n")
                print("In output Image, white colored pixels represent that respective type of analysed image.")
                print("\n")
                print("If the rust_percentage is less than 10%")
                print("     then only it will be considered as an good quality blade")
                print("\n")
                print("In the code, 'expired' stands for presence of rust on the blade")



                print("\n")
                image = cv2.imread("Image3.png")
                cv2.imshow("Original Image",image)

                hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

                nice_lower = np.array([0, 0, 200])
                nice_upper = np.array([180, 30, 255])

                expired_lower = np.array([10, 100, 50])
                expired_upper = np.array([30, 200, 150])

                
                nice_mask = cv2.inRange(hsv,nice_lower,nice_upper)
                expired_mask = cv2.inRange(hsv,expired_lower,expired_upper)

                cv2.imshow("Nice_region",nice_mask)
                cv2.imshow("Expired_region",expired_mask)
                
                nice_area = cv2.countNonZero(nice_mask)
                expired_area = cv2.countNonZero(expired_mask)
                total_area = nice_area + expired_area

                
                nice_percent = (nice_area / total_area) * 100
                expired_percent = (expired_area / total_area) * 100

                print("\n")
                print(f"Good Quality Blade Percentage = {nice_percent:.2f}")
                print("\n")
                print(f"Bad quality Blade Percentage = {expired_percent:.2f}")
                print("\n")  

                if expired_percent < 10:
                    print("The blade is useful.")
                else:
                    print("This blade is ineffective for usage.")
                
                print("\n")            

                break
            
            elif nb == 2:

                print("\n")
                print("The first crux factor behind blade's quality analysis is of implementing 'HSV'")
                print("\n")
                print("H -> Hue (dominant/primary color of the given image)")
                print("\n")
                print("S -> Saturation (purity value of the color)")
                print("\n")
                print("V -> Value (Brightness/intensity of the color)")
                print("\n")
                print("Hue includes range of color pixels. Example - 0 to 255")
                print("\n")
                print("'Saturation' and 'Value' also has the same range as of Hue i.e., 0 to 255")
                print("\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\n")
                print("Second crux behind this is implmentation of mask")
                print("\n")
                print("Mask is the process of creating range of the hsv pixels")
                print("With the help of this we can calucalte the nice area and expired(rusted) area of the blade image.")
                print("\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("\n")
                print("In output Image,  white colored pixels represent that respective type of analysed image.")
                print("\n")
                print("If the rust_percentage is less than to 10%")
                print("     then only it will be considered as a good quality blade")
                print("\n")
                print("In the code, 'expired' stands for presence of rust on the blade")
                print("\n")

                image = cv2.imread("Image4.png")
                cv2.imshow("Original Image", image)

                hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

                nice_lower = np.array([0, 0, 200])
                nice_upper = np.array([180, 30, 255])

                expired_lower = np.array([5, 100, 50])
                expired_upper = np.array([25, 200, 120])

                nice_mask = cv2.inRange(hsv, nice_lower, nice_upper)
                expired_mask = cv2.inRange(hsv, expired_lower, expired_upper)

                cv2.imshow("Nice Region", nice_mask)
                cv2.imshow("Expired Region", expired_mask)

                nice_area = cv2.countNonZero(nice_mask)
                expired_area = cv2.countNonZero(expired_mask)
                total_area = nice_area + expired_area

                if total_area > 0:
                    nice_percent = (nice_area / total_area) * 100
                    expired_percent = (expired_area / total_area) * 100
                else:
                    nice_percent = expired_percent = 0

                # Print the results
                print("\n")
                print(f"Clean Blade Percentage = {nice_percent:.2f}%")
                print("\n")
                print(f"Expired percentage Blade Percentage = {expired_percent:.2f}%")
                print("\n") 

                if expired_percent < 10:
                    print("The blade is useful.")
                else:
                    print("This blade is ineffective for usage because its rust percent is greater than 10% ")
                
                print("\n") 

                break



        else:

            print("Please enter 't' OR 'd', thank you.")


quality_analysis()


cv2.waitKey(0)
cv2.destroyAllWindows()




































































