# Brier-Score-
There are two projects, one is calculating the Brier Score and another is showing the probability for a tutor finding the job and and some visualization of job hunting market.


Project Part1：Uses machine learning methods to calculate the probability for a tutor finding the job
1. This data set is the data of "Sunshine Family Education Network", the total sample is 365672
2. The information included is—in the sample interval include the information and data of all tutors registered on this website: gender, university, the times of teachers viewed by students  (clicks), whether to upload their own photos, work experience , Education level, whether the student is successfully matched (0-1 variable)
3. We use machine learning methods to calculate the probability that the teacher can successfully match the student (that is, find a job) without knowing whether the teacher matches the student, and the output result is the predicted probability information


Project Part2 Visualization：Some visualization of job-hunting market
1. This data set is the data of "Zhaopin Recruitment", the total sample is 91793
2. The information include：Posting Date（When did a company post a job ad）,Posting Type(full time of part time), Salary Range, Industry,  Jobtype, Jobname, Cityname, Province, Working experience, Education level, Welfare
3. We did some visualization by using the dataset


Profect part3: Calculating the Brier Score
We are also interested in calculating the Brier Score for a psychology project. Here is the summary for the inroduction of the project:
It is kind of check the accurency of your forecasts, and using the score to represent the accurency.
How Your Forecasts Will Be Scored for Accuracy
How do we calculate your forecasting score when we rank your performance relative to others on the leaderboard? We will use something called the Brier scoring rule, which we explain in detail below. But the bottom lines are these:
1. When the event in question does not occur, you are scored as more accurate when your forecasts are closer to 0%.
2. When the event does occur, you are scored as more accurate when your forecasts are closer to 100%.

To get a perfect score, you need to be omniscient and assign 0% to all non-occurrences of events and 100% to all occurrences of events. Just as it would be rash for a baseball player to try to hit homeruns every time at bat, it would be risky for you to assign either 0% or 100% to all events. Why? You pay a steep penalty when you assign very high percentages to things that do not occur and very low percentages to things that occur. But you also do not want to be excessively cautious. You will pay a steep price for not making strong predictions when you have useful predictive knowledge. Strive for a balance between bold, but risky forecasts and cautious, low- payoff forecasts.
Your Brier score will be best when you report your true beliefs and make sure that irrelevancies, such as what you hope or fear, are kept at bay.
More Technical Discussion of the Brier Scoring Rule
Definition of Brier Scores. For any given forecasting problem, Brier scores range from 0 to 2, with the best possible Brier score being 0.
Suppose a problem asks whether it will rain tomorrow in Berkeley, CA. You report a percentage p that it will rain. For a dichotomous question, this means you believe the chances are 100% - p that it will not rain.
We will represent the two possible states of the world, rain and no rain, as 100% and 0%, respectively. Now, let's suppose it actually rains.
• Your Brier score would be (100% - p)2 + (0% - (100% - p))2. The first term is the squared difference between what actually occurred – rain – and your forecast for rain, and the second term is the squared difference between what didn't occur – no rain – and your forecast for no rain.
If you had said the chance of rain is 100%, your Brier score would be (100% - 100%)2 + (0% - 0%)2 = 0. Note that this is the best score. If you had said the chance of rain is 0%, your Brier score would be (100% - 0%)2 + (0% - 100%)2 = 2. (The answer is 2 because the Brier score is calculated using percentages in their decimal form, where the range 0%-100% is expressed as the interval 0-1.) This is the worst Brier score.
Your forecast will probably fall between 0% and 100%. Obviously, if you think rain is more likely than not, you want to assign a higher probability to rain. But since it might not rain, you want to hedge your bets. Errors in either direction have the same impact: being too high is bad, and being too low is equally bad. You get the best score when you truthfully report your best likelihood estimates.
We can't compute a Brier score for you on any given problem until the problem has closed and we know the "correct" answer. Therefore, we keep track of your predictions on each day, and calculate your daily Brier score after a problem has closed.
• Your score for that forecasting question equals the unweighted average of your daily Brier scores over all days the problem has been open.

How do we determine your daily Brier score?
• The first day a problem is posted, you have the opportunity to make a forecast. If you do not make one, we assign the then-current daily group-average daily Brier score to you for each day until you make your first forecast on that question. (In this context, "group" means everyone who uses the same forecasting website as you do.)
• Once you make a prediction for a question, we presume that your answer remains the same each day until you explicitly update your forecast.
• If you skip a question entirely, you will receive the group-average Brier score for that question.
Your accuracy will be assessed using two metrics: (1) calibration and (2) resolution. Understanding both metrics and how to improve each is essential to being a good forecaster.
1. Calibration is your ability to assign probabilities to events that correspond to their true frequencies of occurrence. If you were perfectly calibrated, 60% of all events to which you assigned a probability of 60% would occur; 70% of events to which you assigned a probability of 70%, would occur; 100% of events to which you assigned a probability of 100% would occur, etc. In brief, good calibration means you know what you know, and what you don’t know. Suppose you are predicting the likelihood of rain for the next 365 days in Memphis
–and all you know is that it rains there 30% of the time. An easy way to get a good calibration score is to predict a 30% chance of rain each day. Your average forecast would be 30%, and the overall chance of rain would be 30%. You’d have a perfect calibration score!
2. Resolution is your ability to assign higher probabilities to things that happen than to things that do not happen. Let’s return to the Memphis example. If you assigned a probability of 30% to rain every day, you would have zero ability to discriminate between rain and shine. Calibration, alone, is not enough. To improve resolution, you need to seek out more information about Memphis beyond the base rate. Suppose that data from the National Weather Service allow you to predict a 20% chance of rain on days without rain and an 80% chance of rain on rainy days. Your resolution score would be great. And if you could predict 0% on days without rain
and 100% on rainy days, both your calibration and resolution would be perfect! In brief, use base rates to help with calibration – but seek more specific diagnostic information, whenever possible, to help with resolution.
