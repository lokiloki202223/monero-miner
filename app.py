import cmake
import sys
import subprocess
import streamlit as st
import pandas as pd
import numpy as np
#import miner
st.title('monero miner on stream lit')

i = 0

if i == 0 : st.write('*miner stopped*')
#end if
if i == 1 : st.write('*miner started*')
 # end if
  
  


# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'  pip==22.1 
cmake
streamlit
py-cryptonight>=0.2.4
requests
git+https://github.com/jtgrassie/pyrx.git#egg=pyrx

'])
  


