import pandas as pd
import difflib as dl
from user import *

def data_collect_clean():
  # This will be the data with various acitivies listed to help burn
  # calories and return to the recommended levels. One important note, all activites
  # listed and their associated calories burned are based on 1-hour intervals
  activities_df = pd.read_csv('exercise_dataset.csv')
 # print(activities.shape, '\n', activities.dtypes) --> checking all is in correct format
  
  # Checks to make sure no values are null or None
  # for col in activities.columns:
   # print(col, activities[col].isnull().sum())
  
  # Converts to non-metric system
  activities_df['Calories per lb'] = activities_df['Calories per kg'] * 2.20462
  
  # Deletes unnecessary columns for this project.
  activities_df.drop(columns=['130 lb', '155 lb', '180 lb', '205 lb'], inplace=True)
  return activities_df


class DataEq(CalEquation):
  def __init__(self, weight, height, measurement, age, activity_level, gender, activities_df):
    super().__init__(weight, height, measurement, age, activity_level, gender)
    self.activities_df = activities_df


  def user_input_act(self):
    # These empty lists will be utilized to collect the different activities from the database and then to further break them down to make it easier for our code to process through it
    act_list = []
    act_list_first = []
    user_act_input = input("\nTell us what activity you'd like to do to burn those calories. Could be anything!: ")
    
    for i in self.activities_df.iloc[:, 0]:
      act_list.append(i)
      
    for k in act_list:
      # We are splitting the list by the first comma since that has the actual name of the activity
      act_list_first.append(k.split(',', 1)[0])
      list_of_matches = dl.get_close_matches(user_act_input, act_list_first, 8, 0.4)
    # Creates new column in DataFrame. This will make it easier for the user input to be matched to the associated row of the activity and to grab the values from it.
    self.activities_df["Activities_First"] = act_list_first
    matches_df = pd.DataFrame(list_of_matches)
    matches_df.rename(columns= {0: "Activities_First"}, inplace= True )
    rec_act_df = pd.merge(self.activities_df, matches_df, on= ["Activities_First"], how= "inner")
    # This will delete the duplicates created in the for loop. The logic behind this is that the get_close_matches method will pull all the matches with the highest similarity ratio. The duplicates are from the for loop, so we can just drop them until the results are all unique (which will only be 8 since that's what's specified in the get_close_matches function)
    rec_act_df.drop_duplicates(subset= "Activity, Exercise or Sport (1 hour)", keep= 'first',inplace= True)
    return rec_act_df

  def cals_to_burn(self):
    while True:
        try:
          curr_cals = int(input("\nHow many calories have you eaten today?: "))
          break
        except:
          continue

    # This while look will allow the program to retain all the user's inputs, but allowing the user to change what kind of activity they'd like to conduct to burn the calories.
    while True:      
      rec_act_df = self.user_input_act()
      rec_act_df.rename(columns= {"Activity, Exercise or Sport (1 hour)": "Activity, Exercise or Sport"}, inplace= True)
      # 
      if self.measurement == "metric":
        rec_act_df["Time_to_burn_calories (m)"] = round(((((curr_cals / rec_act_df["Calories per kg"]) / self.weight) * 60) - ((self.eq_by_gender() / rec_act_df["Calories per kg"]) / self.weight) * 60))
      else:
        rec_act_df["Time_to_burn_calories (m)"] = round(((((curr_cals / rec_act_df["Calories per lb"]) / self.weight) * 60) -   ((self.eq_by_gender() / rec_act_df["Calories per lb"]) / self.weight) * 60))
        
      print("\n\nBelow is a list of activities based on your inputs and how long it will take (in minutes) to reach the recommended calorie intake \n\n", rec_act_df[["Activity, Exercise or Sport", "Time_to_burn_calories (m)"]])
      
      repeat_loop = input("\nWould you like to try with another activity [yes or no]?: ").lower()
      
      if repeat_loop == 'yes':
        continue
      else:
        break
      



  

