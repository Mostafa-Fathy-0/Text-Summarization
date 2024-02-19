import streamlit as st
from summa.summarizer import summarize

def main():
    st.title("Arabic Text Summarization")

    # Text input
    text = st.text_area("Enter your text here:")

    # Ratio parameter for summarization
    ratio = 0.20

    # Button to trigger summarization
    if st.button("Summarize"):
        if text:
            summary = summarize(text, ratio=ratio,language='arabic')
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()