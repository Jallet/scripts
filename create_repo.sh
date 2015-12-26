#!/bin/sh
if [ $# -ne 1 ] && [ $# -ne 3 ]
then
    echo -e '[Usage]\ncreat_repo.sh [User] [password] [repo_name]\ncreate_repo.sh [repo_name]'
    exit
elif [ $# -eq 1 ]
then
    user=Jallet
    password=*yT.h@:7{j
    repo_name=$1
else
    user=$1
    password=$2
    repo_name=$3
fi

curl -u $user:$password https://api.github.com/user/repos -d {\"name\":\"$repo_name\"}

