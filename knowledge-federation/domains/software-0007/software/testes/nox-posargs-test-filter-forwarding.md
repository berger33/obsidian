---
id: software.testes.tranche14.000829
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

# Nox: encaminhar argumentos de diagnóstico sem editar o noxfile

## Em uma frase
Nox expõe argumentos posicionais da sessão para que o chamador acrescente opções do test runner.

## Por que importa
Reutilizar a sessão oficial mantém ambiente e setup iguais enquanto se reduz temporariamente o escopo durante investigação.

## Como funciona
Encaminhe `session.posargs` ao comando de teste e passe argumentos após separador CLI documentado.

## Exemplo
`nox -s tests -- -k checkout` executa somente casos de checkout se a função repassa os argumentos ao pytest.

## Limites e trade-offs
A sessão precisa consumir `posargs`; opções fornecidas na CLI não alteram automaticamente um comando que os descarta.

## Como verificar
Inspecione o comando final ou use um filtro conhecido e depois repita a matriz sem recorte.

## Conexões
- [[nox-external-command-boundary]] — Veja também: Nox: marcar comando externo ao ambiente como exceção.

## Fontes
- [Nox — Configuration and API](https://nox.thea.codes/en/stable/config.html) — definição de sessões, intérpretes, ambientes virtuais, tags e parâmetros; consultado em 2026-10-02.
- [Nox — Command-line usage](https://nox.thea.codes/en/stable/usage.html) — seleção e listagem de sessões, reuso de virtualenvs e opções de CLI; consultado em 2026-10-02.
