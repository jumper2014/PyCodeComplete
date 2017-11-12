#!/bin/bash
cd ..
for folder in totoro cybertron phoebe jazz JaCodeComplete cherry zeus hera loki tapir thor breeze PyCodeComplete
        do
        	echo update $folder
        	cd $folder
            git pull
            cd ..
        done
