from config.app import *
import pandas as pd

def GenerateReportVentas(app:App):
    conn=app.bd.getConnection()
    query="""
        SELECT 
            p.pais,
            v.product_id,
            v.order_date,
            SUM(v.quantity) AS total_vendido
        FROM 
            VENTAS v
        JOIN 
            POSTALCODE p
        ON 
            v.postal_code = p.code
        GROUP BY 
            p.pais, v.product_id
        ORDER BY 
            total_vendido DESC;
    """
    df=pd.read_sql_query(query,conn)
    fecha= pd.Timestamp.today().strftime('%d-%m-%Y')
    path=f"files/data-{fecha}.csv"
    df.to_csv(path)
    sendMail(app,path)

def sendMail(app:App,data):
    app.mail.send_email('from@example.com','Reporte de ventas: Lesly Condor Iturrizaga','Reporte',data)