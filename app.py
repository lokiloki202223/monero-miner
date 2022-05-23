#import cmake
import sys
import subprocess
import streamlit as st
import pandas as pd
import numpy as np
#import miner
st.title('monero miner on stream lit')



  
  


# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'  pip==22.1 '])
 
 


 
 subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'  py-cryptonight>=0.2.4 '])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'  requests'])




subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'  git+https://github.com/jtgrassie/pyrx.git#egg=pyrx'])

