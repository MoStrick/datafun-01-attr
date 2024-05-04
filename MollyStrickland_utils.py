''' This module provides a reusable byline for the author's services.'''

#Import Dependencies
import math
import statistics

#Define Variables Define at least one variable of each of these types: str, int, float, bool, list of strings, list of numbers.
company_name: str = "Numbers Count Analytics"
company_description: str = "Online learning platform for 6-12 mathematics"
Course_enrollment_capacity: list = [.75, .33,.62,.94, .88,.96,.42]
completion_rates: list = [.57, .33,.62,.94, .88,.96,.42,1,1,1]
Course_difficulty_ratings: list = [.6, .3, .8, .5, .9, .4, .6, .5]
Course_duration_weeks: list = [5,6,7,8,9,3,2,8,8,8]
popular_courses: list = ["Financial Math", "Baking with Fractions", "Reading Rulers with Fractions", "Physics", "Sports Statistics"] 
would_recommend_to_a_friend: bool = True
average_tutor_satisfaction: float=7.2
count_employed_tutors: int = 16
count_enrollment_subscription: int = 320

#Define formatted strings
Course_enrollment_capacity_string: str = f"Course Enrollment Capacities: {Course_enrollment_capacity}"
completion_rates_string:str = f"Course completion rates: {completion_rates}"
Course_difficulty_ratings_string:str=f"Course difficulty ratings: {Course_difficulty_ratings}"
Course_duration_weeks_string:str = f"Course completion in weeks: {Course_duration_weeks}"
popular_courses_string:str = f"Popular Courses:{popular_courses}"
would_recommend_to_a_friend_string:str = f"Would recommend to a friend?: {would_recommend_to_a_friend}"
average_tutor_satisfaction_string:str = f"Average tutor satisfaction: {average_tutor_satisfaction}"
count_employed_tutors_string:str = f"Number of employed tutors:{count_employed_tutors}"
count_enrollment_subscription_string:str =f"Total number of monthly subscribers: {count_enrollment_subscription}"

#Calculate Descriptive Statistics calculating 



smallest= min(Course_enrollment_capacity)
largest= max(Course_enrollment_capacity)
total= sum(Course_enrollment_capacity)
count= len(Course_enrollment_capacity)
mean= statistics.mean(Course_enrollment_capacity)
Average_duration=statistics.mean(Course_duration_weeks)
Average_completion=statistics.mean(completion_rates)
Average_difficulty_ratings=statistics.mean(Course_difficulty_ratings)
mode= statistics.mode(Course_enrollment_capacity)
median= statistics.median(Course_enrollment_capacity)
standard_deviation=statistics.stdev(Course_enrollment_capacity)

stats_string: str = f"""
Descriptive Statistics for Our Course Enrollment Capcity:
  Smallest: {smallest}
  Largest: {largest}
  Number of courses available: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {round(standard_deviation,3)}
  
Averages
    Average weeks to complete a course:{Average_duration}
    Average difficulty rating:{Average_difficulty_ratings}
    Average amoount of a course completed:{Average_completion}
"""

Monthly_Payroll = int((count_employed_tutors)*(10)*(4)*(20))
Monthly_income = int((count_enrollment_subscription)*(50))
Difference= (Monthly_income-Monthly_Payroll)
if Difference > 0:
    profit_or_loss=f'''The company profit is ${Difference}'''
else:
    profit_or_loss=f'''The company loss is $ {abs(Difference)}'''
    
Profit_string: str = f"""
Expenses, Income, and Profit Analysis
     Monthly Payroll: ${Monthly_Payroll}
     Monthly Income from Subscibers: ${Monthly_income}
     {profit_or_loss}
"""

#Define byline String Create a multiline string named byline to display your formatted information. We'll use this byline in a future project. For example:
byline: str = f"""
    {company_name}
    {Course_enrollment_capacity_string}
    {completion_rates_string}
    {Course_duration_weeks_string}
    {popular_courses_string}
    {would_recommend_to_a_friend_string}
    {average_tutor_satisfaction_string}
    {count_employed_tutors_string}
    {count_enrollment_subscription_string}
    {stats_string}
    {Profit_string}
"""

#Define Main Function 
def main():
    ''' Display all output'''
    print(company_name)
    print(popular_courses_string)
    print(would_recommend_to_a_friend_string)
    print(average_tutor_satisfaction_string)
    print(count_employed_tutors_string)
    print(count_enrollment_subscription_string)
    print(stats_string)
    print(Profit_string)

    # If all of the above works, then the byline should work too:
#print(byline)


#Conditional Script execution 
if __name__ == '__main__':
    main()
    
    
    
    



