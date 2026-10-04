---
id: software.testes.tranche20.001372
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
fontes: ["https://behave.readthedocs.io/en/stable/api/", "https://behave.readthedocs.io/en/stable/tutorial/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Behave: preparar e limpar com ganchos

## Em uma frase
O arquivo de ambiente define funções executadas antes e depois da suíte, da funcionalidade, do cenário e do passo.

## Por que importa
Escolher o nível adequado evita repetir preparação custosa e garante limpeza mesmo quando o cenário falha.

## Como funciona
Concentre a infraestrutura nos ganchos mais amplos, a preparação de dados no nível do cenário e registre a limpeza correspondente.

## Exemplo
A navegação pode ser aberta uma vez por execução e cada cenário começar com dados próprios, capturando tela em falhas.

## Limites e trade-offs
Ganchos que engolem exceções escondem falhas de preparação, e limpeza ausente deixa recursos ativos entre execuções.

## Como verificar
Desative a limpeza de um recurso e confirme que a segunda execução passa a falhar por resíduo da primeira.

## Conexões
- [[behave-context-sharing]] — Veja também: Behave: compartilhar estado pelo contexto.
- [[behave-tags-and-selection]] — Veja também: Behave: selecionar cenários com etiquetas.

## Fontes
- [Behave — Referência de API](https://behave.readthedocs.io/en/stable/api/) — funções de passo, ganchos, contexto e fixtures; consultado em 2026-10-03.
- [Behave — Tutorial](https://behave.readthedocs.io/en/stable/tutorial/) — primeiros passos, ganchos, etiquetas e fixtures; consultado em 2026-10-03.
