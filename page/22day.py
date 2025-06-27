import streamlit as st

st.title('st.form')

st.header('1. Example of using with notation')
st.subheader('Coffee machine')

with st.form('coffee_form'):
    st.subheader('Order your coffee')

    coffee_bean_vel =st.selectbox('Coffee bean', ['Aranica', 'Robusta'])
    coffee_roast_vel =st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewint_method_vel =st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French','Moka pot', 'Siphon'])
    serving_format_vel =st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_intensity_vel =st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    cup_vel =st.checkbox('Bring own cup')

    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
                ☕ You have ordered:
                Coffee bean:'{coffee_bean_vel}'
                Coffee roast:'{coffee_roast_vel}'
                Brewing:'{brewint_method_vel}' 
                Serving type:'{serving_format_vel}'
                Milk:'{milk_intensity_vel}'
                Bring own cup:'{cup_vel}' 
                ''')
else:
    st.write('☝️ Place your order!')

st.header('2. Example of object notation')

form = st.form('coffee_form2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value:', selected_val)