import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
filter_data=["month","day","none", "both"]
month_data={"january" : 1,
            "february": 2,
            "march": 3,
            "april": 4,
            "may": 5,
            "june": 6,
            "all": "all"}
day_data=["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday","all"]



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
    while True:
        city=input("Please select a city, either Chicago, New York City or Washington:  ").lower()
        if city not in CITY_DATA.keys():
            print("Invalid input, please choose from the specified cities")
        else:
            break
   # TO DO: get user input for either filtering data by month, day, both or none
    while True:
         filter=input("Please select if you want to filter data by month, day, both or none: ").lower()
         if filter=="none":
            day="all"
            month="all"
            break
         elif filter not in filter_data:
                print("Invalid input, please input  month,  day, both or none")
         else:
              break
    # TO DO: get user input for month (all, january, february, ... , june)
    while filter=="month" or filter=="both":
        if filter=="month" or "both":
            month=input("Please select the month as January, February, March, April, May or June or select all: ").lower()
            day="all"
            if month not in month_data.keys():
                print("Invalid input, please input the month or select All")
            else:
                break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while filter=="day" or filter=="both":
        if filter=="day" or "both":
            day=input("Please select the day as Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday or select all: ").lower()
            month="all"
            if day not in day_data:
                     print("Invalid input, please input the day or select all")
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] =df['Start Time'].dt.month
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]



    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    print (df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month

    most_common_month=df['month'].mode()[0]
    print("Most Common travel Month: ",most_common_month)
    print("NB: 1 is January, 2 is February, 3 is March, 4 is April, 5 is May and 6 is June")


    # TO DO: display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print("Most Common travel Day: ",most_common_day)


    # TO DO: display the most common start hour
    df["hour"] =df["Start Time"].dt.hour
    most_common_hour=df["hour"].mode()[0]
    print("Most Common travel hour: ",most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df["Start Station"].mode()[0]
    print("Most Common travel start station: ",most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station=df["End Station"].mode()[0]
    print("Most Common travel end station: ",most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df["Start-End"]=df["Start Station"].str.cat(df["End Station"],sep= " to ")
    combine=df["Start-End"].mode()[0]
    print("Most Common travel start station and end station combination: ",combine)
    print("Most Common travel start station and end station combination: From ",combine)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration=df["Trip Duration"].sum()
    total_trip_duration_minutes=total_trip_duration/60
    print("Total trip duration:{} minutes ".format(total_trip_duration_minutes))

    # TO DO: display mean travel time
    mean_trip_duration=df["Trip Duration"].mean()
    mean_trip_duration_minutes=mean_trip_duration/60
    print("Average travel time:{} minutes".format(mean_trip_duration_minutes))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df["User Type"].value_counts()
    print("Types and numbers of users are: ",user_types)


    # TO DO: Display counts of gender
    try:
        user_gender=df["Gender"].value_counts()
        print("Types and numbers of users are: ",user_gender)
    except:
        print(" No User Gender Data available for Washington")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_bday=df["Birth Year"].min()
        print("Users earliest Birthday year: ", int(earliest_bday))
        recent_bday=df["Birth Year"].max()
        print("Users most recent Birthday year: ", int(recent_bday))
        common_bday=df["Birth Year"].mode()[0]
        print("Users most common Birthday year: ", int(common_bday))
    except:
        print(" No User Birth Year Data available for Washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays raw data upon user request"""
    counter=0
    real_data=" "
    real_response=["yes","no"]
    while real_data not in real_response:
        print("Do you wish to see raw data? Yes or No?")
        real_data=input().lower()
        if real_data=="yes":
            print(df.head())
            real_data2=input("Do you want to see more raw data? Yes or No?  ").lower()
        elif real_data not in real_response:
            print("Please submit valid input, either Yes or No")
            real_data=input().lower()
    while real_data=="yes":
        print("Do you wish to view more data?")
        real_data=input().lower()
        counter+=5
        if real_data=="yes":
            print(df[counter:counter+5])
        elif real_data not in real_response:
            print("Please submit valid input, either Yes or No")
            real_data=input().lower()
    print('-'*40)




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
