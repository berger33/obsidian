---
id: software.devops.tranche03.000227
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

# Excelência operacional e guardrails para desenvolvedores: auto-labeling, NetworkPolicies e probes

## Em uma frase
Na seção Popular Use Cases, os grupos **2. Operational Excellence** e **4. Developer Guardrails** destacam práticas de plataforma como rotular cargas de trabalho automaticamente (auto-label workloads), impor convenções de nomenclatura, gerar configurações padrão (como NetworkPolicies), validar manifestos YAML e Helm, exigir probes de readiness e liveness, impor políticas de ingress/egress, validar versões de imagens e auto-injetar ConfigMaps ou Secrets.

## Por que importa
Automatizar a geração de NetworkPolicies padrão e a injeção de ConfigMaps ou labels reduz a carga cognitiva dos desenvolvedores de produto enquanto garante que nenhum pod suba em produção sem readiness/liveness probes.

## Como funciona
Configure políticas de geração no Kyverno para provisionar recursos padrão a cada novo namespace e regras de validação para exigir readiness/liveness probes e versões explícitas de imagem (proibindo a tag `:latest`).

## Exemplo
Quando um desenvolvedor aplica um Deployment sem definir `readinessProbe`, o Kyverno informa imediatamente a regra de guardrail violada durante o `kubectl apply` ou no pipeline de CI.

## Limites e trade-offs
Regras que auto-injetam Secrets ou ConfigMaps devem restringir estritamente os namespaces de origem e destino para não expor credenciais entre tenants distintos.

## Como verificar
Conferi as subseções 2. Operational Excellence e 4. Developer Guardrails no README oficial de kyverno/kyverno.

## Conexões
- [[kyverno-security-compliance-pod-security-and-cis]] — Veja também: Casos de uso de Segurança e Conformidade: Pod Security Standards, contextos de segurança e CIS Benchmarks.
- [[kyverno-cost-optimization-quotas-labels-and-cleanup]] — Veja também: Otimização de custos no cluster: quotas, labels de alocação, tipos de instância e limpeza de recursos.

## Fontes
- [Kyverno — GitHub README](https://raw.githubusercontent.com/kyverno/kyverno/main/README.md) — Visão geral do Kyverno (motor de políticas nativo para Kubernetes, validação/mutação/geração/limpeza e verificação de imagens, Non-Goals, projetos Chainsaw/Policy Reporter/Kyverno JSON/Envoy Plugin, casos de uso e SBOM CycloneDX).; consultado em 2026-10-03.
- [Kyverno Documentation — Quick Start & Policy Library](https://kyverno.io/docs/introduction/) — Documentação oficial de introdução, instalação e biblioteca de políticas do Kyverno referenciada no README.; consultado em 2026-10-03.
