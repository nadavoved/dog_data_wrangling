# Analysis Report
## Question & Insights:
### Question #1 - What is the most common dog breed prediction ?
- concatenate all prediction columns
- get the top from `.describe()`.
### Question #2 - What is the mean rating numerator ?
- calculate `master_df['rating_numerator'].mean()`
### Question #3 - What is the mean text length for original WeRateDogs tweets?
- Include only original tweets: `master_df['text'][master_df['is_original']]`
- apply `len` for a new series using `.map()`
- get `.mean()`
### Insights:
1. the most common dog breed prediction is <mark>Golden Retriever</mark>.
2. the mean rating numerator is <mark>13.13</mark>.
3. the mean text length (character count) for original WeRateDogs tweets is <mark>120.1</mark>.
## Visualization
### Original tweet count per month(line chart)
- Include only original tweets: `master_df['timestamp'][master_df['is_original']]`
- create a series of only \<month name> \<year> in string format
- use `.value_counts()`
- sort the values according to index in datetime format
- plot a line chart:

![image info](Figure%205.png)