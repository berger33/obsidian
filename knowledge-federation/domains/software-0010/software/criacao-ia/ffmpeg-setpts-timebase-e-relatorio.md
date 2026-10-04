---
id: software.criacao_ia.tranche03.000266
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
fontes: ["https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts", "https://ffmpeg.org/ffprobe.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# FFmpeg: interpretar PTS em conjunto com time base

## Em uma frase
PTS é um valor expresso em unidades da time base da stream, não um número de segundos até ser interpretado com essa escala.

## Por que importa
Comparar inteiros de PTS entre streams com time bases diferentes leva a cálculos errados de atraso. Filtros de tempo usam expressões sobre timestamps e podem trocar time base ou gerar valores não representáveis com a precisão inicialmente presumida.

## Como funciona
Leia PTS junto com `time_base` na stream e converta unidades antes de comparar. `setpts` e `asetpts` reescrevem timestamps por expressão; `STARTPTS`, `PTS` e expressões de escala ajudam a manter ou deslocar timeline. Após filtering, examine o PTS já quantizado na time base recebida pelo próximo estágio.

## Exemplo
Para deslocar vídeo e áudio pelo mesmo intervalo real, calcule a expressão em segundos ou converta para unidades da respectiva time base, em vez de subtrair o mesmo inteiro bruto em ambas. Inspecione frame inicial e pacotes após mux para validar sincronismo.

## Limites e trade-offs
Time base pode ser renegociada por filtros e codificadores, e valores de PTS podem ser desconhecidos ou negativos em fluxos válidos. Aritmética de timestamps não substitui análise de start_time, edit lists e comportamento do muxer.

## Como verificar
Use `ffprobe -show_streams -show_packets` para comparar `pts`, `pts_time`, `time_base` e `start_time`; coloque `showinfo` em cada ramo e valide no container final.

## Conexões
- [[ffmpeg-trim-nao-redefine-pts]] — FFmpeg trim: separar seleção de frames e reinício de timestamps.
- [[ffmpeg-fps-filter-versus-output-r]] — FFmpeg: distinguir filtro fps de opção de output -r.

## Fontes
- [FFmpeg — setpts and asetpts](https://ffmpeg.org/ffmpeg-filters.html#setpts_002c-asetpts) — define PTS expressions, valores de referência e time base usados em filtros Consulta: 2026-10-04.
- [ffprobe documentation](https://ffmpeg.org/ffprobe.html) — documenta campos e seleção de streams para inspecionar timestamps e metadados Consulta: 2026-10-04.
