---
id: software.criacao_ia.tranche03.000262
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
fontes: ["https://ffmpeg.org/ffmpeg.html#Stream-selection", "https://ffmpeg.org/ffmpeg-filters.html#Filtergraph-description"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# FFmpeg: mapear streams de entrada e saídas rotuladas

## Em uma frase
`-map` controla explicitamente quais streams chegam ao output, e labels de outputs de complex filtergraphs identificam streams produzidos por filtros.

## Por que importa
Seleção automática pode escolher um vídeo, áudio ou legenda diferente do pretendido. Filtergraphs complexos também criam streams que não são diretamente uma stream de input, então deixar descoberta implícita dificulta reproduzir uma exportação multi-faixa.

## Como funciona
Use índices de input começando em zero e stream specifiers para escolher tipo ou índice. Nomeie outputs de um `filter_complex` entre colchetes e mapeie cada label no output de destino. Distinga `-map` de filtros: mapeamento seleciona a stream que alimenta arquivo; filtergraph transforma e produz stream nova. Revise automatic stream selection quando não houver mapping explícito.

## Exemplo
Uma composição recebe vídeo do primeiro arquivo e áudio do segundo; um `overlay` cria `[composite]`, que é mapeado como vídeo, enquanto `0:a:0` é mapeado como faixa de áudio. Para um arquivo somente visual, mapeie a saída de filtro e não deixe áudio automático ser escolhido de outra entrada.

## Limites e trade-offs
Mapeamentos incompatíveis com o muxer ou labels usados mais de uma vez podem falhar. Outputs de filtergraph sem label e sem mapping possuem regras automáticas próprias; não generalize que qualquer `-map` suprime toda seleção implícita.

## Como verificar
Leia o bloco Stream mapping no log, inspecione arquivo final com `ffprobe -show_streams` e compare número, codec, idioma e disposição de cada faixa. Teste inputs com múltiplas streams para detectar seleção automática inesperada.

## Conexões
- [[ffmpeg-escopo-opcoes-por-arquivo]] — FFmpeg: posicionar opções no input ou output correto.
- [[ffmpeg-concat-demuxer-precondicoes]] — FFmpeg concat demuxer: conferir streams e durações de entrada.

## Fontes
- [FFmpeg — Stream selection](https://ffmpeg.org/ffmpeg.html#Stream-selection) — define seleção automática, `-map`, índices e tratamento de outputs de filtergraph Consulta: 2026-10-04.
- [FFmpeg — Filtergraph syntax](https://ffmpeg.org/ffmpeg-filters.html#Filtergraph-description) — documenta labels e ligações entre outputs e inputs de filtros Consulta: 2026-10-04.
