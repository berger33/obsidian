---
id: software.criacao_ia.tranche05.000499
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/content-update-builds-overview.html", "https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/builds-update-build.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Addressables: publicar conteúdo alterado com content update build e estado do release

## Em uma frase
Um content update build pode distribuir conteúdo Addressable alterado sem reconstruir todo o Player, desde que use estado da publicação original.

## Por que importa
Reenviar todos os bundles remotos após uma pequena mudança pode consumir tempo e banda, além de forçar atualização do app quando somente assets mudaram.

## Como funciona
Guarde `addressables_content_state.bin` produzido para cada release e plataforma, execute Check Content Update Restrictions e gere atualização a partir do estado da build originalmente publicada.

## Exemplo
Uma equipe corrige textura num capítulo, constrói bundles de atualização usando o arquivo de estado do release e publica catálogo e bundles alterados no CDN.

## Limites e trade-offs
Bundles não carregam alterações de código, e nem toda plataforma suporta distribuição remota; a Unity alerta para não alterar build scripts entre build completa e atualização.

## Como verificar
Em player instalado, aplique update catalog, confira asset novo e conteúdo não alterado, compare bytes baixados e valide que arquivo de estado pertence ao mesmo release/plataforma.

## Conexões
- [[addressables-assetbundle-cache-cleanup]] — Addressables: diferenciar cache remoto em disco de memória e limpar bundles órfãos.
- [[addressables-check-and-update-catalogs-runtime]] — Addressables: detectar atualizações e trocar catálogos no momento apropriado.

## Fontes
- [Unity Addressables 2.7.6 — Introduction to update builds](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/content-update-builds-overview.html) — Define content-only workflow, estado de build obrigatório e limitações a assets. Consulta: 2026-10-04.
- [Unity Addressables 2.7.6 — Create an update build](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/builds-update-build.html) — Detalha ferramenta e restrições para construir atualização baseada em release anterior. Consulta: 2026-10-04.
