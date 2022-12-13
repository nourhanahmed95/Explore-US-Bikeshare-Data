import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   
    city= input("Which city do you want data about(chicago, new york city, washington)? ").lower()
    while True:
            if city in ['chicago', 'new york city', 'washington']:
                    break
            else:
                print("that's not the correct city please choose again. ")
                city= input("Which city do you want data about(chicago, new york city, washington)? ").lower()
        
            
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month do you want data about(all, january, february, march, april, may, june)? ").lower()
    while True:
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("That's not the correct month please choose again. ")
            month = input("Which month do you want data about(all, january, february, march, april, may, june)? ").lower()
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day do you want data about(all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)? ").lower()
    while True:
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("That's not the correct day please choose again. ")
            day = input("Which day do you want data about(all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)? ").lower()
           
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
def display_raw_data(df):
    i = 0
    answer = input('Would you like to display the next 5 rows of data? yes/no ').lower()
    while True:
        if answer == 'no':
            break
        else:
            print(df[i: i+5])
            answer = input('Would you like to display the next 5 rows of data? yes/no ').lower() 
            i +=5
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    Most_Common_Month = df['month'].mode()[0]
    print('Most Common Month: ', Most_Common_Month)
    # TO DO: display the most common day of week
    Most_Common_day = df['day_of_week'].mode()[0] 
    print('Most Common day: ', Most_Common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    Most_Common_Starthour = df['hour'].mode()[0]
    print('Most Common Starthour: ', Most_Common_Starthour) 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Most_Used_StartStation = df['Start Station'].mode()[0]
    print('Most Used StartStation: ', Most_Used_StartStation)
    # TO DO: display most commonly used end station
    Most_Used_EndStation = df['End Station'].mode()[0]
    print('Most Used EndStation: ', Most_Used_EndStation)
    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End'] = df['Start Station'] + df['End Station']
    Most_Frequent_combination = df['Start_End'].mode()[0]
    print('Most Frequent combination: ', Most_Frequent_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total Travel Time: ', Total_Travel_Time, ' Seconds')
    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean Travel Time: ', Mean_Travel_Time, ' Seconds')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_Types = df['User Type'].value_counts()
    print('User Types: ', User_Types)
    # TO DO: Display counts of gender
    Gender = df['Gender'].value_counts()
    print('Gender: ', Gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    Earliest_year = df['Birth Year'].min()
    print('Earliest year: ', Earliest_year)
    Most_Recent_year = df['Birth Year'].max()
    print('Most Recent year: ', Most_Recent_year)
    Most_Common_Year = df['Birth Year'].mode()
    print('Most Common Year: ', Most_Common_Year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
