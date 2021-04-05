# Microsoft_Film_Project

**Authors**: George Ogden, Christopher de la Cruz

## Overview

Our analysis currently reflects what types of films are doing best at the box office in 2021. We take a deep dive into exploring movie profits and popularity and their relationship with other film factors. Our project currently shows that action, adventure, and sci-fi movies are performing best and that the most profitable plots have familiar (and familial) themes and high stakes. This analysis can be used by any film studio currently debating what kinds of movies they should be making

## Business Problem

Microsoft is creating a movie studio and wants the rundown on what types of movies they should be creating. According to a 2016 poll among US adults, the most important factors in determining what to watch were dependant on genre, cast, relatable storylines, and films that were recommended (weight was given first to reccomendations by friends/family and then to other films that were related). We chose to mainly focus on what genres perform best, what synopsises performed best, how budget affects a film's popularity and what time of year of is best for release. The answers to these questions will result in films that are profitable, popular, and relatable. We are ignoring cast for the time being because we believe that that factor is too highly specific to the movie's type and that the answer will change for each genre. ![Influential_Factors](https://user-images.githubusercontent.com/77891283/113523260-b926ba00-9574-11eb-8ff4-5eef97826ad8.png)


## Data

We chose to build our own dataset through IMDb via IMDbPY, a python module which allows you to directly retrieve data from the IMDb website.  Ultimately, our base datasets included 2,475 films from IMDb of the top grossing movies for each year between 2014 and 2019.  This dataset included revenue--domestic and international--and 8 factors that we were interested in analyzing, including:

- Budget<br>
- Rating<br>
- Vote Count<br>
- Genre<br>
- Plot Synopsis<br>
- Year<br>
- Month<br>

## Methods

We mainly stuck to the observations of films in the past 5 years in order to stay relevant to today's trends. We observed mainly how different factors affected a film's profitability and popularity which are the two main driving sources behind any investment. A film's profitability is a large short-term profit but its popularity means more payments for domestic and international licensing fees meaning there is more long term profit to be made.

## Result 1

We have two main key results which are that there is a preferential budget range for movies that are both highly rated and popular

### Visual 1
![budget_sd](https://user-images.githubusercontent.com/77891283/113523642-ef653900-9576-11eb-9cd0-43f22f14e078.png)

## Result 1
Our second main result is that the genres performing best individually and in combination are action, adventure, and sci-fi

### Visual 2
![genre_ind](https://user-images.githubusercontent.com/77891283/113523656-158ad900-9577-11eb-8e14-d7ba4ac637b3.png)

![genre_pairs](https://user-images.githubusercontent.com/77891283/113523659-1d4a7d80-9577-11eb-8fef-89c56c9a2ba6.png)

## Conclusions

These are our business recommendations for a future film:<br>

1. We stick to a budget of 12m - 67.6m. The grand majority of films that are popular and perform well are in this range. Higher budgets are justifiable on a case by case scenario (mainly a film designed to be a blockbuster hit)<br>

2. Action, Adventure and Sci - Fi are all outperforming all the other genres both individually and combined and we highly recommend doing our first film in one or a combination of these genres.<br>

3. We aim for release during what the film industry calls the "slump months" (Jan - Feb & Aug - Sept). These two periods are when quality of movie releases are at their lowest (due to the month before these periods being considered prime time for mega blockbusters). We recommend aiming for a release during one of the slump months as a) we are not equipped to compete with an established blockbuster and 2) there will be less competition, giving our film a higher chance of standing out

4. Keep all story lines high stakes, with strong familial-like relationships and familiar themes

These are the next steps we believe we should take:

1. Franchises are enormously profitable but almost all already owned by other movie studios. We advise doing a deep dive into any existing unowned franchises and potential for creating our own franchise

2. Each genre and genre combination will require its own personal deep dive into further details such as the current hottest actors and directors in each genre, the runtimes that perform best, audience rating that performs best, etc

3. Our research also showed that the profit for online TV streaming and internet content rivals film profits and we advise doing a special deep dive into also creating online streaming television shows and online content
![Revenue_Sources](https://user-images.githubusercontent.com/77891283/113523592-6e0da680-9576-11eb-9ba7-5a2333f18165.png)


## For More Information

Please review our full analysis in our Jupyter Notebook (Microsoft_Film_Industry_Analysis.ipynb located in the code folder) or our [Presentation](https://github.com/cdlc01/Microsoft-Film-Industry-Analysis/files/6255838/Powerpoint_film_analysis.pdf)

For any additional questions, please contact **Christopher de la Cruz at cdelacruz2013@gmail.com, George Ogden at george.p.ogden@gmail.com**

## Repository Structure

```
├── __init__.py                                  <- .py file that signals to python these folders contain packages
├── README.md                                    <- The top-level README for reviewers of this project
├── Powerpoint_film_analysis.pdf                 <- PDF version of project presentation
├── code
│   ├── __init__.py                              <- .py file that signals to python these folders contain packages
│   ├── visualizations.py                        <- .py script to create finalized versions of visuals for project
│   ├── Data_Cleaning.py                         <- .py script used to pre-process and clean data from the IMDbpy module
│   ├── Dataframe_Cleaning.py                    <- .py script used to clean the dataframe directly
│   ├── Data_Collection-DO NOT RUN.py            <- .py script used to gather data using the IMDbpy module. The process takes a full day. We advise not running
│   ├── Analysis.py                              <- .py script for specific genre analysis (courtesy of George)
│   ├── eda_notebook.ipynb                       <- Notebook containing data exploration
|   ├── Microsoft_Film_Industry_Analysis.ipynb   <- Narrative documentation of analysis in Jupyter notebook 
|       ├── data                                 <- Both sourced externally and generated from code
└── images                                       <- Both sourced externally and generated from code
```
