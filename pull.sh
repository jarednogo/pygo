#!/bin/bash

# This will retrieve a zip file of kgs games

START_YEAR='2017'
END_YEAR='2017'
START_MONTH='1'
END_MONTH='12'

# $1 should be the name of a KGS user
if [ -n "$1" ]
then
    if [ -n "$2" ]
    then
        START_YEAR="$2"
    fi
    if [ -n "$3" ]
    then
        END_YEAR="$3"
    fi
    if [ -n "$4" ]
    then
        START_MONTH="$4"
    fi
    if [ -n "$5" ]
    then
        END_MONTH="$5"
    fi

    for year in $(seq $START_YEAR $END_YEAR)
    do
        for month in $(seq $START_MONTH $END_MONTH)
        do
            wget https://www.gokgs.com/servlet/archives/en_US/$1-all-$year-$month.zip
            sleep 5
        done
    done
else
    echo "Usage: $0 [kgs username] [START_YEAR] [END_YEAR] [START_MONTH] [END_MONTH]"
    echo "START_YEAR and END_YEAR default to 2017"
    echo "START_MONTH defaults to 1"
    echo "END_MONTH defaults to 12"
fi
