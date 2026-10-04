---
id: software.seguranca.tranche17.001651
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

# Kyverno: Validação de recursos no admission

## Em uma frase
**Kyverno — Validação de recursos no admission:** Uma regra de validação pode avaliar recurso antes de persistir e negar requisições que contrariem critérios definidos.

## Por que importa
O recorte de **validação de recursos no admission** ajuda a enforçar configuração segura na admissão e reportar desvios sem substituir revisão de cluster. A equipe registra risco, evidência e responsável.

## Como funciona
Para **validação de recursos no admission**, políticas como recursos Kubernetes são avaliadas em requisições de admissão e podem validar, mutar ou gerar recursos conforme a regra. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em namespace de teste, exija label `team` em Pods e observe comportamento `Audit` antes de ativar negação. Teste em staging autorizado.

## Limites e trade-offs
Validação pode interromper deploys existentes; começar com auditoria ajuda medir cobertura e exceções necessárias. Exceções exigem responsável e prazo.

## Como verificar
Teste create e update, namespaces incluídos e excluídos, e confirme evento/report para cada caso. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kyverno-mutacao-de-defaults-seguros]] — Complementa o tópico com kyverno: mutação de defaults seguros.

## Fontes
- [Kyverno — Quick Start](https://kyverno.io/docs/introduction/quick-start/) — guia oficial sobre validação, mutação e geração de políticas; consultado em 2026-10-04.
- [Kyverno — Migration to CEL Policies](https://kyverno.io/docs/guides/migration-to-cel/) — guia atual de migração de ClusterPolicy para tipos de política baseados em CEL; consultado em 2026-10-04.
