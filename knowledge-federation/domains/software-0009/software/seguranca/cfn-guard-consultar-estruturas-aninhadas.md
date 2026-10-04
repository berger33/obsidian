---
id: software.seguranca.tranche18.001798
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-18.md"
fontes: ["https://docs.aws.amazon.com/cfn-guard/latest/ug/writing-rules.html", "https://docs.aws.amazon.com/cfn-guard/latest/ug/validating-rules.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# AWS CloudFormation Guard: Consultar estruturas aninhadas

## Em uma frase
**AWS CloudFormation Guard — Consultar estruturas aninhadas:** Consultas de Guard percorrem propriedades e listas em dados JSON ou YAML para verificar recursos específicos.

## Por que importa
O recorte de **consultar estruturas aninhadas** ajuda a formalizar requisitos de configuração e rodar as mesmas regras em testes locais e pipelines. A equipe registra risco, evidência e responsável.

## Como funciona
Para **consultar estruturas aninhadas**, autores escrevem clauses e named-rule blocks, testam regras contra fixtures e validam arquivos de entrada. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Selecione cada security group e teste intervalo de portas em fixture com dois recursos. Teste em staging autorizado.

## Limites e trade-offs
Listas vazias e ausência de propriedades exigem regras explícitas para evitar avaliação ambígua. Exceções exigem responsável e prazo.

## Como verificar
Cubra zero, um e vários elementos e inspecione `--show-clause-failures`. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cfn-guard-usar-guard-como-gate-de-template]] — Complementa o tópico com aws cloudformation guard: usar guard como gate de template.

## Fontes
- [AWS CloudFormation Guard — Writing rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/writing-rules.html) — guia oficial de DSL, clauses, named-rule blocks e mensagens customizadas; consultado em 2026-10-04.
- [AWS CloudFormation Guard — Validating rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/validating-rules.html) — instruções oficiais do comando validate para um ou vários arquivos e regras; consultado em 2026-10-04.
