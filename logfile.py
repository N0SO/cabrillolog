#!/usr/bin/env python3
from qso import QSO
from cabheader import cabrilloHeader
import sys, os.path

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
                    SOAPBOX=None):
                        
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
                    
        self.fileName = None            
        self.qsoList = []
        self.rawlog = None
        
        if (fileName):
            if (isinstance(fileName, str)):
                if ( os.path.exists(fileName) and \
                        (os.path.isfile(fileName) == True) ):
                    print('Filling from file {} ...'.format(fileName))
                    self.header, self.qsoList = \
                        self.getLogFromFile(fileName)
                    self.fileName =fileName
                elif (len(fileName) < 10):
                    print('Filling from DB call {} ...'.format(fileName))
                    self.header, self.qsoList = \
                                self.getLogfromDB(fileName)
                    self.fileName = fileName
                elif fileName.upper.startswith('START-OF-LOG:'):
                    self.rawlog = fileName

            elif ( (isinstance(fileName, list)) or self.rawlog ):
                print ('Filling from provided RAWLOG parameter ...')
                self.header, self.qsolist = \
                                self.parseRawLog(fileName)
                self.rawlog = fileName
        self.nextQID = self.getqsoListLen()

    def getqsoListLen(self):
        return len(self.qsoList)
        
    def getLogFromFile(self, fileName):
        """
        Read the raw log file, then call parseRawLog to parse.
        """
        from cabrilloutils.qsoutils import QSOUtils
        qsoutils = QSOUtils()
        rawlog = qsoutils.readFile(fileName, linesplit = False)
        if (rawlog == None):
            print('Error reading file {}'.format(fileName))
            return None, None
        self.RAWLOG = rawlog
        return self.parseRawLog(rawlog)

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
        from multicounty.multicounty import multiCounty
        loglines = self.__testRawlog(rawlog)
        if loglines == None:
            return None
        rawlog = loglines

        qsolist = []
        qsosFound = False
        for line in loglines:
            if line.upper().startswith('QSO:'):
                qsosFound = True
                mc=multiCounty(line) # Expand county line QSOs
                if (mc.isMulti()):
                    for i in mc.qsoList:
                        qsolist.append(i)
                else:
                    qsolist.append(mc.qsoText)

        if qsosFound:
            return qsolist
        else:
            return None

    def __sortqs(self, e):
        return e.qtime
            
    def __buildqsoList(self, qlist):
        qs = []
        for q in qlist:
            qso = QSO(qdata=q)
            if qso:
                qs.append(qso)
        qid=0
        qcount = len(qs)
        #Sort qsos by date/time
        qs.sort(key=self.__sortqs)
        #Assign qso ID
        for i in range(qcount):
                qs[i].id = qid
                self.qsoList.append(qs[i])
                qid += 1
        return len(self.qsoList)
            
    def parseRawLog(self, rawlog):
        loglines = self.__testRawlog(rawlog)
        if loglines == None:
            return None, None
        #rawlog = loglines
        headerlist = self.extractHeader(loglines)
        self.header.parseHeader(headerlist)
        
        qlist = self.extractQSOS(loglines)
        #print(qlist)
        self.__buildqsoList(qlist)
        return self.header, self.qsoList
    
    def PrettyPrint(self, log=None):
        """
        Returns log data as a list suitable for printing.
        """
        if log==None:
            log=self
        logData = log.header.prettyprint()
        for qso in log.qsoList:
            logData.append(qso.makeTSV())
        return logData

    def getLogfromDB(self, call):
        from moqputils.moqputils.moqpdbutils import MOQPDBUtils
        from moqputils.moqputils.configs.moqpdbconfig import HOSTNAME, USER, PW,\
                                                    DBNAME
        mydb = MOQPDBUtils(HOSTNAME, USER, PW, DBNAME)
        mydb.setCursorDict()
        headerdata = mydb.fetchLogHeader(call)
        #print (headerdata[0])
        self.header.parseHeader(headerdata[0])
        #print (self.header.getHeader())
        qsos = mydb.ptheseqsos = mydb.read_pquery(\
            "SELECT * FROM `QSOS` WHERE ( `LOGID` = %s )",
                [self.header.ID])
        self.qsoList = []
        for qso in qsos:
            self.qsoList.append(QSO(qdata=qso))
        return self.header, self.qsoList
            

        
       
