---
id: software.criacao_ia.tranche03.000234
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://dev.epicgames.com/documentation/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.8", "https://dev.epicgames.com/documentation/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.8"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal PCG runtime: fontes, raios de geração e limpeza

## Em uma frase
Runtime Generation agenda células perto de PCG Generation Sources e as limpa quando deixam de satisfazer o raio de cleanup.

## Por que importa
O que aparece ao jogador depende tanto da distância de geração como da política de remoção. Configurações de raios incoerentes entre níveis de detalhe podem criar pop-in, carregar detalhe fino longe demais ou remover ativos ainda visíveis.

## Como funciona
Uma source pode vir do viewport do editor, jogador, streaming source de World Partition ou componente dedicado. Defina `Generation Radii` por grid size no graph e, se necessário, override por componente. `Cleanup Radius Multiplier` escala a distância de remoção; a documentação recomenda raios que crescem de grades pequenas para maiores. Frustum culling e bounds modifiers podem adiantar geração e cleanup em relação à visão.

## Exemplo
Um jogo de exploração mantém detalhes amplos carregados a distância maior e ativa grama de alta densidade apenas perto do jogador. Em PIE, habilite o viewport como geração source para observar raios e cleanup antes de testar fontes de streaming reais.

## Limites e trade-offs
Uma source não é necessariamente a câmera do jogador: outras sources também podem ativar células. Raios excessivos elevam memória e trabalho; raio de cleanup e frustum precisam considerar tamanho do objeto e latência do scheduler.

## Como verificar
Desenhe as esferas de geração, mova cada tipo de source separadamente e registre o tempo entre entrada no raio, início e conclusão. Confira objetos visíveis na borda e repita com mudanças de frustum e multiplicador.

## Conexões
- [[ue-pcg-world-partition-data-layers-hlod]] — Unreal PCG: propagar Data Layers e HLOD aos atores gerados.
- [[ue-pcg-scheduler-num-generating-components]] — Unreal PCG runtime: equilibrar scheduler e células concorrentes.

## Fontes
- [Unreal Engine 5.8 — PCG generation modes](https://dev.epicgames.com/documentation/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.8) — define sources, radii, multiplier, scheduling e frustum culling Consulta: 2026-10-04.
- [Unreal Engine 5.8 — PCG runtime debugging](https://dev.epicgames.com/documentation/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.8) — oferece overlay e visualização das células que estão sendo geradas Consulta: 2026-10-04.
