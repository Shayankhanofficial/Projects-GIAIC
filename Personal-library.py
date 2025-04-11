import streamlit as st
import pandas as pd

st.set_page_config(page_title="📚 My Personal Library", layout="centered")
st.title("📚 My Personal Library Manager")
st.write("Keep track of your books easily!")

# Load or initialize session state
if "library" not in st.session_state:
    st.session_state.library = []

# Add new book
st.subheader("➕ Add a Book")
with st.form("book_form"):
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    status = st.selectbox("Reading Status", ["Want to Read", "Currently Reading", "Read"])
    submitted = st.form_submit_button("Add Book")
    if submitted and title and author:
        new_book = {"Title": title, "Author": author, "Status": status}
        st.session_state.library.append(new_book)
        st.success(f"📖 '{title}' added to your library!")

# Display Library
st.subheader("📖 Your Library")
if st.session_state.library:
    df = pd.DataFrame(st.session_state.library)

    # Filter by status
    filter_status = st.selectbox("Filter by status:", ["All"] + df["Status"].unique().tolist())
    if filter_status != "All":
        df = df[df["Status"] == filter_status]

    st.dataframe(df, use_container_width=True)

    # Option to delete a book
    st.subheader("🗑️ Remove a Book")
    book_to_delete = st.selectbox("Select a book to remove:", [f"{b['Title']} by {b['Author']}" for b in st.session_state.library])
    if st.button("Delete Selected Book"):
        index_to_remove = next(i for i, b in enumerate(st.session_state.library)
                               if f"{b['Title']} by {b['Author']}" == book_to_delete)
        st.session_state.library.pop(index_to_remove)
        st.success("Book removed!")
else:
    st.info("Your library is empty. Add some books to get started!")
