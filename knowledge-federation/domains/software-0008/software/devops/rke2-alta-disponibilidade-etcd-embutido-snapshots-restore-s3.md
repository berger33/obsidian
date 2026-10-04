---
id: software.devops.tranche17.001680
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
fontes: ["https://docs.rke2.io/architecture", "https://raw.githubusercontent.com/rancher/rke2/master/README.md", "https://github.com/rancher/rke2"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# RKE2: alta disponibilidade com `etcd` gerenciado, snapshots agendados e restauração de desastres via S3

## Em uma frase
Nos clusters multi-server, o RKE2 gerencia nativamente um cluster `etcd` embutido (iniciando o primeiro server com `cluster-init: true` ou ingresso via `server: https://<ip>:9345` e `token`), com suporte integrado a snapshots periódicos em disco local e upload automático para buckets S3 compatíveis.

## Por que importa
Configurar backups externos de `etcd` com `etcdctl snapshot save`, certificados de cliente e cronjobs manuais em cada nó master costuma falhar silenciosamente ou deixar backups presos no mesmo disco do nó que sofreu pane.

## Como funciona
No RKE2, basta declarar `etcd-snapshot-schedule-cron`, `etcd-snapshot-retention` e opcionalmente `etcd-s3: true` (com endpoint e bucket) no `config.yaml`, ou disparar snapshots sob demanda com `rke2 etcd-snapshot save`. Para recuperar o cluster após desastre, executa-se `rke2 server --cluster-reset --cluster-reset-restore-path=<snapshot>`.

## Exemplo
```bash
rke2 etcd-snapshot save --name pre-upgrade-snapshot
rke2 etcd-snapshot ls
```

## Limites e trade-offs
O supervisor de registro de nós do RKE2 escuta na porta TCP `9345` (enquanto o `kube-apiserver` escuta na porta `6443`); firewalls internos entre nós `server` e `agent` devem permitir explicitamente as portas `9345` e `6443` (além de `2379`-`2380` entre servers para o `etcd`).

## Como verificar
Execute `rke2 etcd-snapshot ls` (ou `kubectl get etcdsnapshotfiles`) para verificar a lista de snapshots válidos armazenados localmente e/ou no S3.

## Conexões
- [[rke2-cadencia-releases-versionamento-semver-rke2r-upgrades]] — Veja também: RKE2: cadência de releases, esquema de versionamento `+rke2r<N>` e upgrades automatizados.

## Fontes
- [RKE2 GitHub — README.md (Rancher's Next-Gen Kubernetes Distribution / RKE Government, FIPS 140-2, CIS Hardening & Configuration File)](https://docs.rke2.io/architecture) — README oficial do rancher/rke2 detalhando conformidade FIPS 140-2 com Go+BoringCrypto, CIS Benchmark, instalação systemd e /etc/rancher/rke2/config.yaml; consultado em 2026-10-03.
- [RKE2 Official Documentation — Architecture (Content Bootstrap from rke2-runtime, Server/Agent Static Pod Lifecycle, CNI, Traefik & CIS/SELinux)](https://raw.githubusercontent.com/rancher/rke2/master/README.md) — Documentação oficial de arquitetura do RKE2 explicando Content Bootstrap, Static Pods do control plane, helm-controller, plugins CNI e transição para Traefik v1.36+; consultado em 2026-10-03.
- [RKE2 — Official GitHub Repository](https://github.com/rancher/rke2) — Repositório oficial Apache-2.0 do Rancher RKE2; consultado em 2026-10-03.
