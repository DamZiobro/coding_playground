#! /bin/bash
#
# bash_tests.sh
# Copyright (C) 2015 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.
#


#for loop example 

echo -e "========================================================="
echo -e "for loop test "
echo -e "========================================================="

for i in `seq 10 20`;
do 
    echo "for loop step $i "
done 


echo -e "========================================================="
echo -e "while loop test "
echo -e "========================================================="
i=10; 
while [ $i -lt 20 ];
do 
    echo "while loop step $i "
    i=$(($i+1))
done 


echo -e "========================================================="
echo -e "if condition for numbers test "
echo -e "========================================================="

a=10 
b=10 
if [ $a -eq $b ];
then 
    echo "$a is equal $b"
fi 

echo -e "========================================================="
echo -e "if condition for strings test "
echo -e "========================================================="

string1="test"
string2="test2"
if [ $string1 == $string2 ];
then 
    echo "$string1 is equal $string2"
else 
    echo "$string1 is not equal $string2"
fi

echo -e "========================================================="
echo -e "multicondition-based if condition test "
echo -e "========================================================="

if [ $a -eq $b ] && [ $string1 == $string2 ];
then 
    echo "$a is equal $b and $string1 is equal $string2"
elif [ $a -eq $b ];
then
    echo "$a is equal $b" 
else 
    echo "Nothing equal"
fi

echo -e "========================================================="
echo -e "variables test"
echo -e "========================================================="

hello="Hello world"
echo hello  
echo $hello


echo -e "========================================================="
echo -e "case statement test  "
echo -e "========================================================="

case $a in 
    10) echo "a is equal 10";;
    20) echo "a is equal 20";; 
    * ) echo "a is not equal 10 or 20";;
esac
        

echo -e "========================================================="
echo -e "find substring in string  "
echo -e "========================================================="

string="Linux"
substring="inu"

if echo $string | grep -q $substring 
then
    echo "$substring is in $string"
else    
    echo "$substring is NOT in $string"
fi

echo -e "========================================================="
echo -e "check if file exist"
echo -e "========================================================="

file="/tmp/test.txt"
if [ -e "$file" ] 
then
    echo "$file exists"
else    
    echo "$file does not exists"
fi

echo -e "========================================================="
echo -e "check if variable is set"
echo -e "========================================================="

if [ -z "$file2" ] 
then
    echo "variable \$file2 NOT set"
else    
    echo "variable \$file2 set to value $file2"
fi


echo -e "========================================================="
echo -e "check file extension"
echo -e "========================================================="

touch $file
if [ ${file##*.} != "txt" ] 
then
    echo "file $file2 is NOT .txt file"
else    
    echo "file $file2 is .txt file"
fi

echo -e "========================================================="
echo -e "variables examples "
echo -e "========================================================="

echo -e "\$HOME = $HOME"
echo -e "\$HOSTNAME = $HOSTNAME"
echo -e "\$BASH = $BASH"
echo -e "\$BASH_VERSION = $BASH_VERSION"
echo -e "\$EDITOR = $EDITOR"
echo -e "\$HOSTTYPE = $HOSTTYPE"
echo -e "\$MACHTYPE = $MACHTYPE"
echo -e "\$OLDPWD = $OLDPWD"
echo -e "\$OSTYPE = $OSTYPE"
echo -e "\$PATH = $PATH"
echo -e "\$PS1 = $PS1"
echo -e "\$PWD = $PWD"
echo -e "\$UID = $UID"
echo -e "\$LOGNAME = $LOGNAME"

echo -e "========================================================="
echo -e "getopts examples "
echo -e "========================================================="

while getopts a:b:h  flag
do
    case $flag in
    a ) echo -e "a variable set to: $OPTARG"
    ;;
    b ) file="$OPTARG"
        echo -e "b variable set to $file"
    ;;
    h ) E_BADARGS=65
        echo "Usage: `basename $0` argument"
        exit $E_BADARGS
    ;;
    esac
done
shift $(($OPTIND - 1))
     
echo -e "========================================================="
echo -e "date/time manipulation examples + printf formatting"
echo -e "========================================================="

printf "Today is %dth day of year %d\n" "`date +%j`" "`date +%Y`"
cal #prints calendar

echo -e "========================================================="
echo -e "wc command usage example"
echo -e "========================================================="

file=/usr/share/dict/words 
printf "File %s contains %s characters %s words and %s lines of text.\n" $file "`cat $file | wc -c `" "`cat $file | wc -w `" "`cat $file | wc -l `"

echo -e "========================================================="
echo -e "print message and exit test"
echo -e "========================================================="
rm /tmp/aaaaa/aaaaa || { echo -e "Error during command. Exiting..."; exit -1; }
echo -e "After test..."

echo "test" || { echo -e "test"; exit -1; }


