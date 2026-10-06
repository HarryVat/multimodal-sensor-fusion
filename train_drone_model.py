import os
from ultralytics import YOLO

def train_model():
    # 1. Ladda in en förtränad YOLO-modell (nano-versionen är bäst och snabbast för bärbara datorer)
    model = YOLO('yolov8n.pt')

    # 2. Hitta sökvägen till din data.yaml som Roboflow skapade åt dig
    # Det är den filen som talar om för AI:n var bilderna ligger
    yaml_path = os.path.abspath("./drone-detection-2/data.yaml")

    print(f"Startar AI-träning med konfigurationen: {yaml_path}")

    # 3. Starta träningen (Vi kör 20 epoker till en början så det går fort att testa)
    # imgsz=640 är standardstorleken på bilderna
    results = model.train(
        data=yaml_path,
        epochs=20,
        imgsz=640,
        device='mps'  # Körs på din Mac-processor. Ändra till device='mps' om du har M1/M2/M3 Mac för hårdvaruacceleratmps!
    )

    print("Träningen är klar! Modellen har sparats i mappen 'runs/detect/train/'")

if __name__ == '__main__':
    train_model()

