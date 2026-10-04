---
id: software.criacao_ia.tranche03.000265
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
fontes: ["https://ffmpeg.org/ffmpeg-filters.html#trim", "https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# FFmpeg trim: separar seleção de frames e reinício de timestamps

## Em uma frase
Os filtros `trim` e `atrim` selecionam intervalo de frames ou amostras, mas não redefinem automaticamente seus timestamps de apresentação.

## Por que importa
Um trecho pode começar com PTS alto mesmo depois de ser recortado. Em concatenação ou sincronização com outra fonte, esse offset mantido pode introduzir silêncio, atraso ou timestamps não esperados apesar de a duração visual parecer correta.

## Como funciona
Use `trim` ou `atrim` para escolher conteúdo e, quando for desejado iniciar novo timeline em zero, aplique `setpts=PTS-STARTPTS` ou `asetpts=PTS-STARTPTS` depois. Se precisar preservar relação temporal com outras streams, mantenha ou transforme PTS deliberadamente em vez de zerar às cegas.

## Exemplo
Um áudio é recortado de 12 a 18 segundos para começar junto de um vídeo novo. `atrim` seleciona seis segundos, e `asetpts` ajusta o primeiro sample a zero antes do ramo chegar a `concat` ou muxer.

## Limites e trade-offs
Zerar PTS em apenas um dos ramos pode destruir sincronização intencional entre streams; trim baseado em timestamps ou duração também depende de time base e precisão das amostras. O filtro não garante que codificador ou container preserve todos os valores exatamente.

## Como verificar
Coloque `ashowinfo`/`showinfo` antes e depois, inspecione PTS e time base com `ffprobe -show_packets` e compare início de áudio e vídeo na reprodução.

## Conexões
- [[ffmpeg-concat-filter-timestamps-zero]] — FFmpeg concat filter: alinhar cada segmento e normalizar streams.
- [[ffmpeg-setpts-timebase-e-relatorio]] — FFmpeg: interpretar PTS em conjunto com time base.

## Fontes
- [FFmpeg — trim and atrim filters](https://ffmpeg.org/ffmpeg-filters.html#trim) — documenta que trim seleciona frames e recomenda setpts/asetpts para alterar timestamps Consulta: 2026-10-04.
- [FFmpeg — setpts and asetpts](https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts) — define expressões temporais para transformação dos PTS de vídeo e áudio Consulta: 2026-10-04.
