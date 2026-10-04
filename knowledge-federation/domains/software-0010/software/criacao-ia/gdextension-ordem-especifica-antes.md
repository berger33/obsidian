---
id: software.criacao_ia.tranche04.000357
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html", "https://docs.godotengine.org/en/stable/tutorials/export/feature_tags.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: no .gdextension, a linha mais específica precisa vir antes — o matching é sequencial

## Em uma frase
As entradas de [libraries] são avaliadas de cima para baixo e a primeira que fecha com as flags ativas vence; duas linhas compatíveis com o mesmo sistema exigem ordenação consciente.

## Por que importa
É a regra que resolve o conflito 'editor vs. jogador' na mesma plataforma: um editor build tem editor+debug+macos ativos, e a linha macos.debug pura também casa. Sem a ordenação, o carregamento escolhe a lib errada — a variante 'template_debug' em vez da 'editor', ou vice-versa — e a falha aparece como ausência de ClassDB registrations só dentro do editor.

## Como funciona
A doc demonstra com o par 'linux.release.editor.x86_64' (a variante com editor) listado antes de 'linux.release.x86_64' (a variante de runtime), com a instrução explícita: 'Entries are matched in order, so if two sets of feature tags could match the same system, be sure to put the more specific ones first'. Convenção de projeto: ordenar por número de flags, decrescente; manter editor×release×debug no topo; revisar a ordem sempre que um preset de export com flag customizada entrar no produto.

## Exemplo
O preset 'demo' exporta com a tag 'demo' e precisa de um stub nativo leve; a linha 'windows.release.demo' entra antes de 'windows.release.x86_64' para não ser engolida pela geral — exatamente o mecanismo das flags de export customizadas da linha anterior.

## Limites e trade-offs
A regra é de primeiro-match, não de melhor-match: reordenar por estética quebra o carregamento silenciosamente. Flags excludentes não existem (não há 'NOT editor') — especificidade só se expressa por mais linhas. E o debug do editor é coberto pelo fato de que builds de editor sempre trazem a flag debug; ordenar para 'editor' resolve a sobra.

## Como verificar
Inverta a ordem do par da doc num projeto de teste e observe qual lib carrega — é a demonstração da regra em duas linhas de diff. No seu produto, o teste real é o export com as duas variantes presentes: se o runtime não quebra por registrar classes em export de jogo, a ordem está certa.

## Conexões
- [[gdextension-libraries-feature-tags]] — Godot 4: a seção [libraries] é um filtro por feature flags, não uma lista de caminhos.
- [[gdextension-double-single-api-json]] — Godot 4: a extensão só carrega no build de motor com a mesma precisão de float.

## Fontes
- [Godot — The .gdextension file](https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html) — o exemplo 'put the more specific ones first' e os dois trechos de configuração que o acompanham Consulta: 2026-10-04.
- [Godot — Feature tags](https://docs.godotengine.org/en/stable/tutorials/export/feature_tags.html) — a fonte das flags (inclusive customizadas) que interagem com a regra de ordem Consulta: 2026-10-04.
