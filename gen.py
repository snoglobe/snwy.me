import sys
from shutil import copyfile
import fileinput

def genpage(page):
    template = ""
    replace = ""
    title = ""
    output = ""
    for line in page.split('\n'):
        if line != "" and line[0] == '~':
            if line[1:].partition('[')[0] == "template":
                template = line[line.find("[")+len("["):line.rfind("]")]
            elif line[1:].partition('[')[0] == "replace":
                replace = line[line.find("[")+len("["):line.rfind("]")]
            elif line[1:].partition('[')[0] == "title":
                title = line[line.find("[")+len("["):line.rfind("]")]
        elif line != "":
            tag = line[0:].partition('[')[0]
            content = line[line.find("[")+len("["):line.rfind("]")]
            output += "<%s>%s</%s>\n" % (tag, content, tag)
    copyfile(template, "%s.html" % (title))
    with fileinput.FileInput("%s.html" % (title), inplace=True) as file:
        for line in file:
            print(line.replace(replace, output), end="")

if __name__ == "__main__":
    page = open(sys.argv[1]).read()
    genpage(page)
