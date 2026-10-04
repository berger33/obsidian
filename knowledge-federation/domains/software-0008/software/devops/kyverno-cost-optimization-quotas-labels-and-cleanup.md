---
id: software.devops.tranche03.000228
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

# Otimização de custos no cluster: quotas, labels de alocação, tipos de instância e limpeza de recursos

## Em uma frase
Na seção Popular Use Cases, o grupo **3. Cost Optimization** enumera quatro frentes em que o Kyverno reduz desperdício financeiro na nuvem: impor quotas e limites de recursos (`resource quotas and limits`), exigir labels de alocação de custos (`cost allocation labels`), validar tipos de instância (`validate instance types`) e limpar recursos não utilizados (`clean up unused resources`).

## Por que importa
Em clusters multi-equipe, namespaces sem `ResourceQuota`, pods sem `requests`/`limits` ou jobs e ambientes de teste esquecidos após o expediente inflam a fatura de nuvem e dificultam o chargeback financeiro por área.

## Como funciona
Combine políticas que exigem labels financeiros obrigatórios e limites de CPU/memória na admissão com políticas de limpeza (`CleanupPolicy`) para remover automaticamente recursos efêmeros expirados.

## Exemplo
Pods criados em um namespace de testes recebem um tempo de vida (TTL) por label e são removidos automaticamente pela política de limpeza do Kyverno após 24 horas.

## Limites e trade-offs
Antes de ativar regras de limpeza automática (`clean up unused resources`), valide cuidadosamente os seletores de escopo para nunca excluir recursos produtivos ou volumes persistentes de estado.

## Como verificar
Conferi a subseção 3. Cost Optimization em Popular Use Cases no README oficial de kyverno/kyverno.

## Conexões
- [[kyverno-operational-excellence-and-developer-guardrails]] — Veja também: Excelência operacional e guardrails para desenvolvedores: auto-labeling, NetworkPolicies e probes.
- [[kyverno-policy-library-and-interactive-playground]] — Veja também: Biblioteca oficial de políticas prontas para produção e Kyverno Playground.

## Fontes
- [Kyverno — GitHub README](https://raw.githubusercontent.com/kyverno/kyverno/main/README.md) — Visão geral do Kyverno (motor de políticas nativo para Kubernetes, validação/mutação/geração/limpeza e verificação de imagens, Non-Goals, projetos Chainsaw/Policy Reporter/Kyverno JSON/Envoy Plugin, casos de uso e SBOM CycloneDX).; consultado em 2026-10-03.
- [Kyverno Documentation — Quick Start & Policy Library](https://kyverno.io/docs/introduction/) — Documentação oficial de introdução, instalação e biblioteca de políticas do Kyverno referenciada no README.; consultado em 2026-10-03.
