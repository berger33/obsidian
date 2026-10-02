---
id: software.testes.tranche07.000109
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://sre.google/sre-book/reliable-product-launches/", "https://sre.google/sre-book/testing-reliability/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Validação de canário com telemetria e rollback", "Teste: Validação de canário com telemetria e rollback"]
lote: software-testes-2000-0001
---

# Validação de canário com telemetria e rollback

## Em uma frase
Use uma parcela controlada de tráfego real para observar se uma versão nova preserva sinais de saúde antes de ampliar o rollout.

## Por que importa
Nem todos os efeitos de uma mudança podem ser reproduzidos em staging; uma exposição gradual limita o impacto e coleta evidência em condições representativas.

## Como funciona
Defina baseline, duração mínima, métricas de saúde e critérios de parada antes da implantação. Compare canário e grupo de referência com tráfego e contexto semelhantes; automatize rollback quando um limite importante for violado.

## Exemplo
Libere uma versão a um pequeno grupo autorizado, compare erro, latência e resultado de negócio com a versão estável, mantenha a exposição pelo período necessário e só então amplie o rollout se as verificações passarem.

## Limites e trade-offs
Tráfego de canário pode ser pequeno ou enviesado, e diferenças simultâneas entre grupos confundem a comparação. Um canário não substitui testes pré-lançamento nem resolve por si só problemas de observabilidade.

## Como verificar
Confirme que a atribuição de tráfego e a coleta de métricas funcionam, simule violação de guardrail em ambiente controlado e prove que a ampliação é bloqueada ou revertida conforme a política.

## Conexões
- [[ci-feedback-testes-regressao]] — aprofundamento relacionado.
- [[regression-testing-change-effects]] — aprofundamento relacionado.

## Fontes
- [Google SRE — Reliable Product Launches](https://sre.google/sre-book/reliable-product-launches/) — rollouts graduais, observação de canários e rollback após falha de validação; consultado em 2026-10-01.
- [Google SRE — Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — testes reduzem incerteza sobre confiabilidade após mudanças; consultado em 2026-10-01.
