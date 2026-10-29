import flet as ft


def main(page: ft.Page):
    page.title = "Greeting App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    name_field = ft.TextField(label="Enter your name", width=300)
    greeting_text = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)

    def greet_clicked(e):
        greeting_text.value = f"Hello, {name_field.value}!"
        page.update()

    greet_button = ft.Button(content="Greet Me", on_click=greet_clicked)

    page.add(
        ft.Column(
            controls=[name_field, greet_button, greeting_text],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


ft.run(main)