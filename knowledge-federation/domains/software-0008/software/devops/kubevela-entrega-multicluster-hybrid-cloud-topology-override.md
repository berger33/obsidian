---
id: software.devops.tranche11.001087
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
fontes: ["https://raw.githubusercontent.com/kubevela/kubevela/master/README.md", "https://kubevela.io/docs/quick-start/", "https://kubevela.io/docs/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Entrega Multi-Cluster e Hybrid-Cloud no KubeVela: políticas topology, override e rollout progressivo

## Em uma frase
O KubeVela trata a entrega de aplicações em múltiplos clusters e nuvens híbridas como cidadã de primeira classe, combinando políticas **`topology`** (seleção de clusters e namespaces de destino), políticas **`override`** (diferenciação de réplicas, imagens ou traits por ambiente) e estratégias de rollout progressivo (canary, blue-green e verificação contínua).

## Por que importa
Em arquiteturas distribuídas onde uma aplicação precisa ser promovida do cluster de desenvolvimento para o cluster de staging e depois para múltiplos clusters regionais de produção, gerenciar pastas duplicadas de YAML por cluster dificulta manter a consistência. No KubeVela, a definição base do componente permanece única e as políticas `topology` + `override` adaptam a entrega a cada alvo.

## Como funciona
Conforme documentam o README oficial (`kubevela/kubevela`) e o exemplo do *Quick Start* (`kubevela.io/docs/quick-start/`): (1) cada política do tipo **`topology`** define em quais `clusters` (ex.: `["local"]` ou seletores de labels de clusters gerenciados via ClusterGateway) e em qual `namespace` os componentes serão aplicados; (2) cada política do tipo **`override`** especifica apenas os deltas de configuração para aquele ambiente (por exemplo, alterar o trait `scaler` de `replicas: 1` para `replicas: 2`); e (3) os passos `type: deploy` dentro de `spec.workflow.steps` referenciam a combinação desejada de políticas (`policies: ["target-prod", "deploy-ha"]`), permitindo intercalar aprovações (`suspend`), verificações de métricas e promoções graduais entre ambientes.

## Exemplo
```yaml
# Definição declarativa de políticas topology e override para promoção entre ambientes no KubeVela
policies:
  - name: target-staging
    type: topology
    properties:
      clusters: ["local"]
      namespace: "staging"
  - name: target-prod
    type: topology
    properties:
      clusters: ["cluster-prod-sa-east-1", "cluster-prod-us-east-1"]
      namespace: "prod"
  - name: prod-scaling
    type: override
    properties:
      components:
        - name: express-server
          traits:
            - type: scaler
              properties:
                replicas: 4
```

## Limites e trade-offs
Quando uma única `Application` gerencia implantações simultâneas em múltiplos clusters via `workflow`, uma falha de conectividade com um dos clusters remotos pausará ou falhará o passo `deploy` correspondente; monitore o status detalhado por cluster com `vela status <app>`.

## Como verificar
Associe um cluster ou crie múltiplos namespaces de ambiente (`vela env init`) e verifique em `vela status <app>` a tabela `Services:` listando o `Cluster`, `Namespace`, `Healthy Ready` e `Traits` de cada instância entregue.

## Conexões
- [[kubevela-extensibilidade-modulos-cue-definitions-addons]] — Veja também: Extensibilidade do KubeVela: programação de Definitions com CUE e ecossistema de Addons.
- [[kubevela-seguranca-multitenancy-rbac-ldap-observabilidade]] — Veja também: Governança no KubeVela: multi-tenancy, autenticação LDAP/SSO, módulos RBAC granulares e observabilidade integrada.
- [[kubevela-anatomia-crd-application-components-traits-policies-workflow]] — Referência cruzada direta com kubevela-anatomia-crd-application-components-traits-policies-workflow.
- [[kubevela-fluxo-entrega-multi-ambiente-suspend-resume-cli]] — Referência cruzada direta com kubevela-fluxo-entrega-multi-ambiente-suspend-resume-cli.

## Fontes
- [KubeVela GitHub — README.md & Introduction Docs (Deployment as Code, OAM, CUE, 0.5c1g Control Plane & Comparison Matrix)](https://raw.githubusercontent.com/kubevela/kubevela/master/README.md) — README oficial e introdução da documentação do KubeVela (v1.11) detalhando Open Application Model (OAM), extensibilidade com CUE, footprint de control plane (1 pod 0.5c1g) e comparação com CI/CD, GitOps, PaaS e Helm; consultado em 2026-10-03.
- [KubeVela Official Documentation — Deploy First Application Quick Start (Application CRD, Components, Traits, Policies, Workflow Suspend/Resume & VelaUX)](https://kubevela.io/docs/quick-start/) — Guia prático oficial Quick Start do KubeVela demonstrando a estrutura da CRD Application (core.oam.dev/v1beta1), políticas topology e override, workflow com suspend/resume na CLI vela e regra de sincronização com o console VelaUX; consultado em 2026-10-03.
- [KubeVela — Official Documentation & Repository](https://kubevela.io/docs/) — Documentação e repositório oficial do KubeVela; consultado em 2026-10-03.
