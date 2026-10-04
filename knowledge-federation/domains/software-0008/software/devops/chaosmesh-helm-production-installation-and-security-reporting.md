---
id: software.devops.tranche06.000520
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

# Instalação em produção via Helm, matriz de releases suportadas e reporte de segurança (SECURITY.md) no Chaos Mesh

## Em uma frase
As seções *Get started* e *Contributing* do README oficial orientam a operação segura do Chaos Mesh em produção: a instalação recomendada utiliza o **Helm chart oficial** (`helm/chaos-mesh/README.md` e `chaos-mesh.org/docs/production-installation-using-helm/`), consultando previamente a página de **releases e ambientes suportados** (`chaos-mesh.org/supported-releases/`). Para experimentação rápida sem precisar provisionar um cluster próprio, o README disponibiliza o **playground interativo no navegador via Killercoda** (onde se instala o Chaos Mesh em um cluster Kubernetes real de 2 nós e se executam `PodChaos`, `NetworkChaos`, Dashboard e `Workflow` em cerca de 20 minutos). Problemas de segurança devem ser reportados seguindo estritamente o arquivo **`SECURITY.md`**.

## Por que importa
Como o `Chaos Daemon` opera com capacidades privilegiadas nos nós do cluster Kubernetes para manipular namespaces de rede, processos, FUSE e relógios, manter o chart Helm alinhado às versões suportadas e seguir as políticas de `SECURITY.md` é indispensável para a segurança do cluster.

## Como funciona
Instale o Chaos Mesh via Helm fixando a versão da release suportada em `chaos-mesh.org/supported-releases/`, configure o runtime socket correto (por exemplo `/run/containerd/containerd.sock` em clusters containerd) e habilite namespaces filtrados ou anotações de permissão para evitar injeção de caos no namespace `kube-system`.

## Exemplo
Antes de instalar o Chaos Mesh no cluster corporativo, um novo membro da equipe de SRE pratica no cenário oficial do Killercoda no navegador e, em seguida, implanta o chart Helm em homologação com `chaosDaemon.runtime=containerd`.

## Limites e trade-offs
Nunca permita que experimentos do Chaos Mesh selecionem pods dos namespaces críticos do plano de controle (`kube-system`, `chaos-mesh`, `metallb-system`, `rook-ceph`) a menos que você esteja conduzindo um teste de infraestrutura especificamente planejado para esses componentes.

## Como verificar
Verifique os valores aplicados no release Helm (`helm get values chaos-mesh -n chaos-mesh`) e confirme que os webhooks e controladores estão operando na versão suportada.

## Conexões
- [[chaosmesh-adding-new-top-level-chaos-kinds-and-make-generate]] — Veja também: Fluxo de criação de novos tipos de caos (api/v1alpha1, chaosimpl, Fx e make generate) no Chaos Mesh.

## Fontes
- [Chaos Mesh GitHub — README.md (Fault Coverage, Controller Manager, Chaos Daemon, Dashboard, Workflows & Multi-Cluster)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/README.md) — README oficial do Chaos Mesh (projeto CNCF Incubating sob Apache-2.0) detalhando cobertura ampla de falhas (Pod, rede, DNS, HTTP, I/O, tempo/clock skew, stress, kernel, block device, JVM, máquina física, AWS, Azure e GCP), recursos Schedule/Workflow/StatusCheck, execução multi-cluster e os três componentes de runtime Chaos Controller Manager, Chaos Daemon e Chaos Dashboard.; consultado em 2026-10-03.
- [Chaos Mesh GitHub — controllers/README.md (Uber Fx Architecture, One Writer Per Field, Level-Based Reconcilers & Requeue Semantics)](https://raw.githubusercontent.com/chaos-mesh/chaos-mesh/master/controllers/README.md) — Guia oficial de arquitetura dos controladores do Chaos Mesh detalhando composição com Uber Fx (controllers/fx.go), pipeline comum (desiredphase, condition, records, finalizers), CRDs filhos PodHTTPChaos/PodIOChaos/PodNetworkChaos, regra One writer per field, reconciliação idempotente baseada em nível e semântica do controller-runtime v0.21.; consultado em 2026-10-03.
- [Chaos Mesh — Official GitHub Repository](https://github.com/chaos-mesh/chaos-mesh) — Repositório oficial Apache-2.0 do Chaos Mesh na CNCF.; consultado em 2026-10-03.
