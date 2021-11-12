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
        One more edit to the comments
        2nd code refactoring in the comments
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(
            'Enter one of the following cities to analyse: chicago, new york city, washington:  ').lower()
        if city not in (CITY_DATA.keys()):
            print("Sorry, you did not enter a valid city option:\n")
            continue
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            'Enter the month you would like to analyse from jan to june (or "all"):  ').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        if month not in months:
            print("Sorry, you did not enter a valid month option:\n")
            continue
        else:
            break
    # get user input for day of week (all, monday, tuesdz`wway, ... sunday)
    while True:
        day = input(
            'Enter the day of week you would like to analyse (or "all"):  ').lower()
        days = ['monday', 'tuesday', 'wednesday','thursday', 'friday','all']
        if day not in days:
            print("Sorry, you did not enter a valid week day option:\n")
            continue
        else:
            break
    

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
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




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular month:', popular_month)

    # display the most common day of week
    df['weekday'] = df['Start Time'].dt.day_name()
    popular_dow = df['weekday'].mode()[0]
    print('Most common day of the week:', popular_dow)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start)

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end)

    # display most frequent combination of start station and end station trip
    
    df['combination'] = popular_start +" & "+ popular_end
    print('Most Popular Start and End Station combo is:', df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Trip duration is: {} minutes!'.format(total_time))
    
    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('\nMean Trip Duration is: {} minutes!'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    if 'Gender' in df:
    # Display counts of gender
        gender_types = df['Gender'].value_counts()
        print(gender_types)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        
        earliest = int(df['Birth Year'].min())    
        print('The earliest birth year is: {}'.format(earliest))
    
        most_recent = int(df['Birth Year'].max())
        print('The most recent birth year is: {}'.format(most_recent))
    
        most_common = int(df['Birth Year'].mode()[0])
        print('Most Common Birth Year is: {}'.format(most_common))

    else:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    while True:
        view_five = input('\nWould you like to see next 5 rows of data? Y/N:').lower()
        n = 0
        if view_five in ('y'):
            print(df.iloc[n:n+5])
            n += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
