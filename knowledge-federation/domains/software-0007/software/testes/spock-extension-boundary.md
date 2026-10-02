---
id: software.testes.tranche13.000729
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://spockframework.org/spock/docs/2.4/extensions.html", "https://spockframework.org/spock/docs/2.4/all_in_one.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Spock: usar extension para política transversal

## Em uma frase
Extensions registram comportamento reaproveitável que intercepta ou complementa lifecycle de specs e features.

## Por que importa
Uma política comum pode ser aplicada sem copiar boilerplate, desde que o escopo e efeitos do interceptor permaneçam visíveis à suite.

## Como funciona
Implemente extension para necessidade transversal real, aplique annotation compatível e documente ordem com setup da própria specification.

## Exemplo
Uma extensão pode recolher metadados de execução de todos os specs sem reescrever cada feature com chamadas manuais.

## Limites e trade-offs
Interceptar lifecycle amplia poder e pode introduzir side effects globais; uma helper local é mais simples quando só uma suite precisa da lógica.

## Como verificar
Aplique extension a uma suite mínima e confirme callback, ordem e cleanup durante sucesso e falha.

## Conexões
- [[spock-exception-condition]] — Veja também: Spock: capturar exceção como parte da condição esperada.

## Fontes
- [Spock 2.4 — Extensions](https://spockframework.org/spock/docs/2.4/extensions.html) — extension annotations and lifecycle interception; consultado em 2026-10-02.
- [Spock 2.4 — Reference Documentation](https://spockframework.org/spock/docs/2.4/all_in_one.html) — specifications, feature blocks, fixtures and runner; consultado em 2026-10-02.
