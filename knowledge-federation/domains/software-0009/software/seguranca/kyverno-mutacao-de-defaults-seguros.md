---
id: software.seguranca.tranche17.001652
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

# Kyverno: Mutação de defaults seguros

## Em uma frase
**Kyverno — Mutação de defaults seguros:** Mutação pode preencher ou ajustar configuração no fluxo de admission antes que o objeto seja aceito.

## Por que importa
O recorte de **mutação de defaults seguros** ajuda a enforçar configuração segura na admissão e reportar desvios sem substituir revisão de cluster. A equipe registra risco, evidência e responsável.

## Como funciona
Para **mutação de defaults seguros**, políticas como recursos Kubernetes são avaliadas em requisições de admissão e podem validar, mutar ou gerar recursos conforme a regra. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Aplique label padrão a Pod de laboratório somente quando o campo estiver ausente, preservando valor explícito aprovado. Teste em staging autorizado.

## Limites e trade-offs
Mutação repetida deve ser idempotente e não alterar silenciosamente valores definidos pelo operador. Exceções exigem responsável e prazo.

## Como verificar
Envie recurso com campo ausente e já preenchido e compare o objeto armazenado após admissão. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kyverno-geracao-de-recursos-auxiliares]] — Complementa o tópico com kyverno: geração de recursos auxiliares.

## Fontes
- [Kyverno — Quick Start](https://kyverno.io/docs/introduction/quick-start/) — guia oficial sobre validação, mutação e geração de políticas; consultado em 2026-10-04.
- [Kyverno — Migration to CEL Policies](https://kyverno.io/docs/guides/migration-to-cel/) — guia atual de migração de ClusterPolicy para tipos de política baseados em CEL; consultado em 2026-10-04.
