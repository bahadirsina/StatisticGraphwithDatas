import pandas
import matplotlib.pyplot as plt
import numpy as np
import math

SetofData= pandas.read_csv('number_of_cases_in_the_city.csv')

def MeanDatas(CaseList): # Find mean of column data.
    sumCase = 0
    for x in CaseList:
        sumCase = sumCase + x
    meanCase = sumCase / len(CaseList)
    return meanCase

def MedianDatas(CaseList2): # Find median of column data.
    size = len(CaseList2)
    CaseList2 = sorted(CaseList2)
    if size % 2 == 1:
        return CaseList2[int(size / 2)]
    else:
        num2 = CaseList2[int(size / 2) - 1]
        num = CaseList2[int(size / 2)]
        medianCase = (num + num2) / 2
        return medianCase

def VarianceDatas(CaseList3): # Find the variance.
    mean = MeanDatas(CaseList3)
    size2 = len(CaseList3)
    varianceList = [(x - mean) ** 2 for x in CaseList3]
    varianceCase = sum(varianceList) / (size2 - 1)
    return varianceCase

def StandardDeviationDatas(CaseList4): # Find the standard deviation.
    variance = VarianceDatas(CaseList4)
    standardDeviationCase = math.sqrt(variance)
    return standardDeviationCase

def StandardError(CaseList5): # Find the standard error.
    size3 = len(CaseList5)
    standardDev = StandardDeviationDatas(CaseList5)
    standardError = standardDev / math.sqrt(size3)
    return standardError

def ShapeofDistribution(CaseList6): # Find the shape of distribution.
    Mean = MeanDatas(CaseList6)
    Median = MedianDatas(CaseList6)
    StandartDev = StandardDeviationDatas(CaseList6)
    Skewed = (3*(Mean - Median))/StandartDev
    print("Shape of Distribution: ")
    if Skewed < 0:
        print("Left-Skewed\n")
    elif Skewed > 0:
        print("Right-Skewed\n")
    else:
        print("Symmetric\n")

def Outliers(CaseList7): # Find the outliers.
    size4 = len(CaseList7)
    order = sorted(CaseList7)
    Q1 = order[(round((size4 * 0.25)+ 0.01))-1]
    Q3 = order[(round((size4 * 0.75)+ 0.01))-1]
    IQR= Q3 - Q1
    RangeMin = Q1 - (1.5 * IQR)
    RangeMax = Q3 + (1.5 * IQR)
    print("Outliers:")
    for x in order:
        if not(x > RangeMin and x < RangeMax):
            print(x,end="-")

def ConfidenceInterval(CaseList8):  # Find the %95 confidence interval.
    size5 = len(CaseList8)
    Mean2 = MeanDatas(CaseList8)
    StandartDev2 = StandardDeviationDatas(CaseList8)
    Z = 1.96 #  1 - alfa = %95 -> alfa = %5 = 0.05 -> Z(alfa/2)= Z(0.025) = 1.96 in Table A4
    ConfInterMın = Mean2 - (Z * (StandartDev2 / math.sqrt(size5)))
    ConfInterMax = Mean2 + (Z * (StandartDev2 / math.sqrt(size5)))
    nlist = [round(ConfInterMın,2),round(ConfInterMax,2)]
    return nlist

def marginConfidence(CaseList9):  # Margin at most 0.1 units with confidence 90%.
    margin = 0.1
    Z = 1.645 #  1 - alfa = %90 -> alfa = %10 = 0.1 -> Z(alfa/2) = Z(0.05) = 1.645 in Table A4
    StandartDev3 = StandardDeviationDatas(CaseList9)
    SampleLargeSize = ((Z*StandartDev3)/margin)**2
    print("n >=",round(SampleLargeSize,2))

Case_mean = MeanDatas(SetofData["Number of Case"].to_list())
Case_median = MedianDatas(SetofData["Number of Case"].to_list())
Case_variance = VarianceDatas(SetofData["Number of Case"].to_list())
Case_standardDeviation = StandardDeviationDatas(SetofData["Number of Case"].to_list())
Case_standardError = StandardError(SetofData["Number of Case"].to_list())
Case_ConfidenceInterval = ConfidenceInterval(SetofData["Number of Case"].to_list())

print("Mean: ", round(Case_mean))
print("Median: ", Case_median)
print("Variance: ", round(Case_variance))
print("Standard Deviation: ", round(Case_standardDeviation))
print("Standard Error: ", round(Case_standardError))
print("----------------------------------------------\n")
ShapeofDistribution(SetofData["Number of Case"].to_list())
print("----------------------------------------------\n")
Outliers(SetofData["Number of Case"].to_list())
print("\n")
print("----------------------------------------------\n")
print("%95 Confidence Interval: ",Case_ConfidenceInterval)
print("\n")
print("----------------------------------------------\n")
marginConfidence(SetofData["Number of Case"].to_list())


x = SetofData["Number of Case"].to_list()
plt.style.use("ggplot")
bins = np.arange(0,1300,20)
plt.hist(x,color='green',ec= 'black',bins = bins)
plt.title('Number of cases in cities in Turkey')
plt.xlabel('Number of Case')
plt.ylabel('Number of Cities')
plt.show()

plt.boxplot(x)
plt.title('Number of cases in cities in Turkey')
plt.xlabel('Number of Cities')
plt.ylabel('Number of Case')
plt.show()
