"""
Datasets can have missing data. The reason why data is missing in a dataset can be for one or more reasons (at the same time). Knowing why data is missing will help you in deciding what to do with that missing data. 

Important

Let's define the term "bias". A bias in statistics is when a distortion in a statistical conclusion is not the result of randomness. Biases can be caused during the gathering, processing or analysis of data.

For example: when researchers approach people on the street to ask questions they're more likely to approach people who are similar to them. This is more specifically called "selection bias".

Another example: Let's say some researchers interview people and those interviews are recorded in audio. During analysis it's discovered that some participants are hard to understand. The reason could be either the volume of their voice or their skill in a language. Excluding these participants can cause a bias in the result of the research.

We want to minimize the bias in our research results and analyses so that we accurately reflect reality.

Below we'll discuss the various ways in which data can be missing. 

MCAR: Missing completely at random

This mechanism is the simplest and least realistic reason for "missingness" of data.

Note

"This effectively implies that causes of the missing data are unrelated to the data."

Flexible Imputation of Missing Data - Stef van Buuren(opens in a new tab)

Example: You have a 1000 thermometers in all kinds of places that read temperature every minute and transmit it to a central location. If each thermometer randomly cannot transmit once every 400 times they try to, this does not result in a dataset that misrepresents the real world. We do have a little less data overall but we don't have more or less missing data from specific groups of thermometers.

The nice thing about completely random missing data is: we can simply drop those measurements and there will be no bias.

Conclusion: If the measurements you're missing are completely random dropping those measurements will essentially not change the representation of the real world thing you're measuring.

MAR: Missing at Random, aka "missing data rate"

This mechanism is not the same as MCAR and is much more common. The name for this mechanism is not a good name because there's not that much randomness involved.

In short: We can discover why the data is missing based on the data we do have.

Example: You have a 1000 thermometers in all kinds of places that read temperature every minute and transmit it to a central location. These thermometers have a higher chance of transmission failure when they're placed at a high altitude (in the mountains for example). We know the altitude for each thermometer.

If we remove these measurements we disregard more measurements with high altitude relative to measurements with lower altitude. So dropping those high-altitude measurements introduces a bias.

Conclusion: If the measurements you're missing are not random dropping those measurements will change the representation of the real world thing you're measuring.

Fix: we can look at and compare groups of measurements that have the same value for the reason-that-data-is-missing.

So in the example: if the altitude is a consistent predictor of missingness we can group thermometers at the same altitude and we'll see the same amount of missingness. We can also use this information to help us estimate (impute) the missing data (more on imputing later).

MNAR: Missing Not At Random (also known as NMAR)

We can not discover why the data is missing, because it is based on data that we are missing.

This one is the most complex missing data mechanism and is also quite common.

Example: You have a 1000 thermometers in all kinds of places that read temperature every minute and transmit it to a central location. These thermometers have a higher chance of transmission failure the higher the humidity is. Because a high humidity is influenced by the temperature and we can't read the temperature we cannot (easily) discover why the data is missing.

If we remove those measurements we disregard more measurements with high humidity relative to measurements with non-high humidity. So dropping those high-humidity measurements introduces a "bias".

Conclusion: If the measurements you're missing are not random dropping those measurements will change the representation of the real world thing you're measuring.

The fix for this: get actual measurements and try to figure out why the data is missing. This will help you choose a strategy to fill the missing data.

So in the example we would either get the actual temperature or the humidity and see if we can use that data to estimate (impute) the missing data.
"""

# Read more


# Missing data on Wikipedia (https://en.wikipedia.org/wiki/Missing_data)

# Bias on Wikipedia (https://en.wikipedia.org/wiki/Bias)

# Flexible Imputation of Missing Data - Stef van Buuren (https://stefvanbuuren.name/fimd/sec-MCAR.html)