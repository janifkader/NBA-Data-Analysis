import pandas as pd
pd.set_option('display.max_columns', None)
import plotly.express as px

# Data Preparation

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
# Data Analysis

twentiesFig = px.imshow(twentiesDf.corr())
tensFig = px.imshow(tensDf.corr())
ninetiesFig = px.imshow(ninetiesDf.corr())
allFig = px.imshow(allDf.corr())
twentiesFig.show()
tensFig.show()
ninetiesFig.show()
allFig.show()