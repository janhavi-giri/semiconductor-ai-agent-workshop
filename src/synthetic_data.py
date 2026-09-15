import numpy as np
import pandas as pd
FEATURES=["Yield_Pct","Defect_Density","Temperature_C","Pressure_kPa","Process_Time_Min","Thickness_nm"]
def generate_wafer_data(n_wafers=600,random_state=42):
    rng=np.random.default_rng(random_state); family=rng.choice(4,n_wafers,p=[.3,.28,.24,.18])
    df=pd.DataFrame({"Wafer_ID":[f"W{i:05d}" for i in range(n_wafers)],"Yield_Pct":rng.normal(np.array([96,89,80,68])[family],2.8),"Defect_Density":rng.exponential(np.array([.08,.25,.6,1.2])[family]),"Temperature_C":rng.normal(345+family*9,3.5),"Pressure_kPa":rng.normal(98+family*4,2.2),"Process_Time_Min":rng.normal(112+family*8,6),"Thickness_nm":rng.normal(500+family*18,10)})
    df["Yield_Pct"]=df["Yield_Pct"].clip(0,100); return df.round(4)
