if [ $UID -eq 0 ]
then

    puc function(){
        FILE=/etc/portage/package.use/custom
        echo $1 >> $FILE
        echo "Adding" $1 "to the end of '$FILE'"

        python 'order.py' $FILE
        echo "Reordering the" $FILE
    }

fi
