from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict, Annotated, Optional
import streamlit as st

model = ChatOpenAI(model_name="gpt-4", api_key=st.secrets['api_key'], temperature=0)
 
st.title("Review Analysis")
class Review(TypedDict):
    sentiment: Annotated[str, "Sentiment of the review"]
    key_theme: Annotated[list[str], "Key theme of the review"]
    Summary: Annotated[str, "Summary of the review"]
    pros=Annotated[Optional[list[str]], "Pros of the review"]
    cons=Annotated[Optional[list[str]], "Cons of the review"]

structured_model = model.with_structured_output(Review)

review=st.text_input("Enter your review")



if st.button('Summarize'):
    # ✅ Send the final string to the model
    
    result = structured_model.invoke(review)

    # ✅ Show model output
    st.write(result)
