---
id: software.devops.tranche11.001084
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
fontes: ["https://kubevela.io/docs/quick-start/", "https://kubevela.io/docs/", "https://raw.githubusercontent.com/kubevela/kubevela/master/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Console UI VelaUX vs CLI/GitOps no KubeVela: arquitetura de metadados e regra de fonte única da verdade

## Em uma frase
O addon de interface gráfica **VelaUX** (`addon-velaux` em `vela-system`) utiliza uma camada própria de banco de dados de metadados separada do `etcd` do Kubernetes: aplicações gerenciadas via CLI/K8s API são sincronizadas automaticamente para a UI como visualização, mas uma vez que uma aplicação é implantada pela UI Console, a sincronização automática a partir da CLI é interrompida para preservar a fonte da verdade.

## Por que importa
Misturar edições manuais na interface web (VelaUX) com edições via `kubectl`/`vela up` (GitOps/CLI) sobre a mesma aplicação é uma das principais causas de confusão operacional no KubeVela. Compreender a regra de separação de fontes de verdade documentada no *Quick Start* evita conflitos de estado.

## Como funciona
Conforme explica a seção *Manage application with UI Console* (`kubevela.io/docs/quick-start/`): (1) após habilitar o VelaUX, acessa-se a interface com `vela port-forward addon-velaux -n vela-system 8080:80` (cujo login inicial padrão é usuário `admin` e senha `VelaUX12345`, exigindo troca obrigatória no primeiro acesso); (2) o console VelaUX opera como uma arquitetura PaaS que adota um banco de dados próprio como fonte da verdade em vez do `etcd`; (3) por padrão, se você gerencia as aplicações diretamente pela CLI/API do Kubernetes, o KubeVela sincroniza automaticamente os metadados para o backend da UI (associando ao projeto do ambiente correspondente ou ao projeto `default`); porém (4) **assim que você implanta a aplicação a partir do console UI (VelaUX), o processo de sincronização automática da CLI para a UI é interrompido**, pois a fonte da verdade passou a ser o VelaUX.

## Exemplo
```bash
# Acessar o console web VelaUX via port-forward após habilitar o addon no namespace vela-system
vela port-forward addon-velaux -n vela-system 8080:80
```

## Limites e trade-offs
Conforme a recomendação conclusiva da documentação oficial: se você é um usuário de **CLI, YAML ou GitOps**, utilize **apenas a CLI/GitOps** para gerenciar a CRD `Application` e use o console VelaUX estritamente como um dashboard de visualização; inversamente, se optar por gerenciar uma aplicação pelo VelaUX, conduza todas as alterações subsequentes pela UI, API ou Webhook do VelaUX, nunca modificando a mesma aplicação pelos dois lados.

## Como verificar
Ao acessar o VelaUX, verifique o grafo de recursos da `first-vela-app` e confirme se há avisos de diferença (*diff*) entre o estado da CLI/cluster e o estado do painel.

## Conexões
- [[kubevela-fluxo-entrega-multi-ambiente-suspend-resume-cli]] — Veja também: Operação de Workflows e CLI do KubeVela: vela up, status, workflowSuspending, workflow resume, port-forward, exec e logs.
- [[kubevela-comparacao-cicd-gitops-paas-helm-posicionamento]] — Veja também: Posicionamento arquitetural do KubeVela frente a CI/CD, GitOps (Argo CD / Flux), PaaS tradicional e Helm.
- [[kubevela-anatomia-crd-application-components-traits-policies-workflow]] — Referência cruzada direta com kubevela-anatomia-crd-application-components-traits-policies-workflow.

## Fontes
- [KubeVela GitHub — README.md & Introduction Docs (Deployment as Code, OAM, CUE, 0.5c1g Control Plane & Comparison Matrix)](https://kubevela.io/docs/quick-start/) — README oficial e introdução da documentação do KubeVela (v1.11) detalhando Open Application Model (OAM), extensibilidade com CUE, footprint de control plane (1 pod 0.5c1g) e comparação com CI/CD, GitOps, PaaS e Helm; consultado em 2026-10-03.
- [KubeVela Official Documentation — Deploy First Application Quick Start (Application CRD, Components, Traits, Policies, Workflow Suspend/Resume & VelaUX)](https://kubevela.io/docs/) — Guia prático oficial Quick Start do KubeVela demonstrando a estrutura da CRD Application (core.oam.dev/v1beta1), políticas topology e override, workflow com suspend/resume na CLI vela e regra de sincronização com o console VelaUX; consultado em 2026-10-03.
- [KubeVela — Official Documentation & Repository](https://raw.githubusercontent.com/kubevela/kubevela/master/README.md) — Documentação e repositório oficial do KubeVela; consultado em 2026-10-03.
