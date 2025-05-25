#!/bin/bash

#file search
find / -name 'foobar*' > /tmp/list_foobar.txt
for path in $(cat /tmp/list_foobar.txt)

#Search Unit files
do
        if test -f $path; then
                Unit=$(grep "Unit" $path)
                name=$(basename "$path")
                if test -n "$Unit"; then

                        #reload unit, moving files
                        old_path="/opt/misc/${name}"
                        new_path="/srv/data/${name}"
                        mv $old_path $new_path
                        systemctl stop $path
                        sed -i 's/opt\/misc/srv\/data/g' $path
                        systemctl start $path
                fi
        fi
done

rm /tmp/list_foobar.txt