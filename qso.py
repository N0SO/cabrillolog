#!/usr/bin/env python3
from cabrilloutils.qsoutils import QSOUtils


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
                    qdata = None):

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
        self.qdata=qdata

        if (qdata):
            self.parseQSO(qdata)
        
    def parseQSO(self, qdata):
        """
        Populate qso data elements from qdata. Expected format:
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
        """
        qsoutils=QSOUtils()
        MAXELEMENTS=10
        self.qerrors = []
        if (qdata == None):
            self.qerrors.append('No data for this QSO.')
            self.valid=False
            return None
        qelements = qdata.split()
        if (len(qelements)!=MAXELEMENTS):
            self.qerrors.append(\
              '{} QSO parameters detected, there should be only {}.'\
              .format(len(qelements), MAXELEMENTS))
            if (len(qelements)<MAXELEMENTS):
                self.valid=False
                return false
        self.freq = qelements[0]
        self.mode = qelements[1]
        
        self.qtime = qsoutils.qsotimeOBJ(qelements[2], qelements[3])
                        
        self.mycall = qelements[4]
        self.myrst = qelements[5]
        self.myqth = qelements[6]
               
        self.urcall = qelements[7]
        self.urrst = qelements[8]
        self.urqth = qelements[9]

        self.valid = True
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
        from headerdefs import QSODEFS, DBQSODEFS
        index = 0
        qso = dict()
        for dbtag in DBQSODEFS:
            tag = QSODEFS[index]
            if dbtag in vars(self).keys():
                qso[dbtag] = self.__dict__[tag]
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
        Return this QSO as a Tsb Separated Line (TSV).
        """
        fmt = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'
        return self.__dofmt(fmt)
                            
    def makeHTML(self):
        """
        Return this QSO as an HTML Table Row (HTR).
        """
        fmt='<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td>' +\
            '<td>{}</td><td>{}</td><td>{}</td><td>{}</td>' +\
            '<td>{}</td><td>{}</td><td>{}</td>'
        return self.__dofmt(fmt)

    def show(self):
        print(self.makeTSV())
        
    def showh(self):
        print(self.makeHTML())

class dbQSO(QSO):
    """
    QSO class with added storage for database fields:
    id = record id.
    logid = the database of the logheader for this QSO.
    qsl = the ID of the QSO record this QSO CONFIRMS (QSL).
    nolog True = no log from URCALL in database for this QSO.
    noqsos True = no matching qso in URCALL log for this QSO.
    """
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
                    qdata = None,
                    id = None,
                    logid=None,
                    qsl=None,
                    nolog=False,
                    noqsos = False):
        
        self.id=id
        self.logid=logid
        self.qsl=qsl
        self.nolog=nolog
        self.noqsos=noqsos
        # Call parent init to complete
        super().__init__(   \
                            freq=freq,
                            mode=mode,
                            qtime=qtime,
                            mycall=mycall,
                            myrst=myrst,
                            myqth=myqth,
                            urcall=urcall,
                            urrst=urrst,
                            urqth=urqth,
                            valid=valid,
                            dupe=dupe,
                            qdata=qdata)

    def parseQSO(self,  qso):
        """
        QSOs input from a database will be a Dict() object
        instead of a list if strings. Fetch the data from
        the dict() object read from the DN and put it in
        the corrosponding QSO object element.
        NOTE: This code relys on the QSODES and DBQSODEFS
        order and alignmenet matching. 
        (See notes in headedefs.py).
        """
        if isinstance(qso, str):
            #print('string')
            #call parent
            super().parseQSO(qso)
            return True
        #else parse the dict() qso  
        from headerdefs import QSODEFS, DBQSODEFS        
        index = 0
        for dbTag in DBQSODEFS:
            Tag = QSODEFS[index]
            if dbTag in qso.keys():
                self.__dict__[Tag] = qso[dbTag]
            else:
                self.__dict__[Tag] = None          
            index += 1
        return True
        

        