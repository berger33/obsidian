---
id: software.criacao_ia.tranche03.000263
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
fontes: ["https://ffmpeg.org/ffmpeg-formats.html#concat-1", "https://ffmpeg.org/ffprobe.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# FFmpeg concat demuxer: conferir streams e durações de entrada

## Em uma frase
O concat demuxer lê uma lista de arquivos como uma sequência de pacotes, exigindo estrutura de streams compatível e estimativas de duração confiáveis.

## Por que importa
Concatenar no nível de pacotes pode evitar decodificar e recodificar, mas timestamps do próximo arquivo dependem de informações temporais do segmento anterior. Se arquivos divergem em codecs, streams ou durações registradas, o resultado pode ter timestamps sobrepostos, lacunas ou sincronização incorreta.

## Como funciona
Crie um arquivo de lista com diretivas `file` e invoque o demuxer concat. Verifique que todos os arquivos têm mesmas streams, codecs e parâmetros relevantes antes do concat; durações informadas pelo container ou especificadas na lista participam da localização temporal do próximo arquivo. Para mídia incompatível, transforme streams para formato comum ou use concat filter após decodificação.

## Exemplo
Clipes codificados de forma idêntica e com áudio/vídeo correspondentes podem ser concatenados em stream copy. Antes, `ffprobe` mede streams e duração; depois, a saída é reaberta para verificar duração, início de pacotes e sincronismo nas fronteiras.

## Limites e trade-offs
Concat demuxer não reamostra, redimensiona ou reconcilia diferenças de codec e parâmetros. Duração de stream pode ser estimada com erro ou ausente; arquivos com edit lists ou timestamps fora de zero exigem atenção adicional.

## Como verificar
Compare `ffprobe -show_format -show_streams` de cada segmento, examine os pacotes próximo às junções e procure warning do demuxer. Valide áudio e vídeo com reprodução e teste a duração total contra a lista.

## Conexões
- [[ffmpeg-map-filtergraph-stream-labels]] — FFmpeg: mapear streams de entrada e saídas rotuladas.
- [[ffmpeg-concat-filter-timestamps-zero]] — FFmpeg concat filter: alinhar cada segmento e normalizar streams.

## Fontes
- [FFmpeg — concat demuxer format](https://ffmpeg.org/ffmpeg-formats.html#concat-1) — especifica formato da lista, compatibilidade e tratamento de duration no concat demuxer Consulta: 2026-10-04.
- [ffprobe documentation](https://ffmpeg.org/ffprobe.html) — descreve inspeção de formatos, streams, metadados e writers estruturados Consulta: 2026-10-04.
