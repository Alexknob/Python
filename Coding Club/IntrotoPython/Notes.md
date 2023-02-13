
# Intro to Python

### Importing and exploring data with Python, writing good scientific code

* https://ourcodingclub.github.io/tutorials/python-intro/

## Notes

### Tutorial aims

* Understand why Python is so useful for scientific programming
* Installing Python and running a simple Python program
* Reading data from a file
* Get a feel for how Python looks and feels
* Load data from a text file into memory and basic data structures
* Moving beyond the core Python language with modules
* A brief introduction to data analysis with the pandas package
* Plotting data with Matplotlib

### Understand why Python is so useful for scientific programming

* general purpose programming language with no specific application; can be used for multiple purposes
* wide range of functions: data analysis, plots, modelling, website creation...
* used by developers, tech companies, social media apps, financial services companies, scientists

### Installing Python and running a simple Python program

* Python scripts can be written in any plain text editor
* Python scripts can be wtitten in an IDE (integrated Development Environment) like Spyder (similar to RStudio)
    * Spyder Documentation: https://docs.spyder-ide.org/current/index.html
    * Python Documentation: https://docs.python.org/3/library/functions.html#open
   
### Reading Data from a file

* use command ````with open('file name', 'r') as assignednameforfile:````
* this command does not require a closing command to close the file
* ````'r'```` tells Python that we want to read the file
* we could also use ````'w'```` to write the file

### Get a feel for how Python looks and feels (A note on code blocks)

* Python does not require end statements to end a line of commands such as for loops or functions
* Python inferrs the end of a code block from the whitespace (indentation level)
* to end a code block you need to change the indentation level and un-indent the code
* this requires consistency with indentation and tabs!

### Load data from a text file into memory and basic data structures

* when importing csv files Python will read each line as string
* to seperate data by , we can run ````line.split(',')````
* indexing values: Python starts counting from 0
* ````next(variablename)```` allows to skip an item in a list or data file
* ````.append()```` allows to add values to a list

### Moving beyond the core Python language with modules

* modules help to make coding in Python quicker
* Import modules with ````import modulename````
* ````csv```` module: allows to deal with csv files

* Packages vs libraries vs modules

   |Package|Library|Module|
   |-----|------|-----|
   |externally developed piece of Python software that has to be installed seperately|Add-ons that are already bundled in the standard Python isntallation|A Python source file that groups together similar functions, data structures and variables|
   
* Datetime package to deal with time data
   
### A brief introduction to data analysis with the pandas package

* **Pandas**
   * package widely used for data analysis
   * useful to deal with data in table-like form and columns of different data types
   * when to use pandas:
      * table like columnar data
      * interfacing with databases (MySQL)
      * Multiple data types in a single data file
   * when NOT to use pandas
      * for really simple data files 
      * for large gridded datasets with one data type (use numpy)
      * for heavy matrix calculations (use numpy)
   * allows to access data items without indexing it by number but we can do it by column names
   
### Plotting data with Matplotlib

* **Matplotlib**
   * plotting library
   * matplotlib is a big package but we are only importing a submodule of it called pyplot 
   * matplotlib works similar to matlab plotting
   
   * create figures with ````plt.plot(x, y)````
   * save images with ````plt.savefig('name.pngs')````
 



