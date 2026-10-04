---
id: software.devops.tranche14.001308
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/pixie-io/pixie/main/README.md", "https://docs.px.dev/about-pixie/what-is-pixie/", "https://github.com/pixie-io/pixie"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Pixie: Dynamic Go Logging em Produção sem Recompilação ou Redeploy de Binários

## Em uma frase
O recurso de **Dynamic Go Logging** do Pixie permite inspecionar os valores dos argumentos e variáveis retornadas por funções específicas de binários **Go** rodando em produção sem recompilar o código nem reiniciar os Pods.

## Por que importa
Em incidentes reais, adicionar um `log.Printf` para ver o valor de um parâmetro passado para uma função interna exigiria abrir PR, rodar o pipeline de CI, construir nova imagem e reiniciar os Pods (perdendo o estado em memória que causou o bug).

## Como funciona
Utilizando `uprobes` eBPF ancoradas nas informações DWARF do binário Go, o Pixie anexa um probe dinâmico no endereço de entrada/saída da função alvo e grava os valores dos argumentos a cada invocação em uma tabela de telemetria temporária.

## Exemplo
```bash
# Listar scripts de coleta customizada e tracing dinamico disponiveis:
px script list | grep -E "go|trace"
```

## Limites e trade-offs
Compilar binários Go com as flags `-ldflags="-s -w"` remove completamente as informações de depuração DWARF, impedindo que o Dynamic Go Logging localize a assinatura e os offsets dos argumentos da função.

## Como verificar
Se desejar utilizar Dynamic Go Logging em serviços críticos, preserve as informações DWARF nos binários Go ou utilize imagens com símbolos de debug.

## Conexões
- [[pixie-distributed-bpftrace-deployment-tabelas-customizadas]] — Veja também: Pixie: Implantação Distribuída de Programas bpftrace no Cluster com Tabelas PxL.
- [[pixie-service-performance-mapas-latencia-slowest-requests]] — Veja também: Pixie: Monitoramento de Performance de Serviços (Service Maps, Latência por Endpoint e Slowest Requests).

## Fontes
- [Pixie Official Documentation — Pixie Overview & Architecture (PEM, Vizier, Pixie Cloud, CLI & eBPF Auto-Telemetry)](https://raw.githubusercontent.com/pixie-io/pixie/main/README.md) — Visão geral e arquitetura oficial do Pixie detalhando o Pixie Edge Module (PEM), Vizier, Pixie Cloud, coleta eBPF sem instrumentação manual e linguagem PxL; consultado em 2026-10-03.
- [Pixie GitHub — README.md (Network Monitoring, Service Performance, Database Query Profiling, Continuous Profiling, bpftrace & Dynamic Go Logging)](https://docs.px.dev/about-pixie/what-is-pixie/) — README oficial do pixie-io/pixie (CNCF Sandbox) documentando casos de uso de monitoramento de rede/DNS/TCP drops, profiling de queries SQL, Flame Graphs, bpftrace distribuído e Dynamic Go Logging; consultado em 2026-10-03.
- [Pixie — Official GitHub Repository](https://github.com/pixie-io/pixie) — Repositório oficial do Pixie na CNCF; consultado em 2026-10-03.
