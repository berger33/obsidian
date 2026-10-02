---
id: software.testes.tranche14.000821
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://nox.thea.codes/en/stable/config.html", "https://nox.thea.codes/en/stable/usage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nox: parametrizar entradas de sessão sem duplicar funções

## Em uma frase
`nox.parametrize` expande uma função de sessão em invocações distintas com argumentos definidos pela matriz.

## Por que importa
A configuração mantém lógica de setup compartilhada e torna cada variante visível para seleção e relatório.

## Como funciona
Aplique o decorator a parâmetros de ambiente, dê IDs legíveis quando apropriado e valide o produto de eixos antes de executar.

## Exemplo
Uma sessão instala duas versões de Django como invocações nomeadas de `tests`, em vez de manter duas funções quase iguais.

## Limites e trade-offs
Produto de várias dimensões pode multiplicar custo e não equivale automaticamente a configurar o intérprete Python da sessão.

## Como verificar
Use `nox --list` e a sintaxe da CLI para selecionar uma invocação parametrizada pelo conjunto de argumentos desejado.

## Conexões
- [[nox-python-version-matrix]] — Veja também: Nox: modelar versões Python como sessões separadas.
- [[nox-recreate-vs-reuse-venv]] — Veja também: Nox: escolher reuso de virtualenv sem perder reprodutibilidade.

## Fontes
- [Nox — Configuration and API](https://nox.thea.codes/en/stable/config.html) — definição de sessões, intérpretes, ambientes virtuais, tags e parâmetros; consultado em 2026-10-02.
- [Nox — Command-line usage](https://nox.thea.codes/en/stable/usage.html) — seleção e listagem de sessões, reuso de virtualenvs e opções de CLI; consultado em 2026-10-02.
