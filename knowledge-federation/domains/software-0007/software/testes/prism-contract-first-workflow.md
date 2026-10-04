---
id: software.testes.tranche16.001043
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

# Prism: sustentar o fluxo de contrato primeiro

## Em uma frase
A simulação só é útil quando o contrato é a fonte acordada entre quem consome e quem fornece, mantido antes da implementação.

## Por que importa
Contrato escrito depois vira descrição aproximada do que já existe, e a simulação passa a reproduzir divergências em vez de preveni-las.

## Como funciona
Faça a especificação evoluir por revisão conjunta, gere simulação a partir dela e valide o serviço real contra o mesmo documento.

## Exemplo
Uma rota nova pode ser acordada em revisão, simulada para o consumidor e depois implementada com teste de contrato contra a mesma definição.

## Limites e trade-offs
Sem disciplina de atualização, o documento e o serviço divergem, e a simulação passa a enganar quem confia nela.

## Como verificar
Compare a resposta do serviço real com a da simulação para a mesma rota e trate cada diferença como pendência explícita de contrato.

## Conexões
- [[prism-client-programmatic]] — Veja também: Prism: usar a biblioteca em código de teste.
- [[prism-limits]] — Veja também: Prism: reconhecer limites da simulação.

## Fontes
- [Prism — HTTP mocking](https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking) — modos estático e dinâmico, cabeçalho Prefer e respostas de violação; consultado em 2026-10-03.
- [Prism — CLI](https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli) — instalação, subcomandos mock e proxy e opções de validação; consultado em 2026-10-03.
