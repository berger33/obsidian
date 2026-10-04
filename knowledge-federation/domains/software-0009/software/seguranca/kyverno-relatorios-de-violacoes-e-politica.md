---
id: software.seguranca.tranche17.001658
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

# Kyverno: Relatórios de violações e política

## Em uma frase
**Kyverno — Relatórios de violações e política:** Policy Reports consolidam resultado por objeto e ajudam a priorizar rollout de regras.

## Por que importa
O recorte de **relatórios de violações e política** ajuda a enforçar configuração segura na admissão e reportar desvios sem substituir revisão de cluster. A equipe registra risco, evidência e responsável.

## Como funciona
Para **relatórios de violações e política**, políticas como recursos Kubernetes são avaliadas em requisições de admissão e podem validar, mutar ou gerar recursos conforme a regra. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Gere um finding de teste e acompanhe status do report depois de corrigir o recurso. Teste em staging autorizado.

## Limites e trade-offs
Relatório pode estar atrasado ou refletir somente recursos que o background scan alcançou. Exceções exigem responsável e prazo.

## Como verificar
Compare estado do objeto, status do report e evento de admission antes de fechar a não conformidade. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kyverno-excecoes-de-politica-governadas]] — Complementa o tópico com kyverno: exceções de política governadas.

## Fontes
- [Kyverno — Quick Start](https://kyverno.io/docs/introduction/quick-start/) — guia oficial sobre validação, mutação e geração de políticas; consultado em 2026-10-04.
- [Kyverno — Migration to CEL Policies](https://kyverno.io/docs/guides/migration-to-cel/) — guia atual de migração de ClusterPolicy para tipos de política baseados em CEL; consultado em 2026-10-04.
