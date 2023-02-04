 sqscubic
==========
 
 This code reads data from the file `sqscell.out` (generated by mcsqs code) and writes the first 3 cells with the smallest and equal vector lengths to a new file with the same name. The original data is saved in `old-sqscell.out`. The data in `sqscell.out` is in a structured format, with each cell represented by 4 lines: the first line indicates the total number of cells, followed by 3 lines of vector data. The code first reads the original file and saves a copy in `old-sqscell.out`. Then, it calculates the length of each vector and selects the first 3 cells with the smallest and equal vector lengths. Finally, the code writes the selected cells to a new `sqscell.out` file.