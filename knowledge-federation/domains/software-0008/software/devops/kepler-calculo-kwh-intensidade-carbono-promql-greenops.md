---
id: software.devops.tranche15.001419
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md", "https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md", "https://github.com/sustainable-computing-io/kepler"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kepler: conversão de Joules para kWh e cálculo de pegada de carbono em consultas PromQL

## Em uma frase
Como o Kepler exporta energia acumulada na unidade padrão do Sistema Internacional (`joules_total`), operadores convertem facilmente essas séries em quilowatt-hora (`kWh`) em PromQL dividindo o incremento em Joules por `3.600.000` (`3.6e6`).

## Por que importa
Faturas de energia elétrica de datacenters e relatórios ESG de emissões de gases de efeito estufa (Escopo 2 e Escopo 3) são contabilizados em `kWh` e gramas de `CO2eq/kWh`, tornando essa conversão matemática a ponte direta entre observabilidade técnica e relatórios de sustentabilidade.

## Como funciona
Usando a função `increase()` sobre o contador `kepler_container_cpu_joules_total{zone="package"}` em uma janela de tempo (como `[1h]` ou `[24h]`) e dividindo por `3600000`, obtém-se o consumo em `kWh` de cada container, que pode então ser multiplicado pelo fator de PUE (*Power Usage Effectiveness*) do datacenter e pela intensidade de carbono da rede elétrica.

## Exemplo
```promql
# Consumo de energia de CPU em kWh nas últimas 24 horas por container
sum by (container_name, pod_id) (
  increase(kepler_container_cpu_joules_total{zone="package"}[24h])
) / 3600000
```

## Limites e trade-offs
Para obter o consumo total do container quando há aceleradores gráficos, some o incremento de `kepler_container_cpu_joules_total{zone="package"}` (mais `zone="dram"` quando disponível) ao incremento de `kepler_container_gpu_joules_total`, mantendo sempre o cuidado de não somar zonas de CPU sobrepostas.

## Como verificar
Valide no Grafana que a derivada temporal do contador `rate(kepler_node_cpu_joules_total{zone="package"}[5m])` acompanha de perto o valor instantâneo do gauge `kepler_node_cpu_watts{zone="package"}` (já que `1 Watt = 1 Joule/segundo`).

## Conexões
- [[kepler-implantacao-helm-oci-kustomize-alinhamento-tag-probes]] — Veja também: Kepler: implantação via Helm OCI, Kustomize, Kepler Operator e alinhamento estrito entre manifesto e imagem.
- [[kepler-integracao-finops-autoscaling-keda-desenvolvimento-compose]] — Veja também: Kepler: integração com KEDA, OpenCost e ambiente local Docker Compose com Prometheus e Grafana.

## Fontes
- [Kepler GitHub — README.md (v0.10.0+ Ground-Up Rewrite, Reduced Security Requirements, Dynamic RAPL Detection, Helm OCI & Kustomize Deployment)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md) — README oficial do sustainable-computing-io/kepler detalhando a reescrita v0.10.0+, remoção de CAP_SYSADMIN/CAP_BPF, acesso somente leitura a /proc e /sys e métodos de instalação; consultado em 2026-10-03.
- [Kepler Official Documentation — docs/user/metrics.md (RAPL Energy Zones, Node, Container, Process & Virtual Machine Prometheus Metrics)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md) — Referência oficial de métricas Prometheus do Kepler cobrindo zonas RAPL (psys, package, core, uncore, dram) e métricas em Joules e Watts para CPU e GPU; consultado em 2026-10-03.
- [Kepler — Official GitHub Repository](https://github.com/sustainable-computing-io/kepler) — Repositório oficial Apache-2.0 do Kepler na CNCF; consultado em 2026-10-03.
