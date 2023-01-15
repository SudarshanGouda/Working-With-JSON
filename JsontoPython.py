"""

json.loads(jsonstring) - process jsonstring to Python type

json.load(filePointer) - loads json from a file
                        and returns as a result of method Python type

"""

if __name__ == '__main__':

    from PythontoJson import movie

    #print(movie)

    import json

    encMovie=json.dumps(movie,ensure_ascii=False)

    print(encMovie)

##################################### loads #############################

    decMovie=json.loads(encMovie)

    print(decMovie)

#################################### load ##############################
# loads json from a file

    with open('sample.json','r',encoding='UTF-8') as file:

        DecMovie=json.load(file)

    print(DecMovie)