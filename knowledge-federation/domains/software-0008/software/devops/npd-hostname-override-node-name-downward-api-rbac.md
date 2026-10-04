---
id: software.devops.tranche13.001209
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md", "https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json", "https://github.com/kubernetes/node-problem-detector"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Node Problem Detector: Identificação de Nó (--hostname-override e NODE_NAME) e RBAC de Mínimo Privilégio

## Em uma frase
Para atualizar as `NodeConditions` e emitir `Events` associados ao objeto `Node` correto no Kubernetes, o Node Problem Detector resolve o nome do nó seguindo a ordem de precedência: flag `--hostname-override`, variável de ambiente `NODE_NAME` (via Downward API `spec.nodeName`) e, por último, `os.Hostname`.

## Por que importa
Em provedores cloud e ambientes bare-metal onde o hostname retornado pelo sistema operacional (`os.Hostname`) difere do nome registrado pelo objeto `Node` no `kube-apiserver` (por exemplo, nome curto vs. FQDN interno), o NPD falha com erro `nodes "<hostname>" not found` ao tentar reportar problemas.

## Como funciona
No manifesto do `DaemonSet`, injeta-se a variável `NODE_NAME` usando `valueFrom.fieldRef.fieldPath: spec.nodeName` e vincula-se um `ServiceAccount` com `ClusterRole` permitindo `get` e `patch`/`update` em `nodes` e `nodes/status`, além de `create`, `patch` e `update` em `events`.

## Exemplo
```yaml
env:
  - name: NODE_NAME
    valueFrom:
      fieldRef:
        fieldPath: spec.nodeName
```

## Limites e trade-offs
Omitir a variável `NODE_NAME` (com `fieldPath: spec.nodeName`) no `DaemonSet` em nós cujo `os.Hostname` não coincide com `.metadata.name` do `Node` inutiliza silenciosamente o Kubernetes exporter do NPD.

## Como verificar
Defina sempre `NODE_NAME` via Downward API no `DaemonSet` e verifique nos logs iniciais do pod se o NPD identificou e sincronizou o objeto `Node` sem erros de RBAC.

## Conexões
- [[npd-systemd-monitor-frequent-restarts-kubelet-containerd-docker]] — Veja também: Node Problem Detector: Detecção de Reinícios Frequentes (FrequentKubeletRestart e FrequentContainerdRestart).
- [[npd-integracao-remedy-systems-draino-kured-cluster-api-autohealing]] — Veja também: Node Problem Detector: Integração com Sistemas de Auto-Remediação (Draino, Kured e Cluster API Node HealthCheck).

## Fontes
- [Kubernetes Node Problem Detector GitHub — README.md (Problem Daemons, System Log Monitor, Custom Plugin Monitor & Exporters)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/README.md) — README oficial do kubernetes/node-problem-detector detalhando Problem Daemons (SystemLogMonitor, SystemStatsMonitor, CustomPluginMonitor, HealthChecker), Exporters (Kubernetes, Prometheus, Stackdriver) e flags de CLI; consultado em 2026-10-03.
- [Node Problem Detector Official Config — config/kernel-monitor.json (KernelOops, OOMKilled, Ext4Error & TaskHung Rules)](https://raw.githubusercontent.com/kubernetes/node-problem-detector/master/config/kernel-monitor.json) — Arquivo oficial de regras do kernel-monitor.json do Node Problem Detector definindo condições permanentes e eventos temporários a partir do kmsg; consultado em 2026-10-03.
- [Kubernetes Node Problem Detector — Official GitHub Repository](https://github.com/kubernetes/node-problem-detector) — Repositório oficial do Node Problem Detector no projeto Kubernetes; consultado em 2026-10-03.
