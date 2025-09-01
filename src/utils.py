import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def execute_plt_code(code:str, df: pd.DataFrame):
    """Execute the passing code to plot a figure

    Args:
        code (str): action string (contain plt code)
        df (pd.DataFrame): our data frame

    Returns:
        _type_: plt figure
    """
    
    try:
        local_vars = {'plt':plt, 'df':df}
        complied_code = compile(code, "<string>", "exec")
        exec(complied_code, globals(), local_vars)
        return plt.gcf()

    except Exception as e:
        st.error(f'Error executing plt code: "{e}')
        return None