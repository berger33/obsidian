---
id: software.devops.tranche17.001674
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

# RKE2: coreografia de inicialização de `server` e `agent` via goroutines e Static Pods

## Em uma frase
No motor interno do RKE2 (derivado do K3s), todo processo `rke2 server` é também um processo `agent` especializado que aguarda a subida do `containerd` e do `kubelet` local para então orquestrar `etcd`, `kube-apiserver`, `kube-controller-manager` e `kube-scheduler` como Static Pods supervisionados por goroutines.

## Por que importa
Diferentemente do K3s (que executa o control plane em memória dentro do próprio binário Go), o RKE2 executa cada componente do control plane em seu próprio container isolado via Static Pod gerenciado pelo `kubelet`, alinhando-se ao modelo de segurança do `kubeadm`.

## Como funciona
A sequência exata de boot do `rke2 server` dispara goroutines coordenadas: 1) inicia `containerd` e `kubelet`; 2) faz pull da imagem do `etcd`, aguarda o `kubelet` e grava `/var/lib/rancher/rke2/agent/pod-manifests/etcd.yaml`; 3) faz pull do `kube-apiserver`, aguarda o `etcd` responder e grava o manifesto do `kube-apiserver`; 4) aguarda o `kube-apiserver` ficar pronto e grava os manifestos de `kube-controller-manager` e `kube-scheduler`, iniciando em seguida o `helm-controller` embutido.

## Exemplo
```bash
ls -la /var/lib/rancher/rke2/agent/pod-manifests/
kubectl get pods -n kube-system -l tier=control-plane
```

## Limites e trade-offs
Como o control plane roda como Static Pods gerenciados pelo `kubelet` local, parar o `rke2-server.service` via `systemctl stop` interrompe o supervisor, mas os containers existentes podem continuar vivos no `containerd` até que `rke2-killall.sh` seja executado (se desejado encerrar todos os containers).

## Como verificar
Inspecione `/var/lib/rancher/rke2/agent/pod-manifests/` em um nó server e confirme os arquivos YAML gerados para `etcd`, `kube-apiserver`, `kube-controller-manager` e `kube-scheduler`.

## Conexões
- [[rke2-config-yaml-systemd-precedencia-flags-cli-listas]] — Veja também: RKE2: configuração declarativa em `/etc/rancher/rke2/config.yaml` e regras de precedência com flags CLI.
- [[rke2-cni-plugins-canal-cilium-calico-flannel-multus]] — Veja também: RKE2: seleção de plugins CNI (`canal`, `cilium`, `calico`, `flannel`) e composição multi-NIC com `multus`.

## Fontes
- [RKE2 GitHub — README.md (Rancher's Next-Gen Kubernetes Distribution / RKE Government, FIPS 140-2, CIS Hardening & Configuration File)](https://docs.rke2.io/architecture) — README oficial do rancher/rke2 detalhando conformidade FIPS 140-2 com Go+BoringCrypto, CIS Benchmark, instalação systemd e /etc/rancher/rke2/config.yaml; consultado em 2026-10-03.
- [RKE2 Official Documentation — Architecture (Content Bootstrap from rke2-runtime, Server/Agent Static Pod Lifecycle, CNI, Traefik & CIS/SELinux)](https://raw.githubusercontent.com/rancher/rke2/master/README.md) — Documentação oficial de arquitetura do RKE2 explicando Content Bootstrap, Static Pods do control plane, helm-controller, plugins CNI e transição para Traefik v1.36+; consultado em 2026-10-03.
- [RKE2 — Official GitHub Repository](https://github.com/rancher/rke2) — Repositório oficial Apache-2.0 do Rancher RKE2; consultado em 2026-10-03.
