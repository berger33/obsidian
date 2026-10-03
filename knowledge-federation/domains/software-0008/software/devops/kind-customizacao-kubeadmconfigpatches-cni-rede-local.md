---
id: software.devops.tranche09.000839
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/kind/main/README.md", "https://kind.sigs.k8s.io/docs/user/quick-start/", "https://github.com/kubernetes-sigs/kind"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kind: customização avançada do cluster com kubeadmConfigPatches, desativação da CNI padrão (kindnet) e redes dual-stack

## Em uma frase
Na configuração `kind.x-k8s.io/v1alpha4`, o bloco `networking` permite configurar `ipFamily` (`ipv4`, `ipv6` ou `dual`), sub-redes e desabilitar a CNI padrão (`disableDefaultCNI: true`), enquanto `kubeadmConfigPatches` aplica patches estratégicos ou JSON6902 à configuração do `kubeadm`.

## Por que importa
O `kind` vem por padrão com uma CNI leve chamada `kindnet`, mas engenheiros que desenvolvem políticas de segurança e observabilidade com **Cilium**, **Tetragon** ou **Calico** precisam iniciar o cluster `kind` sem a CNI padrão para instalar o Cilium/Calico do zero, além de frequentemente precisarem testar clusters IPv6 ou Dual-Stack e ajustar flags do `kube-apiserver` (como OIDC ou audit logs).

## Como funciona
Dentro do manifesto `kind: Cluster` (`apiVersion: kind.x-k8s.io/v1alpha4`): (1) a seção **`networking`** permite definir `disableDefaultCNI: true` (para que o `kind` não instale o `kindnet`, deixando os nós `NotReady` até que o usuário instale sua própria CNI como Cilium ou Calico), além de `podSubnet`, `serviceSubnet`, `ipFamily: dual` (ou `ipv6`) e `kubeProxyMode: "ipvs"` ou `"none"` (para Cilium kube-proxy replacement); e (2) a lista **`kubeadmConfigPatches`** (no nível do cluster ou de um nó específico) injeta configurações `InitConfiguration`, `ClusterConfiguration` ou `KubeletConfiguration` durante o bootstrap do `kubeadm` nos containers nós.

## Exemplo
```yaml
# Configuração kind sem CNI padrão e sem kube-proxy (pronta para instalar Cilium com kube-proxy replacement em Dual-Stack)
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  disableDefaultCNI: true
  kubeProxyMode: "none"
  ipFamily: dual
nodes:
  - role: control-plane
  - role: worker
```

## Limites e trade-offs
Quando você cria um cluster `kind` com `disableDefaultCNI: true`, os nós permanecerão em estado `NotReady` e os pods do `CoreDNS` ficarão `Pending` até que você instale manualmente um plugin CNI no cluster (ex.: `cilium install`); portanto, não use `--wait` longo esperando `Ready` no `kind create cluster` antes do passo que instala a CNI.

## Como verificar
Após criar o cluster com `ipFamily: dual` e instalar sua CNI, execute `kubectl get nodes -o jsonpath='{.items[*].status.addresses}'` para confirmar a atribuição de endereços IPv4 e IPv6 aos nós.

## Conexões
- [[kind-instalacao-reprodutivel-make-gimme-go-install-binarios]] — Veja também: kind: instalação via binários de release, go install e compilação reprodutível sem Go pré-instalado (make build com gimme).
- [[kind-montagem-diretorios-host-extramounts-registries-locais]] — Veja também: kind: compartilhamento de arquivos e dispositivos do host com os nós (extraMounts) e uso de registries locais.
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Referência cruzada direta com kind-clusters-kubernetes-locais-containers-docker-arquitetura.
- [[kind-configuracao-multinode-control-plane-ha-port-mappings]] — Referência cruzada direta com kind-configuracao-multinode-control-plane-ha-port-mappings.
- [[tetragon-ebpf-observabilidade-seguranca-runtime-enforcement]] — Referência cruzada direta com tetragon-ebpf-observabilidade-seguranca-runtime-enforcement.

## Fontes
- [kind GitHub — README.md (Kubernetes IN Docker, Go Packages & Design Principles)](https://raw.githubusercontent.com/kubernetes-sigs/kind/main/README.md) — README oficial do projeto kind (Kubernetes SIGs, Apache-2.0) sobre execução de nós em containers para testes do próprio Kubernetes e CI/CD; consultado em 2026-10-03.
- [kind Official Documentation — Quick Start (Installation, Multi-Node Config, Building & Loading Images, Exporting Logs)](https://kind.sigs.k8s.io/docs/user/quick-start/) — Guia oficial Quick Start do kind cobrindo instalação, criação/exclusão de clusters, imagens kindest/node com digest SHA-256, topologia multi-nó kind.x-k8s.io/v1alpha4, kind build node-image, kind load docker-image/image-archive e kind export logs; consultado em 2026-10-03.
- [Kubernetes SIGs kind — Official GitHub Repository](https://github.com/kubernetes-sigs/kind) — Repositório oficial do kind mantido pelo Kubernetes SIG Testing; consultado em 2026-10-03.
