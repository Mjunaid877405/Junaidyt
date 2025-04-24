import gradio as gr
from TTS.api import TTS

# Load a multi-speaker TTS model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False)

def clone_voice(text):
    tts.tts_to_file(text=text, file_path="output.wav")
    return "output.wav"

# Gradio UI with public link
gr.Interface(
    fn=clone_voice,
    inputs="text",
    outputs="audio",
    title="Voice Clone Demo"
).launch(share=True)
