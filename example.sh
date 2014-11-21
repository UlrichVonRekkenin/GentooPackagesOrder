if [ $UID -eq 0 ]
then

    # Usage: pua "pkg use1 use2 etc"
    function pua(){
        python3 order.py /etc/portage/package.use/custom "pkg use1 use2 etc"
    }

fi
