---
id: software.devops.tranche09.000842
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

# Kubernetes minikube: acesso a serviços locais NodePort (minikube service) e LoadBalancer (minikube tunnel)

## Em uma frase
O `minikube` facilita o acesso da máquina host a aplicações expostas no cluster por meio de dois comandos dedicados: `minikube service <nome>` (para abrir endpoints `NodePort` no navegador/terminal) e `minikube tunnel` (para atribuir IPs roteáveis a serviços `type: LoadBalancer`).

## Por que importa
Em um cluster Kubernetes local (onde o nó roda dentro de uma VM ou de um container Docker isolado da rede de loopback da estação de trabalho, especialmente no macOS e Windows), quando um desenvolvedor cria um Service `type: LoadBalancer`, a coluna `EXTERNAL-IP` fica presa indefinidamente em `<pending>`, e portas `NodePort` não respondem diretamente em `localhost`. O README oficial e o `Basic controls` do `minikube` resolvem ambos os cenários.

## Como funciona
(1) **Acesso `NodePort` (`minikube service`)**: após criar e expor um deployment (`kubectl expose deployment hello-minikube --type=NodePort --port=8080`), executar **`minikube service hello-minikube`** (ou `--url` para apenas imprimir a URL no terminal sem abrir navegador) resolve o IP/porta do nó (e cria um túnel local automático quando necessário em drivers como Docker no macOS/Windows); e (2) **Acesso `LoadBalancer` (`minikube tunnel`)**: roda como um processo em separado criando uma rota de rede na máquina host para o CIDR de serviços do cluster usando o IP do nó como gateway, preenchendo imediatamente o campo `EXTERNAL-IP` de qualquer Service `type: LoadBalancer` com um IP acessível diretamente da estação do desenvolvedor.

## Exemplo
```bash
# Fluxo oficial do Basic controls: criar deployment echo-server, expor como NodePort e acessar via minikube service
kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0
kubectl expose deployment hello-minikube --type=NodePort --port=8080
minikube service hello-minikube --url
```

## Limites e trade-offs
Como o comando `minikube tunnel` precisa configurar interfaces e rotas de rede no sistema operacional hospedeiro (e fazer bind em portas privilegiadas `< 1024` como `80` e `443` em alguns drivers), ele pode solicitar senha administrativa (`sudo`) no terminal e **precisa permanecer em execução** em uma aba de terminal aberta (ou em background) enquanto você estiver acessando os Services `LoadBalancer`.

## Como verificar
Com `minikube tunnel` em execução em outro terminal, crie um Service `type: LoadBalancer` e execute `kubectl get svc` para confirmar que `EXTERNAL-IP` deixou de ser `<pending>` e recebeu um IP ativo.

## Conexões
- [[minikube-clusters-locais-kubernetes-perfis-controles-basicos]] — Veja também: Kubernetes minikube: implementação de clusters Kubernetes locais em macOS, Linux e Windows e controles básicos.
- [[minikube-addons-dashboard-gpu-mounts-container-runtimes]] — Veja também: Kubernetes minikube: marketplace de Addons, Dashboard integrado, suporte a GPUs NVIDIA/AMD e Filesystem Mounts.
- [[telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura]] — Referência cruzada direta com telepresence-desenvolvimento-local-remoto-kubernetes-arquitetura.

## Fontes
- [minikube GitHub — README.md (Local Kubernetes, Multi-Platform Drivers & Design Principles)](https://raw.githubusercontent.com/kubernetes/minikube/master/README.md) — README oficial do projeto minikube detalhando objetivos de simplicidade e conformidade com recursos do Kubernetes local; consultado em 2026-10-03.
- [minikube Official Documentation — Basic Controls (start/pause/stop/delete, kubectl Wrapper, Addons, service/tunnel & profiles)](https://minikube.sigs.k8s.io/docs/handbook/controls/) — Documentação oficial Basic Controls do minikube cobrindo ciclo de vida de clusters, perfis (-p), wrapper minikube kubectl --, addons (dashboard, ingress, metrics-server), minikube service, minikube tunnel e minikube node/image/cache; consultado em 2026-10-03.
- [Kubernetes minikube — Official GitHub Repository](https://github.com/kubernetes/minikube) — Repositório oficial Apache-2.0 do minikube; consultado em 2026-10-03.
