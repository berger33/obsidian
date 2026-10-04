---
id: software.testes.tranche22.001658
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://gcovr.com/en/stable/index.html", "https://gcovr.com/en/stable/changelog.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# gcovr: ciclo de release visível na doc

## Em uma frase
A documentação versiona explícito: o texto corrente descreve o gcovr 8.6, o changelog abre com 8.6 (13 de janeiro de 2026), 8.5 (8 de janeiro de 2026) e 8.4 (27 de setembro de 2025), e o seletor de versões preserva docs de 4.1 a 7.2.

## Por que importa
Ferramenta de toolchain exige casar versão com o GCC do build; o histórico de releases na doc facilita datar quando certa flag entrou e com qual compilador foi validada.

## Como funciona
O seletor oficial lista ainda 8.3, 8.2, 7.1, 7.0 e 6.0_a — o sufixo alpha no 6.0 denota a política de pré-release que o projeto já praticou.

## Exemplo
A própria doc é hospedada com PDF e EPUB públicos por versão, além do Read the Docs project home com builds.

## Limites e trade-offs
Doc estável não significa doc exaustiva para a sua versão antiga: flags criadas depois de 4.1 não existem no seletor daquele ano, e copiar exemplo novo em release velha falha sem mensagem clara.

## Como verificar
Abra /en/8.5/ e /en/stable/ do mesmo guia e difira a página de Output Formats para ver a cadência de mudanças.

## Conexões
- [[gcovr-cookbook]] — Veja também: gcovr: receitas de build difícil.
- [[gcovr-vs-lcov]] — Veja também: gcovr: quando lcov basta e quando não.

## Fontes
- [gcovr — documentação inicial (8.6)](https://gcovr.com/en/stable/index.html) — definição, matriz de formatos de saída e índice da doc; consultado em 2026-10-03.
- [gcovr — Change Log](https://gcovr.com/en/stable/changelog.html) — datas de release da doc 8.6; consultado em 2026-10-03.
