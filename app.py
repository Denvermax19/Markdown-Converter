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

    
    # Create directories if they don't exist
    Path("documents").mkdir(exist_ok=True)
    Path("outputs").mkdir(exist_ok=True)


    # Start session state for conversion result
    if "converted_data" not in st.session_state:
        st.session_state.converted_data = None
    
    if "output_filename" not in st.session_state:
        st.session_state.output_filename = ""

    uploaded_file = st.file_uploader("Choose a file",
                     type=["pdf","docx","pptx"],
                     on_change=lambda: st.session_state.update({"converted_data": None}) #Reset if new file is uploaded
                     )

    if uploaded_file is not None:
        st.success("File uploaded successfully!")

        # Convert Button
        if st.session_state.converted_data is None:
            if st.button("Convert to Markdown",type="primary",use_container_width=True):

                try:
                    st.spinner("Converting file...")
                    file_path = Path(f"documents/{uploaded_file.name}")
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Conversion logic
                    result = md.convert(str(file_path))
                    
                    # Store in session state                
                    st.session_state.converted_data = result.text_content
                    st.session_state.output_filename = file_path.stem + ".md"
                    st.success("File converted successfully!")


                    # Force refresh to hide conversion button and show download button
                    st.rerun()

                
                except Exception as e:
                    st.error(f"Error converting file: {e}")
                

    
    # Download Button
    if st.session_state.converted_data:
        st.divider()
        st.markdown("### Download your Markdown file")


        # Preview markdown content
        with st.expander("Preview Markdown Content"):
            st.code(st.session_state.converted_data, language="markdown")

        st.download_button(
            label="Download Markdown File",
            data=st.session_state.converted_data,
            file_name=st.session_state.output_filename,
            mime="text/markdown",
            type="primary",
            use_container_width=True
        )


if __name__ == "__main__":
    main()
