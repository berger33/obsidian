---
id: software.seguranca.tranche17.001659
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://kyverno.io/docs/introduction/quick-start/", "https://kyverno.io/docs/guides/migration-to-cel/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Kyverno: Exceções de política governadas

## Em uma frase
**Kyverno — Exceções de política governadas:** Exceções autorizadas permitem tratar workload incompatível sem desativar uma política para todo o cluster.

## Por que importa
O recorte de **exceções de política governadas** ajuda a enforçar configuração segura na admissão e reportar desvios sem substituir revisão de cluster. A equipe registra risco, evidência e responsável.

## Como funciona
Para **exceções de política governadas**, políticas como recursos Kubernetes são avaliadas em requisições de admissão e podem validar, mutar ou gerar recursos conforme a regra. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Crie exceção temporária para workload de laboratório, com owner e expiração revisável. Teste em staging autorizado.

## Limites e trade-offs
Exceção ampla por namespace ou sem prazo tende a virar bypass permanente. Exceções exigem responsável e prazo.

## Como verificar
Teste que a exceção cobre apenas o recurso aprovado e que a política volta a valer após expiração. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kyverno-teste-local-de-politicas-antes-do-cluster]] — Complementa o tópico com kyverno: teste local de políticas antes do cluster.

## Fontes
- [Kyverno — Quick Start](https://kyverno.io/docs/introduction/quick-start/) — guia oficial sobre validação, mutação e geração de políticas; consultado em 2026-10-04.
- [Kyverno — Migration to CEL Policies](https://kyverno.io/docs/guides/migration-to-cel/) — guia atual de migração de ClusterPolicy para tipos de política baseados em CEL; consultado em 2026-10-04.
