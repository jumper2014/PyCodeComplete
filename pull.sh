#!/bin/bash
cd ..
for folder in JaCodeComplete cherry zeus hera loki tapir thor breeze PyCodeComplete
        do
        	echo update $folder
        	cd $folder
            git pull
            cd ..
        done
