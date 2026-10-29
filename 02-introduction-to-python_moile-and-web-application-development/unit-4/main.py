import flet as ft


async def main(page: ft.Page):
    page.title = "Two-View Greeting App"

    user_name = ""

    def route_change(_):
        page.views.clear()

        if page.route == "/":
            name_field = ft.TextField(label="Enter your name", width=300)

            async def handle_continue(_):
                nonlocal user_name
                entered_name = (name_field.value or "").strip()

                if not entered_name:
                    page.show_dialog(
                        ft.AlertDialog(
                            title=ft.Text("Name required"),
                            content=ft.Text("Please enter your name."),
                        )
                    )
                    return

                user_name = entered_name
                await page.go("/greeting")

            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        ft.Text(
                            "Welcome to the Greeting App!",
                            size=30,
                            weight=ft.FontWeight.BOLD,
                        ),
                        name_field,
                        ft.Button(content="Continue", on_click=handle_continue),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                )
            )
        elif page.route == "/greeting":
            page.views.append(
                ft.View(
                    route="/greeting",
                    controls=[
                        ft.Text(f"Hello, {user_name}!", size=40),
                        ft.Button(
                            content="Back",
                            on_click=lambda _: page.go("/"),
                        ),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                )
            )

        page.update()

    page.on_route_change = route_change
    route_change(None)


if __name__ == "__main__":
    ft.run(main)
