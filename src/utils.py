import flet as ft


def buttom_regret(page: ft.Page, constrols_remove: list[ft.Control], func) -> None:

    for control in constrols_remove:
        page.remove(control)

    buttom = ft.FilledButton(text="Regresar a la ventana anterior"),

    page.add(buttom)

    page.update()
