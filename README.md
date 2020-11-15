# Investigating Clusters Among US Birth Data
Homework 2 for Data 602, Machine Learning
By <a href="https://github.com/Jcc329">Jessica Conroy Styer</a>

## Table of Contents

<ul>
  <li><a href="https://github.com/Jcc329/Investigating-Clusters-Among-US-Birth-Data/tree/main/Data%20Files">Data Files</a> - The zip files containing the data used in the technical report. The original data file was too large to post but is available upon request</li>
  <li><b>Notebooks</b> - The Jupyter notebooks used to complete this project.</li>
  <ul>
    <li><a href="https://github.com/Jcc329/Investigating-Clusters-Among-US-Birth-Data/blob/main/Notebooks/Data%20Acquisition.ipynb">1. Data Acquisition</a></li> - The notebook showing how the initial data was aqcuired and cleaned to create a csv.
    <li><a href="https://github.com/Jcc329/Investigating-Clusters-Among-US-Birth-Data/blob/main/Notebooks/Data%20Cleaning.ipynb">1. Data Cleaning</a></li> - The notebook showing how the initial data was processed to create the cleaned dataset.
    <li><a href="https://github.com/Jcc329/Select-the-best-Wine-Predicting-wine-quality/blob/main/Jupyter%20Notebooks/Project%201%20Exploratory%20Analysis%20Updated.ipynb">2. Exploratory Analysis</a> - The notebook containing exploratory analyses </li>
    <li><a href="https://github.com/Jcc329/Select-the-best-Wine-Predicting-wine-quality/blob/main/Jupyter%20Notebooks/Project%201%20Technical%20Notebook%20Updated.ipynb">3. Technical Report</a> - The technical notebook containing the report and final models used.</li>
  </ul>
  <li><a href="https://github.com/Jcc329/Investigating-Clusters-Among-US-Birth-Data/blob/main/README.md">README.md</a> - An overview of the project and results</li> 
  <li><a href="https://github.com/Jcc329/Investigating-Clusters-Among-US-Birth-Data/tree/main/Supplemental%20Files">Suplemental files</a> - The .py file containing functions called in the notebooks</li>
</ul>

### Overview

Using a CDC dataset containing 2019 US birth data, this project aimed to determine if there were any hidden clusters in the data, based upon demographics, prenatal characteristics, and post-natal outcomes. The original data file was a text file containing 5gb of data, consisting of 3757582 rows of data and 228 columns. After initial cleaning, the dataset contained 2897669 rows and 87 Columns for a final file size of 561KB

Due to the runtimes involved I chose to use a subset of the data for the majority of data exploration so that the functions would run quickly. I used 1% or abou 29k rows, selected via random sample, for this purpose.

During data exploration, I used a correlation matrix to visualize the relationships between numeric data. In doing so I was able to perform some initial feature selection. I also chose to include only the ordered categorical and numeric data in this analysis in an attempt to limit features and scope of the analysis. Following this visualization I performed basic data preproccessing by encoding and scaling the data. Upon finishing the preprocessing, I fit a KMeans KElboVisualizer as a first step to see if any clusters could be identified. As expected, based on the complexity of the data, no clusters were identified, and I moved on to a DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm. I chose this algorithm due to the complexity and size of nmy data as well as it's ability to handle noise and detect oddly shaped clusters. Ultimately I identified 6 overlapping clusters in the data, but due to the overlap and the data complexity, was not able to extract meaningful insights based on this analysis. 

### Research Questions/ Business Problem:

The research problem posed in this project is based upon infant and maternal outcomes. Hypothetical uses for this analysis would be to target particular populations for additional car in Obstetric care, based upon hidden clusters identified based on outcome metrics and population demographics from CDC natality data. The specific questions to be addressed are:

1. Using U.S,. Natality data, specifically health metrics and pregnancy outcomes, can we identify hidden groups based on demographic characteristics that would benefit from additional care or consideration during the prenatal period?
2. By examining parental demographics and health metrics, are there hiden groups that have better or poorer natality outcomes? Using PCA can we identify the features that most contribute to this variation?

Stakeholders in this endeavor would include the CDC and national health policy makers as well as hospital administrators and potentially even medical practitioners.
The overall business goal of this project would be to reduce incidences of maternal and/or infant morbidity and mortality by identifying upstream population targets for intervention that can improve outcomes. 

The data being used to address this question has high dimensionallity and is very complicated, with multiple categorical and numeric features. This presents a problem that is suited for a Clustering Machine learning algorithm, which can identify patterns in multidimensional space that we would not otherwise be able to access.

### Motivation & Background

The motivation for this project comes from the increasing amount of reasearch showing that US Maternal and infant mortality and morbidity is higher in the US than in other similarly developed countries (Chen, et al., 2016; Singh & Stella, 2019). This trend inspired me to look for data that could be used to investigate how demographic and prenatal characteristics are distributed when examining clusters in pregnancy outcomes. This led me to the Birth Data Files from the CDC.

### Data

The raw data was acquired from the CDC public data files available here: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm

This data is collected from both the mother, the Facility where birth occurred, and certificates of birth (see documentation).

##### Data Dictionary:
The files used for this project included data from 2019 and documentation for the file can be found here: ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/UserGuide2019-508.pdf

##### Data Description:
The original data file was a text file containing 5gb of data, consisting of 3757582 rows of data and 228 columns. After dropping rows with missing data and duplicates, as well as unneeded columns containing duplicate data (such as multiple recodes), data flags, and imputation flags (flags for were data was imputed which is not needed in this analysis) the final dataset contained 2897669 rows and 87 columns for a final file size of 561KB. 

### Conclusion
After dimensionality reduction, there appear to be 6 clusters in the data, however, as the sihouette score (close to 0) and the visualization demonstrate, these clusteres overlap to a high degree. This makes it difficult to draw actionable insights from the data. Additional analysis may be required to tease out the nuances of this data and discover targets for intervension.

Despite not finding clear clusters in the data, I was able to gain experience applying a clustering algorithm as well as working with a larger, more complex dataset than I am used to. I was able to gain a better understanding of PCA and how to apply it practically, as well as what DBSCAN is, when it is best applied, and how to determine the values for each of the parameters. I feel that I have gained a lot through this project in terms of experience and practice. 

### Packages and Software
Software:
Python 3.0
Anaconda 3
Jupyter Notebooks

Packages:
pandas
numpy
sklearn
matplotlib
seaborn
time

### References and Contributions

Chen, A., Oster, E., & Williams, H. (2016). Why is infant mortality higher in the United States than in Europe?. American Economic Journal: Economic Policy, 8(2), 89-124.

Singh, G. K., & Stella, M. Y. (2019). Infant mortality in the United States, 1915-2017: large social inequalities have persisted for over a century. International Journal of Maternal and Child Health and AIDS, 8(1), 19.
