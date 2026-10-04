---
id: software.criacao_ia.tranche01.000071
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview", "https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal Sequencer: distinguir asset e actor

## Em uma frase

Level Sequence guarda dados de tracks e keyframes, enquanto Level Sequence Actor referencia a sequência no nível.

## Por que importa

Separar asset editável da instância de reprodução esclarece onde configurar conteúdo e como associá-lo à cena.

## Como funciona

Crie e salve a sequência no Content Browser, coloque ou localize o actor no level e confira qual asset está associado.

## Exemplo

Uma abertura de fase usa uma sequência compartilhada, ligada ao Level Sequence Actor da cena inicial.

## Limites e trade-offs

Abrir asset sem level que o referencia pode deixar bindings sem contexto, e nomes parecidos favorecem associação errada.

## Como verificar

Abra pela cena e pelo Content Browser, confira referências e confirme que personagens, câmera e props estão vinculados.

## Conexões
- [[blender-revisar-animacao-dentro-do-jogo]] — Blender: revisar animação dentro do jogo.
- [[unreal-sequencer-animar-com-tracks-e-keyframes]] — Unreal Sequencer: animar com tracks e keyframes.

## Fontes
- [Epic Games — Sequencer Overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-sequencer-movie-tool-overview) — Explica Level Sequence, Level Sequence Actor, tracks, keyframes e edição de cinematics. Consulta: 2026-10-04.
- [Epic Games — Movie Render Pipeline](https://dev.epicgames.com/documentation/en-us/unreal-engine/movie-render-pipeline-in-unreal-engine) — Documenta a renderização de cinematics pela Movie Render Queue e Movie Render Graph. Consulta: 2026-10-04.
