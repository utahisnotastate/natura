"""
NATURA COMMAND CENTER
The Unified Entry Point.
"""
import sys
import argparse
from natura import GenerativeModel, tycoon


def launch_evie():
    """Chat with the Core"""
    print(">> SUMMONING EVIE...")
    model = GenerativeModel("evie")
    while True:
        q = input("YOU: ")
        if q in ['exit', 'quit']:
            break
        print(model.generate_content(q).text)


def launch_mirage():
    """Launch the Video Studio"""
    print(">> LAUNCHING MIRAGE STUDIO...")
    from apps import mirage_studio  # noqa: F401  (side-effect: defines app)
    mirage_studio.app.run(port=5000)


def launch_genesis():
    """Launch the AutoML Lab"""
    print(">> LAUNCHING GENESIS LAB...")
    from apps import genesis_lab  # noqa: F401
    genesis_lab.app.run(port=8000)


def launch_tycoon():
    """Run Business Generator"""
    print(">> STARTING TYCOON PROTOCOL...")
    from natura.tycoon import TycoonProtocol
    t = TycoonProtocol()
    t.launch_wizard()


def launch_codex():
    """Launch the Notebook Killer"""
    print(">> OPENING THE CODEX...")
    from apps import codex_reader  # noqa: F401
    codex_reader.app.run(port=9000)


def launch_holodeck():
    """Launch the 3D Ray Tracing Studio"""
    print(">> ENGAGING LIQUID PHOTON ENGINE...")
    print(">> WARNING: NO GPU DETECTED. OPTIMIZING FOR C2 INSTANCE...")
    from natura.photon import Holodeck

    deck = Holodeck()
    prompt = input("ENTER REALITY PROMPT: ")
    output = deck.render_reality(prompt)
    print(f"RENDER COMPLETE: {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Natura Reality Engine")
    parser.add_argument("mode", choices=["chat", "mirage", "genesis", "tycoon", "codex","holodeck"], help="Which interface to launch")

    args = parser.parse_args()

    if args.mode == "chat":
        launch_evie()
    elif args.mode == "mirage":
        launch_mirage()
    elif args.mode == "genesis":
        launch_genesis()
    elif args.mode == "tycoon":
        launch_tycoon()
    elif args.mode == "holodeck":
        launch_holodeck()
    elif args.mode == "codex":
        launch_codex()
