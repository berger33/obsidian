---
id: software.devops.tranche03.000221
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

# Motor de políticas nativo para Kubernetes sem exigir linguagem de programação nova

## Em uma frase
O README oficial no repositório kyverno/kyverno apresenta o Kyverno como um motor de políticas nativo para Kubernetes (Kubernetes-native policy engine) projetado para equipes de engenharia de plataforma sob o lema "Cloud Native Policy Management. No new language required", permitindo governança, conformidade, segurança e automação por meio de policy-as-code operando com ferramentas que a equipe já utiliza — como kubectl, kustomize e Git.

## Por que importa
Diferentemente de motores que exigem aprender uma linguagem de domínio específico separada do ecossistema Kubernetes, declarar políticas como recursos YAML nativos do Kubernetes permite revisá-las, kustomizá-las e sincronizá-las diretamente nos mesmos fluxos de GitOps (Argo CD ou Flux).

## Como funciona
Escreva políticas do Kyverno em YAML nativo, valide-as nos pipelines de CI com a CLI do Kyverno e gerencie sua implantação nos clusters usando kustomize, Helm e Git.

## Exemplo
Uma equipe de plataforma versiona suas políticas de segurança do Kyverno em um repositório Git e aplica overlays por ambiente via Kustomize e Argo CD.

## Limites e trade-offs
Como qualquer código declarativo que governa admissão no cluster, políticas mal testadas podem bloquear deploys legítimos; valide sempre novas regras antes de colocá-las em modo de bloqueio.

## Como verificar
Conferi o cabeçalho e a seção About Kyverno no README oficial de kyverno/kyverno.

## Conexões
- [[kyverno-validate-mutate-generate-cleanup-and-image-verify]] — Veja também: As cinco ações do Kyverno: validar, mutar, gerar, limpar recursos e verificar assinaturas de imagens.

## Fontes
- [Kyverno — GitHub README](https://raw.githubusercontent.com/kyverno/kyverno/main/README.md) — Visão geral do Kyverno (motor de políticas nativo para Kubernetes, validação/mutação/geração/limpeza e verificação de imagens, Non-Goals, projetos Chainsaw/Policy Reporter/Kyverno JSON/Envoy Plugin, casos de uso e SBOM CycloneDX).; consultado em 2026-10-03.
- [Kyverno Documentation — Quick Start & Policy Library](https://kyverno.io/docs/introduction/) — Documentação oficial de introdução, instalação e biblioteca de políticas do Kyverno referenciada no README.; consultado em 2026-10-03.
