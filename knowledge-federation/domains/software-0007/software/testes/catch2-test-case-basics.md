---
id: software.testes.tranche19.001258
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/catchorg/Catch2/blob/devel/docs/tutorial.md", "https://github.com/catchorg/Catch2/blob/devel/docs/command-line.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Catch2: estruturar casos de teste

## Em uma frase
Casos de teste são declarados com macros que os registram automaticamente e recebem nome livre e etiquetas entre colchetes.

## Por que importa
O registro automático elimina listas manuais e as etiquetas permitem selecionar grupos de testes na execução.

## Como funciona
Nomeie o caso descrevendo o comportamento, use etiquetas para agrupar por área ou tipo e mantenha cada caso focado.

## Exemplo
Um caso pode declarar a etiqueta de integração e ser executado apenas quando esse conjunto for selecionado na linha de comando.

## Limites e trade-offs
Nomes vagos dificultam localizar a falha, e etiquetas inconsistentes entre arquivos quebram a seleção por grupo.

## Como verificar
Liste as etiquetas usadas em um arquivo e confirme que o filtro correspondente executa exatamente os casos esperados.

## Conexões
- [[catch2-assertions]] — Veja também: Catch2: escolher entre asserção fatal e não fatal.

## Fontes
- [Catch2 — Tutorial](https://github.com/catchorg/Catch2/blob/devel/docs/tutorial.md) — primeiros passos, casos de teste, seções e asserções; consultado em 2026-10-03.
- [Catch2 — Command line](https://github.com/catchorg/Catch2/blob/devel/docs/command-line.md) — filtros por nome e etiqueta, listagem, embaralhamento e semente; consultado em 2026-10-03.
