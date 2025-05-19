import flet as ft
import requests

# Funciones
# crear vendedores
# ver vendedores
# crear productos y produciones
# ver los pedidos

page_copy: ft.Page = None


def buttom_regression(page: ft.Page, controls_remove: list[ft.Control], func) -> None:

    for control in controls_remove:
        page.remove(control)

    page.update()

    func(page)


def view_general(page: ft.Page) -> None:

    # row = ft.row()
    text = ft.Text("Panel de administrador",
                   color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)

    def view_watch_seller(e) -> None:
        page.remove(row)
        page.remove(row_2)
        page.remove(row_3)
        page.remove(buttom_watch_orders)

        page.update()
        url = "http://127.0.0.1:8000/nutrinal_pa/admin/get_seller"

        r = requests.get(url=url)

        json = r.json()

        data = json.get("data", {})

        items: dict = dict(data.items())
        index: int = 0

        text_1 = ft.Text(f"Vendedor {index}")

        name = items[f"seller_{index}"]["name"]
        text_2 = ft.Text(f"Nombre: {name}")

        identifier = items[f"seller_{index}"]["identifier"]
        text_3 = ft.Text(f"Identificador: {identifier}")

        data_joined = items[f"seller_{index}"]["data_joined"]
        text_4 = ft.Text(f"Fecha de ingreso: {data_joined}")
        text_5 = ft.Text("-" * 30)

        def on_regret(e):
            nonlocal index
            if index != 0:
                index -= 1
                name = items[f"seller_{index}"]["name"]
                identifier = items[f"seller_{index}"]["identifier"]
                identifier = items[f"seller_{index}"]["identifier"]

                text_1.value = f"Vendedor {index}"
                text_2.value = f"Nombre: {name}"
                text_3.value = f"Identificador: {identifier}"
                text_4.value = f"Fecha de ingreso: {data_joined}"

            page.update()

        def on_next(e):
            nonlocal index
            if index <= len(items) - 1:
                index += 1

                name = items[f"seller_{index}"]["name"]
                identifier = items[f"seller_{index}"]["identifier"]
                identifier = items[f"seller_{index}"]["identifier"]

                text_1.value = f"Vendedor {index}"
                text_2.value = f"Nombre: {name}"
                text_3.value = f"Identificador: {identifier}"
                text_4.value = f"Fecha de ingreso: {data_joined}"

            page.update()

        buttom_regret = ft.ElevatedButton(text="Regresar", on_click=on_regret)
        buttom_next = ft.ElevatedButton(text="Siguiente", on_click=on_next)

        row_butom = ft.Row([buttom_regret, buttom_next])

        def on_click(e):
            buttom_regression(
                page, [text_1, text_2, text_3, text_4, text_5, row_butom, regret], view_general)

        regret = ft.ElevatedButton(
            text="Regresar a la anterior vista", on_click=on_click)

        page.add(text_1)
        page.add(text_2)
        page.add(text_3)
        page.add(text_4)
        page.add(text_5)

        page.add(row_butom)
        page.add(regret)

        page.update()

    # fin de wacth seller

    def view_create_seller(e):
        # seller1 = Seller.objects.create(name="Juan Pérez", identifier="123456")
        # seller_login1 = SellerLogin.objects.create(
        # identifier=seller1, username="juan_vendedor", password="securepass")
        page.remove(row)
        page.remove(row_2)
        page.remove(row_3)
        page.remove(buttom_watch_orders)

        text_main = ft.Text("Crear un nuevo vendedor", color=ft.Colors.BLACK,
                            text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)

        row_text_main = ft.Row(
            controls=[text_main], alignment=ft.MainAxisAlignment.CENTER)

        text_name = ft.Text("Nombre")
        text_name_seller = ft.TextField(label="ingrese un nombre")

        text_identifier = ft.Text("Identificacion")
        text_identifier_seller = ft.TextField(
            label="ingrese la identificacion")

        text_username = ft.Text("Usuario y constraseña")
        text_username_seller = ft.TextField(label="Ingrese el usuario")
        text_password_seller = ft.TextField(label="Ingrese la contraseña")

        def on_click_send_info(e):

            data = {"data": {
                "name": text_name_seller.value,
                "id": text_identifier_seller.value,
                "username": text_username_seller.value,
                "password": text_password_seller.value,
            }}

            r = requests.post(
                url="http://127.0.0.1:8000/nutrinal_pa/admin/create_seller_login", json=data)

            if r.status_code != 200:
                error = r.json()["data"]["details"]
                print(
                    f"Hubo un error al mandar la informacion. Detalles {error}")

            else:
                print("La informacion fue mandada exitosamente")

        buttom_send_seller = ft.ElevatedButton(
            "Enviar informacion", on_click=on_click_send_info)

        def on_click(e):
            buttom_regression(
                page, [col, row_text_main, regret], view_general)

        regret = ft.ElevatedButton(
            text="Regresar a la anterior vista", on_click=on_click)

        col = ft.Column(controls=[text_name, text_name_seller, text_identifier,
                        text_identifier_seller, text_username, text_username_seller, text_password_seller, buttom_send_seller])
        page.add(row_text_main)
        page.add(col)
        page.add(regret)

    def view_create_product_and_productions(e):
        # Crear un producto
        # product = Product.objects.create(name="Suplemento Nutricional", code="PROD001",
        #                             price=49.99, description="Mejora la salud y el bienestar.")
        # Crear una producción para el producto
        # production = Production.objects.create(product=product, cant_available=100)
        page.remove(row)
        page.remove(row_2)
        page.remove(row_3)
        page.remove(buttom_watch_orders)

        text_main = ft.Text("Crear un nuevo producto", color=ft.Colors.BLACK,
                            text_align=ft.TextAlign.CENTER, size=40, style=ft.TextAlign.CENTER)
        row_text_main = ft.Row(
            controls=[text_main], alignment=ft.MainAxisAlignment.CENTER)

        text_name = ft.Text("Nombre del producto")
        text_name_product = ft.TextField(
            label="Ingrese el nombre del producto")

        text_code = ft.Text("Codigo del producto")
        text_code_product = ft.TextField(
            label="Ingrese el codigo del producto")

        text_price = ft.Text("El precio del producto")
        text_precio_product = ft.TextField(
            label="Ingrese el precio del producto")

        text_description = ft.Text("Descripcion del producto")
        text_description_product = ft.TextField(
            label="Ingrese la decripcion del producto")

        # buttom_send_seller = ft.ElevatedButton(
        #    "Enviar informacion", on_click=on_click_send_info)

        col = ft.Column(controls=[text_name, text_name_product, text_code,
                        text_code_product, text_price, text_precio_product, text_description, text_description_product])

        page.add(row_text_main)
        page.add(col)

        # content = {"data": {
        #    "name": "Producto Ejemplo",
        #    "code": "P12345",
        #    "price": 1000.50,
        #    "description": "Este es un producto de prueba"
        # }}

    buttom_watch_seller = ft.Container(content=ft.Text("Ver vendedores"), margin=10,
                                       padding=10,
                                       alignment=ft.alignment.center,
                                       bgcolor=ft.Colors.AMBER,
                                       width=150,
                                       height=150,
                                       border_radius=10, on_click=view_watch_seller)

    buttom_create_seller = ft.Container(
        content=ft.Text("Crear vendedores"), margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.BLUE,
        width=150,
        height=150,
        border_radius=10, on_click=view_create_seller)

    buttom_create_production = ft.Container(
        content=ft.Text("Crear producto"), margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.ORANGE,
        width=150,
        height=150,
        border_radius=10,  on_click=view_create_product_and_productions)

    buttom_watch_production = ft.Container(
        content=ft.Text("Ver productos"), margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.ORANGE_700,
        width=150,
        height=150,
        border_radius=10)

    buttom_watch_orders = ft.Container(content=ft.Text("Ver pedidos"), margin=10,
                                       padding=10,
                                       alignment=ft.alignment.center,
                                       bgcolor=ft.Colors.YELLOW,
                                       width=150,
                                       height=150,
                                       border_radius=10)

    row = ft.Row([buttom_create_seller, buttom_watch_seller])
    row_2 = ft.Row([buttom_create_production, buttom_watch_production])

    row_3 = ft.Row([text], alignment=ft.MainAxisAlignment.CENTER)

    page.add(row_3)
    page.add(row)
    page.add(row_2)

    page.add(buttom_watch_orders)

    page.update()
