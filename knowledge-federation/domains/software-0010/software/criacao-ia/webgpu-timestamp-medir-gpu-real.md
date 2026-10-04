---
id: software.criacao_ia.tranche04.000310
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
fontes: ["https://www.w3.org/TR/webgpu/", "https://developer.mozilla.org/en-US/docs/Web/API/GPUQuerySet"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WebGPU: medir tempo de GPU com query sets de timestamp

## Em uma frase
Timestamps medidos na própria GPU exigem a feature 'timestamp-query' e um buffer de resolução — o relógio do navegador não sabe quando o work terminou.

## Por que importa
performance.now() ao redor de submit mede enqueue, não execução; filas e paralelismo escondem a verdade. Para decisões de otimização de shader, tiling e orden de passes, a única cronometragem honesta vem de queries escritas pelo dispositivo e resolvidas num buffer legível.

## Como funciona
Crie o device com requiredFeatures contendo 'timestamp-query' e um GPUQuerySet do tipo 'timestamp' com count par (início/fim por região). No pass, use writeTimestamp(querySet, index) ou os timestamps dos render/compute pass descriptors; resolva com resolveQuerySet para um buffer com COPY_DST|MAP_READ, copie para um segundo buffer de leitura quando necessário, e converta os BigUInt64 subtraindo início do fim. Some os valores apenas como deltas; o período de contagem vem de queue.getTimestampPeriod, que é por plataforma.

## Exemplo
Um profiler de overlay mede cada pass de pós-processamento com dois writeTimestamp por pass, resolve ao fim do frame e exibe a média móvel dos deltas — os spikes de shadow pass ficam visíveis na hora.

## Limites e trade-offs
Timestamps absolutos não têm significado entre dispositivos nem entre passes; deltas são a única grandeza útil. Nem toda implementação expõe a feature (verifique device.features). Contagens altas de queries aumentam o custo do pass, e a janela entre resolve e leitura pode cruzar frames, distorcendo atribuições se a pipeline de render for profunda.

## Como verificar
Confira que 'timestamp-query' está em device.features antes de criar o QuerySet (sem a feature, a criação falha por validação). Compare deltas de timestamp com o relógio da CPU para um trabalho sintético grande e confirme correlação. Rode na CPU-driver de teste (fallback) e confirme o comportamento documentado quando o período não está disponível.

## Conexões
- [[webgpu-erros-asyncronos-escopos]] — WebGPU: capturar erros assíncronos com escopos empilhados.

## Fontes
- [W3C — WebGPU (especificação)](https://www.w3.org/TR/webgpu/) — define GPUQuerySet de timestamps, resolveQuerySet e o significado de getTimestampPeriod Consulta: 2026-10-04.
- [MDN — GPUQuerySet](https://developer.mozilla.org/en-US/docs/Web/API/GPUQuerySet) — documenta tipos de query set e ciclo de vida (count, destroy, reset) Consulta: 2026-10-04.
