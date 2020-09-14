##!/bin/bash

read -p "Choose a file to commit: " -r file
git add $file
git status
read -p "If you would prefer to continue? (Y/N) ->" -r response
if [ "$response" = "N" ]; then
    exit 1
fi

if [ "$response" = 'Y' ]; then
    read -p "leave your commit message: ->" -r message
    git commit -m "$message"
    git status
    read -p "If you would prefer to continue? (Y/N) ->" -r response
    if [ $response = "N" ]; then
        exit 1
    fi
    if [ $response = 'Y' ]; then
        git push
    fi
fi
