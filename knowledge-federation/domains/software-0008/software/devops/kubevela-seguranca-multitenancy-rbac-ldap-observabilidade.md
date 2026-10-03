---
id: software.devops.tranche11.001088
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

# Governança no KubeVela: multi-tenancy, autenticação LDAP/SSO, módulos RBAC granulares e observabilidade integrada

## Em uma frase
O KubeVela inclui suporte nativo para governança corporativa, oferecendo integrações **LDAP/SSO**, autenticação e autorização **multi-tenant e multi-cluster**, módulos **RBAC granulares** customizáveis para a cadeia de suprimentos e dashboards automatizados de observabilidade para todo o processo de entrega.

## Por que importa
Em uma plataforma compartilhada por dezenas de equipes de produto, o plano de controle de entrega precisa garantir que cada equipe só possa implantar aplicações nos namespaces e clusters autorizados para o seu projeto, autenticando-se com suas credenciais corporativas e tendo visibilidade imediata das métricas e logs das suas entregas.

## Como funciona
Conforme destacam os pilares *Built-in observability, multi-tenancy and security support* no README oficial (`kubevela/kubevela`) e em `kubevela.io/docs/`: (1) o KubeVela provê integrações prontas para uso com diretórios **LDAP** e provedores de identidade para autenticar usuários na plataforma; (2) aplica autenticação e autorização multi-tenant através de múltiplos clusters (mapeando projetos, ambientes e permissões RBAC do Kubernetes em vez de usar uma conta superusuário irrestrita para todos os tenants); e (3) fornece blocos de construção de segurança, conformidade e observabilidade automatizada com dashboards Grafana/Prometheus para rastrear a saúde tanto do control plane quanto das aplicações entregues.

## Exemplo
```bash
# Inicializar um ambiente isolado associado a um namespace e verificar os recursos da aplicação naquele ambiente
vela env init equipe-pagamentos --namespace pagamentos-dev
vela env set equipe-pagamentos
vela ls -n pagamentos-dev
```

## Limites e trade-offs
Ao habilitar a camada de projetos e multi-tenancy no VelaUX junto com o uso da CLI `vela`, lembre-se da dica oficial do *Quick Start*: para que uma aplicação criada via CLI seja sincronizada para o projeto correto na UI (em vez de cair no projeto `default`), o namespace da aplicação operada pela CLI já deve estar previamente associado ao respectivo ambiente/projeto.

## Como verificar
Execute `vela env ls` para listar os ambientes configurados e seus respectivos namespaces mapeados no KubeVela.

## Conexões
- [[kubevela-entrega-multicluster-hybrid-cloud-topology-override]] — Veja também: Entrega Multi-Cluster e Hybrid-Cloud no KubeVela: políticas topology, override e rollout progressivo.
- [[kubevela-dimensionamento-control-plane-footprint-vela-core]] — Veja também: Eficiência do plano de controle do KubeVela (vela-core): arquitetura de pod único com 0.5 CPU e 1 GB de RAM.
- [[kubevela-plataforma-entrega-aplicacoes-oam-cue-cncf]] — Referência cruzada direta com kubevela-plataforma-entrega-aplicacoes-oam-cue-cncf.
- [[kubevela-console-velaux-sincronizacao-fonte-verdade-gitops]] — Referência cruzada direta com kubevela-console-velaux-sincronizacao-fonte-verdade-gitops.
- [[dex-conector-ldap-active-directory-buscas-usuarios-grupos]] — Referência cruzada direta com dex-conector-ldap-active-directory-buscas-usuarios-grupos.

## Fontes
- [KubeVela GitHub — README.md & Introduction Docs (Deployment as Code, OAM, CUE, 0.5c1g Control Plane & Comparison Matrix)](https://raw.githubusercontent.com/kubevela/kubevela/master/README.md) — README oficial e introdução da documentação do KubeVela (v1.11) detalhando Open Application Model (OAM), extensibilidade com CUE, footprint de control plane (1 pod 0.5c1g) e comparação com CI/CD, GitOps, PaaS e Helm; consultado em 2026-10-03.
- [KubeVela Official Documentation — Deploy First Application Quick Start (Application CRD, Components, Traits, Policies, Workflow Suspend/Resume & VelaUX)](https://kubevela.io/docs/) — Guia prático oficial Quick Start do KubeVela demonstrando a estrutura da CRD Application (core.oam.dev/v1beta1), políticas topology e override, workflow com suspend/resume na CLI vela e regra de sincronização com o console VelaUX; consultado em 2026-10-03.
- [KubeVela — Official Documentation & Repository](https://kubevela.io/docs/quick-start/) — Documentação e repositório oficial do KubeVela; consultado em 2026-10-03.
