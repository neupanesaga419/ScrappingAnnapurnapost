# Scrapping Annapurna Post

### This script present in app.py helps to scrap the searched data from annapurna post
### and helps to store scrapped data into json file with search name

## File Description

     app.py is Script file containing functions for reading {search_data}_error_page.txt
     running requests for fetching data from annapurna post and creating
     {search_data}_{erro_page}.json file.

     {search_data}_error_page.txt is the text file containing the page that have error
     so that next time when we run the same script with same search_data it can ignore that page. This file is updated everytime when we run script 

     {search_data}_{error_page}.json is the file having at least 30 articles if the pages 
     doesnot have any error. If the pages have error then the script stops thats why all 30 articles might not be scrapped.

### Scrapping Process
    First we need to provide search_data then the the script creates name {search_data}_error_page.txt and checks for file existence. If we are providing new search_data
    then the error_page variable is None if it is previous search_data then error_page
    variable will be updated with the data present in {search_data}_error_page.txt

    And the scripts create a file name {search_data)_{error_page}.json for creating unique json file everytime for keeping articles.

    after that scripting starts with the help of function search_data_from_url
    the function returns updated error_page variable which will be written in the {search_data}_error_page.txt and data_to_store which will be written to {search_data)_{error_page}.json 





