---
id: software.devops.tranche11.001090
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
fontes: ["https://kubevela.io/docs/", "https://raw.githubusercontent.com/kubevela/kubevela/master/README.md", "https://kubevela.io/docs/quick-start/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Composição de aplicações híbridas no KubeVela: unificando containers, Helm charts, Kustomize e infraestrutura Cloud (Terraform)

## Em uma frase
O KubeVela permite compor uma única `Application` híbrida que declara simultaneamente containers nativos (`webservice`/`worker`), pacotes **Helm**, overlays **Kustomize** e módulos **Terraform** de provedores de nuvem (como bancos de dados gerenciados AWS RDS), orquestrando a ordem de provisionamento e injeção de credenciais entre eles.

## Por que importa
Na vida real, uma aplicação moderna raramente consiste apenas em um `Deployment` stateless: ela depende de um banco de dados gerenciado na nuvem (provisionado via Terraform) e de um middleware instalado via Helm (como Redis ou Kafka). Coordenar a criação do banco, aguardar o endpoint ficar pronto, injetar o Secret de conexão e só então subir o container dentro de um único workflow declarativo elimina scripts frágeis de colagem (*glue code*).

## Como funciona
Conforme descreve a seção *KubeVela vs. Helm* e *Key Features* em `kubevela.io/docs/`, o KubeVela atua como um plano de controle de entrega que suporta múltiplos formatos de encapsulamento. Em uma mesma `Application`, o desenvolvedor pode declarar um componente baseado em um chart Helm (ou container) e um componente baseado em um módulo Terraform de nuvem (por exemplo, AWS RDS), usar o workflow OAM/CUE para provisionar e vincular (*resource provision/binding*) os outputs de conexão do recurso de nuvem diretamente ao componente da aplicação e entregá-los através de múltiplos ambientes.

## Exemplo
```bash
# Verificar os tipos de componentes instalados e habilitar addons de integração (como fluxcd para Helm/Kustomize ou terraform)
vela components
vela addon list | grep -E "fluxcd|terraform"
```

## Limites e trade-offs
Como o provisionamento de recursos de nuvem via Terraform (por exemplo, criar uma instância RDS do zero na AWS) leva vários minutos — muito mais tempo do que criar um `Deployment` Kubernetes — o workflow da `Application` permanecerá em execução aguardando a prontidão do recurso cloud antes de avançar para os passos dependentes.

## Como verificar
Inspecione o progresso passo a passo da orquestração com `vela status <nome-da-app>` para verificar quais etapas do workflow já concluíram e quais aguardam provisionamento externo.

## Conexões
- [[kubevela-dimensionamento-control-plane-footprint-vela-core]] — Veja também: Eficiência do plano de controle do KubeVela (vela-core): arquitetura de pod único com 0.5 CPU e 1 GB de RAM.
- [[kubevela-comparacao-cicd-gitops-paas-helm-posicionamento]] — Referência cruzada direta com kubevela-comparacao-cicd-gitops-paas-helm-posicionamento.
- [[kubevela-anatomia-crd-application-components-traits-policies-workflow]] — Referência cruzada direta com kubevela-anatomia-crd-application-components-traits-policies-workflow.

## Fontes
- [KubeVela GitHub — README.md & Introduction Docs (Deployment as Code, OAM, CUE, 0.5c1g Control Plane & Comparison Matrix)](https://kubevela.io/docs/) — README oficial e introdução da documentação do KubeVela (v1.11) detalhando Open Application Model (OAM), extensibilidade com CUE, footprint de control plane (1 pod 0.5c1g) e comparação com CI/CD, GitOps, PaaS e Helm; consultado em 2026-10-03.
- [KubeVela Official Documentation — Deploy First Application Quick Start (Application CRD, Components, Traits, Policies, Workflow Suspend/Resume & VelaUX)](https://raw.githubusercontent.com/kubevela/kubevela/master/README.md) — Guia prático oficial Quick Start do KubeVela demonstrando a estrutura da CRD Application (core.oam.dev/v1beta1), políticas topology e override, workflow com suspend/resume na CLI vela e regra de sincronização com o console VelaUX; consultado em 2026-10-03.
- [KubeVela — Official Documentation & Repository](https://kubevela.io/docs/quick-start/) — Documentação e repositório oficial do KubeVela; consultado em 2026-10-03.
