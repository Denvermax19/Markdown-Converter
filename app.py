import streamlit as st
from markitdown import MarkItDown
from pathlib import Path

md = MarkItDown(enable_plugins=False)

def main():
    st.set_page_config(
        page_title="Markdown Converter",
        page_icon="📄",
        layout="wide"
    )
    st.title("Markdown Converter")
    st.write("Upload a PDF or DOCX file to convert it to Markdown format.")
    uploaded_file = st.file_uploader("Choose a PDF or DOCX file", type=["pdf","docx"])
    
    if uploaded_file is not None:
        try:
            st.success("File uploaded successfully!")
            
            if uploaded_file.type == "application/pdf":
                file_path = Path(f"documents/{uploaded_file.name}")
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                result = md.convert(file_path)
                output_path = Path(f"outputs/{uploaded_file.name.replace('.pdf', '.md')}")
            
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                file_path = Path(f"documents/{uploaded_file.name}")
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                result = md.convert(file_path)
                output_path = Path(f"outputs/{uploaded_file.name.replace('.docx', '.md')}")
        
        except Exception as e:
            st.error(f"Error converting file: {e}")


        if result:
                if st.button("Convert to Markdown",type="primary",use_container_width=True):
                    Path(output_path).write_text(result.text_content, encoding="utf-8")
                    st.success("File converted successfully!")
                        
                st.download_button(
                    label="Download Markdown File",
                    data=result.text_content,
                    file_name=output_path.name,
                    mime="text/markdown",
                    type="primary",
                    use_container_width=True
                )
        

if __name__ == "__main__":
    main()