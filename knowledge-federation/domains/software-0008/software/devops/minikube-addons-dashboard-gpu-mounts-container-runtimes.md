---
id: software.devops.tranche09.000843
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

# Kubernetes minikube: marketplace de Addons, Dashboard integrado, suporte a GPUs NVIDIA/AMD e Filesystem Mounts

## Em uma frase
O `minikube` inclui um marketplace embutido de **Addons** (`minikube addons enable <nome>`), comando nativo para abrir o Kubernetes Dashboard (`minikube dashboard`), seleção de container runtime (`--container-runtime`), montagem de diretórios do host (`minikube mount`) e suporte a GPUs NVIDIA e AMD.

## Por que importa
Configurar manualmente Ingress NGINX, Metrics Server, Registry local, Istio, MetalLB ou passthrough de GPU para cargas de Machine Learning em um cluster de desenvolvimento consome horas de trabalho repetitivo. A seção `Features` do README oficial do `minikube` destaca esses recursos voltados à produtividade do desenvolvedor.

## Como funciona
(1) **Dashboard**: executar **`minikube dashboard`** ativa automaticamente o addon do painel oficial do Kubernetes, abre um proxy seguro e lança o Dashboard no navegador (ou imprime o link com `--url`, inclusive dentro de GitHub Codespaces); (2) **Addons**: `minikube addons list` exibe dezenas de extensões mantidas pela comunidade (`ingress`, `metrics-server`, `registry`, `storage-provisioner`, `volumesnapshots`, `nvidia-device-plugin`), ativáveis com `minikube addons enable <addon>`; (3) **Container runtimes**: `minikube start --container-runtime=containerd` (ou `cri-o` / `docker`) escolhe o runtime do cluster; (4) **Filesystem mounts**: `minikube mount /caminho/host:/caminho/vm` monta diretórios locais em tempo real dentro do nó; e (5) **Suporte a GPU**: permite expor GPUs **NVIDIA** e **AMD** para treinar ou servir modelos de IA/ML localmente no Kubernetes.

## Exemplo
```bash
# Listar os addons disponíveis, habilitar o metrics-server e o ingress no minikube e obter a URL do dashboard
minikube addons list
minikube addons enable metrics-server
minikube addons enable ingress
minikube dashboard --url
```

## Limites e trade-offs
O comando `minikube mount <origem>:<destino>` utiliza um servidor de arquivos 9P em espaço de usuário rodando no processo de linha de comando; se você fechar o terminal onde `minikube mount` está rodando, os pods dentro do cluster perderão imediatamente o acesso aos arquivos montados naquele caminho.

## Como verificar
Após executar `minikube addons enable metrics-server`, aguarde alguns segundos e rode `kubectl top nodes` e `kubectl top pods -A` para confirmar a coleta de métricas de CPU e memória no cluster local.

## Conexões
- [[minikube-exposicao-servicos-service-nodeport-tunnel-loadbalancer]] — Veja também: Kubernetes minikube: acesso a serviços locais NodePort (minikube service) e LoadBalancer (minikube tunnel).
- [[minikube-customizacao-apiserver-kubelet-codespaces-ci]] — Veja também: Kubernetes minikube: customização de flags do apiserver/kubelet (--extra-config), GitHub Codespaces e Dev Containers.
- [[minikube-clusters-locais-kubernetes-perfis-controles-basicos]] — Referência cruzada direta com minikube-clusters-locais-kubernetes-perfis-controles-basicos.

## Fontes
- [minikube GitHub — README.md (Local Kubernetes, Multi-Platform Drivers & Design Principles)](https://raw.githubusercontent.com/kubernetes/minikube/master/README.md) — README oficial do projeto minikube detalhando objetivos de simplicidade e conformidade com recursos do Kubernetes local; consultado em 2026-10-03.
- [minikube Official Documentation — Basic Controls (start/pause/stop/delete, kubectl Wrapper, Addons, service/tunnel & profiles)](https://minikube.sigs.k8s.io/docs/handbook/controls/) — Documentação oficial Basic Controls do minikube cobrindo ciclo de vida de clusters, perfis (-p), wrapper minikube kubectl --, addons (dashboard, ingress, metrics-server), minikube service, minikube tunnel e minikube node/image/cache; consultado em 2026-10-03.
- [Kubernetes minikube — Official GitHub Repository](https://github.com/kubernetes/minikube) — Repositório oficial Apache-2.0 do minikube; consultado em 2026-10-03.
