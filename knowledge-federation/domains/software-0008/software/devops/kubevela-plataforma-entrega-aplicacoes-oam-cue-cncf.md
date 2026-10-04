---
id: software.devops.tranche11.001081
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
fontes: ["https://raw.githubusercontent.com/kubevela/kubevela/master/README.md", "https://kubevela.io/docs/", "https://kubevela.io/docs/quick-start/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# KubeVela: plataforma CNCF de entrega e gerenciamento de aplicações multi-cloud baseada em Open Application Model (OAM) e CUE

## Em uma frase
O KubeVela (`kubevela/kubevela`, projeto CNCF sob licença Apache-2.0) é um plano de controle moderno de entrega e gerenciamento de aplicações que implementa o **Open Application Model (OAM)** e módulos programáveis em **CUE** (`cuelang.org`) sobre o Kubernetes para orquestrar deploys em ambientes híbridos e multi-cloud.

## Por que importa
Em organizações onde desenvolvedores precisam entregar aplicações compostas por containers, Helm charts e recursos de nuvem (como bancos RDS via Terraform) através de múltiplos clusters de teste, staging e produção, escrever scripts ad-hoc de CI/CD ou manter dezenas de CRDs desconexas gera alto custo cognitivo. O KubeVela unifica o plano de entrega no conceito de **Deployment as Code** (`render, orchestrate, deploy`).

## Como funciona
Conforme descrevem o README oficial (`kubevela/kubevela`) e a página de introdução (`kubevela.io/docs/`), o KubeVela opera como um plano de controle extremamente enxuto (capaz de rodar com apenas **1 pod consumindo `0.5 CPU` e `1 GB` de RAM** para gerenciar milhares de entregas de aplicações). Todas as capacidades de infraestrutura e etapas de entrega são encapsuladas como blocos de construção estilo LEGO escritos em **CUE** e expostos aos desenvolvedores por meio de uma única CRD central — `Application` (`core.oam.dev/v1beta1`) — composta por quatro seções declarativas: **`components`**, **`traits`**, **`policies`** e **`workflow`**.

## Exemplo
```bash
# Instalar a CLI vela, inicializar um ambiente e implantar uma Application declarativa do KubeVela
vela env init prod --namespace prod
vela up -f https://kubevela.io/example/applications/first-app.yaml
vela status first-vela-app
```

## Limites e trade-offs
O KubeVela não substitui o seu servidor de Integração Contínua (GitHub Actions, GitLab CI, Jenkins); ele atua **downstream do processo de CI**, assumindo a etapa de Continuous Delivery (CD) e podendo trabalhar em conjunto tanto com fluxos imperativos via CLI/API quanto com fluxos GitOps.

## Como verificar
Verifique a saúde do controlador no cluster com `kubectl -n vela-system get pods` e liste as definições disponíveis com `vela components` e `vela traits`.

## Conexões
- [[kubevela-anatomia-crd-application-components-traits-policies-workflow]] — Veja também: Anatomia do recurso Application (core.oam.dev/v1beta1) no KubeVela: Components, Traits, Policies e Workflow.
- [[kubevela-fluxo-entrega-multi-ambiente-suspend-resume-cli]] — Referência cruzada direta com kubevela-fluxo-entrega-multi-ambiente-suspend-resume-cli.
- [[kubevela-comparacao-cicd-gitops-paas-helm-posicionamento]] — Referência cruzada direta com kubevela-comparacao-cicd-gitops-paas-helm-posicionamento.

## Fontes
- [KubeVela GitHub — README.md & Introduction Docs (Deployment as Code, OAM, CUE, 0.5c1g Control Plane & Comparison Matrix)](https://raw.githubusercontent.com/kubevela/kubevela/master/README.md) — README oficial e introdução da documentação do KubeVela (v1.11) detalhando Open Application Model (OAM), extensibilidade com CUE, footprint de control plane (1 pod 0.5c1g) e comparação com CI/CD, GitOps, PaaS e Helm; consultado em 2026-10-03.
- [KubeVela Official Documentation — Deploy First Application Quick Start (Application CRD, Components, Traits, Policies, Workflow Suspend/Resume & VelaUX)](https://kubevela.io/docs/) — Guia prático oficial Quick Start do KubeVela demonstrando a estrutura da CRD Application (core.oam.dev/v1beta1), políticas topology e override, workflow com suspend/resume na CLI vela e regra de sincronização com o console VelaUX; consultado em 2026-10-03.
- [KubeVela — Official Documentation & Repository](https://kubevela.io/docs/quick-start/) — Documentação e repositório oficial do KubeVela; consultado em 2026-10-03.
