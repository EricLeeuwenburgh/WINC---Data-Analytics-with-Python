# Data Acquisition
So far we have been dealing with data that we already got from a source, but in the real world, you will generally have to first collect data by yourself. There are a number of steps to this process. The first of which is determining what question you are trying to answer, which builds upon which problem you are trying to solve.

## Formulating a data question

The data question (or research question) is at the center of your data project. It is best to model your question around an actual problem. A pitfall is to think "I want to do something with data analytics" - without a goal in mind, the entire process of data analytics becomes extremely unstructured. Consider the following problem: "The distribution of people in a train is uneven, resulting in some cabins being overfull while others are completely empty" - this is a problem that a railway company might experience. To solve this problem, the railway company wants to create a mobile application to help people find empty cabins. However, the development of such an application is costly, so the railway company wants to know if this app would help resolve their problem before investing time and money. An approach you could take is to survey people who use the train to ask if they would make use of such an app; this however is not a scientific approach, people will happily say one thing and then do another thing. So a data question like "Will an app solve the disbalance in train cabins" is flawed in many ways.

A better way would be to split the research into two parts: an exploratory phase and a testing phase. In the first exploratory study you might survey train-goers on what motivates them to pick a specific cabin. A question like "What are the motivations for picking a train cabin?" would fit the bill. This research would likely have multiple open-ended questions to which the responses would have to be examined individually and then boiled down to classifications.

In the second phase we might then select one or more classifications and test them individually. We might ask a question like "How big is the effect of train type on cabin selection for train-goers?". This is a question for which we can collect structured data; we can look at all different types of train and measure the distribution of people in the cabins.

## Defining the required data

Once we have a question, we have to identify what data we need to answer the question. Consider the question "What are the motivations for picking a train cabin?" The data we need is to determine what cabin train-goers select, and a reason why they select that cabin. The first datapoint wil require us to define a set of cabins that people can choose from; this definition may seem easy at first sight, but it requires both empathy and creativity. From a railway point of view, you might identify types of cabins from a technical point of view; you might have options like **standing cabins, business class cabins**, etc. But a train-goer might have a very different idea of the cabins; a train-goer might for instance want to give an answer like **the cabin closest to an elevator**, or **the cabin that is closest to the exit at my destination**. Our question of classification suddenly is not so clear-cut and we might even consider accepting unstructured data. This same thinking applies to the second question.

Furthermore, this data would not have any nuance to it - how often do users actually make use of trains? What destinations do they travel between? These are all factors to consider in an exploratory study. So we have to figure out what nuances are relevant to answering our question. A good way of exploring these additional questions is to hold one-on-one interviews with a sample of your target population. Conducting an unstructured interview can shine a light on many things that you maybe never even thought of.

## Selecting a data acquisition strategy

Once you know the type of data that you want, it is time to get your hands dirty and actually collect the data. There are many ways in which you can do this. If for instance you are interested in weather data, you might find a weather station and track their reportings. Alternatively you could construct a measuring device to collect your own data. There's a myriad of techniques to be used, but we divide them in the following groups:

- _Experiment_ - Manipulate variables and log the differences in behavior
- _Surveying_ - Construct a list of questions and distribute in a population
- _Interview_ - Conduct a verbal interview within a population
- _Observation_ - Log naturally occuring phenomena with no interference
- _Ethnography_ - Participate in phenomena and log your findings
- _Archival research_ - Collect historic data
- _Secondary data collection_ - Use existing data sets to construct a new data set