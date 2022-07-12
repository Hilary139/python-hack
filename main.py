
# IMPORTING DEPENDENCY_MANAGER_PATH
import gradio as gr  # Ui Library
from transformers import pipeline  # transformers library


# LOADING UP PIPELINE
translation_pipeline = pipeline('translation_en_to_de')


# TRANSLATION CONTROLLER_TRACE_DATA_KEY
results = translation_pipeline('I love Hilda')

results[0]['translation_text']

#  CREATING GRADIO FUNCTION AND INTERFACE
def translate_transformrs(from_text):
    results = translation_pipeline(from_text)
    return results[0]['translation_text']


# CREATING THE USER INTERFACE
interface = gr.Interface(fn=translate_transformrs, inputs=gr.input.Textbox(
    lines=2, placeholder='text to translate'), outputs='text')
