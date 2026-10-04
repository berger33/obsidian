---
id: software.criacao_ia.tranche03.000258
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
fontes: ["https://openusd.org/release/tut_xforms.html", "https://openusd.org/release/api/class_usd_attribute.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OpenUSD: retimar animação referenciada com layer offset

## Em uma frase
Layer offsets alteram a correspondência temporal de dados de uma layer referenciada sem reescrever os samples de autoria da layer original.

## Por que importa
Reutilizar a mesma animação em tomadas com início ou velocidade diferentes é um caso de composição, não necessariamente motivo para duplicar e editar todas as chaves. Preservar os samples fonte mantém procedência e permite que várias tomadas usem a mesma versão do asset.

## Como funciona
Adicione a layer ou reference com offset de tempo e escala apropriados no arc de composição. Em USD, time codes da layer subordinada são remapeados ao compor, e a escala de stage interpreta os códigos em tempo real. A API `SdfLayerOffset` representa translação e escala do mapeamento; confira intervalo e direção do mapeamento com samples conhecidos.

## Exemplo
Uma sequência de giro authorada em 24 fps pode começar em outro ponto e tocar em velocidade diferente numa tomada de render. A layer de tomada aplica offset/scale à composição, enquanto os valores originais de rotação continuam intactos no arquivo de animação.

## Limites e trade-offs
Offsets não convertem automaticamente coordenadas espaciais, unidades métricas ou semântica de frames da aplicação. Layer offsets compostos podem ser difíceis de auditar e precisam considerar outros offsets existentes no caminho de composição.

## Como verificar
Inspecione o valor do atributo em tempos de entrada e saída calculados, compare `GetTimeSamples()` na fonte com avaliação no stage e valide start/end time codes, fps e offsets acumulados.

## Conexões
- [[openusd-attribute-default-e-time-samples]] — OpenUSD: separar default value de time samples em atributos.
- [[openusd-flattening-stage-export]] — OpenUSD: flattening exporta resultado composto, não estrutura editável.

## Fontes
- [OpenUSD 26.08 — Transformations, Animation, and Layer Offsets](https://openusd.org/release/tut_xforms.html) — demonstra animação referenciada e retiming por layer offsets Consulta: 2026-10-04.
- [OpenUSD 26.08 — UsdAttribute API](https://openusd.org/release/api/class_usd_attribute.html) — documenta consulta de samples e valores avaliados em time codes Consulta: 2026-10-04.
