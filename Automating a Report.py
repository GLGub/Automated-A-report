from datetime import datetime
import pandas as pd

def timecon(dtime):
    dts=datetime.strptime(dtime,"%d-%B-%Y-%I:%M %p" )
    date_only=list(str(dts.date()).split('-'))
    time_only=list(str(dts.time()).split(':'))
    return dts.year,date_only[1],date_only[2],time_only[0],time_only[1],dtime.split('-')[1]

def report_xpo(subcsv,file_name):
    df = pd.read_csv (subcsv)
    df[['Main','1','2','2','3','4']]=df['1|2|3|4|5'].str.split('|',expand=True)
    df['Out']=df['Main'].apply(lambda x : x[2:]) 
    df["Out"].to_csv(f'report_{file_name}_1.csv',header=False, index=False)
    
def filname(stdt,status,endt):
    stye,stmo,stda,stho,stmi,stmons=timecon(stdt)
    file_name=f"Report_{stye}{stmo}{stda}{stho}{stmi}00"
    etdat,etime='',''
    if status.upper() == "CLOSED":
        etye,etmo,etda,etho,etmi,etmons=timecon(endt)
        etdat=f'{etda}-{etmons}-{etye}'
        etime=f'{etho}{etmi}H'
        file_name=f"Report_{etye}{etmo}{etda}{etho}{etmi}00"
    return file_name