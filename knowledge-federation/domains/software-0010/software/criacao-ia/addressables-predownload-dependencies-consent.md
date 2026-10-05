---
id: software.criacao_ia.tranche05.000496
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/remote-content-predownload.html", "https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/load-assets.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Addressables: medir e pré-baixar dependências antes de entrar no fluxo de jogo

## Em uma frase
`GetDownloadSizeAsync` informa quantos bytes ainda precisam ser obtidos e `DownloadDependenciesAsync` baixa bundles de um endereço ou label antecipadamente.

## Por que importa
Pré-baixar um capítulo ou conjunto de assets em menu ou onboarding evita interromper gameplay para esperar rede e permite pedir consentimento informado.

## Como funciona
Consulte tamanho, apresente estimativa ao usuário se apropriado, baixe dependências com handle, acompanhe status e libere o handle de download ao concluir.

## Exemplo
Antes de carregar nível, o jogo calcula tamanho da label `chapter-2`, pede confirmação em rede móvel e baixa dependências para cache se o jogador aceitar.

## Limites e trade-offs
Tamanho zero normalmente indica conteúdo necessário já em cache; download prévio não substitui load do asset quando a aplicação realmente precisa instanciá-lo.

## Como verificar
Teste primeira instalação, cache existente, rede interrompida e recusa do consentimento; confira que o nível não começa até dependências exigidas estarem prontas.

## Conexões
- [[addressables-download-progress-bytes]] — Addressables: exibir progresso por bytes com GetDownloadStatus.
- [[addressables-profiles-build-load-paths]] — Addressables: usar Profiles para alternar caminhos de build e load por ambiente.

## Fontes
- [Unity Addressables 2.7.6 — Pre-download remote content](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/remote-content-predownload.html) — Mostra GetDownloadSizeAsync, DownloadDependenciesAsync, handles e fluxo de consentimento. Consulta: 2026-10-04.
- [Unity Addressables 2.7.6 — Load assets](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/load-assets.html) — Distingue operação de load do uso do asset e descreve carga assíncrona. Consulta: 2026-10-04.
