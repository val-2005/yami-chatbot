import streamlit as st

st.set_page_config(page_title="YAMI - Evaluador de Autocuidado")

st.title("🤖 YAMI - Tu agente de autocuidado")

st.markdown("""
Hola, soy **YAMI**. Estoy aquí para ayudarte a reflexionar sobre tu bienestar en distintas áreas de tu vida.  
Responde del 1 al 5 cada pregunta, donde **1 = muy mal** y **5 = excelente**.
""")

preguntas = {
    "estado_fisico": "¿Cómo calificarías tu estado físico?",
    "estado_mental": "¿Cómo te sientes emocionalmente?",
    "estres": "¿Qué tan estresado/a te sientes?",
    "relaciones": "¿Cómo están tus relaciones con otras personas?",
    "proyecto_vida": "¿Tienes claridad sobre tus metas y proyecto de vida?",
    "autocuidado": "¿Qué tanto te dedicas tiempo a ti mismo/a?"
}

respuestas = {}

with st.form("formulario_yami"):
    for clave, pregunta in preguntas.items():
        respuestas[clave] = st.slider(pregunta, min_value=1, max_value=5, step=1)

    submit = st.form_submit_button("Evaluar mi autocuidado")

if submit:
    total = sum(respuestas.values())
    promedio = total / len(respuestas)

    st.markdown("## 🔍 Resultado")
    if promedio >= 4:
        st.success("¡Excelente! Tienes un buen nivel de autocuidado. 🟢")
    elif promedio >= 3:
        st.warning("Vas bien, pero podrías mejorar en algunas áreas. 🟡")
    else:
        st.error("Hay varias áreas que podrías trabajar. ¡Ánimo! 🔴")

    st.markdown("### 🧾 Detalle por área:")
    for area, valor in respuestas.items():
        st.write(f"- **{area.replace('_', ' ').capitalize()}**: {valor}/5")
