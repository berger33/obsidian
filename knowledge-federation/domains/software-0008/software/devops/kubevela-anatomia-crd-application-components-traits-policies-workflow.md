---
id: software.devops.tranche11.001082
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

# Anatomia do recurso Application (core.oam.dev/v1beta1) no KubeVela: Components, Traits, Policies e Workflow

## Em uma frase
Na especificação `core.oam.dev/v1beta1` do KubeVela, um objeto **`Application`** modela todo o plano de entrega combinando **`components`** (o que executar, como `webservice`, Helm chart ou módulo cloud), **`traits`** (comportamentos operacionais anexados, como `scaler` ou ingress), **`policies`** (`topology` e `override` por ambiente) e **`workflow`** (a sequência de passos de entrega).

## Por que importa
Nos manifestos tradicionais do Kubernetes, a definição do container (`Deployment`), o escalonamento (`HPA`), a exposição de rede (`Service`/`Ingress`) e a promoção entre ambientes ficam espalhados em múltiplos arquivos YAML e ferramentas externas. O modelo OAM do KubeVela reúne a intenção completa da aplicação em um único artefato coeso e validado.

## Como funciona
Conforme demonstra o manifesto oficial do *Quick Start* (`kubevela.io/docs/quick-start/`): (1) **`spec.components`** declara os componentes da aplicação (por exemplo, `name: express-server`, `type: webservice`, com `properties.image: oamdev/hello-world` e `ports`) e anexa **`traits`** operacionais (como `type: scaler` com `properties: { replicas: 1 }`); (2) **`spec.policies`** define onde e como implantar — usando políticas do tipo **`topology`** (ex.: `target-default` apontando para `clusters: ["local"], namespace: "default"`, e `target-prod` apontando para `namespace: "prod"`) e políticas do tipo **`override`** (ex.: `deploy-ha` sobrescrevendo o trait `scaler` para `replicas: 2` em produção); e (3) **`spec.workflow.steps`** orquestra a ordem exata de execução (ex.: `deploy2default` → `manual-approval` do tipo `suspend` → `deploy2prod` aplicando `["target-prod", "deploy-ha"]`).

## Exemplo
```yaml
# Exemplo oficial de Application (core.oam.dev/v1beta1) com component, trait scaler, policies topology/override e workflow com suspend
apiVersion: core.oam.dev/v1beta1
kind: Application
metadata:
  name: first-vela-app
spec:
  components:
    - name: express-server
      type: webservice
      properties:
        image: oamdev/hello-world
        ports:
          - port: 8000
            expose: true
      traits:
        - type: scaler
          properties:
            replicas: 1
  policies:
    - name: target-default
      type: topology
      properties:
        clusters: ["local"]
        namespace: "default"
    - name: target-prod
      type: topology
      properties:
        clusters: ["local"]
        namespace: "prod"
    - name: deploy-ha
      type: override
      properties:
        components:
          - type: webservice
            traits:
              - type: scaler
                properties:
                  replicas: 2
  workflow:
    steps:
      - name: deploy2default
        type: deploy
        properties:
          policies: ["target-default"]
      - name: manual-approval
        type: suspend
      - name: deploy2prod
        type: deploy
        properties:
          policies: ["target-prod", "deploy-ha"]
```

## Limites e trade-offs
Conforme observa o comentário no exemplo oficial, o namespace de destino referenciado em uma política `topology` (como `namespace: "prod"` em `target-prod`) deve ser criado previamente (por exemplo, com `vela env init prod --namespace prod` ou via step dedicado) antes que a etapa de deploy para aquele destino seja executada.

## Como verificar
Aplique o manifesto com `vela up -f first-app.yaml` e execute `vela status first-vela-app` para inspecionar o estado de cada componente, trait e passo do workflow.

## Conexões
- [[kubevela-plataforma-entrega-aplicacoes-oam-cue-cncf]] — Veja também: KubeVela: plataforma CNCF de entrega e gerenciamento de aplicações multi-cloud baseada em Open Application Model (OAM) e CUE.
- [[kubevela-fluxo-entrega-multi-ambiente-suspend-resume-cli]] — Veja também: Operação de Workflows e CLI do KubeVela: vela up, status, workflowSuspending, workflow resume, port-forward, exec e logs.
- [[kubevela-extensibilidade-modulos-cue-definitions-addons]] — Referência cruzada direta com kubevela-extensibilidade-modulos-cue-definitions-addons.

## Fontes
- [KubeVela GitHub — README.md & Introduction Docs (Deployment as Code, OAM, CUE, 0.5c1g Control Plane & Comparison Matrix)](https://kubevela.io/docs/quick-start/) — README oficial e introdução da documentação do KubeVela (v1.11) detalhando Open Application Model (OAM), extensibilidade com CUE, footprint de control plane (1 pod 0.5c1g) e comparação com CI/CD, GitOps, PaaS e Helm; consultado em 2026-10-03.
- [KubeVela Official Documentation — Deploy First Application Quick Start (Application CRD, Components, Traits, Policies, Workflow Suspend/Resume & VelaUX)](https://kubevela.io/docs/) — Guia prático oficial Quick Start do KubeVela demonstrando a estrutura da CRD Application (core.oam.dev/v1beta1), políticas topology e override, workflow com suspend/resume na CLI vela e regra de sincronização com o console VelaUX; consultado em 2026-10-03.
- [KubeVela — Official Documentation & Repository](https://raw.githubusercontent.com/kubevela/kubevela/master/README.md) — Documentação e repositório oficial do KubeVela; consultado em 2026-10-03.
