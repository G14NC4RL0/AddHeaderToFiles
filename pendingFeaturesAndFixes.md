# List of pending/future changes (The TODO list):

1. Create a configuration file for the script to store all that will be configurable
2. To make the header filename configurable
3. To make the `setHeader` function able to make any number of substitutions
4. To make comparison string in the `headerExists` function configurable
5. To reformat `getFileBrand` and `getFileEnvironment` functions into one generic function that could retrieve useful information from thew file's name
6. To make the initial directory path configurable
7. To allow more than one file type to be considered in the search
8. To rename all variables for more generic (but still meaninful) names. E.g. words like "brand" and "env" should not be present
9. To remove/rethink the file filtration condition present in the main function (i.e. `if cur_brand == "":`)
