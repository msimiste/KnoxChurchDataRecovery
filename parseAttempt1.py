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
    with open("CM_1.DAT", "rb") as f, open("parseOutDelimited_05_17.txt","wb") as od, open("parseOut_05_17.txt","wb") as o:
        f.seek(1048)
        count = 3000;
        while count <> 0:
            title = f.read(30).strip()
            title = myReplace(title)
            f.seek(1,1)
            composer = f.read(20).strip()
            composer = myReplace(composer)
            f.seek(1,1)
            ref = f.read(5).strip()
            ref = myReplace(ref)
            f.seek(1,1)
            arr1 = f.read(20).strip()
            arr1 = myReplace(arr1)
            f.seek(1,1)
            arr2 = f.read(20).strip()
            arr2 = myReplace(arr2)
            f.seek(1,1)
            year = f.read(15).strip()
            year = myReplace(year)
            f.seek(1,1)
            key = f.read(31).strip()
            key = myReplace(key)
            f.seek(1,1)
            arrYear = f.read(4).strip()
            arrYear =myReplace(arrYear)
            f.seek(1,1)
            field4 = f.read(4).strip()
            field4 = myReplace(field4)
            f.seek(1,1)
            publisher = f.read(20).strip()
            publisher = myReplace(publisher)
            f.seek(1,1)
            field5 = myFilter(f.read(38).strip())
            f.seek(1,1)
            field6 = myFilter(f.read(72).strip())
            f.seek(1,1)
            field7 = f.read(3).strip()
            f.seek(1,1)
            field8 = myFilter(f.read(39).strip())
            f.seek(6,1)
            field9 = f.read(6).strip()
            field9 = myFilter(field9)
            f.seek(1,1)
            field10 = f.read(6).strip()
            field10 = myFilter(field10)
            f.seek(1,1)
            field11 = myFilter(f.read(6).strip())
            f.seek(1,1)        
            field12 = myFilter(f.read(6).strip())
            f.seek(1,1)        
            field13 = myFilter(f.read(6).strip())
            f.seek(1,1)        
            field14 = myFilter(f.read(6).strip())
            f.seek(1,1)        
            field15 = myFilter(f.read(6).strip())
            f.seek(1,1)        
            field16 = myFilter(f.read(6).strip())
            f.seek(1,1)        
            field17 = myFilter(f.read(6).strip())
            f.seek(1,1)        
            field18 = myFilter(f.read(6).strip())
            f.seek(1,1)        
            field19 = myFilter(f.read(6).strip())
            f.read(9)          
            field20 = myFilter(f.read(6).strip())
            f.seek(1,1)        
            field21 = myFilter(f.read(6).strip())
            f.seek(1,1)        
            field22 = myFilter(f.read(6).strip())
            f.seek(1,1)        
            field23 = myFilter(f.read(6).strip())
            f.seek(1,1)
            field24 = myFilter(f.read(28).strip())
            f.seek(8,1)
            notes = f.read(548)
            notes = notes.strip().strip('0x00')
            notes = myFilter(notes)
            #notes = filter(lambda x: x in string.printable, str(notes))
            #notes = myReplace(notes)
            count = count-1
            
            #non-delimited
            o.write('Song:{};Composer:{};Ref#:{};arr1:{};arr2:{};Year:{};key:{};ArrYear?:{};field4:{};publisher:{};field5:{};field6:{};field7:{};field8:{};field9:{};field10:{};field11:{};field12:{};field13:{};field14:{};field15:{};field16:{};field17:{};field18:{};field19:{};field20:{};field21:{};field22:{};field23:{};field24:{};notes:{}\n'.format(title,composer,ref,arr1,arr2,year,key,arrYear,field4,publisher,field5,field6,field7,field8,field9,field10,field11,field12,field13,field14,field15,field16,field17,field18,field19,field20,field21,field22,field23,field24,notes).decode('ascii','ignore').encode('ASCII','ignore'))
            
            #delimited
            od.write('{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{};{}\n'.format(title,composer,ref,arr1,arr2,year,key,arrYear,field4,publisher,field5,field6,field7,field8,field9,field10,field11,field12,field13,field14,field15,field16,field17,field18,field19,field20,field21,field22,field23,field24,notes).decode('ascii','ignore').encode('ASCII','ignore'))
        
        o.close()
        od.close()
        f.close()

def myFilter(inVal):
    outVal = filter(lambda x: x in string.printable, str(inVal))
    outVal = myReplace(outVal)
    return outVal
        
def myReplace(inVal):
    outVal = inVal.strip('\xFF')
    outVal = outVal.replace('\n','').replace('\r','').replace('\x0b','').replace('  ','')
    return outVal

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
