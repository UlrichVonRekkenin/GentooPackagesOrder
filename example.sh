if [ $UID -eq 0 ]
then

    # add to the /etc/portage/package.use/custom
    function pua(){
        python3 order.py /etc/portage/package.use/custom "pkg use1 use2 etc"
    }

fi
