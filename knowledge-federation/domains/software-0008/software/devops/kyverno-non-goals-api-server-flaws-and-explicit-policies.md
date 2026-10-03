---
id: software.devops.tranche03.000223
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

# Limites formais (Non-Goals): vulnerabilidades do API Server e manutenção ativa de políticas

## Em uma frase
O primeiro parágrafo da seção Non-Goals do README esclarece que o Kyverno atua apenas sobre as políticas usadas pelo Kubernetes e não foi projetado para corrigir falhas de segurança inerentes ao próprio Kubernetes — exemplificando que ele não protege contra vulnerabilidades no API Server do Kubernetes (como deserialização YAML Billion Laughs ou falhas na implementação de Admission Controllers) nem na infraestrutura subjacente —, além de enfatizar que o Kyverno aplica apenas políticas explicitamente definidas pelos usuários e precisa ser mantido ativamente como qualquer outro produto de segurança.

## Por que importa
Compreender esses Non-Goals evita que gestores tratem a simples instalação do Kyverno como blindagem mágica contra CVEs do plano de controle do Kubernetes ou dispensem a atualização contínua das regras de política.

## Como funciona
Mantenha o API Server do Kubernetes e os nós atualizados independentemente do Kyverno e revise periodicamente o catálogo de políticas instaladas no cluster.

## Exemplo
Uma auditoria de segurança registra que o Kyverno governa a conformidade dos manifestos admitidos, enquanto o endurecimento do API Server e do kernel Linux (com Cilium e Falco) cobre a infraestrutura subjacente.

## Limites e trade-offs
Se o webhook de admissão do próprio Kubernetes sofrer uma falha ou estiver configurado com failurePolicy: Ignore para recursos críticos, requisições podem contornar a avaliação na entrada.

## Como verificar
Conferi o primeiro parágrafo da seção Non-Goals no README oficial de kyverno/kyverno.

## Conexões
- [[kyverno-validate-mutate-generate-cleanup-and-image-verify]] — Veja também: As cinco ações do Kyverno: validar, mutar, gerar, limpar recursos e verificar assinaturas de imagens.
- [[kyverno-complementarity-with-rbac-and-native-admission-policies]] — Veja também: Complementaridade do Kyverno com o RBAC do Kubernetes e com Validating/MutatingAdmissionPolicies.

## Fontes
- [Kyverno — GitHub README](https://raw.githubusercontent.com/kyverno/kyverno/main/README.md) — Visão geral do Kyverno (motor de políticas nativo para Kubernetes, validação/mutação/geração/limpeza e verificação de imagens, Non-Goals, projetos Chainsaw/Policy Reporter/Kyverno JSON/Envoy Plugin, casos de uso e SBOM CycloneDX).; consultado em 2026-10-03.
- [Kyverno Documentation — Quick Start & Policy Library](https://kyverno.io/docs/introduction/) — Documentação oficial de introdução, instalação e biblioteca de políticas do Kyverno referenciada no README.; consultado em 2026-10-03.
