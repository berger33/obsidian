---
id: software.seguranca.tranche18.001795
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

# AWS CloudFormation Guard: Aplicar múltiplas regras e arquivos

## Em uma frase
**AWS CloudFormation Guard — Aplicar múltiplas regras e arquivos:** Guard aceita diretórios de dados e regras para avaliar coleções de templates numa mesma execução.

## Por que importa
O recorte de **aplicar múltiplas regras e arquivos** ajuda a formalizar requisitos de configuração e rodar as mesmas regras em testes locais e pipelines. A equipe registra risco, evidência e responsável.

## Como funciona
Para **aplicar múltiplas regras e arquivos**, autores escrevem clauses e named-rule blocks, testam regras contra fixtures e validam arquivos de entrada. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Rode regras de armazenamento e rede sobre diretório de stacks de infraestrutura. Teste em staging autorizado.

## Limites e trade-offs
Uma pasta extra ou fixture de teste pode entrar no escopo e alterar resultado. Exceções exigem responsável e prazo.

## Como verificar
Liste arquivos encontrados pela pipeline e exclua diretório de fixtures deliberadamente. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cfn-guard-injetar-parametros-de-contexto]] — Complementa o tópico com aws cloudformation guard: injetar parâmetros de contexto.

## Fontes
- [AWS CloudFormation Guard — Writing rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/writing-rules.html) — guia oficial de DSL, clauses, named-rule blocks e mensagens customizadas; consultado em 2026-10-04.
- [AWS CloudFormation Guard — Validating rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/validating-rules.html) — instruções oficiais do comando validate para um ou vários arquivos e regras; consultado em 2026-10-04.
