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

## Results

Present your key results. For Phase 1, this will be findings from your descriptive analysis.

***
Questions to consider:
* How do you interpret the results?
* How confident are you that your results would generalize beyond the data you have?
***

Here is an example of how to embed images from your sub-folder:

### Visual 1
![graph1](./images/viz1.png)

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

Please review our full analysis in [our Jupyter Notebook](./dsc-phase1-project-template.ipynb) or our [presentation](./DS_Project_Presentation.pdf).

For any additional questions, please contact **name & email, name & email**

## Repository Structure

Describe the structure of your repository and its contents, for example:

```
├── README.md                           <- The top-level README for reviewers of this project
├── dsc-phase1-project-template.ipynb   <- Narrative documentation of analysis in Jupyter notebook
├── DS_Project_Presentation.pdf         <- PDF version of project presentation
├── data                                <- Both sourced externally and generated from code
└── images                              <- Both sourced externally and generated from code
```
