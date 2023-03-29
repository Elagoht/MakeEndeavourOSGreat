from os import popen, system


def run_command(command, resultWidget):
    resultWidget.setStatus(int(popen(f"""statusfile=$(mktemp);
        xterm -bg black -fg green -e sh -c '{command}; echo $? > '$statusfile;
        cat $statusfile;
        rm $statusfile
    """).readline()))
