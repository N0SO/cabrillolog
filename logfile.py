#!/usr/bin/env python
from cabrillolog.qso import QSO
from cabrillolog.cabheader import cabrilloHeader
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
                    SOAPBOX)
                    
        self.fileName = fileName            
        self.qsoList = []
        self.rawlog = RAWLOG
        
        if (fileName):
            print('Filling from file {} ...'.format(fileName))
            self.header, self.qsolist = self.getLogFromFile(fileName)
        elif RAWLOG:
            print ('Filling from provided RAWLOG parameter ...')
            self.header, self.qsolist = self.parseRawLog(RAWLOG)
            
        self.nextQID = self.getqsoListLen()

    def getqsoListLen(self):
        return len(self.qsoList)
        
    def getLogFromFile(self, fileName):
        """
        Read the raw log file, then call parseRawLog to parse.
        """
        qsoutils = QSOUtils()
        rawlog = qsoutils.readFile(fileName, linesplit = False)
        if (rawlog == None):
            print('Error reading file {}'.format(fileName))
            return None, None
        self.RAWLOG = rawlog
        return self.parseRawLog(rawlog)
        
    def parseRawLog(self, rawlog):
        qsoutils = QSOUtils()        
        if ( not(qsoutils.IsThisACabFile(rawlog))):
            """Not a valid cab data!"""
            return None, None
        nheader = cabrilloHeader()
        nqsolist = []
        headertext = self.extractHeader(rawlog)
        #cabrilloTags = vars(header)
        #loglines = rawlog.splitlines()
        ln=0
        for line in headertext:
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
        
    def __testRawlog(self, rawlog):
        """
        Test passed parameter rawlog to see if it:
          1. Contains Data
          2. Is a string or a list
          
        If rawlog and self.RAWLOG are both None type, 
            return None to caller, 
        Else 
            if rawlog is a string 
                convert to list of lines 
        Return the list of lines
        """
        if (rawlog == None):
            rawlog = self.RAWLOG
        if rawlog == None:
            return None
        if isinstance(rawlog, str):
            return rawlog.splitlines()
        #else:
            #rawlog is already a list
        return rawlog
        
    def extractHeader(self, rawlog = None):
        """
        Extract and return a list containing just the header 
        lines from the rawlog string or list of lines. 
        
        Skip leading blank lines.
        """
        loglines = self.__testRawlog(rawlog)
        if loglines == None:
            return None
        rawlog = loglines
        header = None
        headerFound = False
        ln = 0
        for line in rawlog:
            ln+=1
            if headerFound:
                if line.upper().startswith('QSO:'):
                    break # End of header
                else:
                    header.append(line)
            else:
                if line.upper().startswith('START-OF-LOG:'):
                    header = [line]
                    headerFound = True
        return header  

    def extractQSOS(self, rawlog=None):
        """
        Extract and return a list of the QSO: lines from the
        rawlog data provided, or None type if no QSOs
        """
        loglines = self.__testRawlog(rawlog)
        if loglines == None:
            return None
        rawlog = loglines

        qsolist = []
        qsosFound = False
        for line in loglines:
            if line.upper().startswith('QSO:'):
                qsosFound = True
                qsolist.append(line)
        if qsosFound:
            return qsolist
        else:
            return None

if __name__ == '__main__':
    wlog = logFile(fileName = 'W0MA.LOG')
    
    #wlog.header.showh()
    wlog.header.show()
    
    for qso in wlog.qsolist:
            qso.show()
  
