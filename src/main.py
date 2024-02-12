from re import I
from turtle import bgcolor, onclick
import flet as ft
from utils.verificar import revisar_codigo, encontrar_x as buscar_x, consultar_codigo
 
def main(page: ft.Page):
  page.title = "Verificador de codigo"
  page.vertical_alignment = ft.MainAxisAlignment.CENTER

  # ____Gerenal____

  tipo_codigo = ft.Text("")

  codigo = ft.TextField(label="Codigo")

  # _______Menu________

  def route_change(e: ft.RouteChangeEvent):
    page.clean()
    page.add(opciones)
    if e.route == "/":
      page.add(verificando)
    elif e.route == "/revisar":
      page.add(consultar)
    elif e.route == "/encontrar_x":
      page.add(encontrar_x_contenido)
      
  def mover(e, valor):
    page.route = valor
    page.update()
  
  main = ft.ElevatedButton(text="Verificar", on_click=lambda e: mover(e,"/"))
  revisar = ft.ElevatedButton(text="Revisar", on_click=lambda e: mover(e,"/revisar"))
  encontrar_x = ft.ElevatedButton(text="Buscar X", on_click=lambda e: mover(e,"/encontrar_x"))

  opciones = ft.Row(
    controls=[main, revisar, encontrar_x],
    alignment=ft.MainAxisAlignment.CENTER,
  )


  # ____ main______

  def analizar_codigo(e):
    print(codigo.value)
    tipo_codigo.value = revisar_codigo(codigo.value)
    page.update()

  boton_verificar = ft.ElevatedButton(
    text="Verificar",
    on_click=analizar_codigo
  )

  verificando = ft.Column(
    controls=[
      ft.Text("Ingrese el codigo a verificar"),
      codigo,
      boton_verificar,
      tipo_codigo
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    height=400,
    width=400,
    #aspect_ratio=16/9
  )

  # ____Revisar____

  def consultar_codigo_tipo(e):
    tipo_codigo.value = str(consultar_codigo(codigo.value, escoger_codigo.value))
    page.update()

  boton_consultar = ft.ElevatedButton(
    text="Consultar",
    on_click=consultar_codigo_tipo
  )

  escoger_codigo = ft.Dropdown(
    label="codigo",
    hint_text="Seleccione el tipo de codigo a verificar",
    options=[
      ft.dropdown.Option("ISIN"),
      ft.dropdown.Option("ISBN-10"),
      ft.dropdown.Option("ISBN-13"),
      ft.dropdown.Option("EAN-8"),
      ft.dropdown.Option("EAN-13"),
     ],
    autofocus=True,
  )

  consultar = ft.Column(
    controls=[
      ft.Text("Ingrese el codigo a consultar"),
      codigo,
      escoger_codigo,
      boton_consultar,
      tipo_codigo
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    height=400,
    width=400,
    #aspect_ratio=9/16
  )

  # ____Encontrar X____

  def buscar_x (e):
    tipo_codigo.value = buscar_x(codigo.value)
    page.update()

  boton_encontrar_x = ft.ElevatedButton(
    text="Encontrar X",
    on_click=analizar_codigo
  )

  encontrar_x_contenido = ft.Column(
    controls=[
      ft.Text("Ingrese el codigo a buscar el valor de X"),
      codigo,
      boton_encontrar_x,
      tipo_codigo
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    height=400,
    width=400,
    #aspect_ratio=9/16
  )

  # ____Configuracion de la pagina____

  page.on_route_change = route_change

  page.add(opciones)
  page.add(verificando)


ft.app(target=main)