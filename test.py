#!/usr/bin/env python3
"""Unit test code"""
import sys
#sys.path.insert(0, '/home/pi/Projects/moqputils')
sys.path.insert(0, 'C:\\Users\\M738513\\Documents\\Projects\\moqputils-master')
#print (sys.path)
#from qso import *
from logfile import *
if __name__ == '__main__':

    """Test code goes here
    import sys
    print(sys.path)
    tt=dbQSO()
    print('dict:\n{}'.format(dir(tt)))
    print('vars:\n{}'.format(vars(tt)))
    print('keys:\n{}'.format(vars(tt).keys()))
    
    tt = dbQSO(qdata = '7074 FT8 2022-07-25 1715 N0SO -10 EM48 AB0RX -05 EM39')
    tt = dbQSO(qdata = {'FREQ':7074,
                        'MODE':'FT8',
                        'DATETIME': (2022, 7, 25, 17, 15),
                        'MYCALL':'N0SO',
                        'MYREPORT': -10,
                        'MYQTH':'EM48',
                        'URCALL':'AB0RX',
                        'URREPORT': -5,
                        'URQTH':'EM39',
                        'ID': 1,
                        'LOGID': 100,
                        'QSL': 300,
                        'VALID': 1,
                        'NOQSOS': 0,
                        'NOLOG': 1,
                        'DUPE': 0
                        })
#    tt = dbQSO(freq=7074)
    print ('populated tt:\n{}'.format(vars(tt)))"""
    wlog = logFile(fileName = 'W0MA.LOG')
    
    wlog.header.showh()
    #wlog.header.show()
    
    #for qso in wlog.qsolist:
    #        qso.show()
    
    header = wlog.extractQSOS()
    for l in header:
        print(l)

   
