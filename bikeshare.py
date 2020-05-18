import time
import pandas as pd
import numpy as np
import json
from input_util import get_user_input

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' ]



def get_filters():
   hello ='Hello! Let\'s explore some US bikeshare data!
    print(hello)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
     city = input('SELECT THE CITY YOU WANT TO EXPLORE <CHICAGO,NEW YORK ,WASHINGTON> \n>' ).lower()
     if city in CITIES:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = get_user_input('GOOD,, NOW ENTER THE MONTH NAME OR YOU CAN ENTER <ALL> IF YOU WANT', MONTHS)

    # TO DO: get user input for day of week or all fo all days
    day = get_user_input('GOOD,, NOW ENTER THE DAY NAME OR YOU CAN ENTER <ALL> IF YOU WANT FOR NO DAY FILTRING', DAYS)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df= pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]
        
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]   


 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month= df['month'].value_counts().index()
    print("The most common month is >", most_common_month)
    
     # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is >", most_common_day_of_week)
    
     # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is >", most_common_start_hour)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)
    
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]print("The most commonly used         start station and end station : {}, {}"\.format(most_common_start_end_station[0],most_common_start_end_station[1]))
     
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))
    
    print()

    if 'Gender' in df.columns:
        user_stats_gender(df)

    if 'Birth Year' in df.columns:
        user_stats_birth(df)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    


    # TO DO: Display counts of gender
    print("Counts of gender:\n")
    gender_counts = df['Gender'].value_counts()
    
    for index,gender_count   in enumerate(gender_counts):
        print("  {}: {}".format(gender_counts.index[index], gender_count))
    
    print()


    # TO DO: Display earliest, most recent, and most common year of birth
     birth_year = df['Birth Year']
  
    most_common_year = birth_year.value_counts().idxmax()
    print("The most common birth year:", most_common_year)
  
    most_recent = birth_year.max()
    print("The most recent birth year:", most_recent)
    
    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)

    
def display_data(df):
    i = 0
    while (True):
        A= input('\n ENTER <YES> TO SEE ROW DATA OTHERWISE <NO>.\n>')
        if (A == 'yes'):
            print (df.iloc[i:i+5])
            i+=5
        elif (A == 'no'):
            break
    return
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
