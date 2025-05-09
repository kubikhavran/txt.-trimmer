import streamlit as st

st.title("Remove First and Last Line from TXT Files")

uploaded_files = st.file_uploader("Upload TXT file(s)", accept_multiple_files=True, type=["txt"])

for uploaded_file in uploaded_files:
    lines = uploaded_file.read().decode("utf-8").splitlines()
    
    if len(lines) > 2:
        trimmed_lines = lines[1:-1]
        result = "\n".join(trimmed_lines)
        st.download_button(f"Download cleaned {uploaded_file.name}", result, file_name=uploaded_file.name)
    else:
        st.warning(f"The file {uploaded_file.name} has too few lines.")
