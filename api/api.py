from os import path


#get drum api version
def drumver():
  return "drum bash py api 0.0.1"



# create a file. returns int as error code
def createfile(create):
  try:
    f = open(create, "x")
    f.close()
    # return 0 for no error
    return 0
  except:
    # return 1 for error
    return 1




# check if a file exists. reurns bool
def filecheck(check):
  return path.exists(check)
