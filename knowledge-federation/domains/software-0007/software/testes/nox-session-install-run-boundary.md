---
id: software.testes.tranche14.000827
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
fontes: ["https://nox.thea.codes/en/stable/config.html", "https://nox.thea.codes/en/stable/cookbook.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nox: separar dependências instaladas do executável chamado

## Em uma frase
`session.install()` prepara pacotes no ambiente da sessão, enquanto `session.run()` invoca comandos dentro do contexto daquela sessão.

## Por que importa
Separar setup do trabalho deixa explícito qual ferramenta roda e evita depender de binário global no PATH.

## Como funciona
Instale framework e pacote como dependências declaradas, depois invoque runner com argumentos em `session.run`.

## Exemplo
A sessão instala pytest no ambiente virtual e chama `session.run("pytest", "tests")` para executar a suite.

## Limites e trade-offs
Backend `uv` pode não instalar pip por padrão; comandos de instalação e ferramentas disponíveis variam com backend escolhido.

## Como verificar
Imprima o interpretador e caminho do executável durante diagnóstico e valide a sessão após trocar backend.

## Conexões
- [[nox-tag-filtered-ci-selection]] — Veja também: Nox: selecionar sessões por tags em jobs especializados.
- [[nox-external-command-boundary]] — Veja também: Nox: marcar comando externo ao ambiente como exceção.

## Fontes
- [Nox — Configuration and API](https://nox.thea.codes/en/stable/config.html) — definição de sessões, intérpretes, ambientes virtuais, tags e parâmetros; consultado em 2026-10-02.
- [Nox — Cookbook](https://nox.thea.codes/en/stable/cookbook.html) — receitas para sessões, instalação, comandos e lockfiles; consultado em 2026-10-02.
