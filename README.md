# AddHeaderToConfigFiles.py

This scripts will add the header present in the file `baseHeader.txt` to each config file inside the `src/conf` and `src/conf/env` folders, after replacing the `<TEXT1>` and `<TEXT2>` markers in it for the corresponding brand and environment of each file.
It is possible to edit the header file, although it is not recommended so all config files could have the same header.

## Setup
AddHeaderToConfigFiles.py will require Python v2.7+. If your Python version is lower, please update it.

## Execution
To run the script, exedcute the command:
```
python AddHeaderToConfigFiles.py <ABSOLUTE_PATH_TO_THE_APP_REPO>
```
Replacing `<ABSOLUTE_PATH_TO_THE_APP_SRC_FOLDER>` with the aboslute path to the main folder of the app.

E.g.: python AddHeaderToConfigFiles.py /home/${USER}/repository/your-product
