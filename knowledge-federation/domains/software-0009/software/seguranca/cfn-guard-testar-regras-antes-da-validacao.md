---
id: software.seguranca.tranche18.001793
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

# AWS CloudFormation Guard: Testar regras antes da validação

## Em uma frase
**AWS CloudFormation Guard — Testar regras antes da validação:** O comando test verifica regras contra casos de teste e ajuda confirmar que política encontra violações pretendidas.

## Por que importa
O recorte de **testar regras antes da validação** ajuda a formalizar requisitos de configuração e rodar as mesmas regras em testes locais e pipelines. A equipe registra risco, evidência e responsável.

## Como funciona
Para **testar regras antes da validação**, autores escrevem clauses e named-rule blocks, testam regras contra fixtures e validam arquivos de entrada. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Mantenha regra e arquivos de teste na mesma revisão do template CloudFormation. Teste em staging autorizado.

## Limites e trade-offs
Um teste que cobre só o caso negativo não demonstra que a regra permite configuração válida. Exceções exigem responsável e prazo.

## Como verificar
Inclua expectativas de PASS e FAIL e execute a suíte antes de atualizar bundle de regras. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cfn-guard-validar-arquivo-de-entrada-com-rules-file]] — Complementa o tópico com aws cloudformation guard: validar arquivo de entrada com rules file.

## Fontes
- [AWS CloudFormation Guard — Writing rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/writing-rules.html) — guia oficial de DSL, clauses, named-rule blocks e mensagens customizadas; consultado em 2026-10-04.
- [AWS CloudFormation Guard — Validating rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/validating-rules.html) — instruções oficiais do comando validate para um ou vários arquivos e regras; consultado em 2026-10-04.
