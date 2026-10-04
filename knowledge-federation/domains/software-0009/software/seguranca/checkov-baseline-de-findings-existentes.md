---
id: software.seguranca.tranche17.001678
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

# Checkov: Baseline de findings existentes

## Em uma frase
**Checkov — Baseline de findings existentes:** Baseline pode separar dívida já conhecida de novos findings durante adoção gradual.

## Por que importa
O recorte de **baseline de findings existentes** ajuda a identificar controles de segurança ausentes ainda no repositório ou plano de infraestrutura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **baseline de findings existentes**, descobre os arquivos e frameworks suportados, executa checks sobre definições ou plano e apresenta finding com identificador e localização. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Crie baseline versionado sobre branch estável e bloqueie somente regressões novas em pipeline experimental. Teste em staging autorizado.

## Limites e trade-offs
Baseline desatualizado ou regenerado sem revisão pode incorporar achados recém-introduzidos como aceitos. Exceções exigem responsável e prazo.

## Como verificar
Compare delta do baseline em revisão e exija aprovação para cada atualização. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[checkov-selecao-por-diretorio-e-framework]] — Complementa o tópico com checkov: seleção por diretório e framework.

## Fontes
- [Checkov — What is Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) — introdução oficial aos frameworks IaC e modelos de análise; consultado em 2026-10-04.
- [Checkov — CLI Command Reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html) — referência oficial da CLI, escopo, formatos e opções; consultado em 2026-10-04.
