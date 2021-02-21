import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#adding comment
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    city, month, day = "", "", ""

    while city not in ("chicago", "new york city", "washington"):
        city = input("Choose the city 'chicago', 'new york city', 'washington':\n")
        city = city.lower()

    while month not in ['All', 'January', 'February', 'March', 'April', 'May', 'June', 'July', \
                        'August', 'September', 'October', 'November', 'December']:
        month = input("Choice month: 'All', 'January', 'February'...'December'\n")

    while day not in ['All', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']:
        day = input("Choice day: ('All', 'Monday'... 'Sunday'\n")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    MONTH_DICT = {1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'July',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}

    DAYOFWEEK_DICT = {0: 'Monday',
                      1: 'Tuesday',
                      2: 'Wednesday',
                      3: 'Thursday',
                      4: 'Friday',
                      5: 'Saturday',
                      6: 'Sunday'}

    for key, value in CITY_DATA.items():
        if key == city:
            city = value

    data = pd.read_csv(city)
    df = data
    df['Start Time'] = pd.to_datetime(df["Start Time"], format='%Y-%m-%d %H:%M:%S')

    if day == "All" and month == "All":
        return df

    if day != "All":
        day = list(key for key, value in DAYOFWEEK_DICT.items() if value == day)
        day = str(day[0])

    if month != "All":
        month = list(key for key, value in MONTH_DICT.items() if value == month)
        month = str(month[0])

    if day == "All" and str(month) != "All":
        df = df[df["Start Time"].dt.month == int(month)]
    elif day != "All" and month == "All":
        df = df[df["Start Time"].dt.dayofweek == int(day)]
    elif day != "All" and month != "All":
        df = df[df["Start Time"].dt.dayofweek == int(day)]
        df = df[df["Start Time"].dt.month == int(month)]

    return df


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(f'The most common month: {df["Start Time"].dt.month.value_counts()[:1].sort_values(ascending=False)}')

    # TO DO: display the most common day of week
    print(f'The most common day of week: {df["Start Time"].dt.dayofweek.value_counts()[:1].sort_values(ascending=False)}')

    # TO DO: display the most common start hour
    print(f'The most common hour: {df["Start Time"].dt.hour.value_counts()[:1].sort_values(ascending=False)}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f'The most commonly used start station: {df["Start Station"].value_counts()[:1].sort_values(ascending=False)}')

    # TO DO: display most commonly used end station
    print(f'The most commonly used end station: {df["End Station"].value_counts()[:1].sort_values(ascending=False)}')

    # TO DO: display most frequent combination of start station and end station trip
    print(f"The most commonly used end station: {df.groupby(['Start Station','End Station']).size().idxmax()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    sum_ = sum.sum()
    print(f'Sum total travel time: {sum_}')

    # TO DO: display mean travel time

    len_ = len(sum)
    mean_ = sum_ / len_

    print(f"Mean travel time: {mean_}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"Counts of user types: {df.groupby(['User Type']).size()}")

    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print("Column 'Gender' doesn't exist")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)
        pass
    else:
        print(f"Counts of user types: {df.groupby(['Gender']).size()}")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print("Column 'Birth Year' doesn't exist")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)

    else:
        earliest_birth = df["Birth Year"].min()
        most_recent = df["Birth Year"].max()
        most_common_year = df["Birth Year"].value_counts().nlargest(n=1).values[0]

        print(most_common_year)
        print(f"The earliest birth year is: {earliest_birth}\n"
              f"The most recent birth year is: {most_recent}\n"
              f"The most common birth year is: {most_common_year}\n")

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

        print_data = 'yes'
        n = 0
        while print_data == 'yes':
            print_data = input("\nWould you like to show 5 rows of data? Enter yes or no.\n")
            print(df.iloc[n:n+5])
            n = n + 5


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
