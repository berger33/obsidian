---
id: software.devops.tranche03.000225
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
fontes: ["https://raw.githubusercontent.com/kyverno/kyverno/main/README.md", "https://github.com/kyverno/kyverno"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Ecossistema de projetos companheiros: Chainsaw, Policy Reporter, Kyverno JSON e Kyverno Envoy Plugin

## Em uma frase
O quarto parágrafo da seção Non-Goals do README documenta que capacidades fora do escopo do motor central são atendidas por projetos companheiros na organização kyverno, cada um com seu próprio ciclo de release: **Chainsaw** (`kyverno/chainsaw`, ferramenta de testes end-to-end), **Policy Reporter** (`kyverno/policy-reporter`, relatórios e interface UI de violações de políticas), **Kyverno JSON** (`kyverno/kyverno-json`, avaliação de políticas para payloads JSON não-Kubernetes) e **Kyverno Envoy Plugin** (`kyverno/kyverno-envoy-plugin`, política de autorização para service meshes e Envoy).

## Por que importa
Isolar testes declarativos e2e (Chainsaw), visualização gráfica (Policy Reporter), validação de JSON genérico como planos do OpenTofu/Terraform (Kyverno JSON) e autorização no Envoy mantém o controlador central do Kyverno no cluster focado e enxuto.

## Como funciona
Implante o Policy Reporter quando precisar de dashboards visuais de violações no cluster, adote o Chainsaw para testar operadores e políticas de ponta a ponta e utilize o Kyverno JSON em pipelines de CI para validar payloads fora do Kubernetes.

## Exemplo
Uma equipe de plataforma testa suas políticas no CI com o Chainsaw e exibe as não conformidades de background scan para os desenvolvedores por meio do Policy Reporter.

## Limites e trade-offs
Como cada projeto companheiro possui ciclo de lançamento independente do core do Kyverno, verifique a compatibilidade de versões ao atualizá-los.

## Como verificar
Conferi o quarto parágrafo da seção Non-Goals no README oficial de kyverno/kyverno.

## Conexões
- [[kyverno-complementarity-with-rbac-and-native-admission-policies]] — Veja também: Complementaridade do Kyverno com o RBAC do Kubernetes e com Validating/MutatingAdmissionPolicies.
- [[kyverno-security-compliance-pod-security-and-cis]] — Veja também: Casos de uso de Segurança e Conformidade: Pod Security Standards, contextos de segurança e CIS Benchmarks.

## Fontes
- [Kyverno — GitHub README](https://raw.githubusercontent.com/kyverno/kyverno/main/README.md) — Visão geral do Kyverno (motor de políticas nativo para Kubernetes, validação/mutação/geração/limpeza e verificação de imagens, Non-Goals, projetos Chainsaw/Policy Reporter/Kyverno JSON/Envoy Plugin, casos de uso e SBOM CycloneDX).; consultado em 2026-10-03.
- [Kyverno — Repositório Oficial no GitHub](https://github.com/kyverno/kyverno) — Repositório oficial do Kyverno na CNCF com código-fonte, CONTRIBUTING.md, DEVELOPMENT.md e pacotes SBOM.; consultado em 2026-10-03.
