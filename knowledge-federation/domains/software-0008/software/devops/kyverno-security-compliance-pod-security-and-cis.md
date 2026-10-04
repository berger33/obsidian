---
id: software.devops.tranche03.000226
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

# Casos de uso de Segurança e Conformidade: Pod Security Standards, contextos de segurança e CIS Benchmarks

## Em uma frase
Na seção Popular Use Cases, o grupo **1. Security & Compliance** lista quatro aplicações diretas do Kyverno em produção: aplicar os Pod Security Standards (PSS), exigir contextos de segurança específicos (`securityContext`), validar fontes e assinaturas de imagens de contêineres e impor políticas do CIS Benchmark.

## Por que importa
Permitir pods privilegiados, execução como root ou imagens vindas de registros públicos arbitrários expõe os nós do cluster a escalação de privilégio; codificar os Pod Security Standards e o CIS Benchmark no Kyverno padroniza a defesa em todos os clusters.

## Como funciona
Importe da biblioteca oficial (`kyverno.io/policies/`) as políticas de Pod Security Standards (Baseline e Restricted) e de validação de registros e assinaturas de imagens.

## Exemplo
Um cluster de produção bloqueia na admissão qualquer pod que tente montar volumes do host (`hostPath`) ou rodar com `privileged: true` fora dos namespaces de sistema excepcionados.

## Limites e trade-offs
Ao introduzir políticas de PSS ou CIS Benchmark em um cluster já existente, inicie em modo de auditoria (background scan) por meio do relatório de violações antes de mudar para bloqueio na admissão.

## Como verificar
Conferi a subseção 1. Security & Compliance em Popular Use Cases no README oficial de kyverno/kyverno.

## Conexões
- [[kyverno-companion-projects-chainsaw-reporter-json-envoy]] — Veja também: Ecossistema de projetos companheiros: Chainsaw, Policy Reporter, Kyverno JSON e Kyverno Envoy Plugin.
- [[kyverno-operational-excellence-and-developer-guardrails]] — Veja também: Excelência operacional e guardrails para desenvolvedores: auto-labeling, NetworkPolicies e probes.

## Fontes
- [Kyverno — GitHub README](https://raw.githubusercontent.com/kyverno/kyverno/main/README.md) — Visão geral do Kyverno (motor de políticas nativo para Kubernetes, validação/mutação/geração/limpeza e verificação de imagens, Non-Goals, projetos Chainsaw/Policy Reporter/Kyverno JSON/Envoy Plugin, casos de uso e SBOM CycloneDX).; consultado em 2026-10-03.
- [Kyverno Documentation — Quick Start & Policy Library](https://kyverno.io/docs/introduction/) — Documentação oficial de introdução, instalação e biblioteca de políticas do Kyverno referenciada no README.; consultado em 2026-10-03.
