# NYCDSA - Web Scraping Project

This readme file is an explainer on the components of my Python webscraping project for the NYC Data Science Academy.

## Github Repo Location

https://github.com/jwattier/nycdsa_web_scrape_project 

## Project Goal

My web-scraping project centered on pulling salary information for NFL players. The goal of this indever was to discern if there was any association between how team’s spent their money and higher win totals.

## Project File Structure

1. Scrapy Spider
2. Data Processing
3. Data Analysis
4. Powerpoint

### I. Scrapy Spider

The components of the project related the collection of nfl salary contract information from the website spotrac.com is located in the _sprtContracts/sprtContracts_ folder.

The result of the spiders scraped contract information is reflected in the _nfl_team_contracts.csv_ file. 

### II. Data Processing

The data processing steps focused primarily on i) combing individual monetary categories (e.g., base salary, workout bonuses) into one overall amount by player, ii) aggregating player salary amounts at the team level and, lastly 3) bucketizing a team's roster into five categories.

The five categories were "dead_cap," which represents players that have been cut from a team but still occupy a portion of the team's salary allotment; "injured," which represents players that do not count to the 53-player roster limit but do count towards an nfl team's salary cap; "offense," representing players that are designated under offensive positions (e.g., QB for quarterback, WR for wide receiver); "defense" for players listed under defensive positions (e.g., LB for linebacker); and "specialty" for active roster players with positions that do not fall into offensive or defensive categories (e.g., K for Kicker).

These files are located in the parent _SprtContracts_ parent folder. The data process is performed in the .ipynb files _1_data_preprocess.ipynb_ and _2_nfl_pre_process_fnl.ipynb_.

The csv file _2_nfl_contracts_preprocess.csv_ is the output from the first .ipynb file (and used as the starting point for the second ipynb file). The csv file _3_post_data_clean.csv_ is the output of the second ipynb file and the input for the _3_analyze_visualize.ipynb_ file.

### III. Data Analysis

Data analysis and some visualizations based off of the output of the data processing steps are reflected in the third ipynb file. 

A basic mulitiple linear regression analysis is performed utilizing the standard ordinary least squares method.

### IV. Powerpoint

The powerpoint presentation associated with this process - along with the associated images and plots utilized in this slide deck are reflected in the _presentation_ folder.