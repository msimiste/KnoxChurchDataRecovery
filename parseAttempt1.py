#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parseAttempt1.py
#  
#  Copyright 2018 simdevs <simdevs@simdevs>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import string

def main(args):
    with open("CM.DAT", "rb") as f, open("parseOutDelimited.txt","wb") as od, open("parseOut.txt","wb") as o:
        f.seek(1048)
        count = 3000;
        while count <> 0:
            title = f.read(30).strip()
            f.seek(1,1)
            composer = f.read(20).strip()
            f.seek(1,1)
            ref = f.read(5).strip()
            f.seek(1,1)
            arr1 = f.read(20).strip()
            f.seek(1,1)
            arr2 = f.read(20).strip()
            f.seek(1,1)
            field1 = f.read(15).strip()
            f.seek(1,1)
            field2 = f.read(31).strip()
            f.seek(1,1)
            field3 = f.read(4).strip()
            f.seek(1,1)
            field4 = f.read(4).strip()
            f.seek(1,1)
            publisher = f.read(20).strip()
            f.seek(1,1)
            field5 = myFilter(f.read(38))#f.read(38).strip()
            f.seek(1,1)
            field6 = myFilter(f.read(72))
            #print(field6).strip()
            f.seek(1,1)
            field7 = f.read(3).strip()
            f.seek(1,1)
            field8 = myFilter(f.read(39))
            f.seek(6,1)
            #f.seek(45,1)
            field9 = f.read(6)
            field9 = myFilter(field9)#filter(lambda x: x in string.printable, str(field9))
            #print(field9)
            f.seek(1,1)
            field10 = f.read(6)
            field10 = myFilter(field10)#filter(lambda x: x in string.printable, str(field10))
            #print(field10)
            f.seek(1,1)
            field11 = myFilter(f.read(6))
            f.seek(1,1)        
            field12 = myFilter(f.read(6))
            f.seek(1,1)        
            field13 = myFilter(f.read(6))
            f.seek(1,1)        
            field14 = myFilter(f.read(6))
            f.seek(1,1)        
            field15 = myFilter(f.read(6))
            f.seek(1,1)        
            field16 = myFilter(f.read(6))
            f.seek(1,1)        
            field17 = myFilter(f.read(6))
            f.seek(1,1)        
            field18 = myFilter(f.read(6))
            f.seek(1,1)        
            field19 = myFilter(f.read(6))
            f.read(9)          
            field20 = myFilter(f.read(6))
            f.seek(1,1)        
            field21 = myFilter(f.read(6))
            f.seek(1,1)        
            field22 = myFilter(f.read(6))
            f.seek(1,1)        
            field23 = myFilter(f.read(6))
            f.seek(1,1)
            field24 = myFilter(f.read(28))
            f.seek(8,1)
            notes = f.read(548).strip().strip('0x00')
            notes = filter(lambda x: x in string.printable, str(notes))
            count = count-1
            
            #o.write("Song:{}; Composer:{}; Ref#:{}; Arr:{}; Arr:{}; Publisher:{}; notes:{}\n".format(title,composer,ref,arr1,arr2,publisher,notes).decode('ascii','ignore').encode('ASCII','ignore'))
            #o.write("{};{};{};{};{};{};{}\n".format(title,composer,ref,arr1,arr2,publisher,notes).decode('ascii','ignore').encode('ASCII','ignore'))
            #non-delimited
            o.write('Song:{};Composer:{};Ref#:{};arr1:{};arr2:{};field1:{};field2:{};field3:{};field4:{};publisher:{};field5:{};field6:{};field7:{};field8:{};field9:{};field10:{};field11:{};field12:{};field13:{};field14:{};field15:{};field16:{};field17:{};field18:{};field19:{};field20:{};field21:{};field22:{};field23:{};field24:{};notes:{}\n'.format(title,composer,ref,arr1,arr2,field1,field2,field3,field4,publisher,field5,field6,field7,field8,field9,field10,field11,field12,field13,field14,field15,field16,field17,field18,field19,field20,field21,field22,field23,field24,notes).decode('ascii','ignore').encode('ASCII','ignore'))
            #delimited
            od.write('{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}\n'.format(title,composer,ref,arr1,arr2,field1,field2,field3,field4,publisher,field5,field6,field7,field8,field9,field10,field11,field12,field13,field14,field15,field16,field17,field18,field19,field20,field21,field22,field23,field24,notes).decode('ascii','ignore').encode('ASCII','ignore'))
            #o.write('Song:{};Composer:{};Ref#:{};arr1:{};arr2:{};field1:{};field2:{};field3:{};field4:{};publisher:{};field5:{};field6:{};field7:{};field8:{};notes:{}\n'.format(title,composer,ref,arr1,arr2,field1,field2,field3,field4,publisher,field5,field6,field7,field8,notes))     
            #o.write('field6:{};field7:{}\n'.format(field6,field7).decode('ascii','ignore').encode('ASCII','ignore'))
            #o.flush()
            #o.write('field9:{}; field10{};\n'.format(field9,field10).decode('ascii','ignore').encode('ASCII','ignore'))
            #o.flush()
        o.close()
        od.close()
        f.close()
        
def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

def _Strip(inVal):
    #outVal = insertPrefix(inVal,prefix)
    #print(inVal)
    outVal = ''.join(str(chr(convertPrintable(x))) for x in inVal)
    return outVal

def myFilter(inVal):
    return filter(lambda x: x in string.printable, str(inVal))
    
def convertPrintable(inOrd):
    if((inOrd < 32) or(inOrd > 127)):
        return 46
    else:
        return inOrd

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
