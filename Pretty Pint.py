"""
pretty print (pprint)
"""

if __name__ == '__main__':

    from PythontoJson import movie

    #print(movie)

    import json
################################# indent #################################

    encMovie=json.dumps(movie,ensure_ascii=False,indent=5)

    print(encMovie)

##################################### Sort_keys #############################
### Sort by names of key

    encMovie=json.dumps(movie,ensure_ascii=False,indent=5,sort_keys=True)

    print(encMovie)


    with open('sample.json','w',encoding="UTF-8") as file:
        json.dump(movie,file,ensure_ascii=False,indent=5,sort_keys=True)

##################################### pprint #############################
### Pretty print

    import pprint

    with open('new.json','w',encoding="UTF-8") as file:
        json.dump(movie,file,ensure_ascii=False)

    with open('new.json','r',encoding='UTF-8') as file:
        new=json.load(file)

    pprint.pprint(new)