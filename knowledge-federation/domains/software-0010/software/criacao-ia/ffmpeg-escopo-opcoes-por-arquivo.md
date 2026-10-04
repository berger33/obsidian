---
id: software.criacao_ia.tranche03.000261
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
fontes: ["https://ffmpeg.org/ffmpeg.html", "https://ffmpeg.org/ffmpeg-utils.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# FFmpeg: posicionar opções no input ou output correto

## Em uma frase
A maioria das opções de arquivo FFmpeg aplica-se ao próximo input ou output e é reiniciada entre arquivos.

## Por que importa
Uma flag tecnicamente válida pode parecer ignorada quando aparece após o nome de arquivo errado. Com vários inputs e outputs, reordenar um argumento pode mudar decodificação, time base, codec ou container de um arquivo diferente sem produzir erro de sintaxe.

## Como funciona
Leia a linha de comando como uma sequência de escopos. Opções de input aparecem antes do `-i` correspondente; opções de output aparecem entre os inputs e o caminho do output que devem configurar. Opções globais são exceção e pertencem ao processo. Repita uma opção quando vários arquivos precisam do mesmo comportamento e mantenha inputs agrupados antes dos outputs.

## Exemplo
Para interpretar um arquivo raw a 1 fps e produzir H.264 a 24 fps, coloque a taxa de input antes de `-i` e a taxa de output depois dele. Em dois outputs com codecs distintos, defina cada `-c:v` no bloco que precede seu próprio nome de arquivo.

## Limites e trade-offs
Algumas opções são globais, por stream ou específicas de demuxer/muxer, e stream specifiers podem refinar o alvo. A regra de posição ajuda a reconhecer escopo, mas não substitui a referência da opção individual.

## Como verificar
Use `ffmpeg -h` para consultar opção por componente, examine log de input e stream mapping e teste configurações em um input mínimo. Reordene deliberadamente uma opção em teste para confirmar qual arquivo passa a receber seu efeito.

## Conexões
- [[ffmpeg-map-filtergraph-stream-labels]] — FFmpeg: mapear streams de entrada e saídas rotuladas.

## Fontes
- [FFmpeg — Main documentation](https://ffmpeg.org/ffmpeg.html) — define ordem das opções de arquivo, reset entre arquivos e exemplos de input/output Consulta: 2026-10-04.
- [FFmpeg — Utilities syntax](https://ffmpeg.org/ffmpeg-utils.html) — documenta sintaxe e parsing de argumentos usados pelos utilitários FFmpeg Consulta: 2026-10-04.
