import mysql.connector;
AWSPath='lab1-012499474.cg6o7wykltqr.us-east-2.rds.amazonaws.com' #AWS Endpoint
conn= mysql.connector.connect(host=AWSPath, db='Mousivand_SMD', user='root', password='rezaxc007');

# This function takes actor name and lists his movies 
def searchByActor (actorName):
    cursor = conn.cursor()
    command='select Title from Lab1_V1.Movie where Actors like \'%'+ actorName+'%\' ;'  
    cursor.execute(command)
    rows = cursor.fetchall()
    print("The number of available movies played by "+actorName+" is",cursor.rowcount)
    for row in rows:
        print(row)
    conn.commit()
    cursor.close()



searchByActor('Brad Pitt') #Movies having Brad Pitt as the Actor
