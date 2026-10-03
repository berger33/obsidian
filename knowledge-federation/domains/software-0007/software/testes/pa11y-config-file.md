---
id: software.testes.tranche16.001030
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://github.com/pa11y/pa11y", "https://github.com/pa11y/pa11y-ci"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pa11y: centralizar configuração do projeto

## Em uma frase
As opções podem ser reunidas em arquivo de configuração, o que mantém a linha de comando curta e documenta o comportamento esperado.

## Por que importa
Configuração versionada reduz divergência entre pessoas e ambientes, além de manter exceções visíveis para revisão.

## Como funciona
Reúna padrão, motores, tempo limite, espera, ações e exceções no arquivo, mantendo apenas variações de ambiente por linha de comando.

## Exemplo
Um projeto pode declarar no arquivo o padrão intermediário, os dois motores e os seletores de conteúdo de terceiros a ocultar.

## Limites e trade-offs
Arquivos espalhados criam conflito de precedência; a configuração precisa ser única por projeto e revisada como código.

## Como verificar
Execute com arquivo explícito e sem ele e compare os resultados para confirmar quais opções estão sendo aplicadas.

## Conexões
- [[pa11y-ignore-and-scope]] — Veja também: Pa11y: restringir escopo e registrar exceções.
- [[pa11y-ci-multiple-urls]] — Veja também: Pa11y CI: varrer um conjunto de páginas.

## Fontes
- [Pa11y — repositório oficial](https://github.com/pa11y/pa11y) — linha de comando, padrões, motores, ações, relatórios e limites; consultado em 2026-10-03.
- [Pa11y CI — repositório oficial](https://github.com/pa11y/pa11y-ci) — varredura de múltiplas páginas, configuração e integração contínua; consultado em 2026-10-03.
