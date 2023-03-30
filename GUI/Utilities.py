from os import popen
from Result import ResultWidget


def run_command(command: str, result_widget: ResultWidget):
    result = popen(f"""statusfile=$(mktemp);
        xterm -bg black -fg green -e sh -c '{command}; echo $? > '$statusfile 2> /dev/null;
        cat $statusfile;
        rm $statusfile
""").readline()
    if result == "":
        result = -1
    result_widget.setStatus(int(result))


def aur_helper():
    return popen("""if [ -f /bin/paru ]; then
    aurhelper="/bin/paru"
elif [ -f /bin/yay ]; then
    aurhelper="/bin/yay"
else
    aurhelper=""
fi
echo $aurhelper""").readline().strip()


def has_aur_helper():
    return aur_helper() != ""


def install_if_doesnt_have(package: str, result_widget: ResultWidget):
    run_command(
        f"""if [ ! "$(pacman -Qqs {package})" = "{package}" ]
    then {aur_helper()} -S {package}
fi""" if has_aur_helper() else "false", result_widget)
