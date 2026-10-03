---
id: software.devops.tranche03.000224
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/kyverno/kyverno/main/README.md", "https://kyverno.io/docs/introduction/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Complementaridade do Kyverno com o RBAC do Kubernetes e com Validating/MutatingAdmissionPolicies

## Em uma frase
Os segundo e terceiro parágrafos da seção Non-Goals do README explicam que o Kyverno não substitui, mas trabalha em conjunto com o RBAC do Kubernetes (o RBAC controla quem tem acesso à ação, enquanto o Kyverno garante a conformidade do conteúdo do objeto com as políticas) e tampouco substitui os controles nativos ValidatingAdmissionPolicies e MutatingAdmissionPolicies do Kubernetes, complementando-os com relatórios abrangentes, gerenciamento de exceções (exception management) e varreduras periódicas em segundo plano (periodic background scanning).

## Por que importa
Mesmo que um ServiceAccount tenha permissão RBAC legítima para criar um Deployment, o RBAC nativo não inspeciona se o Deployment declarou limites de CPU ou probes de saúde; por outro lado, o Kyverno não substitui a autorização de identidade do RBAC.

## Como funciona
Use o RBAC do Kubernetes para autorizar usuários e ServiceAccounts e utilize o Kyverno em conjunto com ValidatingAdmissionPolicies/MutatingAdmissionPolicies para governar o conteúdo dos recursos, gerar relatórios de auditoria e gerenciar exceções.

## Exemplo
O RBAC autoriza o controlador do Argo CD a criar Deployments no namespace da equipe, e o Kyverno valida se o Deployment contém os labels de centro de custo e imagens de registros aprovados.

## Limites e trade-offs
Nunca afrouxe permissões de RBAC (como conceder cluster-admin) confiando apenas em políticas de admissão para restringir ações administrativas.

## Como verificar
Conferi os segundo e terceiro parágrafos da seção Non-Goals no README oficial de kyverno/kyverno.

## Conexões
- [[kyverno-non-goals-api-server-flaws-and-explicit-policies]] — Veja também: Limites formais (Non-Goals): vulnerabilidades do API Server e manutenção ativa de políticas.
- [[kyverno-companion-projects-chainsaw-reporter-json-envoy]] — Veja também: Ecossistema de projetos companheiros: Chainsaw, Policy Reporter, Kyverno JSON e Kyverno Envoy Plugin.

## Fontes
- [Kyverno — GitHub README](https://raw.githubusercontent.com/kyverno/kyverno/main/README.md) — Visão geral do Kyverno (motor de políticas nativo para Kubernetes, validação/mutação/geração/limpeza e verificação de imagens, Non-Goals, projetos Chainsaw/Policy Reporter/Kyverno JSON/Envoy Plugin, casos de uso e SBOM CycloneDX).; consultado em 2026-10-03.
- [Kyverno Documentation — Quick Start & Policy Library](https://kyverno.io/docs/introduction/) — Documentação oficial de introdução, instalação e biblioteca de políticas do Kyverno referenciada no README.; consultado em 2026-10-03.
