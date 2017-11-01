## NULL HYPOTHESIS:

State your alpha in a separate paragraph for visibility (I almost missed it)

Note that the word user can be costumer or subscriber, and you are using user and resident both in the title, but that does not easily relaste to a citibike client category.
Clearly state if you want to do the analysis on users (costumers and subscribers) costumers (occasional users) or subscribers (regular users).

"The ratio of users who are over 30 years old biking on weekends over biking on weekdays is the same or higher 
than the ratio of users who are under 30 years old biking over weekends to woman biking on weekdays

H0: the ratio of >30yo (or <=?) biking (really you want a ratio of number of rides

the ratio of number of citibike rides by >=30 yo costumers ( or subscribers? or all?) on weekends over weekdays is the same or higher than 
the ratio of ides by <30 yo costumers ( or subscribers? or all?)

*BUT* state clearly in your report why this ratio relates to your original question (weekend - > no commute etc) 

the mathematical formulae dont render, but the look ok as far as I can tell.
'''
  H0: frac{{under30{weekend}}{under30{\mathrm{week}}} <= frac{over30{weekend}}{over30{week}} 
  H1: frac{under30{weekend}}{under30{\mathrm{week}}} > frac{over30{weekend}}{over30{week}} 

  or: H_0: frac{{under30{weekend}}{under30{week}}} - frac{over30{weekend}}}{over30{week}}} <= 0 
  H_1: frac{{under30{weekend}}{under30{week}}} - frac{over30{weekend}}}{over30{week}}} > 0 

  I will use a significance level alpha=0.05
'''

## DATA: 

the data seems to be parsed correctly and to support the question. The plots that show the distributions are useful, for example they give a sence of distribution size and ratio

## TEST:

You are testing the a ratio with categorical endogenous variable. The distributions are not parametrizable with a Gaussian, that I know. 
Appropriate test then would be Fisher exact test, and chi sq test. 
The Fisher exact test (https://en.wikipedia.org/wiki/Fisher%27s_exact_test) is suitable for small datasets, the chi sq for proportion (contingency table) for large datasets.

A z-test could also work but it assumes simple random sampling from a normally distributed population (typical when testing pharmaceuticals with a placebo and a true medication)

NOTE: For whichever test you chose, you want the one-tailed version

## Further suggestions: 
Your split between weekday and weekend does not fully convey "commute" and this should be discussed

Some tests may be affected by the sample sizes being dramaticallyt different, make sure the test you chose is not
