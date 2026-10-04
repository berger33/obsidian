---
id: software.seguranca.tranche17.001655
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

# Kyverno: Ação de validação Audit versus Enforce

## Em uma frase
**Kyverno — Ação de validação Audit versus Enforce:** Modos de auditoria e bloqueio permitem introduzir política gradualmente, medindo violações antes de interromper admissão.

## Por que importa
O recorte de **ação de validação audit versus enforce** ajuda a enforçar configuração segura na admissão e reportar desvios sem substituir revisão de cluster. A equipe registra risco, evidência e responsável.

## Como funciona
Para **ação de validação audit versus enforce**, políticas como recursos Kubernetes são avaliadas em requisições de admissão e podem validar, mutar ou gerar recursos conforme a regra. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Mantenha uma regra de imagens sem `latest` em modo audit no cluster de pré-produção e examine reports. Teste em staging autorizado.

## Limites e trade-offs
Auditoria não impede criação; confundir relatório com enforcement cria falsa sensação de proteção. Exceções exigem responsável e prazo.

## Como verificar
Inclua requisição deliberadamente não conforme e confirme se ela é aceita ou negada conforme modo configurado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kyverno-politicas-em-cel-e-migracao]] — Complementa o tópico com kyverno: políticas em cel e migração.

## Fontes
- [Kyverno — Quick Start](https://kyverno.io/docs/introduction/quick-start/) — guia oficial sobre validação, mutação e geração de políticas; consultado em 2026-10-04.
- [Kyverno — Migration to CEL Policies](https://kyverno.io/docs/guides/migration-to-cel/) — guia atual de migração de ClusterPolicy para tipos de política baseados em CEL; consultado em 2026-10-04.
