# built-in dependencies
from typing import Any

# project dependencies
from face.core.basemodels import (
    VGGFace,
    OpenFace,
    FbDeepFace,
    DeepID,
    ArcFace,
    SFace,
    Dlib,
    Facenet,
    GhostFaceNet,
)
from face.core.extendedmodels import Age, Gender, Race, Emotion
from face.core.spoofmodels import FasNet


def build_model(model_name: str) -> Any:
    """
    This function builds a deepface model
    Parameters:
            model_name (string): face recognition or facial attribute model
                    VGG-Face, Facenet, OpenFace, DeepFace, DeepID for face recognition
                    Age, Gender, Emotion, Race for facial attributes

    Returns:
            built model class
    """

    # singleton design pattern
    global model_obj

    models = {
        "VGG-Face": VGGFace.VggFaceClient,
        "OpenFace": OpenFace.OpenFaceClient,
        "Facenet": Facenet.FaceNet128dClient,
        "Facenet512": Facenet.FaceNet512dClient,
        "DeepFace": FbDeepFace.DeepFaceClient,
        "DeepID": DeepID.DeepIdClient,
        "Dlib": Dlib.DlibClient,
        "ArcFace": ArcFace.ArcFaceClient,
        "SFace": SFace.SFaceClient,
        "GhostFaceNet": GhostFaceNet.GhostFaceNetClient,
        "Emotion": Emotion.EmotionClient,
        "Age": Age.ApparentAgeClient,
        "Gender": Gender.GenderClient,
        "Race": Race.RaceClient,
        "Fasnet": FasNet.Fasnet,
    }

    if not "model_obj" in globals():
        model_obj = {}

    if not model_name in model_obj.keys():
        model = models.get(model_name)
        if model:
            model_obj[model_name] = model()
        else:
            raise ValueError(f"Invalid model_name passed - {model_name}")

    return model_obj[model_name]
