---
id: software.testes.tranche16.001042
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
fontes: ["https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking", "https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Prism: usar a biblioteca em código de teste

## Em uma frase
A biblioteca permite criar instância de simulação a partir de operações específicas do contrato, com opções de geração dinâmica, validação e erro.

## Por que importa
Criar simulação dentro do próprio teste dispensa processo externo e permite exercitar apenas as operações relevantes para o caso.

## Como funciona
Instancie a partir das operações necessárias, defina validação de requisição e de resposta conforme o objetivo e feche o recurso ao final do teste.

## Exemplo
Um teste que verifica o tratamento de erro do cliente pode instanciar apenas a operação afetada e responder com a variação desejada.

## Limites e trade-offs
A instância precisa ser encerrada corretamente para não deixar porta ocupada, e a configuração programática esconde do contrato o que está sendo simulado.

## Como verificar
Compare o resultado obtido pela biblioteca com o da simulação por linha de comando para a mesma rota e verifique equivalência.

## Conexões
- [[prism-cli-workflow]] — Veja também: Prism: operar a linha de comando.
- [[prism-contract-first-workflow]] — Veja também: Prism: sustentar o fluxo de contrato primeiro.

## Fontes
- [Prism — HTTP mocking](https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking) — modos estático e dinâmico, cabeçalho Prefer e respostas de violação; consultado em 2026-10-03.
- [Prism — CLI](https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli) — instalação, subcomandos mock e proxy e opções de validação; consultado em 2026-10-03.
