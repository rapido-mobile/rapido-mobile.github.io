#!/usr/bin/env python
import os, sys

classes = [
    "AddDocumentFloatingActionButton",
    "DocumentActionsButton",
    "DocumentForm",
    "DocumentList",
    "DocumentListMapView",
    "DocumentListScaffold",
    "DocumentListSortButton",
    "DocumentListView",
    "DocumentPage",
    "TypedInputField",
    "SortOrder"
]

url_base = "https://pub.dartlang.org/documentation/rapido/latest/documents/"
url_tail = "-class.html"

for each c in classes:
    stext = " " + c + " " 
    rtext = url_base + c + url_tail
    input = sys.stdin
    output = sys.stdout
    if nargs > 3:
        input = open(sys.argv[3])
    if nargs > 4:
        output = open(sys.argv[4], 'w')
    for s in input.xreadlines(  ):
        output.write(s.replace(stext, rtext))
    output.close(  )
    input.close(  )