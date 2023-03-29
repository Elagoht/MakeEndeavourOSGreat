from os import popen


def aur_helper():
    return popen("""if [ -f /bin/paru ]; then
    aurhelper="/bin/paru"
elif [ -f /bin/yay ]; then 
    aurhelper="/bin/yay"
else
    aurhelper=""
fi
echo $aurhelper""").readline().replace("\n", "")


def has_aur_helper():
    return aur_helper() != ""
