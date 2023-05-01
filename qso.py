#!/usr/bin/env python3
from cabrilloutils.qsoutils import QSOUtils
from headerdefs import QSODEFS, DBQSODEFS        

MAXELEMENTS=10 # Number of QSO elements in a log file line
  

class QSO():
    def __init__(   self,
                    freq=None,
                    mode=None,
                    qtime=None,
                    mycall=None,
                    myrst=None,
                    myqth=None,
                    urcall=None,
                    urrst=None,
                    urqth=None,
                    valid=False,
                    dupe=False,
                    note=False,
                    id=None,
                    logid=None,
                    qsl=None,
                    nolog=False,
                    noqsos=False,
                    qdata = None):
                        
        """ Set any passed in values """
        self.freq=freq
        self.mode=mode
        self.qtime=qtime
        self.mycall=mycall
        self.myrst=myrst
        self.myqth=myqth
        self.urcall=urcall
        self.urrst=urrst
        self.urqth=urqth
        self.valid=valid
        self.dupe=dupe
        self.note=note
        self.id=id
        self.logid=logid
        self.qsl=qsl
        self.nolog=nolog
        self.noqsos=noqsos

        if (qdata):
            self.parseQSO(qdata)
        
    def parseQSO(self, fdata):
        """
        Parse QSO data from a log file if fdata is tring.
        Populate qso data elements from fdata. Expected format:
            string 'QSO: ' (skipped if present)
            freq (in KHz)
            mode
            date (yyyy-mm-dd)
            time (hhmm in UTC)
            mycall (station making qso)
            myrst
            myqth
            urcall (station qso was with)
            urrst
            urqth
        All elements separated by whitespace.
        This works for the Missouri QSO Party.

        Needs error checking added!

        Skip this and pass fdata to parseQSOdb if
        fdata is type dict().
        """
        if isinstance(fdata, dict):
            #print('dict()')
            #call parseQSOdb
            self.parseQSOdb(fdata)
            return True
        qsoutils=QSOUtils()
        self.qerrors = []
        if (fdata == None):
            self.qerrors.append('No data for this QSO.')
            self.valid=False
            return None
        
        if fdata.upper().startswith('QSO:'):
            """Remove 'QSO: ' string"""
            qdata = fdata[4:].upper().strip()
        else:
            qdata = fdata.upper().strip() 
        qelements = qdata.split()
        if (len(qelements)!=MAXELEMENTS):
            self.qerrors.append(\
              '{} QSO parameters detected, there should be only {}.'\
              .format(len(qelements), MAXELEMENTS))
            if (len(qelements)<MAXELEMENTS):
                self.valid=False
                return false
        index = 0
        for tag in QSODEFS:
            if (tag =='qtime'):
                """Date / time in elemets 2 and 3"""
                self.__dict__[tag] = qsoutils.qsotimeOBJ(\
                              qelements[index].strip(), 
                              qelements[index+1].strip())
                index += 1
            else:
                self.__dict__[tag] = qelements[index].strip()
            index += 1
            if index >= MAXELEMENTS: break
        return True
                                    
    def parseQSOdb(self,  qso):
        """
        QSOs input from a database will be a Dict() object
        instead of a list if strings. Fetch the data from
        the dict() object read from the DB and put it in
        the corrosponding QSO object element.
        NOTE: This code relys on the QSODES and DBQSODEFS
        order and alignmenet matching. 
        (See notes in headedefs.py).
        """
        index = 0
        for dbTag in DBQSODEFS:
            Tag = QSODEFS[index]
            if dbTag in qso.keys():
                self.__dict__[Tag] = qso[dbTag]
            else:
                self.__dict__[Tag] = None          
            index += 1
        return True




    def getQSO(self):
        """
        Return  QSO as a dict() object
        """
        return vars(self)
        
    def getDBQSO(self):
        """
        Return QSO as a dict() object with
        key names matching DB field names.
        QSOs input from a database will be a Dict() object
        instead of a list if strings. Fetch the data from
        the dict() object read from the DN and put it in
        the corrosponding QSO object element.
        NOTE: This code relys on the QSODES and DBQSODEFS
        order and alignmenet matching. 
        (See notes in headedefs.py).
        """
        #from headerdefs import QSODEFS, DBQSODEFS
        index = 0
        qso = dict()
        for dbtag in DBQSODEFS:
            tag = QSODEFS[index]
            if tag in vars(self).keys():
                qso[dbtag] = self.__dict__[tag]
                #print('{}: {}: {}'.format(dbtag, tag, self.__dict__[tag]))
            index += 1
        return qso
        
    

    def __dofmt(self, fmt):
        return (fmt.format(self.freq,
                            self.mode,
                            self.qtime,
                            self.mycall,
                            self.myrst,
                            self.myqth,
                            self.urcall,
                            self.urrst,
                            self.urqth,
                            self.valid,
                            self.dupe))
    
                       
    def makeTSV(self):
        """
        Return this QSO as a Tab Separated Line (TSV).
        """
        fmt = 'QSO:\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'
        return self.__dofmt(fmt)
                            
    def makeHTML(self):
        """
        Return this QSO as an HTML Table Row (HTR).
        """
        fmt='<tr><td>QSO:</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>' +\
            '<td>{}</td><td>{}</td><td>{}</td><td>{}</td>' +\
            '<td>{}</td><td>{}</td><td>{}</td>'
        return self.__dofmt(fmt)

    def show(self):
        print(self.makeTSV())
        
    def showid(self):
        fmt = 'QSO {}:\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'
        print (fmt.format( self.id,
                            self.freq,
                            self.mode,
                            self.qtime,
                            self.mycall,
                            self.myrst,
                            self.myqth,
                            self.urcall,
                            self.urrst,
                            self.urqth,
                            self.valid,
                            self.dupe))
            
        
    def showh(self):
        print(self.makeHTML())

