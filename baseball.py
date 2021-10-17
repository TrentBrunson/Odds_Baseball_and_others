"""
Write a program to calculate the percentage of games won by each team. 
Create a new data file named “mlb-division-standings2019.csv” that contains 
all the original data plus the percentage of games won. You should sort
the data in the new file first by division (ascending order) and second by 
percentage of games won (descending order).
Display the division standings to the user. 
Each division should be listed separate from the other divisions. 
Your standings should include rank (1-5), team, wins, losses, and win % for each team
under a division header. 
You should round the percentage of games won to two places after the decimal."""
#%%
import pandas as pd
file = "data\mlb-games-2019.csv"
# %%
df = pd.read_csv(file, header=None)
header = ['Team', 'Wins', 'Losses', 'Division']
df.columns = header
df
# %%
df.sort_values('Division', inplace = True)
df
# %%
df['Percentage'] = df.Wins / (df.Wins + df.Losses)
df
# %%
df.sort_values(['Division', 'Percentage'], ascending = (True, False), inplace=True)
df
# %%
def main():
    mlb = getData()
    displayResults(mlb)
    return

def getData():
    import pandas as pd
    file = "data\mlb-games-2019.csv"
    df = pd.read_csv(file, header=None)
    header = ['Team', 'Wins', 'Losses', 'Division']
    df.columns = header
    df['Percentage'] = df.Wins / (df.Wins + df.Losses)
    df.sort_values(['Division', 'Percentage'], ascending = (True, False), inplace=True)
    df.to_csv(r'mlb-division-standings-2019.csv', index=False, header=True)
    return df

def displayResults(frame):
    frame.set_index('Team', inplace=True)
    print(frame)
    return

if __name__=='__main__':
    main()
# %%
