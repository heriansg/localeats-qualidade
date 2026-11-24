import re
from playwright.sync_api import Page, expect

URL_LOCALEATS = "https://local-eats-unisenac.vercel.app/"

# Responsável: Herian


def test_exibicao_pagina_inicial_e_interacao(page: Page):
    page.goto(URL_LOCALEATS, wait_until="domcontentloaded")

    # Assertion 1: verifica que a página carregou com título não vazio
    expect(page).to_have_title(re.compile(r".+"))

    # Interação na interface (ex.: clicar no primeiro botão ou link visível)
    primeiro_elemento = page.locator("button, a").first
    expect(primeiro_elemento).to_be_visible()
    primeiro_elemento.click()

    # Assertion 2: verifica que o corpo da página continua visível após a interação
    expect(page.locator("body")).to_be_visible()