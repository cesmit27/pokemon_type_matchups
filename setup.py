from cx_Freeze import setup, Executable
import sys

build_exe_options = {
    "packages": ["tkinter", "json"],
    "include_files": ["pokemon_data.json", "type_effectiveness.json"]
}

#removes the console window on windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Pokémon Type Checker",
    version="1.0",
    description="Learn what types your Pokémon resists and what types it is weak to.",
    options={"build_exe": build_exe_options},
    executables=[Executable("poketest.py", base=base)]
)
