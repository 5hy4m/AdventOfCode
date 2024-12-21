@echo off
:: Prompt the user to enter the year folder name
set /p year_folder=Enter the year folder name: 

:: Prompt the user to enter the day folder name
set /p day_folder=Enter the day folder name: 

set folder_path=%year_folder%\%day_folder%
set file1=%folder_path%\part1.py
set file2=%folder_path%\part1_test.py
set file3=%folder_path%\part2.py
set file4=%folder_path%\part2_test.py

:: Create the year and day folders if they don't exist
if not exist %year_folder% (
    mkdir %year_folder%
)

if not exist %folder_path% (
    mkdir %folder_path%
)

:: Create the .py files inside the day folder
echo # This is part1.py > %file1%
echo # This is part1_test.py > %file2%
echo # This is part2.py > %file3%
echo # This is part2_test.py > %file4%

echo Created 4 .py files in the folder "%folder_path%"