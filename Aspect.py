__author__ = 'Benni'

aspects = {
    "aer" :           { "color": 16777086,   "composition": [       ] },
    "terra":          { "color": 5685248,    "composition": [       ] },
    "ignis":          { "color": 16734721,   "composition": [       ] },
    "aqua":           { "color": 3986684,    "composition": [       ] },
    "ordo":           { "color": 14013676,   "composition": [       ] },
    "perditio":       { "color": 4210752,    "composition": [       ] },
    "vacuos":         { "color": 8947848,    "composition": [ "aer",            "perditio"     ] },
    "lux":            { "color": 16774755,   "composition": [ "aer",            "ignis"        ] },
    "potentia":       { "color": 12648447,   "composition": [ "ordo",           "ignis"        ] },
    "motus":          { "color": 13487348,   "composition": [ "aer",            "aqua"         ] },
    "saxum":          { "color": 8421504,    "composition": [ "terra",          "terra"        ] },
    "victus":         { "color": 14548997,   "composition": [ "aqua",           "terra"        ] },
    "gelum":          { "color": 14811135,   "composition": [ "aqua",           "ordo"         ] },
    "tempestas":      { "color": 16777215,   "composition": [ "aer",            "gelum"        ] },
    "vitreus":        { "color": 8454143,    "composition": [ "saxum",          "aqua"         ] },
    "mortuus":        { "color": 8943496,    "composition": [ "victus",         "perditio"     ] },
    "volatus":        { "color": 15198167,   "composition": [ "aer",            "motus"        ] },
    "tenebrae":       { "color": 2236962,    "composition": [ "vacuos",         "lux"          ] },
    "spiritus":       { "color": 15461371,   "composition": [ "victus",         "mortuus"      ] },
    "sano":           { "color": 16723764,   "composition": [ "victus",         "victus"       ] },
    "iter":           { "color": 14702683,   "composition": [ "motus",          "terra"        ] },
    "venenum":        { "color": 9039872,    "composition": [ "aqua",           "mortuus"      ] },
    "alienis":        { "color": 8409216,    "composition": [ "vacuos",         "tenebrae"     ] },
    "praecantatio":   { "color": 9896128,    "composition": [ "vacuos",         "potentia"     ] },
    "auram":          { "color": 16761087,   "composition": [ "praecantatio",   "aer"          ] },
    "vitium":         { "color": 8388736,    "composition": [ "praecantatio",   "perditio"     ] },
    "granum":         { "color": 15638894,   "composition": [ "victus",         "ordo"         ] },
    "limus":          { "color": 129024,     "composition": [ "victus",         "aqua"         ] },
    "herba":          { "color": 109568,     "composition": [ "granum",         "terra"        ] },
    "arbor":          { "color": 8873265,    "composition": [ "aer",            "herba"        ] },
    "bestia":         { "color": 10445833,   "composition": [ "motus",          "victus"       ] },
    "corpus":         { "color": 15615885,   "composition": [ "mortuus",        "bestia"       ] },
    "exanimis":       { "color": 3817472,    "composition": [ "motus",          "mortuus"      ] },
    "cognitio":       { "color": 16761523,   "composition": [ "terra",          "spiritus"     ] },
    "sensus":         { "color": 1038847,    "composition": [ "aer",            "spiritus"     ] },
    "humanus":        { "color": 16766912,   "composition": [ "bestia",         "cognitio"     ] },
    "messis":         { "color": 14791537,   "composition": [ "herba",          "humanus"      ] },
    "metallum":       { "color": 11908557,   "composition": [ "saxum",          "ordo"         ] },
    "perfodio":       { "color": 14471896,   "composition": [ "humanus",        "saxum"        ] },
    "instrumentum":   { "color": 4210926,    "composition": [ "humanus",        "ordo"         ] },
    "meto":           { "color": 15641986,   "composition": [ "messis",         "instrumentum" ] },
    "telum":          { "color": 12603472,   "composition": [ "instrumentum",   "perditio"     ] },
    "tutamen":        { "color": 49344,      "composition": [ "instrumentum",   "terra"        ] },
    "fames":          { "color": 10093317,   "composition": [ "victus",         "vacuos"       ] },
    "lucrum":         { "color": 15121988,   "composition": [ "humanus",        "perditio"     ] },
    "fabrico":        { "color": 8428928,    "composition": [ "humanus",        "instrumentum" ] },
    "pannus":         { "color": 15395522,   "composition": [ "instrumentum",   "bestia"       ] },
    "machina":        { "color": 8421536,    "composition": [ "motus",          "instrumentum" ] },
    "vinculum":       { "color": 10125440,   "composition": [ "motus",          "perditio"     ] },
    "permutatio":     { "color": 5735255,    "composition": [ "motus",          "aqua"         ] },
}

def makeGraph():
    graph = {}
    for aspect in aspects:
        if aspect not in graph:
            graph[aspect] = []
        for compound in aspects[aspect]["composition"]:
            if compound not in graph:
                graph[compound] = []
            graph[compound].append(aspect)
            graph[aspect].append(compound)
    return graph

def findPaths(graph, aspect, dest, length, path = None):
    if path is None:
        path = []
    path = path + [aspect]
    pathlist = []
    if length <= 0:
        return pathlist
    if aspect == dest:
        return [path]
    for compound in graph[aspect]:
        #if compound not in path:
        newpaths = findPaths(graph, compound, dest, length-1, path)
        for newpath in newpaths:
            pathlist.append(newpath)
    return pathlist



if __name__ == "__main__":
    from pprint import pprint
    graph = makeGraph()
    pprint (findPaths(graph, "cognitio", "herba", 5))