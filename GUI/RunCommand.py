from os import popen, system
from Result import ResultWidget


def run_command(command: str, resultWidget: ResultWidget):
    result = popen(f"""statusfile=$(mktemp);
        xterm -bg black -fg green -e sh -c '{command}; echo $? > '$statusfile 2> /dev/null;
        cat $statusfile;
        rm $statusfile
    """).readline()
    if result == "":
        result = -1
    resultWidget.setStatus(int(result))
