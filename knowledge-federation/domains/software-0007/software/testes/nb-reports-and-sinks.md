---
id: software.testes.tranche20.001454
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://www.nuget.org/packages/NBomber", "https://github.com/PragmaticFlow/NBomber"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NBomber: analisar relatórios e publicar métricas

## Em uma frase
Cada execução gera relatório navegável, e a integração com sistemas de acompanhamento permite publicar métricas em tempo real.

## Por que importa
O relatório sustenta a investigação, e a publicação contínua permite acompanhar a tendência entre execuções.

## Como funciona
Gere o relatório como artefato, publique as métricas no sistema de acompanhamento e mantenha o histórico das execuções relevantes.

## Exemplo
A série histórica de latência de um endpoint pode revelar degradação gradual que uma execução isolada não mostra.

## Limites e trade-offs
Relatórios sem histórico perdem a comparação, e volume alto de execuções sem retenção definida acumula artefatos sem uso.

## Como verificar
Compare dois relatórios de execuções próximas e confirme que a variação observada corresponde a alguma mudança conhecida.

## Conexões
- [[nb-assertions-and-thresholds]] — Veja também: NBomber: falhar o trabalho por limite.
- [[nb-http-metrics-and-plugins]] — Veja também: NBomber: medir detalhes de protocolo.

## Fontes
- [NBomber — Pacote publicado](https://www.nuget.org/packages/NBomber) — versões, dependências e documentação do pacote; consultado em 2026-10-03.
- [NBomber — repositório oficial](https://github.com/PragmaticFlow/NBomber) — código-fonte, integrações e documentação do projeto; consultado em 2026-10-03.
