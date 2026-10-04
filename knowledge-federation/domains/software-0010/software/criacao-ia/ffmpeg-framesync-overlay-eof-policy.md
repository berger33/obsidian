---
id: software.criacao_ia.tranche03.000269
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
fontes: ["https://ffmpeg.org/ffmpeg-filters.html#Options-for-filters-with-several-inputs-_0028framesync_0029", "https://ffmpeg.org/ffmpeg-filters.html#overlay"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# FFmpeg framesync: definir comportamento ao terminar uma entrada

## Em uma frase
Filtros com várias entradas sincronizam frames por timestamps e usam opções framesync para decidir o que acontece quando uma entrada termina.

## Por que importa
Uma composição com overlay pode continuar exibindo o último frame da camada sobreposta ou terminar quando o ramo curto acaba. Essa escolha muda a semântica do vídeo final e pode ser confundida com problema de duração de output.

## Como funciona
Inspecione opções comuns de framesync como `shortest`, `repeatlast` e `eof_action` na referência do filtro. `shortest` determina saída até a entrada mais curta; `repeatlast` controla repetição do último frame secundário; `eof_action` especifica ação em EOF. Ajuste a política para cada filtro e combine com duração do output quando necessário.

## Exemplo
Uma camada de títulos dura cinco segundos e o clipe de fundo dez. Para manter a composição apenas enquanto título existe, configure política de saída curta; para congelar último frame da camada de imagem, habilite repetição documentada. O teste compara fronteira no quinto segundo.

## Limites e trade-offs
Nomes e defaults podem variar por filtro e versão. Diferenças de timestamps ou time base afetam o momento que cada input é considerado encerrado; uma opção do framesync não corrige offsets de origem.

## Como verificar
Teste entradas de durações distintas, PTS deslocados e EOF normal ou prematuro. Observe `showinfo` em cada entrada e saída, e confira primeiro e último frame com `ffprobe` e reprodução.

## Conexões
- [[ffmpeg-filtergraph-escaping-niveis]] — FFmpeg filtergraph: separar escaping do filtro e da shell.
- [[ffprobe-json-inspecao-pipeline]] — ffprobe: produzir inventário estruturado para validar um pipeline.

## Fontes
- [FFmpeg — Framesync options](https://ffmpeg.org/ffmpeg-filters.html#Options-for-filters-with-several-inputs-_0028framesync_0029) — define shortest, repeatlast e eof_action para filtros multi-input Consulta: 2026-10-04.
- [FFmpeg — overlay filter](https://ffmpeg.org/ffmpeg-filters.html#overlay) — mostra uso das opções de sincronização no caso concreto do overlay Consulta: 2026-10-04.
