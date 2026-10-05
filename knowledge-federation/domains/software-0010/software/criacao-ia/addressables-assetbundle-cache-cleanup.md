---
id: software.criacao_ia.tranche05.000498
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/remote-content-assetbundle-cache.html", "https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/memory-assets.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Addressables: diferenciar cache remoto em disco de memória e limpar bundles órfãos

## Em uma frase
AssetBundles remotos são armazenados em cache por padrão depois do download, e bundles sem referência no catálogo atualizado podem ocupar espaço local.

## Por que importa
Memória de assets carregados e cache persistente de bundles são problemas diferentes; limpar um não equivale a liberar handles do runtime.

## Como funciona
Use `Addressables.CleanBundleCache` para remover entradas que nenhum catálogo atual referencia, ou `Caching.ClearCache` apenas quando a política exigir limpar o cache inteiro.

## Exemplo
Após atualizar catálogo, o jogo limpa bundles órfãos antigos por política de armazenamento enquanto mantém bundles ainda referenciados para evitar novo download.

## Limites e trade-offs
Sem cache habilitado, bundles remotos ficam em memória até unload ou encerramento e podem ser baixados de novo no próximo load; WebGL tem particularidades de cache.

## Como verificar
Atualize catálogo com bundle removido, observe tamanho/cache antes e depois da limpeza e confirme que conteúdo referenciado ainda carrega sem download redundante.

## Conexões
- [[addressables-profiles-build-load-paths]] — Addressables: usar Profiles para alternar caminhos de build e load por ambiente.
- [[addressables-content-only-update-build-state]] — Addressables: publicar conteúdo alterado com content update build e estado do release.

## Fontes
- [Unity Addressables 2.7.6 — Remote AssetBundle caching](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/remote-content-assetbundle-cache.html) — Documenta cache padrão, Caching.ClearCache, CleanBundleCache e opção por grupo. Consulta: 2026-10-04.
- [Unity Addressables 2.7.6 — Memory management](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/memory-assets.html) — Separa referências de assets/bundles em memória de outros aspectos de lifecycle. Consulta: 2026-10-04.
