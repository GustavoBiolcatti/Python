from cx_Freeze import setup, Executable

setup(
    name="Calculo Salario",
    version="0.8",
    description=".py to .exe",
    executables=[Executable("Calculo_Salario_Interface.py")]
)
