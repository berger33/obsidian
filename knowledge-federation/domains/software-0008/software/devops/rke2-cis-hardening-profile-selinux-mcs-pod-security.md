---
id: software.devops.tranche17.001678
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

# RKE2: endurecimento CIS Kubernetes Benchmark (`profile: cis`) e isolamento SELinux Multi-Category Security (MCS)

## Em uma frase
O RKE2 fornece opções nativas de endurecimento (`profile: cis` em `config.yaml`) e suporte integrado a políticas **SELinux** com **Multi-Category Security (MCS)** para aprovar auditorias do CIS Kubernetes Benchmark com intervenção mínima do operador.

## Por que importa
Endurecer manualmente um cluster Kubernetes upstream para passar em mais de 100 controles do CIS Benchmark exige configurar dezenas de flags criptográficas no `kube-apiserver`, `kubelet` e `etcd`, permissões `0600` em diretórios de PKI, `NetworkPolicies` padrão e contextos de usuário para o `etcd`.

## Como funciona
Quando `profile: cis` é configurado no `/etc/rancher/rke2/config.yaml` (junto aos parâmetros sysctl de kernel exigidos pelo host e ao usuário dedicado `etcd`), o RKE2 valida esses pré-requisitos na partida, aplica automaticamente as flags restritivas nos Static Pods e impõe políticas de admissão de segurança de Pods e isolamento de rede entre namespaces.

## Exemplo
```yaml
# /etc/rancher/rke2/config.yaml para conformidade CIS e SELinux:
profile: "cis"
selinux: true
write-kubeconfig-mode: "0600"
```

## Limites e trade-offs
Se `profile: "cis"` for ativado em `/etc/rancher/rke2/config.yaml` sem que o usuário/grupo de sistema `etcd` exista no host Linux ou sem que os parâmetros `vm.overcommit_memory=1` e `vm.panic_on_oom=0` estejam aplicados no `sysctl`, o `rke2-server` recusará iniciar por segurança.

## Como verificar
Aplique os ajustes de `sysctl` e usuário `etcd` do guia de hardening, inicie o RKE2 com `profile: "cis"` e execute o `kube-bench` com o benchmark específico do RKE2 para comprovar `0` falhas.

## Conexões
- [[rke2-migracao-ingress-nginx-eol-para-traefik-v1-36]] — Veja também: RKE2: transição de Ingress NGINX (EOL em março de 2026) para Traefik como Ingress Controller padrão no RKE2 v1.36+.
- [[rke2-cadencia-releases-versionamento-semver-rke2r-upgrades]] — Veja também: RKE2: cadência de releases, esquema de versionamento `+rke2r<N>` e upgrades automatizados.

## Fontes
- [RKE2 GitHub — README.md (Rancher's Next-Gen Kubernetes Distribution / RKE Government, FIPS 140-2, CIS Hardening & Configuration File)](https://raw.githubusercontent.com/rancher/rke2/master/README.md) — README oficial do rancher/rke2 detalhando conformidade FIPS 140-2 com Go+BoringCrypto, CIS Benchmark, instalação systemd e /etc/rancher/rke2/config.yaml; consultado em 2026-10-03.
- [RKE2 Official Documentation — Architecture (Content Bootstrap from rke2-runtime, Server/Agent Static Pod Lifecycle, CNI, Traefik & CIS/SELinux)](https://docs.rke2.io/architecture) — Documentação oficial de arquitetura do RKE2 explicando Content Bootstrap, Static Pods do control plane, helm-controller, plugins CNI e transição para Traefik v1.36+; consultado em 2026-10-03.
- [RKE2 — Official GitHub Repository](https://github.com/rancher/rke2) — Repositório oficial Apache-2.0 do Rancher RKE2; consultado em 2026-10-03.
