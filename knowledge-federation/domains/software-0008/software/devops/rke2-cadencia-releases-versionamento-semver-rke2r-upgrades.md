---
id: software.devops.tranche17.001679
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
fontes: ["https://raw.githubusercontent.com/rancher/rke2/master/README.md", "https://docs.rke2.io/architecture", "https://github.com/rancher/rke2"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# RKE2: cadência de releases, esquema de versionamento `+rke2r<N>` e upgrades automatizados

## Em uma frase
O RKE2 acompanha de perto o ciclo de lançamento do Kubernetes upstream (com meta de publicar patch releases em até 1 semana e novas versões minor em até 30 dias), utilizando o sufixo SemVer `+rke2r<número>` (por exemplo `v1.36.1+rke2r1`).

## Por que importa
Se uma vulnerabilidade crítica for descoberta no pacote do `containerd`, em um chart CNI empacotado ou no código do próprio RKE2 enquanto o Kubernetes upstream permanece na mesma versão `v1.36.1`, a distribuição precisa publicar uma nova build mantendo compatibilidade SemVer.

## Como funciona
O sufixo `+rke2r1` -> `+rke2r2` permite lançar correções imediatas de empacotamento e segurança sobre a mesma versão base do Kubernetes (`v1.36.1`). Os upgrades podem ser feitos manualmente atualizando o binário/serviço `rke2` nó a nó ou de forma totalmente declarativa no cluster por meio do `system-upgrade-controller` da Rancher.

## Exemplo
```bash
curl -sfL https://get.rke2.io | INSTALL_RKE2_VERSION="v1.36.1+rke2r1" sh -
rke2 --version
kubectl get nodes -o wide
```

## Limites e trade-offs
Ao atualizar clusters RKE2 em alta disponibilidade, atualize sempre todos os nós `server` (control plane) um por vez antes de atualizar os nós `agent` (workers), e nunca pule versões minor intermediárias.

## Como verificar
Execute `rke2 --version` no host e `kubectl get nodes` para confirmar a versão exata `+rke2r<N>` reportada pelo `kubelet`.

## Conexões
- [[rke2-cis-hardening-profile-selinux-mcs-pod-security]] — Veja também: RKE2: endurecimento CIS Kubernetes Benchmark (`profile: cis`) e isolamento SELinux Multi-Category Security (MCS).
- [[rke2-alta-disponibilidade-etcd-embutido-snapshots-restore-s3]] — Veja também: RKE2: alta disponibilidade com `etcd` gerenciado, snapshots agendados e restauração de desastres via S3.

## Fontes
- [RKE2 GitHub — README.md (Rancher's Next-Gen Kubernetes Distribution / RKE Government, FIPS 140-2, CIS Hardening & Configuration File)](https://raw.githubusercontent.com/rancher/rke2/master/README.md) — README oficial do rancher/rke2 detalhando conformidade FIPS 140-2 com Go+BoringCrypto, CIS Benchmark, instalação systemd e /etc/rancher/rke2/config.yaml; consultado em 2026-10-03.
- [RKE2 Official Documentation — Architecture (Content Bootstrap from rke2-runtime, Server/Agent Static Pod Lifecycle, CNI, Traefik & CIS/SELinux)](https://docs.rke2.io/architecture) — Documentação oficial de arquitetura do RKE2 explicando Content Bootstrap, Static Pods do control plane, helm-controller, plugins CNI e transição para Traefik v1.36+; consultado em 2026-10-03.
- [RKE2 — Official GitHub Repository](https://github.com/rancher/rke2) — Repositório oficial Apache-2.0 do Rancher RKE2; consultado em 2026-10-03.
