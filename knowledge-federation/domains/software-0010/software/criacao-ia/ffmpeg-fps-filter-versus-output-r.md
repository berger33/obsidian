---
id: software.criacao_ia.tranche03.000267
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
fontes: ["https://ffmpeg.org/ffmpeg.html", "https://ffmpeg.org/ffmpeg-filters.html#fps"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# FFmpeg: distinguir filtro fps de opção de output -r

## Em uma frase
O filtro `fps` cria uma sequência de frames na taxa escolhida dentro do filtergraph, enquanto `-r` atua conforme seu escopo de input ou output.

## Por que importa
Confundir a flag de taxa de input com uma conversão de frame rate pode reinterpretar timestamps em vez de duplicar ou descartar frames do modo desejado. Aplicar filtro e `-r` sem planejar a cadeia também pode gerar conversão dupla ou cadência irregular.

## Como funciona
Use `fps` quando a transformação de frames fizer parte do filtergraph e precise ocorrer antes de outras etapas. Use a opção `-r` no escopo correto do arquivo e confirme seu efeito na versão atual. A opção antes de `-i` pode definir taxa de formatos de entrada apropriados; depois do input pode definir política do output. Escolha um ponto de conversão claro.

## Exemplo
Para converter uma origem com taxa variável a saída 24 fps, o projeto coloca filtro `fps=24` no ramo de vídeo e confere frames descartados/duplicados. Para uma fonte raw sem timing incorporado, define taxa de input antes de `-i` e trata conversão de output separadamente.

## Limites e trade-offs
Comportamento depende de formato, timestamps e modo de sincronização; opção `-r` pode ser ignorada ou interpretada de forma específica pelo pipeline. FPS nominal de container não descreve sempre cadence efetiva de timestamps.

## Como verificar
Compare quantidade de frames, `avg_frame_rate`, `r_frame_rate` e `pts_time` com ffprobe; reproduza trechos com movimento e confira duplicate/drop policy antes e depois do encode.

## Conexões
- [[ffmpeg-setpts-timebase-e-relatorio]] — FFmpeg: interpretar PTS em conjunto com time base.
- [[ffmpeg-filtergraph-escaping-niveis]] — FFmpeg filtergraph: separar escaping do filtro e da shell.

## Fontes
- [FFmpeg — Main documentation and -r examples](https://ffmpeg.org/ffmpeg.html) — distingue taxa do arquivo de entrada raw e frame rate do arquivo de saída Consulta: 2026-10-04.
- [FFmpeg — fps filter](https://ffmpeg.org/ffmpeg-filters.html#fps) — documenta filtro que converte a sequência para taxa de frames definida Consulta: 2026-10-04.
