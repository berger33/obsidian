---
id: software.testes.tranche16.001039
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

# Prism: entender as respostas de violação

## Em uma frase
Quando a requisição não corresponde ao contrato, a ferramenta responde com documento de problema estruturado e cabeçalho descrevendo a violação.

## Por que importa
Formato padronizado de erro permite que ferramentas e pessoas entendam a causa sem depender de mensagem textual específica da implementação.

## Como funciona
Trate esse formato no consumidor de teste, verifique o código devolvido e registre a violação como sinal de desalinhamento entre cliente e contrato.

## Exemplo
Um cliente que envia campo com tipo errado recebe resposta de erro que aponta o caminho do campo e a regra violada.

## Limites e trade-offs
O formato de erro é da simulação e não substitui o tratamento de erro do serviço real, que precisa seguir o contrato acordado para a aplicação.

## Como verificar
Compare uma resposta de sucesso com uma de violação e confirme a diferença de código, tipo de conteúdo e estrutura do corpo.

## Conexões
- [[prism-proxy-mode]] — Veja também: Prism: intermediar serviço real com contrato.
- [[prism-spec-quality]] — Veja também: Prism: a simulação depende da qualidade do contrato.

## Fontes
- [Prism — HTTP mocking](https://docs.stoplight.io/docs/prism/83dbbd75532cf-http-mocking) — modos estático e dinâmico, cabeçalho Prefer e respostas de violação; consultado em 2026-10-03.
- [Prism — CLI](https://docs.stoplight.io/docs/prism/beeaad4dc0227-prism-cli) — instalação, subcomandos mock e proxy e opções de validação; consultado em 2026-10-03.
