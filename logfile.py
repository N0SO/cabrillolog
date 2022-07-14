#!/usr/bin/env python
from cablog.qso import QSO
from cablog.cabheader import cabrilloHeader
from cabrilloutils.qsoutils import QSOUtils

class logFile():
    def __init__(self,
                    fileName = None,
                    START_OF_LOG=None,
                    END_OF_LOG=False,
                    CALLSIGN=None,
                    CONTEST=None,
                    CATEGORY_ASSISTED=False,
                    CATEGORY_BAND=None,
                    CATEGORY_MODE=None,
                    CATEGORY_OPERATOR=None,
                    CATEGORY_POWER=None,
                    CATEGORY_STATION=None,
                    CATEGORY_TIME=None,
                    CATEGORY_TRANSMITTER=None,
                    CATEGORY_OVERLAY=None,
                    CERTIFICATE=False,
                    CLAIMED_SCORE=0,
                    CLUB=None,
                    CREATED_BY=None,
                    EMAIL=None,
                    GRID_LOCATOR=None,
                    LOCATION=None,
                    NAME=None,
                    ADDRESS=None,
                    ADDRESS_CITY=None,
                    ADDRESS_STATE_PROVINCE=None,
                    ADDRESS_POSTALCODE=None,
                    ADDRESS_COUNTRY=None,
                    OPERATORS=None,
                    OFFTIME=None,
                    SOAPBOX=None,
                    RAWLOG=None):
                        
        self.header = cabrilloHeader(\
                    START_OF_LOG,
                    END_OF_LOG,
                    CALLSIGN,
                    CONTEST,
                    CATEGORY_ASSISTED,
                    CATEGORY_BAND,
                    CATEGORY_MODE,
                    CATEGORY_OPERATOR,
                    CATEGORY_POWER,
                    CATEGORY_STATION,
                    CATEGORY_TIME,
                    CATEGORY_TRANSMITTER,
                    CATEGORY_OVERLAY,
                    CERTIFICATE,
                    CLAIMED_SCORE,
                    CLUB,
                    CREATED_BY,
                    EMAIL,
                    GRID_LOCATOR,
                    LOCATION,
                    NAME,
                    ADDRESS,
                    ADDRESS_CITY,
                    ADDRESS_STATE_PROVINCE,
                    ADDRESS_POSTALCODE,
                    ADDRESS_COUNTRY,
                    OPERATORS,
                    OFFTIME,
                    SOAPBOX,
                    RAWLOG)
                    
        self.fileName = fileName            
        self.qsoList = []
        
        if (fileName):
            print('Filling from file {}'.format(fileName))
            self.header, self.qsolist = self.getLogFromFile(fileName)
        self.nextQID = self.getqsoListLen()

    def getqsoListLen(self):
        return len(self.qsoList)
        
    def getLogFromFile(self, fileName):
        qsoutils = QSOUtils()
        rawlog = qsoutils.readFile(fileName, linesplit = False)
        if (rawlog == None):
            print('Error reading file {}'.format(fileName))
            return None, None
        if ( not(qsoutils.IsThisACabFile(rawlog))):
            """Not a valid cab file!"""
            return None, None
        nheader = cabrilloHeader(RAWLOG=rawlog)
        nqsolist = []
        #cabrilloTags = vars(header)
        loglines = rawlog.splitlines()
        ln=0
        for line in loglines:
            ln+=1
            uline = line.strip().upper()
            #print ('uline ={} - LEN={}'.format(uline, len(uline)))
            cabparts = uline.split(':',1)
            #print (len(cabparts))
            if(len(cabparts)<2):
                print('Skipping line {}: {}'.format(ln, line))
            else:
                cabtag = cabparts[0]
                cabdata = cabparts[1]
                #print('{}, {}'.format(cabtag, cabdata))
                if (cabtag == 'QSO'):
                    qso = QSO(qdata=cabdata)
                    if (qso):
                        nqsolist.append(qso)
                else:
                    gcabtag = nheader.setTagData(cabtag, cabdata)
                    if gcabtag == False:
                        print('Header tag {} at line {} unknown.'.\
                                format(line, ln))
            
        return nheader, nqsolist

if __name__ == '__main__':
    wlog = logFile(fileName = 'W0MA.LOG')
    
    #wlog.header.showh()
    wlog.header.show()
    
    for qso in wlog.qsolist:
            qso.show()
  
