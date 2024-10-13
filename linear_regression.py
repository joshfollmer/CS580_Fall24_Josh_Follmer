import pandas as pd
import matplotlib.pyplot as plt

#function to read data values from provided files
def read_data(data_file):
    data = pd.read_csv(data_file)
    return data.iloc[:, 0].values, data.iloc[:, 1].values

#returns the slope and intercept of linear regression line given data
def linear_regression(x_vals, y_vals):
    #find the mean of each axis of data
    x_mean = sum(x_vals) / len(x_vals)
    y_mean = sum(y_vals) / len(y_vals)

    
    covariance_sum = 0
    for i in range(len(x_vals)):
        covariance_sum += (x_vals[i] - x_mean) * (y_vals[i] - y_mean)
    covariance = covariance_sum / len(x_vals)

    variance_x_sum = 0
    for x in x_vals:
        variance_x_sum += (x - x_mean) ** 2
    variance_x = variance_x_sum / len(x_vals)

    beta_1 = covariance / variance_x
    beta_0 = y_mean - beta_1 * x_mean

    return beta_0, beta_1



#plots the data and the regression line
def plot_regression(x_vals, y_vals, slope, intercept):
    line_y_vals = [intercept + slope * x for x in x_vals]

    plt.scatter(x_vals, y_vals, color='blue', label='Data Points')  #plots the data points
    plt.plot(x_vals, line_y_vals, color='red', label=f'Regression Line: y = {intercept:.2f} + {slope:.2f}x')  #plots the regression line

   
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Linear Regression')
    plt.legend()

    
    plt.show()


#you may need to add the complete file path to this variable
file_path = 'linear_regression_data.csv'

x_vals, y_vals = read_data(file_path)
intercept, slope = linear_regression(x_vals, y_vals)
plot_regression(x_vals, y_vals, slope, intercept)

