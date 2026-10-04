---
id: software.seguranca.tranche17.001677
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://www.checkov.io/1.Welcome/What%20is%20Checkov.html", "https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Checkov: Formato JSON e SARIF

## Em uma frase
**Checkov — Formato JSON e SARIF:** Relatórios estruturados facilitam importação de findings em plataformas de revisão e segurança.

## Por que importa
O recorte de **formato json e sarif** ajuda a identificar controles de segurança ausentes ainda no repositório ou plano de infraestrutura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **formato json e sarif**, descobre os arquivos e frameworks suportados, executa checks sobre definições ou plano e apresenta finding com identificador e localização. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Exporta JSON/SARIF de uma branch demonstrativa e confira se o consumidor preserva ID e path do recurso. Teste em staging autorizado.

## Limites e trade-offs
Integração pode remapear severidade e agrupar checks; consumidor precisa manter contexto original. Exceções exigem responsável e prazo.

## Como verificar
Valide schema e reconcilie uma amostra entre console e sistema de tickets. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[checkov-baseline-de-findings-existentes]] — Complementa o tópico com checkov: baseline de findings existentes.

## Fontes
- [Checkov — What is Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) — introdução oficial aos frameworks IaC e modelos de análise; consultado em 2026-10-04.
- [Checkov — CLI Command Reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html) — referência oficial da CLI, escopo, formatos e opções; consultado em 2026-10-04.
