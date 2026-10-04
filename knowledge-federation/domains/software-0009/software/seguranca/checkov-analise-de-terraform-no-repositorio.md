---
id: software.seguranca.tranche17.001671
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

# Checkov: Análise de Terraform no repositório

## Em uma frase
**Checkov — Análise de Terraform no repositório:** Checkov avalia arquivos Terraform e configurações relacionadas antes de provisionar infraestrutura.

## Por que importa
O recorte de **análise de terraform no repositório** ajuda a identificar controles de segurança ausentes ainda no repositório ou plano de infraestrutura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **análise de terraform no repositório**, descobre os arquivos e frameworks suportados, executa checks sobre definições ou plano e apresenta finding com identificador e localização. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Rode scan no diretório de módulo e examine finding de recurso exposto antes do plano ser aplicado. Teste em staging autorizado.

## Limites e trade-offs
Variáveis não resolvidas e módulos remotos podem limitar a interpretação estática. Exceções exigem responsável e prazo.

## Como verificar
Compare recursos do código com plano de teste e documente diferenças de avaliação. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[checkov-analise-de-plano-terraform]] — Complementa o tópico com checkov: análise de plano terraform.

## Fontes
- [Checkov — What is Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) — introdução oficial aos frameworks IaC e modelos de análise; consultado em 2026-10-04.
- [Checkov — CLI Command Reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html) — referência oficial da CLI, escopo, formatos e opções; consultado em 2026-10-04.
