from app.predictor import predict_experience

def run_app():
    # Simulamos la entrada de datos (la imagen que vendrá del usuario)
    result = predict_experience({"image": "sample_data"})
    
    if result["status"] == "success":
        print(f"Emoción: {result['emotion']}")
        print(f"Canción sugerida: {result['data']['song']}")
        print(f"Frase: {result['data']['quote']}")
    else:
        print(f"Error: {result['message']}")

if __name__ == "__main__":
    run_app()