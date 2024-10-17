import sqlite3
import pandas as pd
conn=sqlite3.connect('database.sqlite')
readCountry=pd.read_sql("select * from Country;",conn)
#print(readCountry)
readCity=pd.read_sql("SELECT * FROM City;",conn)
#print(readCity)

readInnerJoin=pd.read_sql("SELECT C.Country_Name ,CT.City_Name, CT.City_Id FROM Country C INNER JOIN City CT ON C.Country_Id==CT.Country_id ",conn)
print(readInnerJoin)
readingplayer=pd.read_sql("SELECT * FROM player",conn)
print(readingplayer.info())
readingseason=pd.read_sql("SELECT * FROM season",conn)
print(readingseason.info())
leftjoining=pd.read_sql("SELECT * FROM player LEFT JOIN season ON season.Man_of_the_Series==player.Player_Name",conn)
print(leftjoining)