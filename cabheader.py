#!/usr/bin/env python3
from cabrilloutils.qsoutils import QSOUtils

class cabrilloHeader():
    def __init__(   self,
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
                    ID=None,
                    CABBONUS=False,
                    TIMESTAMP=None,
                    HEADERTEXT=None):
  
        self.START_OF_LOG=START_OF_LOG
        self.END_OF_LOG=END_OF_LOG
        self.CALLSIGN=CALLSIGN
        self.CONTEST=CONTEST
        self.CATEGORY_ASSISTED=CATEGORY_ASSISTED
        self.CATEGORY_BAND=CATEGORY_BAND
        self.CATEGORY_MODE=CATEGORY_MODE
        self.CATEGORY_OPERATOR=CATEGORY_OPERATOR
        self.CATEGORY_POWER=CATEGORY_POWER
        self.CATEGORY_STATION=CATEGORY_STATION
        self.CATEGORY_TIME=CATEGORY_TIME
        self.CATEGORY_TRANSMITTER=CATEGORY_TRANSMITTER
        self.CATEGORY_OVERLAY=CATEGORY_OVERLAY
        self.CERTIFICATE=CERTIFICATE
        self.CLAIMED_SCORE=CLAIMED_SCORE
        self.CLUB=CLUB
        self.CREATED_BY=CREATED_BY
        self.EMAIL=EMAIL
        self.GRID_LOCATOR=GRID_LOCATOR
        self.LOCATION=LOCATION
        self.NAME=NAME
        self.ADDRESS=ADDRESS
        self.ADDRESS_CITY=ADDRESS_CITY
        self.ADDRESS_STATE_PROVINCE=ADDRESS_STATE_PROVINCE
        self.ADDRESS_POSTALCODE=ADDRESS_POSTALCODE
        self.ADDRESS_COUNTRY=ADDRESS_COUNTRY
        self.OPERATORS=OPERATORS
        self.OFFTIME=OFFTIME
        self.SOAPBOX=SOAPBOX
        self.ID=ID
        self.CABBONUS=CABBONUS
        self.TIMESTAMP=TIMESTAMP

        if (HEADERTEXT):
            self.parseHeaderList(HEADERTEXT)
    
    def __dofmt(self, fmt):
        return (fmt.format(\
                    self.START_OF_LOG,
                    self.END_OF_LOG,
                    self.CALLSIGN,
                    self.CONTEST,
                    self.CATEGORY_ASSISTED,
                    self.CATEGORY_BAND,
                    self.CATEGORY_MODE,
                    self.CATEGORY_OPERATOR,
                    self.CATEGORY_POWER,
                    self.CATEGORY_STATION,
                    self.CATEGORY_TIME,
                    self.CATEGORY_TRANSMITTER,
                    self.CATEGORY_OVERLAY,
                    self.CERTIFICATE,
                    self.CLAIMED_SCORE,
                    self.CLUB,
                    self.CREATED_BY,
                    self.EMAIL,
                    self.GRID_LOCATOR,
                    self.LOCATION,
                    self.NAME,
                    self.ADDRESS,
                    self.ADDRESS_CITY,
                    self.ADDRESS_STATE_PROVINCE,
                    self.ADDRESS_POSTALCODE,
                    self.ADDRESS_COUNTRY,
                    self.OPERATORS,
                    self.OFFTIME,
                    self.SOAPBOX))
                    
    def makeTSV(self):
        """
        Return this header as a Tsb Separated Line (TSV).
        """
        fmt = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t' +\
              '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t' +\
              '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'
        return self.__dofmt(fmt)

    def makeHTML(self):
        """
        Return this header as an HTML Table Row (HTR).
        """
        fmt='<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>' +\
            '<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>' +\
            '<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>' +\
            '<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>' +\
            '<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>' +\
            '<td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'
        return self.__dofmt(fmt)

    def show(self):
        print(self.makeTSV())
        
    def showh(self):
        print(self.makeHTML())
                    
    def setTagData(self, tag, tdata):
        result = False
        taglist = vars(self).keys()
        #print(taglist)
        mtag = tag.replace('-','_')
        if (mtag in taglist):
            if mtag == 'END_OF_LOG': tdata = True
            #print('Setting {} = {}'.format(mtag, tdata))
            self.__dict__[mtag] = tdata
            result = True
        return result
     
    def getHeader(self):
        return vars(self)

    def parseHeader(self, headertext):
        if isinstance(headertext, dict):
            self.parseHeaderdb(headertext)
            return self
        #else continue and process as a list
        
        qsoutils = QSOUtils()        
        cabrilloTags = vars(self).keys()
        ln=0
        for line in headertext:
            ln+=1
            uline = line.strip().upper()
            cabparts = uline.split(':',1)
            if(len(cabparts)<2):
                print('Skipping line {}: {}'.format(ln, line))
            else:
                cabtag = cabparts[0].upper().strip()
                cabdata = cabparts[1].upper().strip()
                #print('{}, {}'.format(cabtag, cabdata))
                gcabtag = self.setTagData(cabtag, cabdata)
                if gcabtag == False:
                    print('Header tag {} at line {} unknown.'.\
                                format(line, ln))
        return self

    def parseHeaderdb(self, hd):  
        from headerdefs import HEADERDEFS, DBHEADERDEFS
        #print ("hd=\n{}keys\n{}".format(hd, hd.keys()))
        index = 0
        for tag in HEADERDEFS:
            dbtag = DBHEADERDEFS[index]
            if dbtag in hd.keys():
                res = self.setTagData(tag, hd[dbtag])
            index += 1
        return self

    def prettyprint(self, rtype='csv'):
        """
        Returns header data as a list suitable for printing.
        """
        from headerdefs import HEADERDEFS
        if (rtype == 'html'):
            headerlines = ['<table>']
            rowfmt = '<tr><td>{}</td><td>{}</td></tr>'
        else:    
            headerlines = []
            rowfmt ='{}: {}'

        for tag in HEADERDEFS:
            if ('_' in tag):
                tagstg = tag.replace('_', '-')
            else:
                tagstg = tag
            if tag in vars(self).keys():
                headerlines.append(rowfmt\
                           .format(tagstg, self.__dict__[tag]))
        from headerdefs import HEADERDEFS
        if (rtype == 'html'):
            headerlines.append('</table>')
        return headerlines

