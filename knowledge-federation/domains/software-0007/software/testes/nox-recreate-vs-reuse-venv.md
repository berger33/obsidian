---
id: software.testes.tranche14.000822
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
fontes: ["https://nox.thea.codes/en/stable/usage.html", "https://nox.thea.codes/en/stable/config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nox: escolher reuso de virtualenv sem perder reprodutibilidade

## Em uma frase
Por padrão, Nox recria virtualenvs a cada execução; reuso é opção consciente para acelerar ciclos locais.

## Por que importa
Ambiente reaproveitado pode conter pacotes antigos ou configuração residual que não aparece numa execução limpa de CI.

## Como funciona
Use `reuse_venv` ou opção CLI de maneira explícita e mantenha uma execução limpa periódica para validar dependências declaradas.

## Exemplo
Um desenvolvedor pode usar `nox -r` enquanto itera e o pipeline usa o padrão recriado para provar setup limpo.

## Limites e trade-offs
`--no-install` junto ao reuso pula etapas de instalação; não use esse atalho para alegar que a configuração reproduz dependências do projeto.

## Como verificar
Compare falhas em virtualenv recriada com reutilizada e registre qual política foi aplicada na investigação.

## Conexões
- [[nox-parametrize-session-axis]] — Veja também: Nox: parametrizar entradas de sessão sem duplicar funções.
- [[nox-no-virtualenv-scope]] — Veja também: Nox: dispensar virtualenv apenas quando o ambiente atual for parte do contrato.

## Fontes
- [Nox — Command-line usage](https://nox.thea.codes/en/stable/usage.html) — seleção e listagem de sessões, reuso de virtualenvs e opções de CLI; consultado em 2026-10-02.
- [Nox — Configuration and API](https://nox.thea.codes/en/stable/config.html) — definição de sessões, intérpretes, ambientes virtuais, tags e parâmetros; consultado em 2026-10-02.
