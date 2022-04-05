import mysql.connector;
AWSPath='lab1-012499474.cg6o7wykltqr.us-east-2.rds.amazonaws.com' #AWS Endpoint
conn= mysql.connector.connect(host=AWSPath, db='Lab1_V1', user='root', password='rezaxc007');

# This function takes actor name and lists his movies 
def searchByActor (actorName):
    cursor = conn.cursor()
    command='select Title from Lab1_V1.Movie where Actors like \'%'+ actorName+'%\' ;'  
    cursor.execute(command)
    rows = cursor.fetchall()
    print("Total uumber of movies played by "+actorName+" in our archive is",cursor.rowcount)
    for row in rows:
        print(row)
    conn.commit()
    cursor.close()



searchByActor('Brad Pitt') #Movies having Brad Pitt as the Actor
