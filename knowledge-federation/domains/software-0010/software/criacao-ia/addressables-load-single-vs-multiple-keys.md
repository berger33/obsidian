---
id: software.criacao_ia.tranche05.000491
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/load-assets.html", "https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/load-assets-location.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Addressables: escolher LoadAssetAsync ou LoadAssetsAsync conforme o número de resultados

## Em uma frase
`LoadAssetAsync` retorna um único asset mesmo quando uma chave corresponde a vários, enquanto `LoadAssetsAsync` carrega um conjunto com regras de combinação explícitas.

## Por que importa
Usar um label coletivo com API singular pode selecionar apenas um resultado, e combinar labels sem definir união ou interseção pode carregar coleção errada.

## Como funciona
Use `LoadAssetAsync<T>` para uma chave que identifica um asset, `LoadAssetsAsync<T>` para conjunto, e configure `MergeMode.Union`, `Intersection` ou `UseFirst` quando passar múltiplas chaves.

## Exemplo
Uma tela carrega prefab único pelo address; uma cena carrega personagens e animais por labels com `Union` e trata falhas do grupo conforme a operação.

## Limites e trade-offs
O resultado individual de uma chave não promete qual asset de múltiplos correspondentes será o primeiro; dependências ainda são resolvidas pelo sistema Addressables.

## Como verificar
Crie duas entradas com o mesmo label, teste API singular e plural, e valide coleção e comportamento para cada modo de merge.

## Conexões
- [[addressables-assetreference-explicit-load-release]] — Addressables: tratar AssetReference como referência serializada, não como carregamento automático.

## Fontes
- [Unity Addressables 2.7.6 — Load assets](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/load-assets.html) — Distingue carregamento singular e em lote, limita chave múltipla e lista merge modes. Consulta: 2026-10-04.
- [Unity Addressables 2.7.6 — Load assets by location](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/load-assets-location.html) — Explica resolução de endereços, labels e resource locations antes do carregamento. Consulta: 2026-10-04.
