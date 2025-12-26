#!/usr/bin/env python3

import base64
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
import pyperclip
import argparse
import yaml

config = yaml.safe_load(open("config.yaml","r").read())

if config is None:
    config = {}

MODEL_NAME = config.get("model_name", "google/gemini-2.0-flash-001")

DEFAULT_PROMPT = "Convert this document to markdown and Katex for calculations / maths. Provide the content as it is provided. Don't remove or add anything. Your only role is to provide some formatting and conversion. Don't translate the content. Return only the content in markdown format with Katex for maths."
PROMPT_OCR = config.get("prompt_ocr", DEFAULT_PROMPT)


def get_api_key():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError(
            "API key not found. Please set the OPENROUTER_API_KEY environment variable."
        )
    return api_key


client = OpenAI(api_key=get_api_key(), base_url="https://openrouter.ai/api/v1")


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def generate_image_url(base64_image):
    image_url = f"data:image/png;base64,{base64_image}"

    return image_url


def ocr_katex_from_image(image_path):
    base64_image = encode_image_to_base64(image_path)
    image_url = generate_image_url(base64_image)

    prompt = PROMPT_OCR

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_url}},
                ],
            },
        ],
    )

    latex_code = response.choices[0].message.content

    return latex_code


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", help="Path to the image file")
    args = parser.parse_args()
    latex_code = ocr_katex_from_image(args.image_path)
    if latex_code:
        lines = latex_code.splitlines()
        if lines[0].strip().startswith("```markdown") or lines[0].strip().startswith(
            "```"
        ):
            latex_code = "\n".join(lines[1:-1])
    pyperclip.copy(latex_code)
    print("LaTeX code copied to clipboard.")
