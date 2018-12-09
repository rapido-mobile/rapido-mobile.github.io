#!/usr/bin/env python
import os
import sys

classes = [
    "AddDocumentFloatingActionButton",
    "DocumentActionsButton",
    "DocumentForm",
    "DocumentListMapView",
    "DocumentListScaffold",
    "DocumentListSortButton",
    "DocumentListView",
    "DocumentPage",
    "TypedInputField",
    "SortOrder",
    "DocumentList",
]

url_base = "https://pub.dartlang.org/documentation/rapido/latest/documents/"
url_tail = "-class.html"

input = sys.stdin
output = sys.stdout
input = open(sys.argv[1])
output = open(sys.argv[2], 'w')
for line in input.xreadlines():
    for c in classes:
        rtext = " [" + c + "](" + url_base + c + url_tail + ")"
        rtext1 = " [" + c + "](" + url_base + c + url_tail + "). "
        rtext2 = " [" + c + "](" + url_base + c + url_tail + "), "
        rtext3 = "[" + c + "](" + url_base + c + url_tail + ")"

        stext = " " + c + " "
        stext1 = " " + c + ". "
        stext2 = " " + c + ", "

        line = line.replace(stext, rtext)
        line = line.replace(stext1, rtext1)
        line = line.replace(stext2, rtext2)

        if(line.find(c) == 0):
            line = line.replace(c, rtext3, 1)
    output.write(line)
output.close()
input.close()
