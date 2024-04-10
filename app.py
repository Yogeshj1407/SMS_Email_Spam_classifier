import streamlit as st
import pickle
import sklearn
import preprocessing

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


st.title('SMS/Email Spam Classifier')

input_sms = st.text_area('Enter the message')

if st.button('Check Message'):

    #preprocessing
    transformed_sms = preprocessing.transfrom_text(input_sms)
    #vectorize
    vector_input = tfidf.transform([transformed_sms])
    #predict
    result = model.predict(vector_input)[0]
    #display
    if result == 1:
        st.header('Spam !!! Be Aware ...')
    else:
        st.header('Relax ... Not Spam :)')