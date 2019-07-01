# makeCSV
Script to make a csv file of numbers for use with InDesign. Helps with numbering tickets and what not.

# Usage
Run `makeCSV.py`, include the following arguments (? denotes optional input):  
`<n-up>` = How many times the file is up on the page  
`<needed>` = Number of the tickets or whatever you need  
`<startNum>` = Your starting number  
`<leading zeros>` = How many leading zeros you need  
`<?receipt style>` = Whether you want numbering to be receipt styling, as in 1-4 on the first page, like a receipt booklet

The script will automatically figure out how many rows are needed, rounding up if it's not a whole number.  
There's no real error catching in this thing, at most it'll just complain at you and not create the file though.
