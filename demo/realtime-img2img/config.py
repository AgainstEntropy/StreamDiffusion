from typing import NamedTuple
import argparse
import os


class Args(NamedTuple):
    host: str
    port: int
    reload: bool
    mode: str
    max_queue_size: int
    timeout: float
    safety_checker: bool
    taesd: bool
    ssl_certfile: str
    ssl_keyfile: str
    debug: bool
    acceleration: str
    use_denoising_batch: bool
    cfg_type: str

    def pretty_print(self):
        print("\n")
        for field, value in self._asdict().items():
            print(f"{field}: {value}")
        print("\n")


MAX_QUEUE_SIZE = int(os.environ.get("MAX_QUEUE_SIZE", 0))
TIMEOUT = float(os.environ.get("TIMEOUT", 0))
SAFETY_CHECKER = os.environ.get("SAFETY_CHECKER", None) == "True"
USE_TAESD = os.environ.get("USE_TAESD", "True") == "True"
default_host = os.getenv("HOST", "0.0.0.0")
default_port = int(os.getenv("PORT", "7860"))
default_mode = os.getenv("MODE", "default")

parser = argparse.ArgumentParser(description="Run the app")
parser.add_argument("--host", type=str, default=default_host, help="Host address")
parser.add_argument("--port", type=int, default=default_port, help="Port number")
parser.add_argument("--reload", action="store_true", help="Reload code on change")
parser.add_argument(
    "--mode", type=str, default=default_mode, help="App Inferece Mode: txt2img, img2img"
)
parser.add_argument(
    "--max-queue-size",
    dest="max_queue_size",
    type=int,
    default=MAX_QUEUE_SIZE,
    help="Max Queue Size",
)
parser.add_argument("--timeout", type=float, default=TIMEOUT, help="Timeout")
parser.add_argument(
    "--safety-checker",
    dest="safety_checker",
    action="store_true",
    default=SAFETY_CHECKER,
    help="Safety Checker",
)
parser.add_argument(
    "--taesd",
    dest="taesd",
    action="store_true",
    help="Use Tiny Autoencoder",
)
parser.add_argument(
    "--no-taesd",
    dest="taesd",
    action="store_false",
    help="Use Tiny Autoencoder",
)
parser.add_argument(
    "--ssl-certfile",
    dest="ssl_certfile",
    type=str,
    default=None,
    help="SSL certfile",
)
parser.add_argument(
    "--ssl-keyfile",
    dest="ssl_keyfile",
    type=str,
    default=None,
    help="SSL keyfile",
)
parser.add_argument(
    "--debug",
    action="store_true",
    default=False,
    help="Debug",
)
parser.add_argument(
    "--acceleration",
    type=str,
    default="tensorrt",
    choices=["none", "xformers", "sfast", "tensorrt"],
    help="Acceleration",
)
parser.add_argument(
    "--use-denoising-batch",
    action="store_true",
    default=True,
    help="Use denoising batch",
)
parser.add_argument(
    "--cfg-type",
    dest="cfg_type",
    type=str,
    default="initialize",
    choices=["none", "full", "self", "initialize"],
    help="Config type",
)
parser.set_defaults(taesd=USE_TAESD)

args = Args(**vars(parser.parse_args()))
