#!/usr/bin/env python

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
                    SOAPBOX=None):
  
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
        Return this header as an HTML Table R
        ow (HTR).
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
            #print('Setting {} = {}'.format(mtag, tdata))
            self.__dict__[mtag] = tdata
            result = True
        return result
     
    def getHeader(self):
        return vars(self)

class dbcabrilloHeader(cabrilloHeader):

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
                    TIMESTAMP=None):
  
        self.ID=ID
        self.CABBONUS=CABBONUS=False
        self.TIMESTAMP=TIMESTAMP=None
        super().__init__(    \
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


