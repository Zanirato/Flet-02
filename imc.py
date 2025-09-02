import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

    # Campos de entrada
    peso = ft.TextField(label="🏋️ Peso (kg)", width=200, keyboard_type=ft.KeyboardType.NUMBER)
    altura = ft.TextField(label="📏 Altura (m)", width=200, keyboard_type=ft.KeyboardType.NUMBER)

    resultado = ft.Text(
        "Digite os valores e clique em Calcular",
        size=20,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.GREY_600
    )

    # Função de cálculo
    def calcular(e):
        try:
            p = float(peso.value)
            a = float(altura.value)

            if a <= 0:
                resultado.value = "❌ Erro: altura deve ser maior que zero!"
                resultado.color = ft.Colors.RED
            else:
                imc = p / (a * a)

                # Classificação do IMC
                if imc < 18.5:
                    classificacao = "Baixo peso"
                    cor = ft.Colors.ORANGE
                elif 18.5 <= imc < 25:
                    classificacao = "Peso normal"
                    cor = ft.Colors.GREEN
                elif 25 <= imc < 30:
                    classificacao = "Sobrepeso"
                    cor = ft.Colors.AMBER
                else:
                    classificacao = "Obesidade"
                    cor = ft.Colors.RED

                resultado.value = f"📊 Seu IMC é {imc:.2f} → {classificacao}"
                resultado.color = cor

        except ValueError:
            resultado.value = "❌ Digite números válidos!"
            resultado.color = ft.Colors.RED

        page.update()

    # Função limpar
    def limpar(e):
        peso.value = altura.value = ""
        resultado.value = "Digite os valores e clique em Calcular"
        resultado.color = ft.Colors.GREY_600
        page.update()

    # Interface
    page.add(
        ft.Column([
            ft.Text("🧮 Calculadora de IMC", size=24, weight=ft.FontWeight.BOLD),
            altura,
            peso,
            ft.Row([
                ft.ElevatedButton("🟢 Calcular", on_click=calcular, width=150,
                                  bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
                ft.ElevatedButton("🧹 Limpar", on_click=limpar, width=150,
                                  bgcolor=ft.Colors.GREY, color=ft.Colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20),
            ft.Divider(),
            resultado
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20)
    )

ft.app(target=main)
