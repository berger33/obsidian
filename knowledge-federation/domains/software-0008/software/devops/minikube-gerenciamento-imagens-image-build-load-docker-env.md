---
id: software.devops.tranche09.000845
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
fontes: ["https://raw.githubusercontent.com/kubernetes/minikube/master/README.md", "https://minikube.sigs.k8s.io/docs/handbook/controls/", "https://github.com/kubernetes/minikube"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubernetes minikube: construção e carregamento de imagens locais (minikube image load, image build e docker-env)

## Em uma frase
Para usar imagens de container locais sem fazer push para um registry externo, o `minikube` oferece os subcomandos `minikube image load <img:tag>`, `minikube image build -t <img:tag> .` e `eval $(minikube -p minikube docker-env)`.

## Por que importa
Assim como ocorre em outros clusters locais baseados em VM ou container (`kicbase`), o ambiente interno do nó `minikube` possui seu próprio armazenamento de imagens isolado do daemon Docker da máquina host; entender as formas nativas de disponibilizar imagens locais no `minikube` acelera drasticamente o loop de desenvolvimento (`inner loop`).

## Como funciona
O `minikube` disponibiliza três fluxos para trabalhar com imagens locais: (1) **`minikube image load minha-app:v1`**: transfere uma imagem já construída no host para dentro de todos os nós do cluster `minikube` (independentemente de o runtime do cluster ser `docker`, `containerd` ou `cri-o`); (2) **`minikube image build -t minha-app:v1 .`**: constrói o `Dockerfile` diretamente dentro do runtime do nó `minikube`, sem gastar espaço duplicado no host; e (3) **`eval $(minikube -p minikube docker-env)`** (quando o cluster usa o runtime `docker`): aponta o cliente `docker` do terminal atual diretamente para o daemon Docker de dentro do `minikube`, de modo que qualquer `docker build` subsequente já grava a imagem diretamente no cluster.

## Exemplo
```bash
# Construir uma imagem diretamente dentro do cluster minikube e listar as imagens presentes no nó
minikube image build -t meu-servico:v1.0.0 .
minikube image ls | grep meu-servico
```

## Limites e trade-offs
Assim como no Kubernetes em geral, ao usar imagens construídas ou carregadas localmente no `minikube`, evite usar a tag `:latest` (ou defina `imagePullPolicy: IfNotPresent` / `Never` no manifesto do Pod), pois a tag `:latest` aciona `imagePullPolicy: Always` por padrão, fazendo o `kubelet` tentar buscar a imagem em um registry remoto na internet.

## Como verificar
Execute `minikube image ls` para confirmar que `docker.io/library/meu-servico:v1.0.0` está registrada no armazenamento interno do nó `minikube`.

## Conexões
- [[minikube-customizacao-apiserver-kubelet-codespaces-ci]] — Veja também: Kubernetes minikube: customização de flags do apiserver/kubelet (--extra-config), GitHub Codespaces e Dev Containers.
- [[minikube-drivers-execucao-docker-kvm2-qemu-vfkit-none]] — Veja também: Kubernetes minikube: arquitetura de drivers multiplataforma (Docker/Podman containers, VMs KVM2/QEMU/VFKit/Hyper-V e bare-metal).
- [[minikube-clusters-locais-kubernetes-perfis-controles-basicos]] — Referência cruzada direta com minikube-clusters-locais-kubernetes-perfis-controles-basicos.
- [[kind-carregamento-imagens-locais-load-docker-image-archive]] — Referência cruzada direta com kind-carregamento-imagens-locais-load-docker-image-archive.
- [[buildpacks-cli-pack-build-lifecycle-builders-oci]] — Referência cruzada direta com buildpacks-cli-pack-build-lifecycle-builders-oci.

## Fontes
- [minikube GitHub — README.md (Local Kubernetes, Multi-Platform Drivers & Design Principles)](https://raw.githubusercontent.com/kubernetes/minikube/master/README.md) — README oficial do projeto minikube detalhando objetivos de simplicidade e conformidade com recursos do Kubernetes local; consultado em 2026-10-03.
- [minikube Official Documentation — Basic Controls (start/pause/stop/delete, kubectl Wrapper, Addons, service/tunnel & profiles)](https://minikube.sigs.k8s.io/docs/handbook/controls/) — Documentação oficial Basic Controls do minikube cobrindo ciclo de vida de clusters, perfis (-p), wrapper minikube kubectl --, addons (dashboard, ingress, metrics-server), minikube service, minikube tunnel e minikube node/image/cache; consultado em 2026-10-03.
- [Kubernetes minikube — Official GitHub Repository](https://github.com/kubernetes/minikube) — Repositório oficial Apache-2.0 do minikube; consultado em 2026-10-03.
