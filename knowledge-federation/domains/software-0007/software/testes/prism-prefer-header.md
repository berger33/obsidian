---
id: software.testes.tranche16.001036
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

# Prism: negociar respostas pelo cabeçalho de preferência

## Em uma frase
O cabeçalho de preferência permite escolher código de resposta, exemplo específico e modo de geração para uma requisição simulada.

## Por que importa
Uma mesma rota tem várias respostas previstas, e a negociação por cabeçalho permite testar casos de erro sem alterar o contrato.

## Como funciona
Envie o cabeçalho com o código desejado, informe o exemplo quando houver mais de um para o mesmo código e use a variante dinâmica quando precisar de valores gerados.

## Exemplo
Para verificar o tratamento de recurso ausente, basta pedir a resposta de erro correspondente e conferir como a interface se comporta.

## Limites e trade-offs
O cabeçalho é específico da ferramenta e depende do servidor de simulação; o comportamento precisa ser reproduzido em teste de contrato para não depender só dele.

## Como verificar
Compare a resposta padrão com a resposta negociada da mesma rota e confirme que código e corpo mudaram conforme pedido.

## Conexões
- [[prism-static-vs-dynamic]] — Veja também: Prism: escolher entre exemplo e esquema.
- [[prism-validation-errors]] — Veja também: Prism: validar requisição contra o contrato.

## Fontes
- [Prism — HTTP mocking](https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking) — modos estático e dinâmico, cabeçalho Prefer e respostas de violação; consultado em 2026-10-03.
- [Prism — CLI](https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli) — instalação, subcomandos mock e proxy e opções de validação; consultado em 2026-10-03.
