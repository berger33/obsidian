---
id: software.testes.tranche14.000820
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

# Nox: modelar versões Python como sessões separadas

## Em uma frase
Uma sessão Nox pode declarar vários intérpretes e gerar uma execução isolada para cada versão suportada.

## Por que importa
Matriz explícita encontra incompatibilidades de runtime sem misturar resultados ou dependências instaladas em uma única virtualenv mutável.

## Como funciona
Declare `python` com as versões alvo na sessão e confirme com `nox --list` quais invocações concretas foram expandidas.

## Exemplo
A sessão `tests` roda uma vez em Python 3.13 e outra em Python 3.14, instalando o projeto e as dependências em ambientes próprios.

## Limites e trade-offs
Versão pedida precisa existir ou ser baixável pelo backend e plataforma; matrizes maiores aumentam custo de CI.

## Como verificar
Registre versão efetiva do interpretador e rode cada sessão no CI principal, em vez de supor que alias encontrado localmente é equivalente.

## Conexões
- [[nox-parametrize-session-axis]] — Veja também: Nox: parametrizar entradas de sessão sem duplicar funções.

## Fontes
- [Nox — Configuration and API](https://nox.thea.codes/en/stable/config.html) — definição de sessões, intérpretes, ambientes virtuais, tags e parâmetros; consultado em 2026-10-02.
- [Nox — Command-line usage](https://nox.thea.codes/en/stable/usage.html) — seleção e listagem de sessões, reuso de virtualenvs e opções de CLI; consultado em 2026-10-02.
