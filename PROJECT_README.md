# Microsoft_Film_Project

**Authors**: George Ogden, Christopher de la Cruz

## Overview

A one-paragraph overview of the project, including the business problem, data, methods, results and recommendations.

## Business Problem

Summary of the business problem you are trying to solve, and the data questions that you plan to answer in order to solve them.

***
Questions to consider:
* What are the business's pain points related to this project?
* How did you pick the data analysis question(s) that you did?
* Why are these questions important from a business perspective?
***

## Data

Building Our Database:

Rather than tying together the datasets provided, we chose to build our own dataset with the IMBDpy package. This package's 'get_movie' method, given the appropriate identification number, provides access to information on a movie's IMDb page.

To find the appropriate ids, we refered to the 't_const' column in 'imbd.title.basics.csv' which contains roughly ~146k entries. These entries then had to be cleaned up, by removing 'tt' at the beginning of each string, in order to use them in the 'get_movie' method.

We next filtered out movies by their release date to removie movies that were A) released in 2020 & 2021YTD (an outlier due to COVID pandemic); B) have not yet been released; or C) released prior to 2017.

During our exploration of the database, we discovered that there were some erroneous entries which had to be accounted. Errors fell into one of two buckets: 1) Erroneous Year Date & 2) Non-existant ids. Example entries from the original dataset:

As a result we chose to collect the data from IMDb while also filtering out ids that were not found in IMDb and movies that were not released after 2009.

With the IMDb information now stored locally, we created a dataframe containing the variables we believed were worth looking at for our analysis:
-Total Revenue & Budget
-Rating & Vote Count
-R/PG13/etc & Languages
-Genre & Plot Outline
-Producers, Writers, Directors & Actors
-Year
-Release Date
-Runtime

***
Questions to consider:
* Where did the data come from, and how do they relate to the data analysis questions?
* What do the data represent? Who is in the sample and what variables are included?
* What is the target variable?
* What are the properties of the variables you intend to use?
***

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
