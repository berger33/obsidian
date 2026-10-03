---
id: software.devops.tranche11.001041
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md", "https://goldilocks.docs.fairwinds.com/installation/", "https://goldilocks.docs.fairwinds.com/advanced/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fairwinds Goldilocks: utilitário Kubernetes para dimensionamento (right-sizing) de resource requests e limits via VPA

## Em uma frase
O Fairwinds Goldilocks (`FairwindsOps/goldilocks`, Apache-2.0) é um controlador e dashboard para Kubernetes que cria e gerencia objetos **VerticalPodAutoscaler (VPA)** em modo de recomendação (`updateMode: "Off"`) para ajudar equipes a identificar o ponto ideal (*"Just Right"*) de `requests` e `limits` de CPU e memória de seus workloads.

## Por que importa
Definir `requests` e `limits` de CPU e memória no Kubernetes por adivinhação leva a dois extremos custosos: superdimensionamento (desperdício de capacidade de nós e fatura de nuvem inflada) ou subdimensionamento (estrangulamento de CPU — *CPU throttling* — e mortes por falta de memória — `OOMKilled`). O Goldilocks automatiza a coleta de recomendações baseadas no consumo histórico real sem alterar os pods em produção.

## Como funciona
Conforme explicam o README oficial e o guia de instalação (`goldilocks.docs.fairwinds.com/installation/`), quando um namespace é habilitado no Goldilocks, o controlador monitora qualquer controlador de workload que possua um template de PodSpec (`spec.template.spec.containers[]`, incluindo `Deployments`, `DaemonSets` e `StatefulSets`) e cria automaticamente um objeto `VerticalPodAutoscaler` para cada workload. O componente **VPA Recommender** (que consome dados do `metrics-server` e, opcionalmente, histórico do Prometheus) calcula as faixas recomendadas de recursos, e o **Goldilocks Dashboard** consulta esses objetos VPA para exibir comparações visuais entre os valores atuais e as sugestões para classes QoS *Guaranteed* e *Burstable*.

## Exemplo
```bash
# Instalar o Goldilocks via Helm chart oficial e habilitar um namespace para geração automática de VPAs
helm repo add fairwinds-stable https://charts.fairwinds.com/stable
helm repo update
kubectl create namespace goldilocks
helm install goldilocks --namespace goldilocks fairwinds-stable/goldilocks

# Habilitar o monitoramento do Goldilocks em um namespace de aplicação
kubectl label ns minha-app goldilocks.fairwinds.com/enabled=true
```

## Limites e trade-offs
O Goldilocks não coleta métricas diretamente dos nós por conta própria: ele exige que o **`metrics-server`** e o **VPA Recommender** estejam instalados e operacionais no cluster para que os objetos `VerticalPodAutoscaler` gerados recebam dados de recomendação.

## Como verificar
Após aplicar a label `goldilocks.fairwinds.com/enabled=true` no namespace, execute `kubectl -n minha-app get vpa` para confirmar que o controlador do Goldilocks criou automaticamente um objeto VPA para cada Deployment/StatefulSet/DaemonSet.

## Conexões
- [[goldilocks-requisitos-vpa-recommender-metrics-server-gke]] — Veja também: Requisitos de infraestrutura do Goldilocks: VPA Recommender isolado (sem webhook), metrics-server, Prometheus e GKE.
- [[goldilocks-controlador-flags-labels-namespaces-metricas]] — Referência cruzada direta com goldilocks-controlador-flags-labels-namespaces-metricas.
- [[opencost-eficiencia-recursos-rightsizing-buffer-multiplier]] — Referência cruzada direta com opencost-eficiencia-recursos-rightsizing-buffer-multiplier.

## Fontes
- [Fairwinds Goldilocks Official Documentation — Installation & Requirements (VPA Recommender, metrics-server, Helm & GKE)](https://raw.githubusercontent.com/FairwindsOps/goldilocks/master/README.md) — Documentação oficial de instalação do Goldilocks detalhando requisitos (VPA Recommender sem webhook, metrics-server, Prometheus opcional, GKE Standard vs Autopilot), Helm chart, manifestos e habilitação de namespaces; consultado em 2026-10-03.
- [Fairwinds Goldilocks Official Documentation — Advanced Usage & README (Controller Flags, Metrics, vpa-update-mode, vpa-resource-policy & v4.15.0+ Images)](https://goldilocks.docs.fairwinds.com/installation/) — Guia oficial de uso avançado e README do Goldilocks cobrindo flags do controlador, métricas Prometheus, anotações vpa-update-mode e vpa-resource-policy, comandos summary/dashboard, --exclude-containers e imagens assinadas v4.15.0+; consultado em 2026-10-03.
- [Fairwinds Goldilocks — Official Documentation & Repository](https://goldilocks.docs.fairwinds.com/advanced/) — Documentação e repositório oficial do Fairwinds Goldilocks; consultado em 2026-10-03.
