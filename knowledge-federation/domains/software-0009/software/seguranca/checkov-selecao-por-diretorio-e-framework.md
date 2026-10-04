---
id: software.seguranca.tranche17.001679
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

# Checkov: Seleção por diretório e framework

## Em uma frase
**Checkov — Seleção por diretório e framework:** Seleção correta da origem ajuda a evitar que código irrelevante ou gerado distorça o resultado.

## Por que importa
O recorte de **seleção por diretório e framework** ajuda a identificar controles de segurança ausentes ainda no repositório ou plano de infraestrutura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **seleção por diretório e framework**, descobre os arquivos e frameworks suportados, executa checks sobre definições ou plano e apresenta finding com identificador e localização. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Execute scan em diretório de IaC dedicado e compare arquivos descobertos com inventário esperado. Teste em staging autorizado.

## Limites e trade-offs
Exclusões amplas podem deixar configuração crítica fora do escopo. Exceções exigem responsável e prazo.

## Como verificar
Registre caminhos incluídos e excluídos e teste arquivo-canário em cada pasta crítica. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[checkov-gates-de-ci-por-politica]] — Complementa o tópico com checkov: gates de ci por política.

## Fontes
- [Checkov — What is Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) — introdução oficial aos frameworks IaC e modelos de análise; consultado em 2026-10-04.
- [Checkov — CLI Command Reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html) — referência oficial da CLI, escopo, formatos e opções; consultado em 2026-10-04.
