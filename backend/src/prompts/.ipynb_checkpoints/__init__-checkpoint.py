"""Define and create prompts for the application to run"""
import os
from pathlib import Path
from langchain.prompts import PromptTemplate


def load_prompt_template(path, input_variables):
    with open(str(path), "r") as fp:
        return PromptTemplate(template=fp.read(), input_variables=input_variables)


prompts = Path(os.path.realpath(__file__)).parent.parent / "prompts"

prompt_generate_text = load_prompt_template(
    prompts / "base_prompt.txt", ["text"]
)
