from typing import Optional
from fastapi import FastAPI, File, UploadFile
from service import display_image_8bpp, clear_display
from IT8951.display import AutoEPDDisplay

print('Initializing EPD...')

display = AutoEPDDisplay(vcom=-1.39, rotate=None, spi_hz=24000000)

app = FastAPI()

@app.get("/healthz")
def healthCheck():
    return "OK"

@app.get("/clear")
def clear():
    clear_display(display)
    return "OK"

@app.post("/display")
def display_image(file: UploadFile = File(...)):
    clear_display(display)
    display_image_8bpp(display, file.file)
    return {"Hello": "World"}
