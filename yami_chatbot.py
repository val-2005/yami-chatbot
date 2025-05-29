import streamlit as st

st.set_page_config(page_title="YAMI - Evaluador de Autocuidado")

st.title("🤖 YAMI - Tu agente de autocuidado")

st.markdown("""
Hola, soy **YAMI**, tu guía para evaluar tu autocuidado en diferentes aspectos de tu vida.  
Responde del **1 al 5** cada afirmación:  
**1 = Muy en desacuerdo** | **5 = Muy de acuerdo**  
""")

# Preguntas organizadas por subtema
subtemas = {
    "Estado físico del adulto": [
        "Siento que mi resistencia física se mantiene estable a lo largo del día.",
        "He notado cambios leves en mi visión, fuerza muscular o reflejos, pero no afectan significativamente mi vida diaria.",
        "Realizo actividad física al menos 30 minutos, cinco días a la semana.",
        "Procuro seguir una alimentación equilibrada y evitar hábitos nocivos como el sedentarismo o el consumo excesivo de grasas y azúcares.",
        "Soy consciente de que las decisiones que tomo hoy influyen en mi bienestar físico futuro."
    ],
    "Estrés y manejo emocional": [
        "Soy capaz de identificar rápidamente cuándo una situación me está generando estrés.",
        "Cuando enfrento un problema, busco estrategias para modificar el entorno o resolver la causa del conflicto.",
        "Tengo herramientas personales (respiración, distracción, diálogo interno, etc.) para calmarme en momentos de tensión emocional.",
        "Considero que el manejo de mis emociones influye directamente en mis decisiones personales y laborales.",
        "Conozco bien lo que me afecta emocionalmente y esto me ayuda a controlar mis reacciones."
    ],
    "Proyecto de vida y sentido": [
        "Tengo metas claras que orientan las decisiones importantes que tomo en mi vida.",
        "Siento que mi vida tiene un propósito que le da sentido a lo que hago cada día.",
        "He identificado lo que me apasiona y lo que sé hacer bien, y procuro integrar ambas cosas en mi vida.",
        "Confío en mi capacidad para lograr los objetivos que me propongo, incluso cuando enfrento dificultades.",
        "Conozco mis valores y los tengo presentes al tomar decisiones sobre mi futuro."
    ],
    "Relaciones y apoyo social": [
        "Cuento con personas cercanas con quienes puedo compartir mis emociones, pensamientos y experiencias.",
        "Mi red de apoyo social (familia, amigos, comunidad) contribuye positivamente a mi bienestar emocional.",
        "En momentos difíciles, me siento acompañado/a por personas que me brindan apoyo afectivo o práctico.",
        "Siento que el entorno social en el que vivo favorece la interacción, el cuidado mutuo y la conexión entre personas.",
        "Creo que mantener relaciones significativas es esencial para tener una buena calidad de vida a lo largo del envejecimiento."
    ],
    "Salud mental y resiliencia": [
        "Me considero una persona capaz de adaptarme a los cambios y dificultades que surgen en mi entorno.",
        "Mantengo una actitud positiva ante los desafíos de la vida y procuro aprender de ellos.",
        "Me siento satisfecho/a conmigo mismo/a y puedo manejar mis emociones sin sentirme abrumado/a.",
        "Soy capaz de mantener relaciones personales duraderas, abiertas y basadas en la confianza mutua.",
        "Creo que, a pesar de las experiencias difíciles, puedo seguir creciendo como persona y construir un futuro positivo."
    ],
    "Autocuidado y prevención": [
        "Realizo actividades cotidianas que me permiten cuidar de mi salud física, como alimentarme bien, dormir adecuadamente y realizar ejercicio.",
        "Considero que tengo la capacidad de tomar decisiones responsables sobre mi salud y bienestar.",
        "Creo que el autocuidado también debe atender aspectos emocionales, sociales y espirituales, no solo físicos.",
        "Me esfuerzo por prevenir enfermedades mediante chequeos médicos y prácticas saludables.",
        "Mantener relaciones sociales positivas y tener una actitud optimista contribuye a mi salud y calidad de vida."
    ]
}

# Recomendaciones nuevas por subtema
recomendaciones = {
    "Estado físico del adulto": """• Realizar ejercicio físico regular adaptado (caminar, yoga, natación o gimnasia suave) para mantener movilidad, fuerza y equilibrio.
• Mantener una alimentación balanceada rica en frutas, verduras, proteínas y agua para conservar la energía y prevenir enfermedades.
• Asistir a chequeos médicos periódicos para monitorear la salud, detectar problemas tempranamente y ajustar tratamientos.""",

    "Estrés y manejo emocional": """• Practicar técnicas de relajación y respiración profunda diariamente para reducir la ansiedad y controlar el estrés.
• Participar en grupos de apoyo o terapia emocional donde puedan compartir experiencias y fortalecer su bienestar psicológico.
• Realizar actividades recreativas y sociales que generen placer y distraigan la mente, como la pintura, la música o el baile.""",

    "Proyecto de vida y sentido": """• Fijar metas personales alcanzables y proyectos que motiven (como aprender algo nuevo, voluntariado o cuidar un huerto).
• Reflexionar sobre su historia y legado para fortalecer la autoestima y encontrar propósito en sus experiencias.
• Mantenerse activos en roles familiares y sociales para sentirse útiles y valorados en la comunidad.""",

    "Relaciones y apoyo social": """• Mantener contacto regular con familiares y amigos a través de llamadas, visitas o reuniones para evitar el aislamiento.
• Participar en actividades comunitarias o clubes de personas mayores para crear nuevos vínculos sociales.
• Buscar apoyo cuando lo necesiten y ofrecer ayuda a otros, fomentando relaciones de confianza y reciprocidad.""",

    "Salud mental y resiliencia": """• Desarrollar hábitos de pensamiento positivo y autoaceptación, enfocándose en sus fortalezas y logros.
• Enfrentar dificultades buscando soluciones activas, aprendiendo a adaptarse y a buscar ayuda si es necesario.
• Practicar actividades que fortalezcan la mente, como leer, hacer juegos de memoria o aprender cosas nuevas.""",

    "Autocuidado y prevención": """• Adoptar rutinas diarias de higiene, alimentación y descanso para preservar la salud integral.
• Informarse sobre señales de alerta y acudir a revisiones médicas regularmente para prevenir enfermedades.
• Involucrar a la familia y cuidadores en su cuidado, asegurando apoyo y seguimiento constante."""
}

# Recolección de respuestas
respuestas = {}
with st.form("formulario_yami"):
    for subtema, preguntas in subtemas.items():
        st.markdown(f"### {subtema}")
        for i, pregunta in enumerate(preguntas, 1):
            key = f"{subtema}_{i}"
            respuestas[key] = st.slider(pregunta, 1, 5, 3)
    submit = st.form_submit_button("Evaluar")

# Evaluación
if submit:
    st.markdown("## 🔍 Resultados por subtema:")
    puntajes_subtemas = {}
    total_general = 0

    for subtema, preguntas in subtemas.items():
        claves = [f"{subtema}_{i}" for i in range(1, 6)]
        puntajes = [respuestas[k] for k in claves]
        promedio = sum(puntajes) / len(puntajes)
        puntajes_subtemas[subtema] = promedio
        total_general += promedio
        st.write(f"- **{subtema}**: {promedio:.2f}/5")

    promedio_total = total_general / len(subtemas)

    st.markdown("## 🧠 Evaluación general:")
    if promedio_total >= 4:
        st.success("¡Excelente! Tienes un alto nivel de autocuidado. 🟢")
    elif promedio_total >= 3:
        st.warning("Tu autocuidado es aceptable, pero podrías mejorar en algunas áreas. 🟡")
    else:
        st.error("Hay aspectos importantes de tu autocuidado que podrías fortalecer. 🔴")

    st.markdown("## 💡 Recomendaciones personalizadas:")
    alguna_recomendacion = False
    for subtema, promedio in puntajes_subtemas.items():
        if promedio <= 4:
            st.write(f"**{subtema}**")
            st.markdown(recomendaciones[subtema])
            alguna_recomendacion = True

    if not alguna_recomendacion:
        st.success("¡No necesitas recomendaciones en este momento! Sigue así. 🎉")

