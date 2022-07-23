#!/usr/bin/env python
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
        
    def parseDBQSO(self,  qso):
        self.freq = qso['FREQ']
        self.mode = qso['MODE']
        
        self.qtime = qso['DATETIME']
                        
        self.mycall =qso['MYCALL']
        self.myrst = qso['MYREPORT']
        self.myqth = qso['MYQTH']
               
        self.urcall = qso['URCALL']
        self.urrst = qso['URREPORT']
        self.urqth = qso['URQTH']
        self.valid =  qso['VALID']
        return True

                             
    def getQSO(self):
        """
        Return  QSO as a dict() object
        """
        return vars(self)

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

if __name__ == '__main__':
    """Test code goes here"""
   
