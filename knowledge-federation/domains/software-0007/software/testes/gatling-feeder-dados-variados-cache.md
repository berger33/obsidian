---
id: software.testes.tranche11.000532
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://docs.gatling.io/concepts/session/feeders/", "https://docs.gatling.io/concepts/session/api/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: alimentar usuários com registros distintos para workload

## Em uma frase
Feeder fornece records aos virtual users por meio de feed e os atributos passam para Session.

## Por que importa
Se todos os usuários consultam o mesmo objeto, caches do alvo podem ficar mais quentes que o workload real.

## Como funciona
Prepare dataset controlado e escolha estratégia de consumo/reciclagem coerente com unicidade e tamanho necessário.

## Exemplo
Feeder CSV dá user id e produto a cada usuário para que requests usem recursos distintos.

## Limites e trade-offs
Dado único aumenta cobertura de objetos mas requer dataset suficiente; exhausted feeder pode falhar conforme estratégia usada.

## Como verificar
Rode pequena população, registre records distribuídos e valide fim de arquivo, recycle e ausência de dados sensíveis.

## Conexões
- [[gatling-session-estado-por-virtual-user]] — Veja também: Gatling: manter atributos na Session do próprio usuário.
- [[gatling-check-saveas-apos-sucesso]] — Veja também: Gatling: validar resposta antes de guardar valor com saveAs.

## Fontes
- [Gatling — Feeders](https://docs.gatling.io/concepts/session/feeders/) — consumo de registros e injeção de dados na sessão do usuário; consultado em 2026-10-02.
- [Gatling — Session API](https://docs.gatling.io/concepts/session/api/) — estado de cada virtual user e propagação de atributos; consultado em 2026-10-02.
