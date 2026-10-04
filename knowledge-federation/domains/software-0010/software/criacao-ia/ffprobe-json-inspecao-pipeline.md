---
id: software.criacao_ia.tranche03.000270
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
fontes: ["https://ffmpeg.org/ffprobe.html", "https://ffmpeg.org/ffmpeg.html#Stream-specifiers"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ffprobe: produzir inventário estruturado para validar um pipeline

## Em uma frase
`ffprobe` inspeciona container, streams e pacotes e pode serializar seções de saída num writer JSON legível por máquina.

## Por que importa
Mensagens humanas variam com versões e não são um contrato robusto para scripts. Uma resposta estruturada permite verificar codec, duração, dimensões, idioma, índices e timestamps antes de transcodificar ou aprovar um artefato.

## Como funciona
Selecione explicitamente dados necessários com `-show_format`, `-show_streams`, `-show_packets` ou `-show_frames` e escolha `-of json`. Parseie tipos e campos opcionais sem pressupor que todo arquivo tenha mesmo número de streams ou todos os metadados. `-select_streams` e stream specifiers restringem consulta; código de saída indica falha de abertura ou reconhecimento.

## Exemplo
Um validador extrai video stream primária, codec, largura, altura, time base, duração e faixas de áudio. Compara com contrato do projeto e bloqueia concatenação se streams ou formatos divergem, preservando JSON de diagnóstico para cada input e output.

## Limites e trade-offs
ffprobe informa o que pode ler dos demuxers e metadados; duração pode ser estimada e campos podem faltar. JSON é estruturado mas seu schema efetivo acompanha versão e tipo do container, então consumidor precisa tolerar chaves opcionais e formatos numéricos documentados.

## Como verificar
Valide parser com vídeo sem áudio, múltiplas faixas, streams incompletas e arquivo corrompido. Compare sumário JSON com pacotes selecionados e revise stderr/código de saída para diferenciar arquivo inválido de campo ausente.

## Conexões
- [[ffmpeg-framesync-overlay-eof-policy]] — FFmpeg framesync: definir comportamento ao terminar uma entrada.

## Fontes
- [ffprobe Documentation](https://ffmpeg.org/ffprobe.html) — define opções de seleção, sections e JSON writer para saída automatizada Consulta: 2026-10-04.
- [FFmpeg — Stream specifiers](https://ffmpeg.org/ffmpeg.html#Stream-specifiers) — documenta seleção de streams por índice, tipo, programa e metadata Consulta: 2026-10-04.
