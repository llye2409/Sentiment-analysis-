from lib.mylib import *

# Page setting
st.set_page_config(page_title="My App", page_icon=":😊:", layout="centered")
# Introdution
show_introduction()
# Contact form
create_contact_form()
# Infomations app
create_infomation_app(name_app, version_app, current_time)
# Load model
vectorizer = load_vectorizer()
model_setiment_analysis = load_model_setiment_analysis()
# Add a file uploader to allow users to upload a txt file
uploaded_file = st.file_uploader("Upload a txt file", type=["txt"])
if uploaded_file is not None:
    # Read the contents of the file
    text_upload = uploaded_file.read().decode("utf-8")
    text_input = st.text_area(label='Input text', value=text_upload, height=200)
else:
    # Add a text area for users to input text
    labels = """
    Nhập văn bản (Ví dụ: Sản phẩm rất tốt | Giao hàng nhanh chóng và đúng hạn | Chất lượng sản phẩm tuyệt vời | Tính cho shop 5 sao 
    nhưng nghĩ lại, shipper bắt mk đứng đợi nửa tiếng vừa rông về nhà thì gọi,xong lại rông nên vừa đứng đợi thì bị chửi là con này nó bị điên vì shipper mà mk bị chửi nên ko cho 5 sao nữa)
    """
    st.write(labels)
    text_input = st.text_area(label='Your comment', value='', height=200)

# Add the "Predict" button
if st.button('Analyze'):
    if text_input.strip() == '':
        st.warning('Bạn chưa nhập đoạn văn bản')
    else:
        # Show result
        st.write('Results:')
        result = get_sentiment_label(text_input, vectorizer, model_setiment_analysis)