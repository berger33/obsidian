---
id: software.testes.tranche11.000538
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
fontes: ["https://docs.gatling.io/reference/script/http/protocol/", "https://docs.gatling.io/concepts/scenario/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: centralizar protocolo HTTP comum sem esconder overrides

## Em uma frase
Protocol configuration reúne base URL, headers e opções compartilhadas que podem ser associadas a um ou mais cenários.

## Por que importa
Configuração duplicada deriva entre cenários; override global oculto pode alterar comportamento sem ficar evidente no request.

## Como funciona
Declare configuração HTTP legível, aplique-a nos cenários pretendidos e mantenha headers específicos junto ao request que os exige.

## Exemplo
Dois cenários usam mesmo baseUrl e accept header, enquanto fluxo admin define token em sua ação autenticada.

## Limites e trade-offs
Defaults compartilhados não são automaticamente aplicados se protocolo não for associado ao setup do cenário.

## Como verificar
Inspecione requests emitidos por cada cenário e faça teste de configuração quando mudar base URL ou TLS.

## Conexões
- [[gatling-pauses-e-pacing]] — Veja também: Gatling: distinguir pausa do usuário de arrival-rate injection.
- [[gatling-session-debug-fora-da-carga]] — Veja também: Gatling: limitar logging e inspeção de Session fora da carga.

## Fontes
- [Gatling — HTTP Protocol](https://docs.gatling.io/reference/script/http/protocol/) — configuração de protocolo reutilizável por cenário; consultado em 2026-10-02.
- [Gatling — Scenario](https://docs.gatling.io/concepts/scenario/) — sequência de ações, exec, controles de fluxo e pausas; consultado em 2026-10-02.
