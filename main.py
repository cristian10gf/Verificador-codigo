from turtle import color
import flet as ft
from src.utils.verificar import revisar_codigo, encontrar_x, consultar_codigo

BG = '#041955'
FG = '#3450a1'
PINK= '#eb06ff'
FWG = '#97b4ff'
RED = '#ff0000'
fondo = '#041955'


def contenedor_text(texto):
  return ft.Container(
    width=250,
    height=200,
    bgcolor= FG,
    border_radius=35, 
    alignment=ft.alignment.center,
    padding=ft.padding.only(20,20,20,20),
    content=texto,
    border=ft.Border(top=ft.BorderSide(color=PINK, width=2), bottom=ft.BorderSide(color=PINK, width=2))
  )

 
def main(page: ft.Page):
  page.title = "Verificador de codigo"
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  page.bgcolor = fondo

  # ____Gerenal____

  tipo_codigo = ft.Text("", color='white', size=20, text_align=ft.TextAlign.CENTER)

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
  
  main = ft.ElevatedButton(text="Verificar", on_click=lambda e: mover(e,"/"), bgcolor=BG, color='white')
  revisar = ft.ElevatedButton(text="Revisar", on_click=lambda e: mover(e,"/revisar"), bgcolor=BG, color='white')
  digito_control = ft.ElevatedButton(text="Buscar X", on_click=lambda e: mover(e,"/encontrar_x"), bgcolor=BG, color='white')

  opciones = ft.Container(
    bgcolor=FWG,
    padding=ft.padding.only(10,20,10,20),
    border_radius=20,
    width=400,
    content=ft.Row(
      controls=[main, revisar, digito_control],
      alignment=ft.MainAxisAlignment.CENTER,
    )
  )


  # ____ main______

  def analizar_codigo(e):
    print(codigo.value)
    tipo_codigo.value = revisar_codigo(codigo.value)
    page.update()

  boton_verificar = ft.ElevatedButton(
    color= 'white',
    text="Verificar",
    on_click=analizar_codigo
  )

  verificando = ft.Container(
    width=400,
    height=550,
    bgcolor= FG,
    border_radius=35, 
    padding=ft.padding.only(20,50,20,50),
    content= ft.Column(
      controls=[
        ft.Text("Ingrese el codigo a verificar"),
        codigo,
        boton_verificar,
        contenedor_text(tipo_codigo)
      ],
      alignment=ft.MainAxisAlignment.CENTER,
      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
  )

  # ____Revisar____

  def consultar_codigo_tipo(e):
    tipo_codigo.value = str(consultar_codigo(codigo.value, escoger_codigo.value))
    page.update()

  boton_consultar = ft.ElevatedButton(
    color= 'white',
    text="Consultar",
    on_click=consultar_codigo_tipo
  )

  escoger_codigo = ft.Dropdown(
    label="tipo",
    hint_text="tipo de codigo a verificar",
    options=[
      ft.dropdown.Option("ISIN"),
      ft.dropdown.Option("ISBN-10"),
      ft.dropdown.Option("ISBN-13"),
      ft.dropdown.Option("EAN-8"),
      ft.dropdown.Option("EAN-13"),
     ],
     border_radius=20,
     bgcolor=FWG,
     alignment=ft.alignment.center,
    autofocus=True,
  )

  consultar = ft.Container(
    width=400,
    height=550,
    bgcolor= FG,
    border_radius=35, 
    padding=ft.padding.only(20,50,20,50),
    content=ft.Column(
    controls=[
      ft.Text("Ingrese el codigo a consultar"),
      codigo,
      escoger_codigo,
      boton_consultar,
      contenedor_text(tipo_codigo)
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
  ))

  # ____Encontrar X____

  def buscar_x(e):
    tipo_codigo.value = str(encontrar_x(codigo.value))
    page.update()

  boton_encontrar_x = ft.ElevatedButton(
    color= 'white',
    text="Encontrar X",
    on_click=buscar_x
  )

  encontrar_x_contenido = ft.Container(
    width=400,
    height=550,
    bgcolor= FG,
    border_radius=35, 
    padding=ft.padding.only(20,50,20,50),
    content=ft.Column(
      controls=[
        ft.Text("Ingrese el codigo a buscar el valor de X"),
        codigo,
        boton_encontrar_x,
        contenedor_text(tipo_codigo)
      ],
      alignment=ft.MainAxisAlignment.CENTER,
      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
  )

  # ____Configuracion de la pagina____

  page.on_route_change = route_change

  page.add(opciones)
  page.add(verificando)


ft.app(target=main)
