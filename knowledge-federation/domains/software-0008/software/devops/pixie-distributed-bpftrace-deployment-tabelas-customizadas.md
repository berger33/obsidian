---
id: software.devops.tranche14.001307
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

# Pixie: Implantação Distribuída de Programas bpftrace no Cluster com Tabelas PxL

## Em uma frase
O Pixie permite implantar dinamicamente programas **bpftrace** customizados em todos os nós do cluster Kubernetes a partir de um único script PxL, coletando a saída estruturada dos `printf` do bpftrace diretamente em uma tabela consultável na UI e na CLI.

## Por que importa
Executar `bpftrace` manualmente exige abrir sessões SSH privilegiadas em dezenas de worker nodes simultaneamente e consolidar textos soltos de terminal.

## Como funciona
Dentro de um script PxL, utiliza-se `pxtrace.UpsertTracepoint(...)` passando o código bpftrace inline; o Vizier distribui o programa para todos os PEMs dos nós, valida sua segurança via verificador eBPF do kernel e canaliza os eventos emitidos para uma tabela temporária consultada com `px.DataFrame`.

## Exemplo
```python
import px
import pxtrace

program = """
tracepoint:skb:kfree_skb {
  printf("drop_location:%p protocol:%d\\n", args->location, args->protocol);
}
"""
pxtrace.UpsertTracepoint('custom_skb_drops', 'skb_drops_table', program, pxtrace.all_nodes(), "10m")
df = px.DataFrame(table='skb_drops_table')
px.display(df)
```

## Limites e trade-offs
Definir um tempo de vida (`ttl`) excessivamente longo para dezenas de tracepoints `bpftrace` experimentais deixa probes extras ativas no kernel após o término da investigação.

## Como verificar
Defina sempre um TTL curto (como `"5m"` ou `"10m"`) em `pxtrace.UpsertTracepoint` para que o Pixie remova automaticamente as probes bpftrace quando a sessão encerrar.

## Conexões
- [[pixie-continuous-profiling-flamegraphs-cpu-pod-node]] — Veja também: Pixie: Continuous Application Profiling e Flame Graphs de CPU por Pod e Nó.
- [[pixie-dynamic-go-logging-uprobes-debug-producao-sem-redeploy]] — Veja também: Pixie: Dynamic Go Logging em Produção sem Recompilação ou Redeploy de Binários.

## Fontes
- [Pixie Official Documentation — Pixie Overview & Architecture (PEM, Vizier, Pixie Cloud, CLI & eBPF Auto-Telemetry)](https://raw.githubusercontent.com/pixie-io/pixie/main/README.md) — Visão geral e arquitetura oficial do Pixie detalhando o Pixie Edge Module (PEM), Vizier, Pixie Cloud, coleta eBPF sem instrumentação manual e linguagem PxL; consultado em 2026-10-03.
- [Pixie GitHub — README.md (Network Monitoring, Service Performance, Database Query Profiling, Continuous Profiling, bpftrace & Dynamic Go Logging)](https://docs.px.dev/about-pixie/what-is-pixie/) — README oficial do pixie-io/pixie (CNCF Sandbox) documentando casos de uso de monitoramento de rede/DNS/TCP drops, profiling de queries SQL, Flame Graphs, bpftrace distribuído e Dynamic Go Logging; consultado em 2026-10-03.
- [Pixie — Official GitHub Repository](https://github.com/pixie-io/pixie) — Repositório oficial do Pixie na CNCF; consultado em 2026-10-03.
