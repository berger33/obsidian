---
id: software.devops.tranche06.000511
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md", "https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md", "https://github.com/chaos-mesh/chaos-mesh"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquitetura de runtime do Chaos Mesh: Chaos Controller Manager, Chaos Daemon e Chaos Dashboard

## Em uma frase
O Chaos Mesh (`chaos-mesh.org`), projeto **Incubating da CNCF** sob licença Apache-2.0, é uma plataforma cloud-native de Engenharia de Caos para Kubernetes que utiliza Custom Resources para definir, orquestrar e observar injeção controlada de falhas. Conforme documenta a seção *Architecture* do README oficial, o Chaos Mesh possui três componentes principais em tempo de execução: (1) o **Chaos Controller Manager**, que observa os recursos do Chaos Mesh, valida requisições via webhooks de admissão, agenda workflows e experimentos e coordena a injeção e recuperação; (2) o **Chaos Daemon**, que roda nos nós Kubernetes como um `DaemonSet` executando operações privilegiadas no nível do nó e do contêiner (envolvendo runtimes, processos, redes, sistemas de arquivos, relógios e kernels); e (3) o **Chaos Dashboard**, que fornece a API HTTP e a interface web (sendo opcional quando os experimentos são gerenciados diretamente via API do Kubernetes).

## Por que importa
Dividir claramente a inteligência de orquestração (`Chaos Controller Manager`) da atuação privilegiada no kernel/namespaces dos nós (`Chaos Daemon`) permite manter os privilégios elevados restritos exclusivamente ao DaemonSet local de cada nó e até desabilitar o `Chaos Dashboard` em ambientes puramente GitOps.

## Como funciona
Implante o Chaos Mesh via Helm (`chaos-mesh.org/docs/production-installation-using-helm/`), garantindo que o `Chaos Daemon` esteja configurado com o socket correto do container runtime do seu cluster (containerd, CRI-O ou Docker) e protegendo o `Chaos Dashboard` com autenticação RBAC do Kubernetes.

## Exemplo
Um operador aplica um manifesto `NetworkChaos` via `kubectl`; o `Chaos Controller Manager` valida o recurso no webhook, seleciona os pods alvo e instrui o `Chaos Daemon` nos respectivos nós via gRPC a entrar no network namespace dos contêineres e programar as regras `tc`/`iptables`.

## Limites e trade-offs
Se você gerenciar todos os experimentos declarativamente via API do Kubernetes e pipelines automatizados, considere desabilitar ou restringir o `Chaos Dashboard` em produção, já que o próprio README destaca que ele é opcional quando se usa a API do Kubernetes diretamente.

## Como verificar
Execute `kubectl get pods -n chaos-mesh` e verifique que o `chaos-controller-manager`, todos os pods do DaemonSet `chaos-daemon` e (se habilitado) o `chaos-dashboard` estão `Running` e `Ready`.

## Conexões
- [[chaosmesh-broad-fault-coverage-pod-network-io-time-jvm-and-cloud]] — Veja também: Cobertura abrangente de falhas no Chaos Mesh: Pod, Rede, DNS, HTTP, I/O, Clock Skew, Kernel, JVM, Bare-Metal e Nuvens.

## Fontes
- [Chaos Mesh GitHub — README.md (Fault Coverage, Controller Manager, Chaos Daemon, Dashboard, Workflows & Multi-Cluster)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md) — README oficial do Chaos Mesh (projeto CNCF Incubating sob Apache-2.0) detalhando cobertura ampla de falhas (Pod, rede, DNS, HTTP, I/O, tempo/clock skew, stress, kernel, block device, JVM, máquina física, AWS, Azure e GCP), recursos Schedule/Workflow/StatusCheck, execução multi-cluster e os três componentes de runtime Chaos Controller Manager, Chaos Daemon e Chaos Dashboard.; consultado em 2026-10-03.
- [Chaos Mesh GitHub — controllers/README.md (Uber Fx Architecture, One Writer Per Field, Level-Based Reconcilers & Requeue Semantics)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md) — Guia oficial de arquitetura dos controladores do Chaos Mesh detalhando composição com Uber Fx (controllers/fx.go), pipeline comum (desiredphase, condition, records, finalizers), CRDs filhos PodHTTPChaos/PodIOChaos/PodNetworkChaos, regra One writer per field, reconciliação idempotente baseada em nível e semântica do controller-runtime v0.21.; consultado em 2026-10-03.
- [Chaos Mesh — Official GitHub Repository](https://github.com/chaos-mesh/chaos-mesh) — Repositório oficial Apache-2.0 do Chaos Mesh na CNCF.; consultado em 2026-10-03.
