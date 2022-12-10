# USER GUIDE
___
## Overview
This is a data wrangling and analysis project of WeRateDogs tweeter archive, using pandas, tweepy and Tweeter's API.
___
## Manual
**Verify Python Version - 3.11**
1. *Required Setup(Command Line)*
   1. `cd <project root>`
   2. `python3.11 -m venv venv`
   3. `./venv/Scripts/activate`
   4. `pip install -r requirements.txt`
   5. `jupyter notebook`
2. *Re - downloading or adding data* 
- Fill your API credentials (*without any spaces*) at the empty auth file at `data/auth_blank.txt`.
- See the docstrings of `gather.py` for info about available functions.
3. *Exploring Within Jupyter Notebook:*
   - open `wrangle_act.ipynb` for step-by-step walkthrough of the entire wrangling and analysis process.
   - open `gather.py` for detailed code and docstring of gathering functions.
4. *More Info:*
     - view `wrangle_report.md` for wrangling report.
     - view `act_report.md` for analysis report.








