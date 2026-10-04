---
id: software.seguranca.tranche17.001676
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

# Checkov: Políticas customizadas

## Em uma frase
**Checkov — Políticas customizadas:** Políticas próprias permitem traduzir requisitos internos em checks de infraestrutura.

## Por que importa
O recorte de **políticas customizadas** ajuda a identificar controles de segurança ausentes ainda no repositório ou plano de infraestrutura. A equipe registra risco, evidência e responsável.

## Como funciona
Para **políticas customizadas**, descobre os arquivos e frameworks suportados, executa checks sobre definições ou plano e apresenta finding com identificador e localização. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Crie regra de teste para recurso cloud obrigatório e confirme comportamento em arquivo compliant e noncompliant. Teste em staging autorizado.

## Limites e trade-offs
Custom check incorreto pode dar falso senso de conformidade e precisa de manutenção com API IaC. Exceções exigem responsável e prazo.

## Como verificar
Versione regras, teste casos limítrofes e peça revisão do time dono do controle. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[checkov-formato-json-e-sarif]] — Complementa o tópico com checkov: formato json e sarif.

## Fontes
- [Checkov — What is Checkov](https://www.checkov.io/1.Welcome/What%20is%20Checkov.html) — introdução oficial aos frameworks IaC e modelos de análise; consultado em 2026-10-04.
- [Checkov — CLI Command Reference](https://www.checkov.io/2.Basics/CLI%20Command%20Reference.html) — referência oficial da CLI, escopo, formatos e opções; consultado em 2026-10-04.
