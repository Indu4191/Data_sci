# Review Problem 7
'''
Write a function to calculate the root mean squared error, often written as RMSE. The RMSE is a popular measure of performance of predictions when you have a set of observed values and a set of predicted values. Your predicted values in this case are your "predictions" of what the true, observed values are.

Your function will:

    Accept two predefined lists as arguments: true_values and predictions.
    Calculate the error between predictions and true_values as variable errors:
        Element by element, calculate the prediction minus the true value.
    Calculate the square of each element in errors and assign this to variable sq_errors.
    Calculate avg_sq_error, the mean of sq_errors.
    Calculate rmse, the square root of avg_sq_error using np.sqrt().
    Print rmse.
    Return rmse.
'''
print("Problem 7")

import numpy

# define a function to calculate the root mean squared error
def root_mean_sq_error(true_values, predictions):
    sq_errors = []
    for tv, pv in zip(true_values, predictions):
        # calculate the prediction minus the true value
        errors = pv - tv
        # calculate the square of errors and append to sq_errors list
        sq_errors.append(errors ** 2)
        
    # calculate the average square error
    avg_sq_error = numpy.mean(sq_errors)

    # calcualte rmse, the square root of avg_sq_error
    rmse = numpy.sqrt(avg_sq_error)
    print("rmse =", rmse)
    return rmse

predictions = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

true_values = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

root_mean_sq_error(true_values, predictions)