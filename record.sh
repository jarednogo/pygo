#!/bin/bash


if [ ! -n "$3" ]
then
    echo "Usage: $0 [user] [year] [pattern]"
    echo "Example: $0 jarstar 2017 Kobayashi"
    exit 1
fi

user="$1"
year="$2"
pattern="$3"
filename="$1-$2-$3.txt"
rm -rf $filename


for item in $(find -iname "*$user*.sgf")
do
    if [[ "$item" == *"$year"* ]]
    then
        #./pygo.py $item jarstar Chinese
        var=$(./pygo.py $item $user $pattern)
        match=$(echo $var | awk '{print $1}')
        win=$(echo $var | awk '{print $2}')
        if [[ "$match" == "True" ]]
        then
            echo "$item:$win" >> $filename
        fi
    fi
done

echo "Results written to $filename"

./analyze.py $filename
