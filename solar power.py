import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

inverter = pd.read_csv(r'C:/Namit/360DigiTMG Projects/Project 2- Optimization in Solar Power Generation/Dataset/inverter_numeric.csv')
weather  = pd.read_csv(r'C:/Namit/360DigiTMG Projects/Project 2- Optimization in Solar Power Generation/Dataset/WMS Report.csv')
inverter.info()
print(inverter.columns)
inverter.columns = inverter.columns.str.strip() 

weather.info()
print(weather.columns)
weather.columns = weather.columns.str.strip()         #GII column had trailing spaces

#INVERTER & WEATHER Dataset Business Moments
#First Business Moments

mean1 = inverter['Unit 1_INV1'].mean()
mean2 = inverter['Unit 1_INV2'].mean()
mean3 = inverter['Unit 2_INV1'].mean()
mean4 = inverter['Unit 2_INV2'].mean()
mean5 = weather['GII'].mean()
mean6 = weather['MODULE TEMP.1'].mean()
mean7 = weather['RAIN'].mean()
mean8 = weather['AMBIENT TEMPRETURE'].mean()

median1 = inverter['Unit 1_INV1'].median()
median2 = inverter['Unit 1_INV2'].median()
median3 = inverter['Unit 2_INV1'].median()
median4 = inverter['Unit 2_INV2'].median()
median5 = weather['GII'].median()
median6 = weather['MODULE TEMP.1'].median()
median7 = weather['RAIN'].median()
median8 = weather['AMBIENT TEMPRETURE'].median()

mode1 = inverter['Unit 1_INV1'].mode()
mode2 = inverter['Unit 1_INV2'].mode()
mode3 = inverter['Unit 2_INV1'].mode()
mode4 = inverter['Unit 2_INV2'].mode()
mode5 = weather['GII'].mode()
mode6 = weather['MODULE TEMP.1'].mode()
mode7 = weather['RAIN'].mode()
mode8 = weather['AMBIENT TEMPRETURE'].mode()


#Second Business Moments
range1 = max(inverter['Unit 1_INV1'] - min(inverter['Unit 1_INV1']))
range2 = max(inverter['Unit 1_INV2'] - min(inverter['Unit 1_INV2']))
range3 = max(inverter['Unit 2_INV1'] - min(inverter['Unit 2_INV1']))
range4 = max(inverter['Unit 2_INV2'] - min(inverter['Unit 2_INV2']))
range5 = max(weather['GII'] - min(weather['GII']))
range6 = max(weather['MODULE TEMP.1'] - min(weather['MODULE TEMP.1']))
range7 = max(weather['RAIN'] - min(weather['RAIN']))
range8 = max(weather['AMBIENT TEMPRETURE'] - min(weather['AMBIENT TEMPRETURE']))

var1 = inverter['Unit 1_INV1'].var()
var2 = inverter['Unit 1_INV2'].var()
var3 = inverter['Unit 2_INV1'].var()
var4 = inverter['Unit 2_INV2'].var()
var5 = weather['GII'].var()
var6 = weather['MODULE TEMP.1'].var()
var7 = weather['RAIN'].var()
var8 = weather['AMBIENT TEMPRETURE'].var()

sd1 = inverter['Unit 1_INV1'].std()
sd2 = inverter['Unit 1_INV2'].std()
sd3 = inverter['Unit 2_INV1'].std()
sd4 = inverter['Unit 2_INV2'].std()
sd5 = weather['GII'].std()
sd6 = weather['MODULE TEMP.1'].std()
sd7 = weather['RAIN'].std()
sd8 = weather['AMBIENT TEMPRETURE'].std()


#Third Business Moment
skew1 = inverter['Unit 1_INV1'].skew()
skew2 = inverter['Unit 1_INV2'].skew()
skew3 = inverter['Unit 2_INV1'].skew()
skew4 = inverter['Unit 2_INV2'].skew()
skew5 = weather['GII'].skew()
skew6 = weather['MODULE TEMP.1'].skew()
skew7 = weather['RAIN'].skew()
skew8 = weather['AMBIENT TEMPRETURE'].skew()



#Fourth Business Moment
kurt1 = inverter['Unit 1_INV1'].kurt()
kurt2 = inverter['Unit 1_INV2'].kurt()
kurt3 = inverter['Unit 2_INV1'].kurt()
kurt4 = inverter['Unit 2_INV2'].kurt()
kurt5 = weather['GII'].kurt()
kurt6 = weather['MODULE TEMP.1'].kurt()
kurt7 = weather['RAIN'].kurt()
kurt8 = weather['AMBIENT TEMPRETURE'].kurt()


#Graphical Representation of INVERTER dataset
#Univariate plots---------Histogram
plt.figure(figsize = (8,6))
sns.histplot(inverter['Unit 1_INV1'], bins= 40, kde= 'True', color= 'green')
plt.xlabel('Unit 1_INV1')
plt.ylabel('Frequency')
plt.title('Histogram Inverter plot 1')
plt.show()

plt.figure(figsize = (8,6))
sns.histplot(inverter['Unit 1_INV2'], bins= 40, kde= 'True', color= 'green')
plt.xlabel('Unit 1_INV2')
plt.ylabel('Frequency')
plt.title('Histogram Inverter plot 2')
plt.show()

plt.figure(figsize = (8,6))
sns.histplot(inverter['Unit 2_INV1'], bins= 40, kde= 'True', color= 'green')
plt.xlabel('Unit 2_INV1')
plt.ylabel('Frequency')
plt.title('Histogram Inverter plot 3')
plt.show()

plt.figure(figsize = (8,6))
sns.histplot(inverter['Unit 2_INV2'], bins= 40, kde= 'True', color= 'green')
plt.xlabel('Unit 2_INV2')
plt.ylabel('Frequency')
plt.title('Histogram Inverter plot 4')
plt.show()


#Box Plot
sns.boxplot(x= inverter['Unit 1_INV1'], color= 'salmon')
plt.title('BoxPlot Inverter 1')
plt.xlabel('Unit 1_INV1')
plt.show()

sns.boxplot(x= inverter['Unit 1_INV2'], color= 'salmon')
plt.title('BoxPlot Inverter 2')
plt.xlabel('Unit 1_INV2')
plt.show()

sns.boxplot(x= inverter['Unit 2_INV1'], color= 'salmon')
plt.title('BoxPlot Inverter 3')
plt.xlabel('Unit 2_INV1')
plt.show()

sns.boxplot(x= inverter['Unit 2_INV2'], color= 'salmon')
plt.title('BoxPlot Inverter 4')
plt.xlabel('Unit 2_INV2')
plt.show()


#KDE Plot
sns.kdeplot(inverter['Unit 1_INV1'], fill=True, color='purple')
plt.title('KDE Inverter plot 1')
plt.xlabel('Unit 1_INV1')
plt.show()

sns.kdeplot(inverter['Unit 1_INV2'], fill=True, color='purple')
plt.title('KDE Inverter plot 2')
plt.xlabel('Unit 1_INV2')
plt.show()

sns.kdeplot(inverter['Unit 2_INV1'], fill=True, color='purple')
plt.title('KDE Inverter plot 3')
plt.xlabel('Unit 2_INV1')
plt.show()

sns.kdeplot(inverter['Unit 2_INV2'], fill=True, color='purple')
plt.title('KDE Inverter plot 4')
plt.xlabel('Unit 2_INV2')
plt.show()


#Violin Plot
sns.violinplot(x=inverter['Unit 1_INV1'], color='red')
plt.title('Violin Plot Inverter 1')
plt.xlabel('Unit 1_INV1')
plt.show()

sns.violinplot(x=inverter['Unit 1_INV1'], color='red')
plt.title('Violin Plot Inverter 2')
plt.xlabel('Unit 1_INV2')
plt.show()

sns.violinplot(x=inverter['Unit 2_INV1'], color='red')
plt.title('Violin Plot Inverter 3')
plt.xlabel('Unit 2_INV1')
plt.show()

sns.violinplot(x=inverter['Unit 2_INV2'], color='red')
plt.title('Violin Plot Inverter 4')
plt.xlabel('Unit 2_INV2')
plt.show()


#Bivariate Plot
#Scatter Plot for Unit 1_INV1 vs Unit 1_INV2, Unit 2_INV1, Unit 2_INV2
sns.scatterplot(data= inverter, x='Unit 1_INV1', y='Unit 1_INV2', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for Unit 1_INV1 vs Unit 1_INV2')
plt.xlabel('Unit 1_INV1')
plt.ylabel('Unit 1_INV2')
plt.show()

sns.scatterplot(data=inverter, x='Unit 1_INV1', y='Unit 2_INV1', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for Unit 1_INV1 vs Unit 2_INV1')
plt.xlabel('Unit 1_INV1')
plt.ylabel('Unit 2_INV1')
plt.show()

sns.scatterplot(data=inverter, x='Unit 1_INV1', y='Unit 2_INV2', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for Unit 1_INV1 vs Unit 2_INV2')
plt.xlabel('Unit 1_INV1')
plt.ylabel('Unit 2_INV2')
plt.show()


#Scatter Plot for Unit 1_INV2 vs Unit 1_INV1, Unit 2_INV1, Unit 2_INV2
sns.scatterplot(data= inverter, x='Unit 1_INV2', y='Unit 1_INV1', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for Unit 1_INV2 vs Unit 1_INV1')
plt.xlabel('Unit 1_INV2')
plt.ylabel('Unit 1_INV1')
plt.show()

sns.scatterplot(data= inverter, x='Unit 1_INV2', y='Unit 2_INV1', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for Unit 1_INV2 vs Unit 2_INV1')
plt.xlabel('Unit 1_INV2')
plt.ylabel('Unit 2_INV1')
plt.show()

sns.scatterplot(data= inverter, x='Unit 1_INV2', y='Unit 2_INV2', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for Unit 1_INV2 vs Unit 2_INV2')
plt.xlabel('Unit 1_INV2')
plt.ylabel('Unit 2_INV2')
plt.show()


#Scatter Plot for Unit 2_INV1 vs Unit 1_INV1, Unit 1_INV2, Unit 2_INV2
sns.scatterplot(data= inverter, x='Unit 2_INV1', y='Unit 1_INV1', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for Unit 2_INV1 vs Unit 1_INV1')
plt.xlabel('Unit 2_INV1')
plt.ylabel('Unit 1_INV1')
plt.show()

sns.scatterplot(data= inverter, x='Unit 2_INV1', y='Unit 1_INV2', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for Unit 2_INV1 vs Unit 1_INV2')
plt.xlabel('Unit 2_INV1')
plt.ylabel('Unit 1_INV2')
plt.show()

sns.scatterplot(data= inverter, x='Unit 2_INV1', y='Unit 2_INV2', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for Unit 2_INV1 vs Unit 2_INV2')
plt.xlabel('Unit 2_INV1')
plt.ylabel('Unit 2_INV2')
plt.show()


#Scatter Plot for Unit 2_INV2 vs Unit 1_INV1, Unit 1_INV2, Unit 2_INV1
sns.scatterplot(data= inverter, x='Unit 2_INV2', y='Unit 1_INV1', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for Unit 2_INV2 vs Unit 1_INV1')
plt.xlabel('Unit 2_INV2')
plt.ylabel('Unit 1_INV1')
plt.show()

sns.scatterplot(data= inverter, x='Unit 2_INV2', y='Unit 1_INV2', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for Unit 2_INV2 vs Unit 1_INV2')
plt.xlabel('Unit 2_INV2')
plt.ylabel('Unit 1_INV2')
plt.show()

sns.scatterplot(data= inverter, x='Unit 2_INV2', y='Unit 2_INV1', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for Unit 2_INV2 vs Unit 2_INV1')
plt.xlabel('Unit 2_INV2')
plt.ylabel('Unit 2_INV1')
plt.show()


#Graphical Representation of WEATHER dataset
#Univariate plots---------Histogram
plt.figure(figsize = (8,6))
sns.histplot(weather['GII'], bins= 40, kde= 'True', color= 'green')
plt.xlabel('GII')
plt.ylabel('Frequency')
plt.title('Histogram Weather plot 1')
plt.show()

plt.figure(figsize = (8,6))
sns.histplot(weather['MODULE TEMP.1'], bins= 40, kde= 'True', color= 'green')
plt.xlabel('MODULE TEMP.1')
plt.ylabel('Frequency')
plt.title('Histogram Weather plot 2')
plt.show()

plt.figure(figsize = (8,6))
sns.histplot(weather['RAIN'], bins= 40, kde= 'True', color= 'green')
plt.xlabel('RAIN')
plt.ylabel('Frequency')
plt.title('Histogram Weather plot 3')
plt.show()

plt.figure(figsize = (8,6))
sns.histplot(weather['AMBIENT TEMPRETURE'], bins= 40, kde= 'True', color= 'green')
plt.xlabel('AMBIENT TEMPRETURE')
plt.ylabel('Frequency')
plt.title('Histogram Weather plot 4')
plt.show()


#Box Plot
sns.boxplot(x= weather['GII'], color= 'salmon')
plt.title('BoxPlot Weather 1')
plt.xlabel('GII')
plt.show()

sns.boxplot(x= weather['MODULE TEMP.1'], color= 'salmon')
plt.title('BoxPlot Weather 2')
plt.xlabel('MODULE TEMP.1')
plt.show()

sns.boxplot(x= weather['RAIN'], color= 'salmon')
plt.title('BoxPlot Weather 3')
plt.xlabel('RAIN')
plt.show()

sns.boxplot(x= weather['AMBIENT TEMPRETURE'], color= 'salmon')
plt.title('BoxPlot Weather 4')
plt.xlabel('AMBIENT TEMPRETURE')
plt.show()


#KDE Plot
sns.kdeplot(weather['GII'], fill=True, color='purple')
plt.title('KDE Weather plot 1')
plt.xlabel('GII')
plt.show()

sns.kdeplot(weather['MODULE TEMP.1'], fill=True, color='purple')
plt.title('KDE Weather plot 2')
plt.xlabel('MODULE TEMP.1')
plt.show()

sns.kdeplot(weather['RAIN'], fill=True, color='purple')
plt.title('KDE Weather plot 3')
plt.xlabel('RAIN')
plt.show()

sns.kdeplot(weather['AMBIENT TEMPRETURE'], fill=True, color='purple')
plt.title('KDE Weather plot 4')
plt.xlabel('AMBIENT TEMPRETURE')
plt.show()


#Bivariate Plot
#Scatter Plot for GII vs MODULE TEMP.1, RAIN, AMBIENT TEMPRETURE
sns.scatterplot(data= weather, x='GII', y='MODULE TEMP.1', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for GII vs MODULE TEMP.1')
plt.xlabel('GII')
plt.ylabel('MODULE TEMP.1')
plt.show()

sns.scatterplot(data= weather, x='GII', y='RAIN', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for GII vs RAIN')
plt.xlabel('GII')
plt.ylabel('RAIN')
plt.show()

sns.scatterplot(data= weather, x='GII', y='AMBIENT TEMPRETURE', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for GII vs AMBIENT TEMPRETURE')
plt.xlabel('GII')
plt.ylabel('AMBIENT TEMPRETURE')
plt.show()


#Scatter Plot for MODULE TEMP.1 vs GII, RAIN, AMBIENT TEMPRETURE
sns.scatterplot(data= weather, x='MODULE TEMP.1', y='GII', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for MODULE TEMP.1 vs GII')
plt.xlabel('MODULE TEMP.1')
plt.ylabel('GII')
plt.show()

sns.scatterplot(data= weather, x='MODULE TEMP.1', y='RAIN', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for MODULE TEMP.1 vs RAIN')
plt.xlabel('MODULE TEMP.1')
plt.ylabel('RAIN')
plt.show()

sns.scatterplot(data= weather, x='MODULE TEMP.1', y='AMBIENT TEMPRETURE', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for MODULE TEMP.1 vs AMBIENT TEMPRETURE')
plt.xlabel('MODULE TEMP.1')
plt.ylabel('AMBIENT TEMPRETURE')
plt.show()


#Scatter Plot for RAIN vs GII, MODULE TEMP.1, AMBIENT TEMPRETURE
sns.scatterplot(data= weather, x='RAIN', y='GII', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for RAIN vs GII')
plt.xlabel('RAIN')
plt.ylabel('GII')
plt.show()

sns.scatterplot(data= weather, x='RAIN', y='MODULE TEMP.1', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for RAIN vs MODULE TEMP.1')
plt.xlabel('RAIN')
plt.ylabel('MODULE TEMP.1')
plt.show()

sns.scatterplot(data= weather, x='RAIN', y='AMBIENT TEMPRETURE', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for RAIN vs AMBIENT TEMPRETURE')
plt.xlabel('RAIN')
plt.ylabel('AMBIENT TEMPRETURE')
plt.show()


#Scatter Plot for AMBIENT TEMPRETURE vs RAIN, GII, MODULE TEMP.1
sns.scatterplot(data= weather, x='AMBIENT TEMPRETURE', y='GII', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for AMBIENT TEMPRETURE vs GII')
plt.xlabel('AMBIENT TEMPRETURE')
plt.ylabel('GII')
plt.show()

sns.scatterplot(data= weather, x='AMBIENT TEMPRETURE', y='MODULE TEMP.1', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for AMBIENT TEMPRETURE vs MODULE TEMP.1')
plt.xlabel('AMBIENT TEMPRETURE')
plt.ylabel('MODULE TEMP.1')
plt.show()

sns.scatterplot(data= weather, x='AMBIENT TEMPRETURE', y='RAIN', color='yellow', s=10, marker='o')
plt.title('Scatter Plot for AMBIENT TEMPRETURE vs RAIN')
plt.xlabel('AMBIENT TEMPRETURE')
plt.ylabel('RAIN')
plt.show()



#INVERTER Dataset................DATA PREPROCESSING.................................
#Typecasting
inverter.dtypes
print(inverter.columns)
inverter['DATE/TIME']= pd.to_datetime(inverter['DATE/TIME'], format= "%d-%m-%Y %H:%M")
inverter[inverter.columns.difference(['DATE/TIME'])] = inverter[inverter.columns.difference(['DATE/TIME'])].astype(float)       #for other columns


#Handling Duplicates
duplicates= inverter[inverter.duplicated()]              #no duplicate records
duplicate_count = duplicates.shape[0]
duplicate_count


#Missing values
inverter.isnull().sum()                            #no missing values
inverter.isna().sum()


#Outlier Analysis
sns.boxplot(x= inverter['Unit 1_INV1'])            #no outliers
plt.title('Boxplot of Unit 1_INV1')
plt.xlabel('Unit 1_INV1')
plt.show()

sns.boxplot(x= inverter['Unit 1_INV2'])            #no outliers
plt.title('Boxplot of Unit 1_INV2')
plt.xlabel('Unit 1_INV2')
plt.show()

sns.boxplot(x= inverter['Unit 2_INV1'])             #no outliers
plt.title('Boxplot of Unit 2_INV1')
plt.xlabel('Unit 2_INV1')
plt.show()

sns.boxplot(x= inverter['Unit 2_INV2'])             #no outliers
plt.title('Boxplot of Unit 2_IVN2')
plt.xlabel('C:/Namit/EDA/Data PreProcessing/InClass_DataPreprocessing_datasets/ethnic diversity.csv')
plt.show()

#Dual confirmation of outliers presence..........no outliers in any column
#IQR method
IQR1= inverter['Unit 1_INV1'].quantile(0.75) - inverter['Unit 1_INV1'].quantile(0.25)
lower_limit1= inverter['Unit 1_INV1'].quantile(0.25)- (IQR1*1.5)
upper_limit1= inverter['Unit 1_INV1'].quantile(0.75)+ (IQR1*1.5)

outliers1= np.where(inverter['Unit 1_INV1'] > upper_limit1, True, np.where(inverter['Unit 1_INV1'] < lower_limit1, True, False))


#Winsorization method
from feature_engine.outliers import Winsorizer
winsor_iqr1= Winsorizer(capping_method='iqr',
                       tail= 'both',
                       fold= 1.5,
                       variables= ['Unit 2_INV1'])

check1= winsor_iqr1.fit_transform(inverter[['Unit 2_INV1']])
sns.boxplot(x= check1['Unit 2_INV1'])


#Discretization using Binarizing method
inverter['Unit 2_INV2_new']= pd.cut(inverter['Unit 2_INV2'],
                                    bins=[
                                          min(inverter['Unit 2_INV2']), 
                                          inverter['Unit 2_INV2'].mean(), 
                                          max(inverter['Unit 2_INV2'])
                                         ], 
                                    include_lowest=True,
                                    labels=["Low",  "High"])     

inverter['Unit 2_INV2_new'].value_counts()     

inverter['Unit 2_INV1_new']= pd.cut(inverter['Unit 2_INV1'],
                                    bins=[
                                          min(inverter['Unit 2_INV1']), 
                                          inverter['Unit 2_INV1'].mean(), 
                                          max(inverter['Unit 2_INV1'])
                                         ], 
                                    include_lowest=True,
                                    labels=["Low",  "High"])     

inverter['Unit 2_INV1_new'].value_counts()     


#Discretization using quantile method
inverter['Unit 1_INV1_multi']= pd.cut(inverter['Unit 1_INV1'],
                                      bins=[
                                             min(inverter['Unit 1_INV1']),
                                                inverter['Unit 1_INV1'].quantile(0.25),
                                                inverter['Unit 1_INV1'].mean(),
                                                inverter['Unit 1_INV1'].quantile(0.75),
                                             max(inverter['Unit 1_INV1'])
                                            ],
                                      include_lowest=True,
                                      labels= ['G1', 'G2', 'G3'],
                                      duplicates= 'drop'
                                      )
inverter['Unit 1_INV1_multi'].value_counts()                                      )

inverter['Unit 1_INV2_multi']= pd.cut(inverter['Unit 1_INV2'],
                                      bins=[
                                             min(inverter['Unit 1_INV2']),
                                                inverter['Unit 1_INV2'].quantile(0.25),
                                                inverter['Unit 1_INV2'].mean(),
                                                inverter['Unit 1_INV2'].quantile(0.75),
                                             max(inverter['Unit 1_INV2'])
                                            ],
                                      include_lowest=True,
                                      labels= ['g1', 'g2', 'g3'],
                                      duplicates= 'drop'
                                      )
inverter['Unit 1_INV2_multi'].value_counts()

#Normal Q-Q plot
import scipy.stats as stats
import pylab

stats.probplot(inverter['Unit 1_INV1'], dist="norm", plot=pylab)    #not distrubuted normally
stats.probplot(inverter['Unit 1_INV2'], dist="norm", plot=pylab)    #not distrubuted normally
stats.probplot(inverter['Unit 2_INV1'], dist="norm", plot=pylab)    #not distrubuted normally
stats.probplot(inverter['Unit 2_INV2'], dist="norm", plot=pylab)    #not distrubuted normally


#Transformation.........Johnson Transformation for all columns
from feature_engine import transformation

tf1 = transformation.YeoJohnsonTransformer(variables= 'Unit 1_INV1')
inv_tf1 = tf1.fit_transform(inverter)
inver1 = stats.probplot(inv_tf1['Unit 1_INV1'], dist=stats.norm, plot=pylab)

tf2 = transformation.YeoJohnsonTransformer(variables= 'Unit 1_INV1')
inv_tf2 = tf2.fit_transform(inverter)
inver2 = stats.probplot(inv_tf2['Unit 1_INV2'], dist=stats.norm, plot=pylab)

tf3 = transformation.YeoJohnsonTransformer(variables= 'Unit 1_INV1')
inv_tf3 = tf3.fit_transform(inverter)
inver3 = stats.probplot(inv_tf3['Unit 2_INV1'], dist=stats.norm, plot=pylab)

tf4 = transformation.YeoJohnsonTransformer(variables= 'Unit 1_INV1')
inv_tf4 = tf4.fit_transform(inverter)
inver4 = stats.probplot(inv_tf4['Unit 2_INV2'], dist=stats.norm, plot=pylab)


#Robust scaling(using)
#Considering the presence of many zero values and the wide range of values (e.g., minimum 0 and maximum ~2800),robust scaling would be highly appropriate. 
#Normalization (Min-Max scaling): If you need all values in a strict range (e.g., 0 to 1), use normalization
#Standardization (Z-score scaling): Given the high variability and outliers (large standard deviation relative to the mean), standardization would work well
from sklearn.preprocessing import RobustScaler
rob1= RobustScaler()

numeric_columns1 = ['Unit 1_INV1', 'Unit 1_INV2', 'Unit 2_INV1', 'Unit 2_INV2']
inverter_scaled = inverter.copy() 

inverter_scaled[numeric_columns1] = rob1.fit_transform(inverter[numeric_columns1])

#Generating descriptive statistics of the dataset after Robust scaling
res_robust = inverter_scaled.describe()



#WEATHER Dataset...........DATA PREPROCESSING...............................................
#Typecasting
weather.dtypes
weather['DATE/TIME']= pd.to_datetime(weather['DATE/TIME'], format= '%d-%m-%Y %H:%M')


#Handling Duplicates
dup= weather[weather.duplicated()]                     #no duplicates
dup_count= dup.shape[0]
dup_count


#Missing Values
weather.isnull().sum()                                 #no missing values
weather.isna().sum()


#Outlier Analysis
sns.boxplot(x=weather['GII'])                          #no outliers
plt.title("Boxplot of GII")
plt.xlabel('GII')
plt.show()

sns.boxplot(x=weather['MODULE TEMP.1'])                #outliers present
plt.title("Boxplot of MODULE TEMP.1")
plt.xlabel('MODULE TEMP.1')
plt.show()


#analysis requires capturing normal variations in rainfall (e.g., from light rain to heavy rain), these values may not be true outliers
sns.boxplot(x=weather['RAIN'])  
plt.title("Boxplot of RAIN")                    
plt.xlabel('RAIN')
plt.show()

sns.boxplot(x=weather['AMBIENT TEMPRETURE'])           #outliers present
plt.title("Boxplot of AMBIENT TEMPRETURE") 
plt.xlabel('AMBIENT TEMPRETURE')
plt.show()

#Outliers Treatment MODULE TEMP.1
IQR2= weather['MODULE TEMP.1'].quantile(0.75) - weather['MODULE TEMP.1'].quantile(0.25)
lower_limit2= weather['MODULE TEMP.1'].quantile(0.25) - (IQR2*1.5)
upper_limit2= weather['MODULE TEMP.1'].quantile(0.75) - (IQR2*1.5)

# Creating a boolean array indicating whether each value in the 'MODULE TEMP.1' column is an outlier
outliers2= np.where(weather['MODULE TEMP.1'] > upper_limit2, True, np.where(weather['MODULE TEMP.1'] < lower_limit2, True, False)) 

# Filtering the DataFrame to include only rows where 'MODULE TEMP.1' column contains outliers
outliers_out = weather.loc[outliers2, ]

# Filtering the DataFrame to exclude rows containing outliers
outliers_trimmed = weather.loc[~(outliers2), ]

weather.shape, outliers_trimmed.shape

sns.boxplot(x=outliers_trimmed['MODULE TEMP.1'])
plt.title('Boxplot of MODULE TEMP.1')
plt.xlabel('MODULE TEMP.1')
plt.show()

#Outlier Treatment AMBIENT TEMPERATURE                           #winsor iqr didnt work because of float data type
from feature_engine.outliers import Winsorizer
winsor2= Winsorizer(capping_method= 'quantiles',
                        tail= 'both',
                        fold= 0.05,
                        variables= ['AMBIENT TEMPRETURE']
                        )

weather['AMBIENT TEMPRETURE'] = winsor2.fit_transform(weather[['AMBIENT TEMPRETURE']])
sns.boxplot(x= weather['AMBIENT TEMPRETURE'])



#Discretization
weather['GII_bin']= pd.cut(weather['GII'],
                       bins= [
                              min(weather['GII']),
                              weather['GII'].mean(),
                              max(weather['GII'])
                             ],
                       include_lowest= True,
                       labels= ['Low', 'High']
                        )
weather['GII_bin'].value_counts()


weather['RAIN_bin']= pd.cut(weather['RAIN'],
                        bins= [
                               min(weather['RAIN']),
                               weather['RAIN'].mean(),
                               max(weather['RAIN'])
                               ],
                        include_lowest= True,
                        labels= ['Low', 'High']
                        )
weather['RAIN_bin'].value_counts()


weather['MODULE TEMP.1_multi']= pd.cut(weather['MODULE TEMP.1'],
                                 bins= [
                                        min(weather['MODULE TEMP.1']),
                                        weather['MODULE TEMP.1'].quantile(0.25),
                                        weather['MODULE TEMP.1'].mean(),
                                        weather['MODULE TEMP.1'].quantile(0.75),
                                        max(weather['MODULE TEMP.1'])
                                       ],
                                 include_lowest= True,
                                 labels= ['L1', 'L2', 'L3', 'L4'],
                                 duplicates= 'drop'
                                 )
weather['MODULE TEMP.1_multi'].value_counts()       
                            

weather['AMBIENT TEMPRETURE_multi']= pd.cut(weather['AMBIENT TEMPRETURE'],
                                 bins= [
                                        min(weather['AMBIENT TEMPRETURE']),
                                        weather['AMBIENT TEMPRETURE'].quantile(0.25),
                                        weather['AMBIENT TEMPRETURE'].mean(),
                                        weather['AMBIENT TEMPRETURE'].quantile(0.75),
                                        max(weather['AMBIENT TEMPRETURE'])
                                       ],
                                 include_lowest= True,
                                 labels= ['L1', 'L2', 'L3', 'L4'],
                                 duplicates= 'drop'
                                 )
weather['AMBIENT TEMPRETURE_multi'].value_counts()                                   


#Normal Q-Q plot
import scipy.stats as stats
import pylab 

stats.probplot(weather['GII'], dist='norm', plot= pylab)                   #not distributed normally
stats.probplot(weather['RAIN'], dist='norm', plot= pylab)                  #not distributed normally
stats.probplot(weather['MODULE TEMP.1'], dist='norm', plot= pylab)         #not distributed normally
stats.probplot(weather['AMBIENT TEMPRETURE'], dist='norm', plot= pylab)    #not distributed normally


#Transformation.........Johnson Transformation for all columns
from feature_engine.transformation import YeoJohnsonTransformer
yjt= YeoJohnsonTransformer()

col1= yjt(variables= 'GII')
tf_jt1 = col1.fit_transform(weather)
w1 = stats.probplot(tf_jt1['GII'], dist=stats.norm, plot=pylab)

col2= yjt(variables= 'RAIN')
tf_jt2 = col2.fit_transform(weather)
w2 = stats.probplot(tf_jt2['RAIN'], dist=stats.norm, plot=pylab)

col3= yjt(variables= 'MODULE TEMP.1')
tf_jt3 = col3.fit_transform(weather)
w3 = stats.probplot(tf_jt3['MODULE TEMP.1'], dist=stats.norm, plot=pylab)

col4= yjt(variables= 'AMBIENT TEMPRETURE')
tf_jt4 = col4.fit_transform(weather)
w4 = stats.probplot(tf_jt4['AMBIENT TEMPRETURE'], dist=stats.norm, plot=pylab)


#Robust Scaling
from sklearn.preprocessing import RobustScaler
rob2= RobustScaler()

numeric_columns2 = ['GII', 'MODULE TEMP.1', 'RAIN', 'AMBIENT TEMPRETURE']
weather_scaled = weather.copy() 

weather_scaled[numeric_columns2] = rob2.fit_transform(weather[numeric_columns2])

#Generating descriptive statistics of the dataset after Robust scaling
res_robust2 = weather_scaled.describe()


#Auto EDA for INVERTER dataset.........................................................
#SWEETVIZ
import sweetviz as sv
report = sv.analyze(inverter)
report.show_html("inverter_data_sweetviz_report.html")


#D-TALE
import dtale
dtale.show(inverter)


#AUTOVIZ
from autoviz.AutoViz_Class import AutoViz_Class
av = AutoViz_Class()
av.AutoViz("C:/Namit/360DigiTMG Projects/Project 2- Optimization in Solar Power Generation/Dataset/inverter_numeric.csv")


#PANDAS PROFILING
pip install joblib==1.1.0 visions==0.7.4
pip install ydata-profiling
from ydata_profiling import ProfileReport
profile = ProfileReport(inverter)
profile.to_widgets() 
profile.to_file("inverter_report.html")


#DATAPREP
pip install -U dataprep
from dataprep.datasets import load_dataset
from dataprep.eda import create_report
dp = load_dataset("C:/Namit/360DigiTMG Projects/Project 2- Optimization in Solar Power Generation/Dataset/inverter_numeric.csv")
create_report(dp).show_browser()


#Auto EDA for WEATHER dataset.........................................................
#SWEETVIZ
import sweetviz as sv
report = sv.analyze(weather)
report.show_html("weather_data_sweetviz_report.html")


#D-TALE
import dtale
dtale.show(weather)


#AUTOVIZ
from autoviz.AutoViz_Class import AutoViz_Class
av = AutoViz_Class()
av.AutoViz("C:/Namit/360DigiTMG Projects/Project 2- Optimization in Solar Power Generation/Dataset/WMS Report.csv")


#PANDAS PROFILING
pip install joblib==1.1.0 visions==0.7.4
pip install ydata-profiling
from ydata_profiling import ProfileReport
profile = ProfileReport(weather)
profile.to_widgets() 
profile.to_file("weather_pandas_report.html")
 

#DATAPREP
pip install -U dataprep
from dataprep.datasets import load_dataset
from dataprep.eda import create_report
dp = load_dataset("C:/Namit/360DigiTMG Projects/Project 2- Optimization in Solar Power Generation/Dataset/WMS Report.csv")
create_report(dp).show_browser()

