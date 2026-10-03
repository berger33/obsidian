---
id: software.devops.tranche11.001089
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

# Eficiência do plano de controle do KubeVela (vela-core): arquitetura de pod único com 0.5 CPU e 1 GB de RAM

## Em uma frase
Conforme documentado oficialmente nos destaques de arquitetura do KubeVela, o controlador central **`vela-core`** foi projetado para operar com um footprint mínimo de **apenas 1 pod com `0.5 CPU` e `1 GB` de memória (`0.5c1g`)** sendo capaz de processar a entrega de milhares de aplicações.

## Por que importa
Muitas plataformas de Continuous Delivery e PaaS exigem dezenas de microsserviços, bancos de dados pesados, filas de mensageria e vários gigabytes de RAM apenas para manter o plano de controle em pé — o que inviabiliza sua execução em clusters de borda (Edge/IoT), ambientes de desenvolvimento local (`kind`, `k3s`, `vCluster`) ou clusters enxutos.

## Como funciona
Conforme explicam o README oficial (`kubevela/kubevela`) e a página `kubevela.io/docs/`, o KubeVela atinge essa eficiência porque delega o armazenamento de estado das aplicações ao próprio Kubernetes (via CRDs OAM) e executa a renderização de componentes, traits, policies e steps de workflow dentro do motor unificado do `vela-core` usando avaliação em memória de templates CUE. Capacidades extras (como a interface web VelaUX, provedores Terraform ou observabilidade) são mantidas desacopladas como **addons opcionais**, de modo que o núcleo do controlador permanece extremamente leve.

## Exemplo
```bash
# Inspecionar o consumo real de CPU e memória do pod vela-core no namespace vela-system
kubectl -n vela-system top pods
kubectl -n vela-system get deployment kubevela-vela-core -o jsonpath='{.spec.template.spec.containers[0].resources}' | jq .
```

## Limites e trade-offs
Embora um único pod com `0.5 CPU` e `1 GB` de RAM seja suficiente para operar o plano de controle com baixo custo, em ambientes críticos de produção recomenda-se executar múltiplas réplicas do `vela-core` (com eleição de líder ativa) e calibrar os limites de memória conforme a quantidade de revisões de `Application` (`ApplicationRevision`) e tamanho dos gráficos Helm/CUE renderizados simultaneamente.

## Como verificar
Execute `kubectl -n vela-system get pods -l app.kubernetes.io/name=vela-core` para verificar a prontidão e o consumo de recursos do controlador central.

## Conexões
- [[kubevela-seguranca-multitenancy-rbac-ldap-observabilidade]] — Veja também: Governança no KubeVela: multi-tenancy, autenticação LDAP/SSO, módulos RBAC granulares e observabilidade integrada.
- [[kubevela-orquestracao-recursos-cloud-helm-kustomize-aplicacoes]] — Veja também: Composição de aplicações híbridas no KubeVela: unificando containers, Helm charts, Kustomize e infraestrutura Cloud (Terraform).
- [[kubevela-plataforma-entrega-aplicacoes-oam-cue-cncf]] — Referência cruzada direta com kubevela-plataforma-entrega-aplicacoes-oam-cue-cncf.
- [[kubevela-extensibilidade-modulos-cue-definitions-addons]] — Referência cruzada direta com kubevela-extensibilidade-modulos-cue-definitions-addons.

## Fontes
- [KubeVela GitHub — README.md & Introduction Docs (Deployment as Code, OAM, CUE, 0.5c1g Control Plane & Comparison Matrix)](https://raw.githubusercontent.com/kubevela/kubevela/master/README.md) — README oficial e introdução da documentação do KubeVela (v1.11) detalhando Open Application Model (OAM), extensibilidade com CUE, footprint de control plane (1 pod 0.5c1g) e comparação com CI/CD, GitOps, PaaS e Helm; consultado em 2026-10-03.
- [KubeVela Official Documentation — Deploy First Application Quick Start (Application CRD, Components, Traits, Policies, Workflow Suspend/Resume & VelaUX)](https://kubevela.io/docs/) — Guia prático oficial Quick Start do KubeVela demonstrando a estrutura da CRD Application (core.oam.dev/v1beta1), políticas topology e override, workflow com suspend/resume na CLI vela e regra de sincronização com o console VelaUX; consultado em 2026-10-03.
- [KubeVela — Official Documentation & Repository](https://kubevela.io/docs/quick-start/) — Documentação e repositório oficial do KubeVela; consultado em 2026-10-03.
