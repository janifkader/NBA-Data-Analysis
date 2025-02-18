# NBA Data Analysis

## Project Overview

This data analysis project works to see which of the 'four factors' in NBA advanced statistics is most pertinent to winning.

### What are the Four Factors?

The four factors of Basketball are Shooting, Turnovers, Rebounding and Free Throws. These are measured with Effective Field Goal Percentage (eFG%), Turnover Percentage (TOV%), Offensive Rebound Percentage (ORB%) and Free Throw Rate respectively. These factors are considered the most important aspects of a basketball game, and if a team achieves remarkable numbers in each of these categories, the team is essentially guaranteed to be successful.

### Data Cleaning

In the initial data preparation, we performed the following tasks:

1. Dropped irrelevant columns
2. Dropped columns with unfulfilled data
3. Formatted data in a more fitting way

The initial data set can be found in 'allfourfactors.csv', '2023fourfactors.csv', '2010fourfactors.csv', '1996fourfactors.csv'. These statistics have been pulled straight from NBA.com in their 'Four Factors' section. It looks at team statistics from the 2023-24, 2010-11 and 1996-97 seasons. In said set, we can see many columns that are simply not important for our analysis. Things like the ranks, names, ids, and minutes aren't terribly relevant for our goal, so dropping said columns would be the correct path forward. The code used to prepare the data can be seen below:
```python
twentiesNBA = "2023fourfactors.txt"
tensNBA = "2010fourfactors.txt"
ninetiesNBA = "1996fourfactors.txt"
allNBA = "allfourfactors.txt"
headers = ["TEAM_ID","TEAM_NAME","GP","W","L","W_PCT","MIN","EFG_PCT","FTA_RATE","TM_TOV_PCT","OREB_PCT","OPP_EFG_PCT",
           "OPP_FTA_RATE","OPP_TOV_PCT","OPP_OREB_PCT","GP_RANK","W_RANK","L_RANK","W_PCT_RANK","MIN_RANK",
           "EFG_PCT_RANK","FTA_RATE_RANK","TM_TOV_PCT_RANK","OREB_PCT_RANK","OPP_EFG_PCT_RANK","OPP_FTA_RATE_RANK",
           "OPP_TOV_PCT_RANK","OPP_OREB_PCT_RANK"]
twentiesDf = pd.read_csv(twentiesNBA, sep=',', header=None, names=headers)
tensDf = pd.read_csv(tensNBA, sep=',', header=None, names=headers)
ninetiesDf = pd.read_csv(ninetiesNBA, sep=',', header=None, names=headers)
allDf = pd.read_csv(allNBA, sep=',', header=None, names=headers)
twentiesDf = twentiesDf.drop(columns=["TEAM_ID","TEAM_NAME","GP","W","L","MIN","GP_RANK","W_RANK","L_RANK","W_PCT_RANK",
                                      "MIN_RANK","EFG_PCT_RANK","FTA_RATE_RANK","TM_TOV_PCT_RANK","OREB_PCT_RANK",
                                      "OPP_EFG_PCT_RANK","OPP_FTA_RATE_RANK","OPP_TOV_PCT_RANK","OPP_OREB_PCT_RANK"],
                             axis=1)
tensDf = tensDf.drop(columns=["TEAM_ID","TEAM_NAME","GP","W","L","MIN","GP_RANK","W_RANK","L_RANK","W_PCT_RANK",
                                      "MIN_RANK","EFG_PCT_RANK","FTA_RATE_RANK","TM_TOV_PCT_RANK","OREB_PCT_RANK",
                                      "OPP_EFG_PCT_RANK","OPP_FTA_RATE_RANK","OPP_TOV_PCT_RANK","OPP_OREB_PCT_RANK"],
                             axis=1)
ninetiesDf = ninetiesDf.drop(columns=["TEAM_ID","TEAM_NAME","GP","W","L","MIN","GP_RANK","W_RANK","L_RANK","W_PCT_RANK",
                                      "MIN_RANK","EFG_PCT_RANK","FTA_RATE_RANK","TM_TOV_PCT_RANK","OREB_PCT_RANK",
                                      "OPP_EFG_PCT_RANK","OPP_FTA_RATE_RANK","OPP_TOV_PCT_RANK","OPP_OREB_PCT_RANK"],
                             axis=1)
allDf = allDf.drop(columns=["TEAM_ID","TEAM_NAME","GP","W","L","MIN","GP_RANK","W_RANK","L_RANK","W_PCT_RANK",
                                      "MIN_RANK","EFG_PCT_RANK","FTA_RATE_RANK","TM_TOV_PCT_RANK","OREB_PCT_RANK",
                                      "OPP_EFG_PCT_RANK","OPP_FTA_RATE_RANK","OPP_TOV_PCT_RANK","OPP_OREB_PCT_RANK"],
                             axis=1)
```

### Data Analysis

To preform our analysis, we must:

1. Find the correlation between each of the four factors and winning percentage for NBA Teams.
2. We must perform this analysis across multiple seasons and see which of the factors is most involved in winning.
3. Perform a regression analysis to see the relationship between our factors and winning.
4. Look at the overall winner and see how the correlation varies between eras.

To preform this analysis we will find the correlation between the four factors an win percentage and plot it on a correlation heat map. The code can be seen below:

```python
twentiesFig = px.imshow(twentiesDf.corr())
tensFig = px.imshow(tensDf.corr())
ninetiesFig = px.imshow(ninetiesDf.corr())
allFig = px.imshow(allDf.corr())
twentiesFig.show()
tensFig.show()
ninetiesFig.show()
allFig.show()
```

## Results
The heatmaps can be seen below:

2023-24:

<img width="442" alt="image" src="https://github.com/user-attachments/assets/aac097d2-63e3-4b10-aea2-6e23d1fcb0c8" />

2010-11:

<img width="425" alt="image" src="https://github.com/user-attachments/assets/8801ca06-ffff-4ea9-8482-4fadd8eae370" />

1996-97:

<img width="440" alt="image" src="https://github.com/user-attachments/assets/47ed4f68-0790-41a8-b950-5ec9edbe5ce3" />

Color scale for heatmaps:

<img width="68" alt="image" src="https://github.com/user-attachments/assets/e3c2a6d6-5f77-405c-af19-c3f2a211b68f" />

### Overall Picture

When looking at the heatmap, the first column/row is what's the most important to us, because it shows us how every other four factor category correlates with win percentage. When looking at the combination of all of the years, it is clear to see that eFG% is the most heavily correlated with winning percentage (0.4658789) and opponent eFG% (-0.4272192) is the most negatively correlated to about the same degree. eFG% is followed by TOV% (-0.2479357) as the most highly correlated factor to winning, more specifically, it is relatively negatively correlated as teams lose possession and the opportunity to take a good shot when the ball is turned over, and opponent TOV% is positively correlated as the more the ball is turned over by the other team, the more opportunities the team has to score. FTA% (0.1976621) follows closely behind as the next most correlated statistic. The last is OREB% (-0.08145548) which is interestingly enough, negatively correlated with WIN%. We can attribute this to the fact that if a team is getting a lot of offensive rebounds, that also means that they are missing shots, which would make an offensive rebound necessary to regain possession. This further emphasizes the importance of shooting as a factor. 

### Evolution of Four Factors

The game of basketball has evolved tremendously over its long history and that evolution is evident in this data. The correlation between eFG% and WIN% has decreased as the correlation between everything else and WIN% has increased. This happens as teams are more willing to take low-percentage three-point shots rather than the heavy reliance on the two-point game of the past. Something interesting to note is that in the most recent season, 2023-24, OREB% has a positive correlation with WIN%. This could be due to more teams converting on second chance possessions after offensive rebounds, but more analysis would need to be conducted before coming to that conclusion.

### Regression Analysis

To attack this problem in another way, we can perform a simple Multiple Regression Analysis to see the relationship between our independent variables (EFG_PCT, FTA_RATE, TM_TOV_PCT, OREB_PCT) and our dependent variable (W_PCT). We do this by optimizing the parameters or coefficients of the model. The variable with the coefficient of the largest magnitude has the most impact on winning, the sign of the coefficient determines whether or not that impact is positive or negative.

#### Data Preprocessing

For multiple regression analysis, each of our inputs and outputs should be in the following format:

x = [EFG_PCT, FTA_RATE, TM_TOV_PCT, OREB_PCT, 1], y = [W_PCT]

The coefficients should be in the following format:

w = [c_1, c_2, c_3, c_4, b]

The whole of our data is represented as such:

X = [x_1, x_1, x_3, ... , x_n], Y = [y_1, y_2, y_3, ... , y_n], W = [w_1, w_2, w_3, ... , w_n]

The code used to perform this preproccessing can be seen below:

```python
model = MultipleRegression()
df = pd.read_csv("allfourfactors.csv")
train_X = df[["EFG_PCT", "FTA_RATE", "TM_TOV_PCT", "OREB_PCT"]]
train_X = np.concatenate((train_X.to_numpy(), np.ones((89, 1), dtype=np.float32)), axis=1)
train_Y = df["W_PCT"]
train_Y = train_Y.to_numpy().reshape((89, 1))
```

To determine our optimized parameters, we use the formula derived from the gradient of the energy function, W = (X^T * X)^-1 * X^T * Y, Our regression model can be seen below:

```python
class MultipleRegression:

    def __init__(self):
        self.parameters = np.ones((1, 5), dtype=np.float32)

    def fit(self, train_X, train_Y):
        self.parameters = np.matmul(np.matmul(np.linalg.inv(np.matmul(train_X.T, train_X)), train_X.T), train_Y)
```

### Results

We can see the final parameters with the code below:

```python
model.fit(train_X, train_Y)
print(model.parameters)
```
From which, we recieve the following output:

EFG_PCT: 4.23839586, FTA_RATE: 2.80697118, TM_TOV_PCT: -3.89116642, OREB_PCT: -1.85822008

The regression analysis confirms our previous findings. Shooting, Turnovers, Free Throws and Rebounding in that order have the most impact on winning. This analysis further confirms our observation of the negative impact of offensive rebounding.
 
### Conclusion

Based on our heatmaps and regression analyais, it is evident that eFG% is the most correlated with winning in all of our individual seasons, and in the overall picture. This tells us that Shooting is by far the most important factor to winning. This is followed by Turnovers, Free Throws and Rebounding in that order. This is consistent throughout all of the eras we've analyzed, so despite the amount that Basketball has changed and grown as a sport, the fundamental principles are constant.
