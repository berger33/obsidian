---
id: software.devops.tranche02.000172
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/fluent/fluent-bit/master/README.md", "https://docs.fluentbit.io/manual/pipeline/inputs"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Suporte multi-plataforma (Linux, Windows, macOS, BSD e sistemas embarcados) e escala de produção

## Em uma frase
As seções `About`, `Install Fluent Bit` e `Production Usage` do README destacam que o Fluent Bit suporta uma ampla variedade de plataformas — incluindo **Linux**, **Windows**, **MacOS**, **BSD** e ambientes **Embedded** (embarcados) —, disponibilizando pacotes Linux (Debian, Ubuntu, RHEL, etc.), imagens Docker e binários Windows, e sendo implantado **mais de 10 milhões de vezes por dia** com mais de **15 bilhões de downloads** acumulados.

## Por que importa
Muitas organizações operam frotas mistas com servidores Linux, nós Windows Server, estações macOS, appliances BSD e gateways IoT embarcados; usar o mesmo agente C nativo em todas essas plataformas padroniza os pipelines de telemetria.

## Como funciona
Utilize os pacotes oficiais da distribuição Linux (`docs.fluentbit.io/manual/installation/downloads/linux`), imagens Docker ou binários Windows conforme o sistema operacional do nó monitorado.

## Exemplo
Uma empresa industrial utiliza o Fluent Bit tanto em gateways Linux embarcados na fábrica quanto nos clusters Kubernetes na nuvem para encaminhar telemetria ao mesmo agregador central.

## Limites e trade-offs
Verifique a disponibilidade de plugins específicos por sistema operacional (por exemplo, coletores exclusivos do kernel Linux versus eventos do Windows) ao compartilhar configurações entre plataformas distintas.

## Como verificar
Conferi as seções About, Install Fluent Bit e Production Usage no README oficial de `fluent/fluent-bit`.

## Conexões
- [[fluentbit-lightweight-telemetry-agent-logs-metrics-traces]] — Veja também: Definição do Fluent Bit como agente leve para Logs, Métricas e Traces graduado na CNCF.
- [[fluentbit-release-cadence-v5-1-and-maintenance-policy]] — Veja também: Cadência de releases maiores a cada 3–4 meses, série v5.1 e guia MAINTENANCE.md.

## Fontes
- [Fluent Bit — GitHub README](https://raw.githubusercontent.com/fluent/fluent-bit/master/README.md) — Visão geral do Fluent Bit (agente graduado na CNCF para Logs, Metrics e Traces), suporte multi-plataforma, ciclo de 3–4 meses (v5.1), 70+ plugins, SQL Stream Processing, extensibilidade C/Lua/Go e build CMake.; consultado em 2026-10-03.
- [Fluent Bit Official Documentation — Pipeline Inputs, Filters & Outputs](https://docs.fluentbit.io/manual/pipeline/inputs) — Documentação oficial dos plugins de Input, Filter e Output e guias de instalação do Fluent Bit.; consultado em 2026-10-03.
