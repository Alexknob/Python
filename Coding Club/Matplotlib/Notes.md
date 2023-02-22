
# Python Data Analysis with Pandas and Matplotlib

## Create plots and manipulate data with Pandas and Matplotlib

https://ourcodingclub.github.io/tutorials/pandas-python-intro/

Official Pandas website:
https://pandas.pydata.org/

## Tutorial Aims

* Understand what Pandas is
* Ways of running Python and Pandas
* Understanding the basic Pandas data structures
* Learn how to access data from a Pandas DataFrame
* Learn how to filter data in a Pandas DataFrame
* Learn how to read and sort data from a file
* Understand the basics of the Matplotlib plotting package
* Learn how to bring together other packages to enhance your plots
* Learn how to further customise the appearance of Matplotlib plots
* Bonus Matplotlib: plotting data onto maps with Cartopy


### Understand what Pandas is

* package to deal with data analysis
* simplifies loading data from external sources and databases
* allows data analysis and manipulation
* useufull for:
    * labelled data (= tabular data with headings associated with each column of data)
    * ordered and unordered time series data
    * matrix data with row and column labels
    * any form of statistical or obsrvational data sets (data does not have to be labelled to be placed into a pandas structure)
* fast way to deal with data
* in combination with another library called statsmodels


### Ways of running Python and Pandas

* Conventions when using Python
    * import pandas and give it a nick name
    * functions from the pandas package will later be then specified with ````pd.some_function_name()````
    
    
### Understanding the basic Pandas data structures

* Two Core Data Structures:
  * Series
      * one-dimensional array like structure
      * holds a column of data and an associated array of data labels called index
  * DataFrame
      * tabular data similar to a spreadsheet
      * columns storing a single data-type 
      * indexed by row or column names
      * can be created from a dictionary
      * pd.DataFrame()
      * column names are ordered alphabetically by default
  * Dictionaries
      * core data structure containing Key:value pairs
      * can contain multiple items seperated with a ,
      * corresponding values to keys can also be numbers, lists, tuples or other dictionaries
      * indicated with {}
      * look up items in the dictionary with []
      

### Learn how to access data from a Pandas DataFrame

* View first n items of data frame with ````dataframename.head((n))````
* View last n items of data frame with ````dataframename.tail((n))````
* Access column names with ````dataframename['column-name']````
* Cannot access columns by their index number: ````dataframename[indexnumber]```` will not work
* Access row index with ````dataframename.iloc[rowindexnumber]````
* Access one element by row, column index with ````dataframename.iloc[rowindexnumber, columnindexnumber]````
* iloc means integer location


### Learn how to filter data in a Pandas DataFrame


### Learn how to read and sort data from a file

* read in data with ````read_csv()```` function
* sort data with ````dataframename.sort_values(by = ['columnname'], ascending = True)````


### Understand the basics of the Matplotlib plotting package

* Matplotlib is used fro data plotting and visualisation
* Matplotlib gallery: https://matplotlib.org/2.0.2/gallery.html
* Most suitable submodule package: pyplot
* Scatterplot with ````plt.scatter(x, y)````
* Save figure with ````plt.savefig("my_chart_name.png")````


### Learn how to bring together other packages to enhance your plots

* Statistical library in Python: scipy
* Linear regression with ````linregress(x, y)````
      * will return slope, intercept, rvalue, pvalue and stderr
      *  can access each of these values with dot notation


### Learn how to further customise the appearance of Matplotlib plots

* can format fontsize, linewidt, colour... of plots


### Bonus Matplotlib: plotting data onto maps with Cartopy

* extra python package called cartopy
* installation via command ````conda install -c conda-forge cartopy````
