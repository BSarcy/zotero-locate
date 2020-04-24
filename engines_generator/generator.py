#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Modules externes
import sys
import os
import json

my_rep = "../engines_json"
engines_list = os.listdir(my_rep)
converted_engines_list = []
for engine in engines_list :
    file_engine = my_rep + "/" + engine
    print(file_engine)
    with open(file_engine, "r") as f_read:
        lst_dico = json.load(f_read)
        json_object = {}
        json_object["_name"] = lst_dico['title']
        json_object["_alias"] = lst_dico['title']
        json_object["country"] = "FR"
        json_object["_urlTemplate"] = lst_dico['linktemplate']
        json_object["_description"] = lst_dico['title'] + "search"
        json_object["_urlParams"] = []
        json_object["_hidden"] = False
        if lst_dico["icon"] :
            json_object["_icon"] = lst_dico['icon']
        json_object["_urlNamespaces"] = {
            "rft": "info:ofi/fmt:kev:mtx:journal",
            "z": "http://www.zotero.org/namespaces/openSearch#",
            "": "http://a9.com/-/spec/opensearch/1.1/"
            }
        converted_engines_list.append(json_object)
json_engines_file = open("engines.json", "w",  encoding='utf-8')
json_engines_file.write(json.dumps(converted_engines_list,indent=4))
json_engines_file.close
