---
id: software.criacao_ia.tranche04.000308
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
fontes: ["https://www.w3.org/TR/webgpu/", "https://developer.mozilla.org/en-US/docs/Web/API/GPUBindGroupLayout"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WebGPU: bind groups só valem se o layout for compatível com o pipeline

## Em uma frase
A compatibilidade de pipeline exige que o bind group criado para um layout seja setado exatamente no índice e com o tipo declarados no layout do pipeline.

## Por que importa
O custo da validação no momento do bind é o que permite submissões baratas; em troca, a WebGPU não faz coerção. Layouts estruturalmente idênticos mas criados separados são objetos diferentes, e um bind group do layout errado é rejeitado em setBindGroup, com efeito dominó em todo o pass.

## Como funciona
Declare GPUBindGroupLayoutDescriptor entries com binding, visibility por estágio e tipo exato (buffer com minBindingSize, sampler, textura de viewSampleType específica). Crie o GPUPipelineLayout a partir de layouts indexados e monte o pipeline com o mesmo layout. Reutilize o objeto de layout entre pipelines que compartilham o contrato — a identidade do layout é o que o motor compara. Bind groups são substituíveis por índice a cada pass; para offsets variáveis, prefira dynamic offsets alinhados (256 bytes uniform, 256 storage por default) a recriar grupos.

## Exemplo
Um material com 40 variações compartilha um bind group layout global (texturas de ambiente) e um por-material (uniforms), reduzindo recriações por frame para apenas os grupos que mudam.

## Limites e trade-offs
Pipeline layouts têm contagem de grupos limitada por maxBindGroups; esgotar o orçamento obriga a mesclar blocos. Dynamic offset custa alinhamento e consome entradas do layout; nem todo binding aceita (somente buffer dynamic). Layouts incompatíveis falham em validação — mas só se você a estiver observando.

## Como verificar
Com error scope ativo, atribua um bind group do layout errado e confirme a mensagem de incompatibilidade. Compare contagem de grupos criados por frame antes e depois de compartilhar layouts entre materiais. Valide os offsets dinâmicos com teste que quebre o alinhamento e observe a rejeição.

## Conexões
- [[webgpu-textureusage-views-permitidos]] — WebGPU: declarar cada uso de textura no momento certo.
- [[webgpu-erros-asyncronos-escopos]] — WebGPU: capturar erros assíncronos com escopos empilhados.

## Fontes
- [W3C — WebGPU (especificação)](https://www.w3.org/TR/webgpu/) — define compatibilidade de pipeline e os requisitos de layout/bind group Consulta: 2026-10-04.
- [MDN — GPUBindGroupLayout](https://developer.mozilla.org/en-US/docs/Web/API/GPUBindGroupLayout) — documenta o papel do layout como contrato entre pipeline e bind groups Consulta: 2026-10-04.
