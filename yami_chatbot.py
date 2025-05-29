import streamlit as st

# Configuración de la página
st.set_page_config(page_title="LIXY KUN - Evaluador de Autocuidado")

# Título principal
st.title("🐧 LIXY KUN - Tu agente de autocuidado")

# Instrucciones iniciales
st.markdown("""
Hola, soy **LYXI KUN**. Estoy aquí para ayudarte a reflexionar sobre tu bienestar en distintas áreas de tu vida.  
Responde del 1 al 5 cada pregunta, donde **1 = muy mal** y **5 = excelente**.
""")

# Preguntas por categoría
preguntas = {
    "estado_fisico": "¿Cómo calificarías tu estado físico?",
    "estado_mental": "¿Cómo te sientes emocionalmente?",
    "estres": "¿Qué tan estresado/a te sientes?",
    "relaciones": "¿Cómo están tus relaciones con otras personas?",
    "proyecto_vida": "¿Tienes claridad sobre tus metas y proyecto de vida?",
    "autocuidado": "¿Qué tanto te dedicas tiempo a ti mismo/a?"
}

# Diccionario de respuestas
respuestas = {}

# Formulario interactivo
with st.form("formulario_yami"):
    for clave, pregunta in preguntas.items():
        respuestas[clave] = st.slider(pregunta, min_value=1, max_value=5, step=1)
    submit = st.form_submit_button("Evaluar mi autocuidado")

# Análisis de resultados
if submit:
    total = sum(respuestas.values())
    promedio = total / len(respuestas)

    st.markdown("## 🔍 Resultado general")
    if promedio >= 4:
        st.success("¡Excelente! Tienes un buen nivel de autocuidado. 🟢")
    elif promedio >= 3:
        st.warning("Vas bien, pero podrías mejorar en algunas áreas. 🟡")
    else:
        st.error("Hay varias áreas que podrías trabajar. ¡Ánimo! 🔴")

    # Mostrar detalle por área
    st.markdown("### 🧾 Detalle por área:")
    for area, valor in respuestas.items():
        st.write(f"- **{area.replace('_', ' ').capitalize()}**: {valor}/5")

    # Recomendaciones personalizadas por área
    recomendaciones = {
        "estado_fisico": "💪 Intenta hacer al menos 30 minutos de actividad física 3 veces por semana.",
        "estado_mental": "🧘‍♀️ Habla con alguien de confianza o prueba técnicas como la meditación.",
        "estres": "🌿 Tómate pequeños descansos durante el día, respira profundo y duerme bien.",
        "relaciones": "👥 Busca reconectar con alguien cercano o expresar cómo te sientes.",
        "proyecto_vida": "🎯 Escribe tus metas a corto plazo y piensa qué pasos puedes dar hoy.",
        "autocuidado": "🛁 Dedica al menos 10 minutos diarios solo para ti, sin distracciones."
    }

    st.markdown("### 💡 Recomendaciones para mejorar:")
    alguna_recomendacion = False
    for area, valor in respuestas.items():
        if valor <= 3:
            st.write(f"**{area.replace('_', ' ').capitalize()}**: {recomendaciones[area]}")
            alguna_recomendacion = True

    if not alguna_recomendacion:
        st.success("¡Genial! No necesitas recomendaciones en este momento. 🐧🎉")

