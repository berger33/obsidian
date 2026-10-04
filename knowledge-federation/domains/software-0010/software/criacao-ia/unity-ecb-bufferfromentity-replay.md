---
id: software.criacao_ia.tranche04.000332
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/systems-deferring-data.html", "https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/systems-manage-structural-changes.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Entities: a EntityCommandBuffer é replay, não fila mágica

## Em uma frase
Uma EntityCommandBuffer registra operações estruturais para playback posterior; ela vive em buffers-as-entity (BufferFromEntity) e seu ponto de reprodução é decisão explícita do sistema.

## Por que importa
Definir 'quando as mudanças acontecem' é o contrato que o ECB entrega: o mesmo buffer gravado em cinco sistemas pode ser reproduzido no fim do frame num único lugar, com custo de estrutura concentrado e determinístico. Tratar o ECB como 'fire and forget' perde o controle do episódio — a reprodução vira o ponto de sincronização que você precisa projetar.

## Como funciona
Padrão documentado: um sistema grava no 'BufferFromEntity<EntityCommandBuffer>' (com parallel writer quando concorrente), um ponto de commit (geralmente um sistema isolado ao fim do grupo) faz 'Playback(world)' e 'ClearAndDispose'. Para o padrão comum (um ECB por frame), existe a variante com paralelismo gerenciada pelo framework; o detalhe que permanece é o mesmo: gravar separado, reproduzir junto.

## Exemplo
O sistema de projéteis grava 'inimigo perde Health' e 'partícula nasce' no ECB do frame; o sistema de commit roda depois de todos os produtores, garantindo que a query de colisão do próximo frame enxerga um mundo coeso.

## Limites e trade-offs
Entidades criadas num ECB têm handle 'nulo' até o playback — encadear lógica de leitura-escrita no mesmo ECB entre gravação e reprodução exige duas fases. Gravar e nunca reproduzir vaza memória nativa (o dispose é manual na variante explícita). E o replay ainda é mudança estrutural: mover o problema do laço para o commit não apaga o custo por elemento.

## Como verificar
Um teste de unidade: grave 100 spawns, asserte 0 antes do playback e 100 depois. O 'ParallelWriter' com N threads de gravação e asserção de contagem final cobre a ordem. Profiler na transição grava/reproduz mostra a concentração que o padrão promete.

## Conexões
- [[unity-estrutura-mudanca-custo-episodio]] — Unity Entities: criar/destruir é caro porque o layout muda, e por isso é estrutural.
- [[unity-ijobentity-fonte-gerada-main-thread]] — Unity Entities: IJobEntity gera código por assinatura — e pode virar main thread sem aviso de sintaxe.

## Fontes
- [Unity Entities @1.4 — Defer data changes](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/systems-deferring-data.html) — página do manual sobre deferral com command buffers Consulta: 2026-10-04.
- [Unity Entities @1.4 — Manage structural changes](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/systems-manage-structural-changes.html) — enquadra o ECB como uma das três portas de mudança estrutural Consulta: 2026-10-04.
