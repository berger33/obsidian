---
id: software.seguranca.tranche17.001680
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

# Checkov: Gates de CI por política

## Em uma frase
**Checkov — Gates de CI por política:** Um exit code pode transformar finding em gate, mas a severidade e exceções precisam de um contrato explícito.

## Por que importa
O recorte de **gates de ci por política** ajuda a identificar controles de segurança ausentes ainda no repositório ou plano de infraestrutura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **gates de ci por política**, descobre os arquivos e frameworks suportados, executa checks sobre definições ou plano e apresenta finding com identificador e localização. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em branch de teste, introduza falha controlada e confirme que o job sinaliza a política acordada. Teste em staging autorizado.

## Limites e trade-offs
Falha genérica pode bloquear merge sem informar causa; limiar por severidade pode ignorar risco crítico com score baixo. Exceções exigem responsável e prazo.

## Como verificar
Teste finding alto e baixo, caso sem findings e falha de ferramenta para diferenciar estados. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kube-bench-alinhar-versao-do-benchmark]] — Complementa o tópico com kube-bench: alinhar versão do benchmark.

## Fontes
- [Checkov — What is Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) — introdução oficial aos frameworks IaC e modelos de análise; consultado em 2026-10-04.
- [Checkov — CLI Command Reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html) — referência oficial da CLI, escopo, formatos e opções; consultado em 2026-10-04.
