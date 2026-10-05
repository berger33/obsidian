---
id: software.criacao_ia.tranche05.000495
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/remote-content-predownload.html#monitor-download-progress", "https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/load-monitor-wait-operations.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Addressables: exibir progresso por bytes com GetDownloadStatus

## Em uma frase
`PercentComplete` acompanha a conclusão de suboperações, enquanto `GetDownloadStatus` estima progresso em relação ao tamanho total dos downloads.

## Por que importa
Uma operação composta pode ter poucas suboperações de tamanhos muito diferentes, tornando percentuais por quantidade enganadores para uma barra de download.

## Como funciona
Durante predownload, consulte `GetDownloadStatus().Percent` para mostrar bytes baixados em relação ao total; use `PercentComplete` somente se desejar refletir suboperações concluídas.

## Exemplo
Uma label cobre bundle grande e vários pequenos; UI calcula progresso com GetDownloadStatus e publica eventos em incrementos para evitar redesenhar a cada frame.

## Limites e trade-offs
Progresso de download não representa necessariamente todo trabalho de pós-processamento; no WebGL, estimativa de tamanho tem ressalva quando bundle já está em cache.

## Como verificar
Teste operação com um bundle grande e vários pequenos, compare os dois indicadores e confira comportamento em cache e WebGL quando aplicável.

## Conexões
- [[addressables-release-reference-count-memory]] — Addressables: equilibrar cada load com release e entender contagem de referências.
- [[addressables-predownload-dependencies-consent]] — Addressables: medir e pré-baixar dependências antes de entrar no fluxo de jogo.

## Fontes
- [Unity Addressables 2.7.6 — Pre-download remote content](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/remote-content-predownload.html#monitor-download-progress) — Compara PercentComplete e GetDownloadStatus e mostra eventos de progresso. Consulta: 2026-10-04.
- [Unity Addressables 2.7.6 — Async load monitoring](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/load-monitor-wait-operations.html) — Documenta métodos de monitoramento de progresso de operações e downloads. Consulta: 2026-10-04.
