import flet as ft
from utils.verificar import revisar_codigo

tipo_codigo = ft.Text("")

def analizar_codigo(e):
    print(codigo.value)
    tipo_codigo.value = revisar_codigo(codigo.value)
    #page.update()


codigo = ft.TextField(label="Codigo")

boton = ft.ElevatedButton(
  text="Verificar",
  on_click=analizar_codigo
)

verificando = ft.Column(
    controls=[
      ft.Text("Ingrese el codigo a verificar"),
      codigo,
      boton,
      tipo_codigo
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    height=400,
    width=400,
    #aspect_ratio=16/9
)