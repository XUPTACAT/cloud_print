import  os
def lpr(filename,print_time=1):
    command = 'lpr ./'+filename+'-#'+str(print_time)
    try :
        result = os.popen(command)
    except Exception as e:
        print(e)
    #return  result


lpr('asd')