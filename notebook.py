import openai
import streamlit as st
from streamlit_tags import st_tags

# Set the OpenAI API key
openai.api_key = st.secrets["openai_key"]

# Define the function to call GPT-3.5-turbo API
def ask_gpt3_turbo(message, chat_log=None):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Anda adalah seorang sales notebook/laptop yang ulung. Anda mampu memahami apa yang terbaik untuk konsumen Anda. Berikan beberapa rekomendasi notebook/laptop untuk konsumen Anda dengan menyebutkan kelebihan, kekurangan, dan spesifikasi notebook/laptop tersebut. Jangan berikan rekomendasi lain di luar notebook/laptop. Berikan rekomendasi minimal sebanyak 5 jenis.",
            },
            {"role": "user", "content": message},
        ],
    )
    # Returning the response
    return response.choices[0].message.content

  # Streamlit app
def main():
    st.title("Notebook Recommendation")

    layar = st_tags(label="Tentukan jenis layar yang Anda inginkan")
    sistem_operasi = st.multiselect("Sistem operasi", ["Windows", "MacOS", "Linux"])
    prosesor = st.text_input(
        "(optional) Jenis prosesor yang Anda cari"
    )
    ram = st.number_input(
        "(optional) RAM (GB)", min_value=1, max_value=1000, step=1
    )
    tipe_storage = sistem_operasi = st.multiselect("Tipe storage yang Anda inginkan", ["HDD", "SSD"])
    ukuran_storage = st.number_input(
        "(optional) Ukuran storage (GB)", min_value=1, max_value=1000, step=1
    )
    ketahanan_baterai = st.number_input(
        "(optional) Ketahanan baterai (jam)", min_value=1, max_value=168, step=1
    )
    harga = st.radio(
        "Preferensi harga", ("Murah", "Menengah", "Mahal")
    )

    if st.button("Submit"):

        prompt = f"""
          Tolong berikan saya rekomendasi notebook/laptop dengan menyebutkan kelebihan dan kekurangan notebook/laptop tersebut serta berikan range harga dalam Rupiah dan saran sesuai dengan spesifikasi berikut.

                Spesifikasi layar (minimal): {layar}
                Sistem operasi (Jika hanya Windows, tidak boleh ada MacOS dan Linux): {sistem_operasi}
                Prosesor: {prosesor}
                RAM (minimal): {ram} GB
                Tipe Storage: {tipe_storage}
                Ukuran Storage (minimal): {ukuran_storage} GB
                Ketahanan baterai (minimal): {ketahanan_baterai} jam
                Harga: {harga}

                Format output:
                # [Nama Notebook/Laptop]
                ## Spesifikasi:
                [konten]

                ## Kelebihan:
                [konten]

                ## Kekurangan:
                [konten]

                ## Range Harga:
                [konten]

                ## Saran:
                [konten]
        """

        # user_input += additional_prompt
        ai_response = ask_gpt3_turbo(prompt)

        # print(ai_response)
        st.markdown(f"{ai_response}", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
