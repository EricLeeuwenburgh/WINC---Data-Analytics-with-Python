<!-- (Non Technical) Report of assignment Module 5 - Shark Attack -->

# Non-technical Report - Shark Attack
This analysis is part of the WINC Academy course: 'Data Analytics with Python - Module 5'.

1. ## **Starting questions**
By doing this analysis we hope to find answers to the following questions:
- Question 1: What are the most dangerous types of sharks to humans?
- Question 2: Are children more likely to be attacked by sharks? 
- Question 3: Are shark attacks where sharks were provoked more or less dangerous?
- Question 4: Are certain activities more likely to result in a shark attack?

With the findings we hopefully get a better feeling for shark behavior, be able to better warn people about certain risks and overal reduce the amount of shark attacks.

2. ## **Used data and modeling approach**
The dataset used comes from _Kaggle_ (https://www.kaggle.com/datasets/felipeesc/shark-attack-dataset).
This dataset contains information about shark attacks globally. 

Due to the given questions (see above), I have filtered the data in a way to keep the focus on 'global' results.

For this analysis I haven't used all the data from the dataset. Data like geographical location, time, date, year, investigator and some unique data like case-numbers haven't been taken into account for this analysis. The data was analysed in way I would describe as: 'As general as possible'.

The data that was used in this analysis consists of:
- _Type_: 
description of the kind of shark attack
- _Activity_: 
during what activity did the shark attack occur 
- _Sex_:
gender of the victim
- _Age_:
how old was the victim when attacked
- _Injury_:
description of the kind of inury 
- _Fatal (Y/N)_:
did the victim decease due the shark attack (Yes or No) 
- _Species_:
description of the type of shark

The total amount of shark attacks (rows of data) used in this analysis = 6302.

**Note**: The original dataset contains a lot of rows with missing data. Rows that are completely empty are discarded from this analysis.


3. ## **Results of the analysis**

##### Question 1: What are the most dangerous types of sharks to humans?
The following data was taken into account for answering this question: _Fatal (Y/N)_ and  _Species_.

![Alt Text](/Exercises/Module7/3_reporting/images/Q1%20-%20Figure_1.png)

**Answer** =    "1: White shark, 2: Tiger shark, 3: Bull shark" (see bar chart)

_Assumptions_:  (Main) In general the "(Great) White shark" is known to be the most deadly shark to humans.
                I have interpreted 'most dangerous' as 'most deadly' == most fatal injuries.
                If the "Injury" column would contain the word "FATAL" I updated the column "Fatal Y/N" to 'True' even if 
                the original value was 'False'. 

_Reasoning_:    I didn't want to create a certain bias by cleaning/transforming the dataset to much. As shown above there are
                a lot of different kind (unique) of values in the "Species" column which are also hard to group. 
                By looking at the top 20 a lot more values containing 'white shark' are found, but often in combination with 
                uncertainty (like: '?'). Because of this uncertainty I didn't do any more transformations on the values.
                Note: almost 50% of all values in the "Species" column are null values. 
                The current outcome is already according my main assumption.


##### Question 2: Are children more likely to be attacked by sharks?
The following data was taken into account for answering this question: _Type_ and  _Age_.

![Alt Text](/Exercises/Module7/3_reporting/images/Q1%20-%20Figure_2.png)

**Answer** =    "No" because 27.3% of all shark attacks affect children.
                "Yes" (see Pie chart), while "Young Adults" are attacked most often, "Children" come second. So children are attacked
                more often than "Middle-age Adults (36-53)", "Older Adults (54-71)" and "Senior Adults (72+)".

_Assumptions_:  I have assumed 'children' to be persons under the age of 18. (like most international institutions do)
                I have assumed 'more likely' as 'more often' since there isn't enough data to check for any child specific 
                relationships. More data would be needed (like: 'weight', 'height').

_Reasoning_:    I have transformed the "Age" column to single numbers. This means rows considering multiple victims are left out.
                Rows from "Age" column that contained null values are excluded from the calculation since we can't categorize them.
                I have interpreted 'attacked' to be all types exluding: "Boat", "Boating" and "Sea Disaster". I did this because
                I wanted the results to be based on an 'initial attack' from shark to human and not any attacks which are caused by
                a sea disaster or boat attack first. 
                I made a Pie chart because I wanted to make a fair age group split. All bins contain 18 years. Comparing age groups
                0-17 and 18-90 didn't seem fair to me since the adult group is much bigger (age count wise).


##### Question 3: Are shark attacks where sharks were provoked more or less dangerous?
The following data was taken into account for answering this question: _Type_ , _Injury_ and  _Fatal (Y/N)_.

![Alt Text](/Exercises/Module7/3_reporting/images/Q1%20-%20Figure_3.png)

**Answer** =    "Less dangerous" because provoked attacks are relatively less fatal.
                "More dangerous" because provoked attacks relatively cause more injuries.

_Assumptions_:  I have assumed 'less dangerous' to be 'less fatal'. 
                If the "Injury" column would contain the word "PROVOKED" I updated the column "Type" to 'Provoked' even if 
                the original value was 'Unprovoked' or something else.
                If the "Injury" column would contain the word "FATAL" I updated the column "Fatal Y/N" to 'True' even if 
                the original value was 'False'.
                I've split the type of injuries ("Injury" column) into three groups. If column(string) would contain any form of 
                "no injury" in it, the type would be: "no injury". If the "Fatal (Y/N)" column is true then the injury type would 
                be "fatal". All the others are simply put into type "injury", so the "injury" type is positively biased.

_Reasoning_:    I've split the "Injury" column in a few types (bins) the get a better feeling for the damage being done.
                The sum of all kind of injuries = 5170. 'No injuries' = 424, 'fatal' = 1202. So 'injuries' should be 3544, instead it
                is 3545, 1 more than expected. I haven't been able to find this bug, but due the minor difference I've neglected it.


##### Question 4: Are certain activities more likely to result in a shark attack?
The following data was taken into account for answering this question: _Activity_.

![Alt Text](/Exercises/Module7/3_reporting/images/Q1%20-%20Figure_4.png)

**Answer** =    "See (horizontal) bar chart". 

_Assumptions_:  (see cleaning data) I have tried to keep the types of activities as 'pure' as possible. Like "Diving", this is a very
                broad term, I have only transformed values to "Diving" where the original value was pointing towards diving 'for a
                certain thing/object'. Types are diving like 'Free diving', 'Scuba diving' are still seperated.

_Reasoning_:    Due the wide variety of activities I've decided to pick the top 60 from .valuecounts() and started looking (manually)
                for different kind of typos and fixing those one by one. Since the bottom valuecounts ends at 3 if feel that I haven't
                neglected to many values. Transforming all unique values would be very time consuming and I don't feel this would 
                change the outcome of the result.
                To not have to many bars on the resulting bar chart (keep it readable) I've only selected the top 30 results. I think
                this gives a good (enough) answer to the question since the top value contains 1000+ attacks while the bottom values are 
                near 10 attacks (= 1%).
                The sum of the top 30 == 80% of all the values.


3. ## **Conclusions and recommendations**
As stated above I think I have found some good answers by analysing this dataset. The results may be used to better warn people and in doing so hopefully prevent / reduce the amount of shark attacks.

See below some conclusions and recommendations per question:

* _Question 1: What are the most dangerous types of sharks to humans?_
    * While the outcome of the analysis was as expected, the used data for _Species_ contained a lot of missing values.
    To further improve the analysis the _Species_ data could be cleaned further or the input to the original dataset could be altered to perhaps a list of predetermined species instead of a free text input.

* _Question 2: Are children more likely to be attacked by sharks?_ 
    * By splitting the _Age_ data into certain age-groups we get a pretty fare distribution, although it's a very simple split. To get a better, more sophisticated, answer to this question we would need more data. Data like 'weight' and 'height' would be better to use to answer this question.

* _Question 3: Are shark attacks where sharks were provoked more or less dangerous?_
    * While the current answer gives a decent view on the distribution of no injury, fatal and non-fatal attacks when provoked or not. The analyses could be further refined to classify the injuries even further. 

* _Question 4: Are certain activities more likely to result in a shark attack?_
    * I believe the current answer gives a good view of the data. To refine the answer even more, an extra layer (bar) per activity could be added to view the number of fatal attacks vs non-fatal attack. The analysis itself may be expended to classify the activities in groups like 'above' or 'below' the water surface. 



<!-- (Technical) Report of assignment Module 6 - Income Inequality vs GDP -->

# Technical Report - Income Inequality vs GDP