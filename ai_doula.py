import openai
import streamlit as st


with st.sidebar:
    header= st.sidebar.header(":key: Paste your OpenAi API key below?")
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[View the source code](https://github.com/janumirra/ChatBot-creation-with-openai-API/blob/main/ai_doula.py)"

#st.set_page_config(page_title ="AI Doula",page_icon= "📖:AI Doula",layout= "wide")
st.title('AI Doula')
#########################################
choice=['Open ended','Instruction','Multiple Choice','Fill in the blank','Binary','Ordering','Prediction','Explanation','Opinion','Scenario','Comparative']
sample_prompt=["Please ask any questions or share your concerns related to postpartum care, emotional well-being, infant care, or any other aspects of the postpartum period.",
            "Imagine you are a healthcare professional providing postpartum care advice. Write a detailed response explaining the signs and symptoms of postpartum depression.",
            "Which of the following activities should be avoided in the first few days after delivery? a) Heavy lifting b) Gentle walks c) Yoga exercises d) Swimming",
            "One of the important ways to prevent deep vein thrombosis after delivery is to regularly __________.",
            "True or False: Breastfeeding mothers should avoid consuming caffeinated beverages.",
            "Arrange the following steps for physical recovery from birth in the correct order:a) Engage in gentle exercises b) Get plenty of rest c) Eat a balanced diet d) Attend postpartum check-ups",
            "Predict how a lack of proper sleep and fatigue may impact a new mother's emotional well-being.",
            "Explain the importance of ongoing preventive health maintenance during the postpartum period.",
            "What is your opinion on the use of avatars to express user emotions during postpartum care? Do you think it could be beneficial?",
            "Imagine you are a new mother struggling with postpartum depression. Describe how you would seek support and care from your loved ones and healthcare providers.",
            "Compare the challenges of infant care and feeding during the postpartum period to the challenges during pregnancy."]

dictionary=dict(zip(choice,sample_prompt))
    
if not openai_api_key:
    st.warning(
        "Enter your OpenAI API key in the sidebar. You can get a key at"
        " https://platform.openai.com/account/api-keys."
    )
else:
    choice_drop = st.selectbox(
     'What is the type of Prompt that you would like to use?',
     ('Open ended','Instruction','Multiple Choice','Fill in the blank','Binary','Ordering','Prediction','Explanation','Opinion','Scenario','Comparative'))    

    if choice_drop in dictionary:
        st.write("""This is a sample prompt, type in the same or type similar prompt 
                 
                 
                 """,
                dictionary[choice_drop])
        openai.api_key = openai_api_key 
        st.session_state["messages"] = [{"role": "system", "content": dictionary[choice_drop]}]

        def CustomChatGPT(user_input):
            st.session_state.messages.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = st.session_state.messages
            )
            ChatGPT_reply = response["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": ChatGPT_reply})
            return ChatGPT_reply

        #user_input=input()
        #st.write("Type your prompt below")
        user_input = st.text_input("**Type your prompt below**")
        answer=CustomChatGPT(user_input)
        st.write(answer)
    note= '<p style="font-family:Courier; color:Blue; font-size: 20px;"></p>'
    st.write(':blue[*Clear your prompt before selecting your next type of prompt*]')
    
   
