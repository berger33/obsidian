---
id: software.testes.tranche20.001374
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://behave.readthedocs.io/en/stable/fixtures/", "https://behave.readthedocs.io/en/stable/api/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Behave: usar fixtures para recursos

## Em uma frase
Fixtures encapsulam preparação e limpeza com rendimento, podendo ser associadas a etiquetas específicas nos ganchos.

## Por que importa
O recurso só é criado quando o cenário realmente precisa dele, e a limpeza ocorre mesmo em caso de falha.

## Como funciona
Declare a fixture com rendimento, associe-a à etiqueta correspondente e mantenha o recurso disponível no contexto.

## Exemplo
Um servidor de teste pode ser levantado apenas para os cenários marcados com a etiqueta correspondente e encerrado ao final.

## Limites e trade-offs
Fixtures com limpeza incompleta deixam processos ativos, e associação por etiqueta errada cria o recurso em cenários que não o usam.

## Como verificar
Remova a etiqueta de um cenário e confirme que o recurso deixa de ser criado para ele.

## Conexões
- [[behave-tags-and-selection]] — Veja também: Behave: selecionar cenários com etiquetas.
- [[behave-configuration]] — Veja também: Behave: configurar a execução.

## Fontes
- [Behave — Fixtures](https://behave.readthedocs.io/en/stable/fixtures/) — declaração, uso e limpeza de fixtures; consultado em 2026-10-03.
- [Behave — Referência de API](https://behave.readthedocs.io/en/stable/api/) — funções de passo, ganchos, contexto e fixtures; consultado em 2026-10-03.
