import gradio as gr
import numpy as np
import io
import base64
import pathlib
import textwrap
import os
os.environ['PORT1'] = '8080'
from IPython.display import display
from IPython.display import Markdown
import google.generativeai as genai
from PIL import Image

#apiKey = userdata.get('GOOGLE_API_KEY')

from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))



model = genai.GenerativeModel('gemini-1.5-pro')




def generate_aid(image):
    response = model.generate_content(["Analyze the uploaded image to identify the condition or injury. "
    "Do not provide any information outside of medical diagnosis, treatment, or first-aid steps. "
     "Do not provide any general information, non-medical advice, or off-topic responses."
    "Provide a detailed response in the following structured format: "
    "Condition Detected: Name of the condition or injury (e.g., Minor Burn, Bruise, Infection). "
    "Severity Level: Mild, Moderate, or Severe (based on visual analysis). "
    "Symptoms Identified: List the symptoms visible in the image (e.g., redness, swelling, bruising). "
    "Immediate First-Aid Steps:Provide clear and actionable steps to address the condition. "
    "When to Seek Medical Help: Mention signs that require professional attention (e.g., severe pain, signs of infection). "
    "Preventive Tips (Optional) Suggest ways to prevent similar injuries in the future. "
    "End with a reminder: 'Consult a healthcare professional if symptoms worsen or persist.'",
    image])
    return response.text

interface = gr.Interface(fn=generate_aid,
                    inputs=gr.Image(label="Upload or Capture Image", type="pil"),
                    outputs=gr.Textbox(label="QuickAid to the Rescue! 🚑",placeholder="Hang tight, your QuickAid guide is on its way..."),
                    title="QuickAid: Your Pocket First-Aid Companion",
                    description=("Please note that while the model works to offer the most accurate advice possible, the results may occasionally vary."
                                 "To enhance accuracy, future updates will allow you to provide additional context such as age and  highlight areas of concern in the image, A symptom checker and more user inputs will also be integrated to improve precision."
                                  "For now, results might not be perfect, so it's always best to consult a healthcare professional if you're unsure or if symptoms persist."),
                    allow_flagging="never",
                    examples=["/content/B1.jpg", "/content/B2.jpg"])
interface.launch(debug = True)
