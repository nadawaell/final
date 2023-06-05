import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        return pd.read_csv(self.file_path)

    def clean_data(self, data):
        data.dropna(inplace=True)
        data.drop(['Clothing ID'], axis=1, inplace=True)
        return data

class DataAnalyzer:
    def __init__(self):
        pass

    def get_average_of_column(self, data):
        return data.mean()

    def get_distribution_of_column(self, data):
        return data.value_counts()

    def get_median_of_column(self, data):
        return data.median()

    def get_mode_of_column(self, data):
        return data.mode()

class DataVisualizer:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def plot_line_chart(self, data, column_name):
        plt.figure(figsize=(10,5))
        sns.lineplot(data=data[column_name])
        plt.title(column_name)
        plt.xlabel('Index')
        plt.ylabel(column_name)
        plt.savefig(os.path.join(self.output_dir, f'{column_name}_lineplot.png'))
        plt.show()

    def plot_distribution(self, data, column_name):
        plt.figure(figsize=(10,5))
        sns.histplot(data=data, x=column_name, kde=True)
        plt.title(column_name)
        plt.xlabel(column_name)
        plt.ylabel('Count')
        plt.savefig(os.path.join(self.output_dir, f'{column_name}_distribution.png'))
        plt.show()

    def plot_pie(self, data, column_name):
        plt.figure(figsize=(10,5))
        data[column_name].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title(column_name)
        plt.savefig(os.path.join(self.output_dir, f'{column_name}_pieplot.png'))
        plt.show()

    def plot_scatter(self, data, column_name):
        plt.figure(figsize=(10,5))
        sns.scatterplot(x=data.index, y=column_name, data=data)
        plt.title(column_name)
        plt.xlabel('Index')
        plt.ylabel(column_name)
        plt.savefig(os.path.join(self.output_dir, f'{column_name}_scatterplot.png'))
        plt.show()

file_path = 'D:/Downloads2/data/Omar/Womens Clothing E-Commerce Reviews.csv'

# Create an instance of DataProcessor class and use it to load and clean the data
dp = DataProcessor(file_path)
data = dp.load_data()
data = dp.clean_data(data)

# Create an instance of DataAnalyzer class and use it to calculate the average rating for each month and the distribution of ratings, recommendations, and feedback count
da = DataAnalyzer()
average_rating = da.get_average_of_column(data['Rating'])
distribution_of_department_name = da.get_distribution_of_column(data['Department Name'])
median_of_positive_feedback_count = da.get_median_of_column(data['Positive Feedback Count'])
mode_of_division_name = da.get_mode_of_column(data['Division Name'])

# Create an instance of DataVisualizer class and use it to create visualizations of the data
dv = DataVisualizer('D:/Downloads2/data/Omar/output')
dv.plot_line_chart(data, 'Rating')
dv.plot_distribution(data, 'Department Name')
dv.plot_pie(data, 'Positive Feedback Count')
dv.plot_scatter(data, 'Recommended IND')
