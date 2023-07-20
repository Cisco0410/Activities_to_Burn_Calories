from user import *
from data import *

# Begins are calorie burning calculator
def user_inputs():
    # User will enter their info. Inputs will be formatted for consistency in data
    measurement = input("Welcome! Before we begin, what system of measurement do you follow? (metric or non-metric): ").lower()
    gender = input("Gender? (M or F): ").upper()

    # These will verify that all inputs below are entered in the correct format/data type without it repeating the entire input entering process
    avoid_redundant_checks_wt = True
    avoid_redundant_checks_age = True
    avoid_redundant_checks_height = True

    while True:
        # Utilizes logical operators with boolean table to verify correct spelling and input.
        if measurement != "metric" and measurement != "non-metric":
            measurement = input(
                "Sorry we caught an error in your input. Please type either 'metric' or non-metric': ").lower()
            continue   # This will continue the loop until both conditions equate to False
        # Therefore, proceeding to the condition below
        elif gender != "M" and gender != "F":
            gender = input("Please enter you gender as shown. (M or F): ").upper()
            continue
        else:
            pass
        # Below the try statement evaluates the ValueError if input isn't an integer. This prompts it to repeat the input inquiry without breaking the code until the user enters an integer
        if avoid_redundant_checks_wt:
            try:
                weight = int(input("Weight? (enter integer): "))
            except:
                continue
            avoid_redundant_checks_wt = False  # Breaks loop that would otherwise run forever
          
        if avoid_redundant_checks_height:
            try:
              height = int(input("Height? (enter integer in cm or inches): "))      
            except:
              continue
            avoid_redundant_checks_height = False
          
        if avoid_redundant_checks_age:
            try:
                age = int(input("Age? (enter integer): "))
            except:
                continue
            avoid_redundant_checks_age = False
          
        try:
          activity_level = int(input("How active are you?"
                "\n[1] Little or no exercise, desk job"
                "\n[2] Light exercise. Workout/sports 1-2 days/week"
                "\n[3] Moderate exercise. Workout/sport 3-4 days/week"
                "\n[4] Hard exercise. Weight-lifting/sports everyday"
                "\n[5] Very Hard exercise. Weight-lifting/sports 4-8 hours/day, or training for marathon, or triathlon, etc."
                "\n\n Choose between 1-5: "))
                # Will check if input is in range. If not, it will raise a ValueError, forcing it to the "except" block, thus re-intiating the loop and re-asking user input.
          if activity_level in range(1,6):
              break   # Will break all loops - including the while loop
          else:
              raise ValueError("Number inputted not one of the options") 
        except:                                                          
              continue
    user_info = CalEquation(weight, height, measurement, age, activity_level, gender)
    user_info.eq_by_gender()
    
    cals_burn = DataEq(weight, height, measurement, age, activity_level, gender, data_collect_clean())
    cals_burn.cals_to_burn()
