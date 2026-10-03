---
id: software.testes.tranche16.001034
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

# Prism: iniciar um servidor a partir da especificação

## Em uma frase
O comando de simulação lê um documento de contrato e expõe rotas que respondem conforme os exemplos ou os esquemas descritos nele.

## Por que importa
Servir a especificação permite que o trabalho de integração comece antes de o serviço real estar disponível, usando o mesmo contrato acordado.

## Como funciona
Aponte para o arquivo de contrato versionado, escolha o modo conforme a necessidade e fixe a porta usada pelos consumidores.

## Exemplo
Um front-end pode consumir a simulação durante o desenvolvimento enquanto o serviço real ainda não expõe todos os caminhos previstos.

## Limites e trade-offs
A simulação reproduz o contrato, não as regras de negócio, então transições dependentes de estado não são representadas fielmente.

## Como verificar
Compare a resposta simulada de uma rota com o exemplo do contrato e confirme que campos e códigos correspondem ao documento.

## Conexões
- [[prism-static-vs-dynamic]] — Veja também: Prism: escolher entre exemplo e esquema.

## Fontes
- [Prism — HTTP mocking](https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking) — modos estático e dinâmico, cabeçalho Prefer e respostas de violação; consultado em 2026-10-03.
- [Prism — CLI](https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli) — instalação, subcomandos mock e proxy e opções de validação; consultado em 2026-10-03.
