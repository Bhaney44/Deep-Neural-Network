import csv
import numpy as np

with open('data.csv', 'r') as data:
    reader = csv.reader(data)
    for row in reader:
        #True Label
        true_label = int(row[0])
        #Input_Variable 1
        var_1_string = (row[1])
        var_1 = float(var_1_string.replace(',',''))
        #Input_Variable 2
        var_2_string = (row[2])
        var_2 = float(var_2_string.replace(',',''))
        #Input_Variable 3
        var_3_string = (row[3])
        var_3 = float(var_3_string.replace(',',''))

        #Input Array
        input_array = (true_label, var_1, var_2, var_3)

        #Input layer with three nodes and a normalization function
        def input_layer():
            x_1 = (input_array[1])/float(100)
            x_2 = (input_array[2])/float(100)
            x_3 = (input_array[2])/float(100)

            #Hidden layer
            def hidden_layer():
                w_0 = 0.1
                w_1 = 0.1
                w_2 = 0.1
                w_3 = 0.1
                x_4 = (x_1 * w_0)+(x_2 * w_1)
                x_5 = (x_2 * w_2)+(x_3 * w_3)

                #Output layer
                def output_layer():
                    w_4 = 0.1
                    w_5 = 0.1
                    x_6 = (x_4 * w_4)+(x_5 * w_5)

                    #Activation function
                    def activation():
                        #True label
                        x_0 = input_array[0]
                        #decision function
                        if x_6 > 0.5:
                            y = 1
                        else:
                            y = -1

                        #activation function
                        if y is x_0:
                            #Here the network predicted right
                            print('correct')
                        else:
                            #Here I want to adjust the weigh parameters
                            #However, I am not sure where to start, ideas include:
                                #calculate loss function
                                #change the way the wights are structured in the program
                                #use matrices instead of linear coefficients
                            print('update weights')
     
                    activation()
                output_layer()
            hidden_layer()
        input_layer()  
