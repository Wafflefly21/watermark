from typing import List
from pydantic import BaseModel
from lama_cleaner.server import main

class FakeArgs(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080
    model: str = 'lama'
    hf_access_token: str = ""
    sd_disable_nsfw: bool = False
    sd_cpu_textencoder: bool = True
    sd_run_local: bool = False
    device: str = "cpu"
    gui: bool = False
    gui_size: List[int] = [1000, 1000]
    input: str = ''
    disable_model_switch: bool = True
    debug: bool = False

if __name__ == "__main__":
    main(FakeArgs())
