import streamlit as st
import pickle


# Ìnormation app
name_app = 'Sentiment analysis'
version_app = '1.0'
current_time = '2023-04-12 11:16:58'
model_setiment_analysis = None
vectorizer = None
file_name_css = 'assets/css/styles.css'


def load_model_setiment_analysis():
    global model_setiment_analysis
    
    # Nếu model đã được load trước đó thì không cần load lại
    if model_setiment_analysis is not None:
        return model_setiment_analysis
    
    # Nếu model chưa được load thì load model từ file pkl và lưu vào biến toàn cục
    pkl_filename = 'models/model.pkl'
    with open(pkl_filename, 'rb') as file:  
        model_setiment_analysis = pickle.load(file)
    
    return model_setiment_analysis

def load_vectorizer():
    global vectorizer
    
    # Nếu model đã được load trước đó thì không cần load lại
    if vectorizer is not None:
        return vectorizer
    
    # Nếu model chưa được load thì load model từ file pkl và lưu vào biến toàn cục
    pkl_filename = 'models/vectorizer.pkl'
    with open(pkl_filename, 'rb') as file:  
        vectorizer = pickle.load(file)
    
    return vectorizer


def Introduce():
    st.subheader('Business Objective')
    st.write("""**Vấn đề hiền tại:** Công ty kinh doanh quả bơ ở rất nhiều vùng của nước Mỹ với 2 loại bơ là bơ thường và bơ hữu cơ, được đóng gói theo nhiều quy chuẩn *(Small/Large/XLarge Bags)*, và có 3 PLU (Product Look Up) khác nhau *(4046, 4225, 4770)*. Nhưng họ chưa có mô hình để dự đoán giá bơ cho việc mở rộng""")
    st.write("""
    **Mục tiêu/ Vấn đề:**
    => Xây dựng mô hình dự đoán giá trung bình của bơ “Hass” ở Mỹ => xem xét việc mở rộng sản xuất, kinh doanh.
    """)


def get_sentiment_label(text, vectorizer, model_setiment_analysis):
    # Chuyển đổi đoạn văn bản thành feature vector
    text_features = vectorizer.transform([text])
    # Dự đoán lớp của đoạn văn bản
    predicted_class = model_setiment_analysis.predict(text_features)[0]    
    # return result
    result = 'Unknown'
    if predicted_class == 0:
        result = '<p class="negative">Negative 🙁🙁🙁🙁🙁🙁</p>'
    elif predicted_class == 1:
        result = '<p class="neutral">Neutral 😐😐😐😐😐😐</p>'
    elif predicted_class == 2:
        result = '<p class="positive">Positive 😊😊😊😊😊😊</p>'

    st.markdown(f"""
        <style>
            .negative {{
                color: red;
            }}
            .neutral {{
                color: orange;
            }}
            .positive {{
                color: green;
            }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown(result, unsafe_allow_html=True)


def create_contact_form():
    # contact form
    with st.sidebar:
        st.write('Send us your feedback!')
        name_input = st.text_input('Your name')
        comment_input = st.text_area('Your comment')
        submitted = st.button('Submit')

        # Nếu người dùng đã gửi đánh giá, thêm đánh giá vào dataframe
        if submitted:
            # Thêm đánh đánh giá người dùng vào file txt
            pass

def create_infomation_app(name_app, version_app, current_time):
    # Infomations app
    st.sidebar.markdown(
        """
        <div style='position: fixed; bottom: 0'>
            <p> """+ name_app +""" - Version: """+ version_app +""" </br>(For Sentiment analysis of text)</p>
            <p><i>Last Updated: """+ current_time +"""<i/></p>
        </div>
        """,
        unsafe_allow_html=True
    )
    

def convert_month(month):
    if month == 3 or month == 4 or month == 5:
        return 0
    elif month == 6 or month == 7 or month == 8:
        return 1
    elif month == 9 or month == 10 or month == 11:
        return 2
    else:
        return 3


def show_introduction():
    st.sidebar.markdown("<h1 style='color: #2196f3;'>Chào mừng đến với Sentiment analysis app!</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<p>Ứng dụng đơn giản để phân loại cảm xúc positive <span>|</span> negative |</span> neutral dựa trên một comment của người dùng khi mua sắm hàng hóa trên các trang thương mại điện tử.</p>", unsafe_allow_html=True)

