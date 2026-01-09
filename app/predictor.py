import logging
import random
from typing import Dict, Union

# Configuración de observabilidad profesional
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("MLOps-Predictor")

# Mapeo oficial FER2013 (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral)
EMOTION_MAP = {
    0: "Angry", 1: "Disgust", 2: "Fear", 
    3: "Happy", 4: "Sad", 5: "Surprise", 6: "Neutral"
}

# Catálogo de recomendaciones (Lógica de Negocio)
RECOMMENDATIONS = {
    "Angry": {"song": "Killing In The Name - R.A.T.M.", "quote": "Canalizá esa energía en algo constructivo."},
    "Disgust": {"song": "No Surprises - Radiohead", "quote": "A veces, menos es más en un mundo saturado."},
    "Fear": {"song": "Fear of the Dark - Iron Maiden", "quote": "El coraje no es la ausencia de miedo, sino actuar a pesar de él."},
    "Happy": {"song": "Shiny Happy People - R.E.M.", "quote": "¡Tu energía es contagiosa, compartila!"},
    "Sad": {"song": "Everybody Hurts - R.E.M.", "quote": "Está bien no estar bien. Mañana sale el sol de nuevo."},
    "Surprise": {"song": "A Kind of Magic - Queen", "quote": "Lo inesperado es la sal de la vida."},
    "Neutral": {"song": "Weightless - Marconi Union", "quote": "Un momento de calma para recuperar el equilibrio."}
}

def get_model_inference() -> int:
    """
    Simula la salida del modelo DenseNet (Accuracy 0.66).
    En producción, aquí iría la carga del .h5 y la transformación del tensor.
    """
    return random.randint(0, 6)

def predict_experience(input_data=None) -> Dict[str, Union[str, dict]]:
    """
    Orquestador del flujo: Inferencia -> Mapeo -> Recomendación.
    Protege la lógica de negocio con manejo de excepciones.
    """
    logger.info("Iniciando proceso de recomendación...")
    
    try:
        # 1. Obtener predicción (índice numérico)
        class_index = get_model_inference()
        emotion = EMOTION_MAP.get(class_index, "Unknown")
        logger.info(f"Modelo detectó clase {class_index} -> Etiqueta: {emotion}")
        
        # 2. Obtener experiencia de usuario
        experience = RECOMMENDATIONS.get(emotion, {
            "song": "Lo-fi Beats", 
            "quote": "Sigue fluyendo, el sistema está procesando."
        })
        
        logger.info(f"Experiencia generada con éxito para emoción: {emotion}")
        
        return {
            "status": "success",
            "emotion": emotion,
            "data": experience
        }

    except Exception as e:
        logger.error(f"Fallo crítico en el pipeline de predicción: {str(e)}")
        return {
            "status": "error",
            "message": "No se pudo generar la recomendación."
        }

if __name__ == "__main__":
    # Prueba rápida de ejecución local
    resultado = predict_experience()
    print(f"\n--- Resultado del Servicio ---\n{resultado}")
