---
id: software.criacao_ia.tranche03.000264
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
fontes: ["https://ffmpeg.org/ffmpeg-filters.html#concat", "https://ffmpeg.org/ffmpeg.html#Filtering"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# FFmpeg concat filter: alinhar cada segmento e normalizar streams

## Em uma frase
O concat filter combina streams decodificadas por segmentos e pressupõe que cada segmento começa em timestamp zero.

## Por que importa
Diferente da concatenação de pacotes, o filtro pode transformar streams antes da junção e permite lidar com formatos diferentes, mas a graph precisa fornecer quantidade e ordenação correta de entradas. Timestamps de origem fora de zero causam gaps ou sincronismo inesperado.

## Como funciona
Decodifique streams, zere timestamps quando necessário com filtros apropriados e conecte entradas na ordem de segmento e tipo declarada pelo filtro. Padronize resolução, pixel format, sample rate e channel layout se necessário. A duração usada para transicionar para próximo segmento segue a stream mais longa no segmento, exceto último, cujo áudio pode precisar de padding explícito conforme requisito.

## Exemplo
Para duas cenas, conecte vídeo e áudio do segmento um, depois vídeo e áudio do segmento dois ao `concat` configurado para dois segmentos com áudio e vídeo. Normalize vídeo e áudio em ramos separados e inspecione PTS nas duas fronteiras.

## Limites e trade-offs
O filter não repara automaticamente todo tipo de descontinuidade ou diferença semântica. Número de entradas, stream count e layouts precisam corresponder à configuração; bitrate final e codec são escolhidos depois, no output.

## Como verificar
Teste cada segmento isoladamente, use `showinfo` ou `ashowinfo` antes e depois do concat, e confira duração, PTS, frame rate e continuidade de áudio na fronteira de cada par.

## Conexões
- [[ffmpeg-concat-demuxer-precondicoes]] — FFmpeg concat demuxer: conferir streams e durações de entrada.
- [[ffmpeg-trim-nao-redefine-pts]] — FFmpeg trim: separar seleção de frames e reinício de timestamps.

## Fontes
- [FFmpeg — concat filter](https://ffmpeg.org/ffmpeg-filters.html#concat) — define segmentos, ordenação, timestamps e duração de referência do filtro concat Consulta: 2026-10-04.
- [FFmpeg — Filtering introduction](https://ffmpeg.org/ffmpeg.html#Filtering) — explica decodificação, filtergraphs e diferença entre filtros e streamcopy Consulta: 2026-10-04.
