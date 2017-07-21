import os
import subprocess
import tempfile
import logging


main_vim_path = os.path.join(
    os.path.dirname(__file__),
    "main.vim"
)


def pick(
        options,
        header_filter=lambda x: x,
        body_filter=None,
        match_filter=lambda x: x
        ):
    temp_file = tempfile.mktemp()
    fd = open(temp_file, "w+")
    fd.write("# Put your cursor on a line and press enter to pick")
    headers = [
        header_filter(d) for d in
        options
    ]
    for header in headers:
        fd.write(header+"\n")
    process = os.popen(
        " ".join(["vim", "-S", main_vim_path, "-R", temp_file])
    )
    print(process.read())


class Gui(object):


    def __init__(self):
        self.documents = []
        self.logger = logging.getLogger("gui:vim")
        self.main_vim_path = main_vim_path


    def main(self, documents):
        temp_file = tempfile.mktemp()
        self.logger.debug("Temp file = %s" % temp_file)

        fd = open(temp_file, "w+")
        for doc in documents:
            fd.write(doc["title"] + "\n")
        fd.close()

        subprocess.call(
                ["vim", "-S", self.main_vim_path, "-R", temp_file]
        )