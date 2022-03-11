# ImageToASCII
A CLI image-to-ASCII text generator implemented in Python.

The program requires a single argument from the user: an image file name (with the path to it if the image is not located in the same directory as the program). It will then use the image data to generate an ASCII representation of the image and place it in a text file with the same name as the image file (minus the file extension).

Note: There are two separate files for Windows and Linux. This was done as a quick method of dealing with the different file path formats in either system. I am almost certain that there is an easy way to deal with this issue without requiring two separate files, and I will almost certainly make that change in the future.
