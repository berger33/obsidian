---
id: software.devops.tranche09.000835
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

# kind: fixação de versões do Kubernetes por digest SHA-256, habilitação de Feature Gates e uso de Proxy

## Em uma frase
O `kind` permite escolher a versão exata do Kubernetes fixando a imagem `kindest/node:<tag>@sha256:<digest>` (na CLI `--image` ou por nó no arquivo de config), habilitar recursos experimentais via `featureGates` e propagar `HTTP_PROXY`/`HTTPS_PROXY`/`NO_PROXY`.

## Por que importa
Em pipelines de CI que testam operadores Kubernetes, charts Helm ou CRDs contra uma matriz de versões (ex.: Kubernetes `v1.33`, `v1.34` e `v1.35`) ou que precisam validar uma `FeatureGate` alpha/beta recém-lançada no Kubernetes, o engenheiro precisa controlar a versão exata e as flags do control plane de forma reprodutível. A seção `Advanced` do `Quick Start` oficial do `kind` documenta esses recursos.

## Como funciona
(1) **Versão do Kubernetes**: cada release do `kind` publica na página de Releases do GitHub a lista oficial de imagens `kindest/node` com seus respectivos digests `sha256` para cada versão do Kubernetes; o usuário pode passar `--image kindest/node:v1.35.0@sha256:...` na CLI ou definir o campo `image:` em cada nó do arquivo `kind: Cluster`; (2) **Feature Gates**: declarar o mapa `featureGates: { FeatureGateName: true }` no topo do `kind: Cluster` instrui o `kind` a customizar automaticamente a configuração do `kubeadm` (`kube-apiserver`, `kube-controller-manager`, `kube-scheduler` e `kubelet`) com a feature gate ativada; e (3) **Proxy**: se `HTTP_PROXY`, `HTTPS_PROXY` ou `NO_PROXY` estiverem definidas no ambiente (maiúsculas têm precedência), o `kind` as repassa para dentro dos nós e adiciona automaticamente as sub-redes internas do cluster ao `NO_PROXY`.

## Exemplo
```yaml
# Configuração kind habilitando Feature Gates no cluster e fixando a imagem do nó
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
featureGates:
  MutatingAdmissionPolicy: true
nodes:
  - role: control-plane
```

## Limites e trade-offs
Sempre utilize a imagem `kindest/node` correspondente à sua versão atual do binário `kind` (verificada com `kind version` e listada nas notas de release daquela versão no GitHub), pois usar uma imagem `kindest/node` construída para uma versão incompatível do `kind` pode falhar durante a execução dos passos internos do `kubeadm`.

## Como verificar
Após criar o cluster com `featureGates` configuradas, inspecione o manifesto do pod estático do `kube-apiserver` (`kubectl get pod -n kube-system kube-apiserver-kind-control-plane -o yaml | grep feature-gates`) para confirmar a ativação da flag.

## Conexões
- [[kind-configuracao-multinode-control-plane-ha-port-mappings]] — Veja também: kind: configuração declarativa de clusters multi-nós, Control Plane HA e extraPortMappings (kind.x-k8s.io/v1alpha4).
- [[kind-construcao-node-image-codigo-fonte-kubernetes-build]] — Veja também: kind: construção de imagens de nó customizadas (kind build node-image) a partir de source, release, url ou file.
- [[kind-clusters-kubernetes-locais-containers-docker-arquitetura]] — Referência cruzada direta com kind-clusters-kubernetes-locais-containers-docker-arquitetura.

## Fontes
- [kind GitHub — README.md (Kubernetes IN Docker, Go Packages & Design Principles)](https://raw.githubusercontent.com/kubernetes-sigs/kind/main/README.md) — README oficial do projeto kind (Kubernetes SIGs, Apache-2.0) sobre execução de nós em containers para testes do próprio Kubernetes e CI/CD; consultado em 2026-10-03.
- [kind Official Documentation — Quick Start (Installation, Multi-Node Config, Building & Loading Images, Exporting Logs)](https://kind.sigs.k8s.io/docs/user/quick-start/) — Guia oficial Quick Start do kind cobrindo instalação, criação/exclusão de clusters, imagens kindest/node com digest SHA-256, topologia multi-nó kind.x-k8s.io/v1alpha4, kind build node-image, kind load docker-image/image-archive e kind export logs; consultado em 2026-10-03.
- [Kubernetes SIGs kind — Official GitHub Repository](https://github.com/kubernetes-sigs/kind) — Repositório oficial do kind mantido pelo Kubernetes SIG Testing; consultado em 2026-10-03.
