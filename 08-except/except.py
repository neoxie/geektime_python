import sys

f = None
try:
    f = open('file.txt', 'r')
    # ....  # some data processing
except OSError as err:
    print('OS error: {}'.format(err))
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    if f is not None:
        f.close()
    
