import streamlit as st

def render_button():
    st.subheader("Fitness App Button")
    st.code(
        '''
import streamlit as st

if st.button("Start Workout"):
    st.write("Workout Started!")
        ''', language="python"
    )
    if st.button("Start Workout"):
        st.write("Workout Started!")

def render_card():
    st.subheader("Fitness App Card")
    st.code(
        '''
import streamlit as st

st.markdown(
    """
    <div style="border:1px solid #ccc; padding: 16px; border-radius: 8px; max-width: 300px;">
        <h3>Workout Summary</h3>
        <p>Duration: 45 minutes</p>
        <p>Calories Burned: 350</p>
    </div>
    """, unsafe_allow_html=True
)
        ''', language="python"
    )
    st.markdown(
        """
        <div style="border:1px solid #ccc; padding: 16px; border-radius: 8px; max-width: 300px;">
            <h3>Workout Summary</h3>
            <p>Duration: 45 minutes</p>
            <p>Calories Burned: 350</p>
        </div>
        """, unsafe_allow_html=True
    )

def render_modal():
    st.subheader("Fitness App Modal")
    st.code(
        '''
import streamlit as st

if st.button("Show Modal"):
    st.session_state.show_modal = True

if 'show_modal' in st.session_state and st.session_state.show_modal:
    st.markdown(
        """
        <div style="position: fixed; top: 20%; left: 30%; width: 40%; background: white; border: 2px solid #000; padding: 20px; z-index: 1000;">
            <h2>Modal Title</h2>
            <p>This is a modal content for fitness app.</p>
            <button onclick="window.location.reload();">Close</button>
        </div>
        """, unsafe_allow_html=True
    )
        ''', language="python"
    )
    if st.button("Show Modal"):
        st.session_state.show_modal = True

    if 'show_modal' in st.session_state and st.session_state.show_modal:
        st.markdown(
            """
            <div style="position: fixed; top: 20%; left: 30%; width: 40%; background: white; border: 2px solid #000; padding: 20px; z-index: 1000;">
                <h2>Modal Title</h2>
                <p>This is a modal content for fitness app.</p>
                <button onclick="window.location.reload();">Close</button>
            </div>
            """, unsafe_allow_html=True
        )

def main():
    st.title("Fitness App Component Library")
    render_button()
    st.markdown("---")
    render_card()
    st.markdown("---")
    render_modal()

if __name__ == "__main__":
    main()
