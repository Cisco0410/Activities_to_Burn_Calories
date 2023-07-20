# This class will store all the user's info
class User:

  def __init__(self, weight, height, measurement, age, activity_level):
    self.weight = weight
    self.height = height
    self.measurement = measurement
    self.age = age
    self.activity_level = activity_level


# This class will inherit the parent class "User", utilzing the methods created
# from its function to return the user's attributes
class CalEquation(User):

  def __init__(self, weight, height, measurement, age, activity_level, gender):
    # Initializes inheritance and simplifies code re-usabilty
    super().__init__(weight, height, measurement, age, activity_level)
    self.gender = gender

  # Will create the activity modifier based on user input
  def activity_level_mod(self):
    activity_lvl_dict = {
      "Activity_level": {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725,
        5: 1.6
      }
    }
    # Iterates through the created dict. If user input matches a key in "Activity_level", it will assign the associated activity modifier
    for act_lvl in activity_lvl_dict["Activity_level"]:
      if act_lvl == self.activity_level:
        return activity_lvl_dict["Activity_level"][self.activity_level]

  # We will utilize the Harris-Benedict equation to find the Basal Metabolic Rate (BMR)
  # and adjust it based on the activity modifier to find the user's recommended
  # caloric intake
  def eq_by_gender(self):
    # We will have 2 different functions based on their corresponding Harris-Benedict equation
    # with regards to gender. It will account for the unit of measurement inputted and
    # will determine the correct equation accordingly.
    def male_user():
      if self.measurement == "metric":
        bmr = 66.5 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 *
                                                                      self.age)
        bmr_mod = round(bmr * self.activity_level_mod())
        print(f"\nYour daily recommended calorie intake should be approximately: {bmr_mod} cals")
        
      else:
        bmr = 66.47 + (6.24 * self.weight) + (12.7 * self.height) - (6.75 * self.age)
        bmr_mod = round(bmr * self.activity_level_mod())
        print(f"\nYour daily recommended calorie intake should be approximately: {bmr_mod} cals")
      return bmr_mod

    def female_user():
      if self.measurement == "metric":
        bmr = 655.1 + (9.563 * self.weight) + (1.850 * self.height) - (
          4.676 * self.age)
        bmr_mod = round(bmr * self.activity_level_mod())
        print(f"\nYour daily recommended calorie intake should be approximately: {bmr_mod} cals")

      else:
        bmr = 655.51 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 *
                                                                     self.age)
        bmr_mod = round(bmr * self.activity_level_mod())
        print(f"\nYour daily recommended calorie intake should be approximately: {bmr_mod} cals")
      return bmr_mod


    # Will determine what equation to use based on gender input
    if self.gender == "M":
      return male_user()
    else:
      return female_user()
