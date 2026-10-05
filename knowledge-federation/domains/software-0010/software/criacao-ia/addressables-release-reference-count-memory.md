---
id: software.criacao_ia.tranche05.000494
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/memory-assets.html", "https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/AddressableAssetsAsyncOperationHandle.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Addressables: equilibrar cada load com release e entender contagem de referências

## Em uma frase
Addressables mantém contagem de referências para assets e AssetBundles, então cada carregamento explícito precisa de release quando o consumidor termina.

## Por que importa
Uma referência esquecida mantém assets e dependências elegíveis para uso e pode parecer vazamento de memória mesmo quando objetos já saíram da cena.

## Como funciona
Associe handle ao dono do load, solte handle ou asset ao encerrar escopo e use profiler para verificar dependências e AssetBundle que ainda têm contagem positiva.

## Exemplo
A cena retém handles de modelos durante gameplay e os libera na saída; uma dependência compartilhada fica carregada até a última referência ser liberada.

## Limites e trade-offs
Release não significa que bytes desaparecem imediatamente: bundle compartilhado não pode descarregar apenas parte dos assets e pode continuar em memória até zerar sua referência.

## Como verificar
Carregue dois assets do mesmo bundle, libere um e depois o outro e observe no Addressables Profiler quando asset e bundle ficam descarregados.

## Conexões
- [[addressables-async-operation-handles]] — Addressables: aguardar operações assíncronas pelo handle sem bloquear a thread.
- [[addressables-download-progress-bytes]] — Addressables: exibir progresso por bytes com GetDownloadStatus.

## Fontes
- [Unity Addressables 2.7.6 — Memory management](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/memory-assets.html) — Explica refcounts, pares load/release, bundles compartilhados e asset churn. Consulta: 2026-10-04.
- [Unity Addressables 2.7.6 — AsyncOperationHandle release](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/AddressableAssetsAsyncOperationHandle.html) — Define duração necessária do handle e efeito de release sobre assets e operação. Consulta: 2026-10-04.
