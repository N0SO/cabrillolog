#!/usr/bin/env python3
"""
DEFs for header variable tags The order of these needs to
line up with the order of the tags in DBHEADERDEFS so the
methods in cabrilloHeader can easily copy data to and from
the dict() objetcs the MySQL code reads from the database.
START_OF_LOG should line uo with START in DBHEADERDEFS,
CALLSIGN should line up with CALLSIGN,
etc
etc
"""
HEADERDEFS =    [\
                'START_OF_LOG',
                'CALLSIGN',
                'OPERATORS',
                'CONTEST',
                'LOCATION',
                'CATEGORY_BAND',
                'CATEGORY_MODE',
                'CATEGORY_OPERATOR',
                'CATEGORY_POWER',
                'CATEGORY_STATION',
                'CATEGORY_TRANSMITTER',
                'CATEGORY_OVERLAY',
                'CATEGORY_ASSISTED',
                'CATEGORY_TIME',
                'CERTIFICATE',
                'CLUB',
                'CLAIMED_SCORE',
                'CREATED_BY',
                'EMAIL',
                'NAME',
                'ADDRESS',
                'ADDRESS_CITY',
                'ADDRESS_STATE_PROVINCE',
                'ADDRESS_POSTALCODE',
                'ADDRESS_COUNTRY',
                'OFFTIME',
                'GRID_LOCATOR',
                'SOAPBOX',
                'END_OF_LOG',
                'ID',
                'CABBONUS',
                'TIMESTAMP']
"""
See comments above about the order of the tags listed below.
Changing it will break the database read/write methods!
"""                
DBHEADERDEFS =  [\
                'START',	
                'CALLSIGN',
                'OPERATORS',
                'CONTEST',
                'LOCATION',
                'CATBAND',
                'CATMODE',
                'CATOPERATOR',
                'CATPOWER',
                'CATSTATION',
                'CATXMITTER',
                'CATOVERLAY',
                'CATASSISTED',
                'CATEGORY_TIME', # Not used in db!
                'CERTIFICATE',
                'CLUB',
                'CLAIMEDSCORE',
                'CREATEDBY',
                'EMAIL',
                'NAME',
                'ADDRESS',
                'CITY',
                'STATEPROV',
                'ZIPCODE',
                'COUNTRY',
                'OFFTIME',
                'GRID_LOCATOR', #Not used in db
                'SOAPBOX',
                'ENDOFLOG',
                'ID',
                'CABBONUS',
                'TIMESTAMP']
"""
DEFs for qso variable tags The order of these needs to
line up with the order of the tags in DBQSODEFS so the
methods in QSO can easily copy data to and from
the dict() objetcs the MySQL code reads from the database.
freq should line uo with FREQ in DBQSODEFS,
mode should line up with MODE,
etc.
etc.
"""                
QSODEFS =   [\
            'freq',
            'mode',
            'qtime',
            'mycall',
            'myrst',
            'myqth',
            'urcall',
            'urrst',
            'urqth',
            'valid',
            'dupe',
            'note',
            'id',
            'logid',
            'qsl',
            'nolog',
            'noqsos']

"""
See comments above about the order of the tags listed below.
Changing it will break the database read/write methods!
"""                
            
DBQSODEFS=  [\
            'FREQ',
            'MODE',
            'DATETIME',
            'MYCALL',
            'MYREPORT',
            'MYQTH',
            'URCALL',
            'URREPORT',
            'URQTH',
            'VALID',
            'DUPE',
            'NOTE',
            'ID',
            'LOGID',
            'QSL',
            'NOLOG',
            'NOQSOS']
			
