---
id: software.criacao_ia.tranche05.000492
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/load-assets.html#use-assetreferences", "https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/AssetReferences.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Addressables: tratar AssetReference como referência serializada, não como carregamento automático

## Em uma frase
Um campo `AssetReference` identifica asset Addressable, mas Unity não carrega nem libera o recurso automaticamente por guardar essa referência.

## Por que importa
Confundir referência no Inspector com asset já carregado pode gerar acesso prematuro, dependências sem lifecycle e recursos retidos após destruir o objeto.

## Como funciona
Declare AssetReference em MonoBehaviour ou ScriptableObject, inicie load via Addressables API no momento necessário e libere asset ou handle quando o consumidor encerrar seu uso.

## Exemplo
Um painel carrega prefab via `reference.LoadAssetAsync<GameObject>()`, instancia no callback de sucesso e executa `reference.ReleaseAsset()` quando a tela é destruída.

## Limites e trade-offs
Atribuir um asset não Addressable ao campo pode torná-lo Addressable e adicioná-lo ao grupo default; considere esse efeito ao editar o catálogo.

## Como verificar
Teste asset ausente e sucesso, acompanhe o handle no Addressables Profiler e confirme que release ocorre também ao cancelar ou encerrar o consumidor.

## Conexões
- [[addressables-load-single-vs-multiple-keys]] — Addressables: escolher LoadAssetAsync ou LoadAssetsAsync conforme o número de resultados.
- [[addressables-async-operation-handles]] — Addressables: aguardar operações assíncronas pelo handle sem bloquear a thread.

## Fontes
- [Unity Addressables 2.7.6 — Load assets](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/load-assets.html#use-assetreferences) — Mostra campo AssetReference, chamada explícita de load e release no ciclo de vida. Consulta: 2026-10-04.
- [Unity Addressables 2.7.6 — Asset references](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/AssetReferences.html) — Define usos da referência para restringir campos e acessar assets por referência ou labels. Consulta: 2026-10-04.
