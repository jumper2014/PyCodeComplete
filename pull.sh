#!/bin/bash
cd ..
for folder in zeus hera loki tapir thor breeze PyCodeComplete
        do
        	echo update $folder
        	cd $folder
            git pull
            cd ..
        done
