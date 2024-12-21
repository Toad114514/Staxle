import os, json
# i18n Lang

class i18n:
    path=os.path.join(os.getcwd(), "core", "i18n", "i18n")
    version=109

def get(ids):
    with open(os.path.join("core","config","lang"),"r") as f:
        lang=f.read()
    try:
        with open(os.path.join(i18n.path, lang),"r") as f:
            langs=f.read()
        langs=json.loads(langs)
        if langs["language_version"] < i18n.version:
            return "i18nFileOld"
        try:
            return str(langs["i18n"][ids])
        except KeyError:
            return "None"
    except Exception as strd:
        return "json/fileError:: "+str(strd)

def out(ids):
    with open(os.path.join("core","config","lang"),"r") as f:
        lang=f.read()
    try:
        with open(os.path.join(i18n.path, lang),"r") as f:
            langs=f.read()
        langs=json.loads(langs)
        if langs["language_version"] < i18n.version:
            print("i18nFileOld")
        try:
            print(str(langs["i18n"][ids]))
        except KeyError:
            print("None")
    except Exception as strd:
        print("json/fileError:: "+str(strd))