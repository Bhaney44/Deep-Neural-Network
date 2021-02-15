#Copyright Brian Haney 2021
#Imports

xtz_0 = input('Close:')
xtz_1 = float(xtz_0)

bch_0 = input('Close:')
bch_1 = float(xtz_0)

xtz_w = 0.1
bch_w = 0.7

def net():
    global xtz_w
    global bch_w
    
    #Prediction
    xtz_2 = xtz_1 + (xtz_1 * xtz_w)
    bch_2 = bch_1 + (bch_1 * bch_w)
    predict = bch_2 * xtz_2
    print(predict)

    #Threshold
    if predict > 9.0:
        print('up')
        prediction = 1
    else:
        print('down')
        prediction = 0
    #return prediction

    #Compare
    real_value = input('Real Value:')
    real_value_1 = float(real_value)
    accuracy = real_value_1 - prediction
    if accuracy > 0:
        print('correct next set', accuracy)
    else:
        print('wrong update weights', accuracy)
        def update():
            global xtz_w
            global bch_w
            xtz_w += 0.2
            bch_w += 0.1
            print(xtz_w, bch_w)
        update()
            
net()
        

    



