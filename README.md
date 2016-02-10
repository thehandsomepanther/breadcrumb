# breadcrumb
This repo contains tools and scripts to clean and organize the CSV generated by crouton.

## Scripts
```
crumb.py
```
This is a script for cleaning the CSV generated by crouton. "Cleaning" in this case means two things: 1) removing the first three columns of each row (as they're only used to keep track of searches) and 2) deleting duplicate rows. Crumb.py is called with two arguments, as in: `crumb.py dirty.csv clean.csv` where `dirty.csv` is the raw file with CTEC information created by crouton, and `clean.csv` is some other CSV file where the cleaned data will go.
