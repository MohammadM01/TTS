import torch
from TTS.api import TTS
import gradio as gr

device = "cuda" if torch.cuda.is_available() else "cpu"

def generated_audio(text=""):
    tts=TTS(model_name='tts_models/en/ljspeech/fast_pitch').to(device)
    wav = tts.tts(text=text, duration_scaling_factor=1.5)
    tts.tts_to_file(text=text,file_path="outputs/output.wav")
    return "outputs/output.wav"

demo = gr.Interface(
    fn=generated_audio,
    inputs=[gr.Text(label="Text"),],
    outputs=[gr.Audio(label="Audio"),],
)

demo.launch()