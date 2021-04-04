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

Describe the process for analyzing or modeling the data. For Phase 1, this will be descriptive analysis.

***
Questions to consider:
* How did you prepare, analyze or model the data?
* Why is this approach appropriate given the data and the business problem?
***

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

Provide your conclusions about the work you've done, including any limitations or next steps.

***
Questions to consider:
* What would you recommend the business do as a result of this work?
* What are some reasons why your analysis might not fully solve the business problem?
* What else could you do in the future to improve this project?
***

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
