from predictor import make_prediction

def run_app():
    result = make_prediction({"test": 1})
    print(f"Resultado: {result}")

if __name__ == "__main__":
    run_app()