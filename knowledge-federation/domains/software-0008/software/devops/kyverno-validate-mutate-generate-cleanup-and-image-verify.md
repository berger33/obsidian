---
id: software.devops.tranche03.000222
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

# As cinco ações do Kyverno: validar, mutar, gerar, limpar recursos e verificar assinaturas de imagens

## Em uma frase
A seção About Kyverno do README sintetiza as capacidades operacionais do motor: validar (validate), mutar (mutate), gerar (generate) e limpar (clean up) recursos utilizando tanto os controles de admissão do Kubernetes quanto varreduras em segundo plano (background scans), além de verificar assinaturas de imagens de contêineres (verify container image signatures) para segurança da cadeia de suprimentos.

## Por que importa
Uma plataforma completa não precisa apenas negar manifestos inválidos na entrada: ela precisa injetar padrões seguros (mutação), criar automaticamente recursos auxiliares como NetworkPolicies ou quotas quando um Namespace nasce (geração), remover recursos temporários expirados (limpeza) e exigir que imagens venham assinadas (por exemplo, com Cosign no Harbor).

## Como funciona
Combine regras de validação, mutação, geração, limpeza e verificação de assinatura de imagens conforme o ciclo de vida dos recursos no seu cluster Kubernetes.

## Exemplo
Quando um time cria um novo Namespace, o Kyverno gera automaticamente uma NetworkPolicy padrão de isolamento e valida no webhook de admissão que todas as imagens implantadas possuem assinatura criptográfica válida.

## Limites e trade-offs
Regras de mutação e geração encadeadas podem interagir com controladores GitOps; configure o Argo CD ou Flux para ignorar campos mutados dinamicamente ou alinhe os defaults no repositório Git.

## Como verificar
Conferi os três tópicos da seção About Kyverno no README oficial de kyverno/kyverno.

## Conexões
- [[kyverno-kubernetes-native-policy-engine-overview]] — Veja também: Motor de políticas nativo para Kubernetes sem exigir linguagem de programação nova.
- [[kyverno-non-goals-api-server-flaws-and-explicit-policies]] — Veja também: Limites formais (Non-Goals): vulnerabilidades do API Server e manutenção ativa de políticas.

## Fontes
- [Kyverno — GitHub README](https://raw.githubusercontent.com/kyverno/kyverno/main/README.md) — Visão geral do Kyverno (motor de políticas nativo para Kubernetes, validação/mutação/geração/limpeza e verificação de imagens, Non-Goals, projetos Chainsaw/Policy Reporter/Kyverno JSON/Envoy Plugin, casos de uso e SBOM CycloneDX).; consultado em 2026-10-03.
- [Kyverno Documentation — Quick Start & Policy Library](https://kyverno.io/docs/introduction/) — Documentação oficial de introdução, instalação e biblioteca de políticas do Kyverno referenciada no README.; consultado em 2026-10-03.
