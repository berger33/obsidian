---
id: software.testes.tranche14.000823
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

# Nox: dispensar virtualenv apenas quando o ambiente atual for parte do contrato

## Em uma frase
`python=False` ou backend `none` executa sessão sem criar virtualenv gerenciada pelo Nox.

## Por que importa
Isso é útil para tarefas que devem operar no ambiente existente, mas amplia o risco de dependências implícitas da máquina.

## Como funciona
Marque a sessão intencionalmente sem venv, instale ferramentas explicitamente no contexto aceito e reserve isolamento para testes de compatibilidade.

## Exemplo
Um comando de lint já executado em container preparado pode rodar na sessão sem virtualenv, enquanto testes de matriz continuam isolados.

## Limites e trade-offs
`session.install()` sem venv modifica o Python global e é desaconselhado na documentação atual.

## Como verificar
Execute a sessão em container limpo ou ambiente documentado e confirme que nenhuma dependência local não listada foi necessária.

## Conexões
- [[nox-recreate-vs-reuse-venv]] — Veja também: Nox: escolher reuso de virtualenv sem perder reprodutibilidade.
- [[nox-default-session-surface]] — Veja também: Nox: tirar tarefas auxiliares da execução padrão.

## Fontes
- [Nox — Configuration and API](https://nox.thea.codes/en/stable/config.html) — definição de sessões, intérpretes, ambientes virtuais, tags e parâmetros; consultado em 2026-10-02.
- [Nox — Cookbook](https://nox.thea.codes/en/stable/cookbook.html) — receitas para sessões, instalação, comandos e lockfiles; consultado em 2026-10-02.
