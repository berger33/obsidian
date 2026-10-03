---
id: software.devops.tranche17.001603
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/karmada-io/karmada/master/README.md", "https://karmada.io/docs/core-concepts/architecture/", "https://github.com/karmada-io/karmada"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Karmada: modos de registro de clusters membros (`Push` direto vs `Pull` via `karmada-agent`)

## Em uma frase
O Karmada suporta dois modos operacionais de conexão para clusters membros (inclusive combinados na mesma frota): o modo **Push** (o plano de controle acessa diretamente o `kube-apiserver` do cluster membro) e o modo **Pull** (um agente `karmada-agent` rodando no cluster membro busca os objetos `Work` no Karmada).

## Por que importa
Clusters em nuvens privadas, filiais de borda (*edge*) ou redes restritas frequentemente ficam atrás de NAT/firewalls rigorosos que proíbem conexões de entrada vindas da internet até o seu `kube-apiserver`, inviabilizando o modo Push.

## Como funciona
No modo `Push` (`karmadactl join`), o `Execution Controller` central empurra os recursos para o endpoint da API do cluster membro. Já no modo `Pull` (`karmadactl register`), o `karmada-agent` instalado dentro do cluster membro abre conexão de saída até o `karmada-apiserver`, monitora apenas seu próprio namespace de execução (`karmada-es-<cluster>`), aplica localmente os manifestos dos objetos `Work` e reporta o status de saúde de volta.

## Exemplo
```bash
karmadactl join member-cloud --cluster-kubeconfig=$HOME/.kube/member-cloud.config
karmadactl register 10.20.0.10:5443 --token abcdef.0123456789abcdef --discovery-token-ca-cert-hash sha256:1234...
```

## Limites e trade-offs
No modo `Pull`, o plano de controle central do Karmada não armazena credenciais de `cluster-admin` do cluster membro, reduzindo significativamente o raio de explosão (*blast radius*) em caso de comprometimento central.

## Como verificar
Execute `kubectl --context karmada-apiserver get clusters -o wide` e verifique a coluna `MODE` (`Push` ou `Pull`) de cada cluster registrado.

## Conexões
- [[karmada-pipeline-propagacao-resourcebinding-work-execution]] — Veja também: Karmada: fluxo de propagação em quatro estágios (`PropagationPolicy` -> `ResourceBinding` -> `Work` -> Member Cluster).
- [[karmada-propagationpolicy-clusterpropagationpolicy-seletores-1-para-n]] — Veja também: Karmada: políticas de posicionamento `PropagationPolicy` e `ClusterPropagationPolicy` com mapeamento `1:N`.

## Fontes
- [Karmada GitHub — README.md (Kubernetes Armada CNCF Incubating Multi-Cloud & Multi-Cluster Kubernetes Orchestration)](https://raw.githubusercontent.com/karmada-io/karmada/master/README.md) — README oficial do karmada-io/karmada (CNCF Incubating) apresentando capacidades multi-cluster, API compatível com Kubernetes nativo e políticas de propagação; consultado em 2026-10-03.
- [Karmada Official Documentation — Core Concepts: Architecture (Control Plane, PropagationPolicy, OverridePolicy, ResourceBinding, Work & Agent)](https://karmada.io/docs/core-concepts/architecture/) — Documentação oficial de arquitetura do Karmada detalhando API Server, Controller Manager, Karmada Scheduler, Execution Space e sincronização para member clusters; consultado em 2026-10-03.
- [Karmada — Official GitHub Repository](https://github.com/karmada-io/karmada) — Repositório oficial Apache-2.0 do projeto Karmada na CNCF; consultado em 2026-10-03.
