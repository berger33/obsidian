---
id: software.criacao_ia.tranche05.000497
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/remote-content-profiles.html", "https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/profiles-build-load-paths.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Addressables: usar Profiles para alternar caminhos de build e load por ambiente

## Em uma frase
Profiles definem variáveis utilizadas pelos grupos Addressables para escolher onde conteúdo é construído e de onde é carregado.

## Por que importa
Construções locais, staging e CDN de produção precisam apontar para destinos diferentes sem editar manualmente cada grupo antes de cada build.

## Como funciona
Defina variáveis de caminho no profile, associe cada grupo a pares Build and Load Paths e selecione profile de ambiente antes de gerar o conteúdo.

## Exemplo
O profile de teste usa Built-In para conteúdo remoto em desenvolvimento; o profile staging usa URL de host de equipe e produção usa variável do CDN.

## Limites e trade-offs
O path preview é calculado pelo profile ativo; URLs complexas ou dinâmicas podem exigir variáveis estáticas ou transformação de InternalId em vez de texto fixo.

## Como verificar
Construa com cada profile e confira catalog, path preview, URL resultante e acesso pelo player correspondente antes de publicar bundles.

## Conexões
- [[addressables-predownload-dependencies-consent]] — Addressables: medir e pré-baixar dependências antes de entrar no fluxo de jogo.
- [[addressables-assetbundle-cache-cleanup]] — Addressables: diferenciar cache remoto em disco de memória e limpar bundles órfãos.

## Fontes
- [Unity Addressables 2.7.6 — Remote content profiles](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/remote-content-profiles.html) — Descreve variáveis de profiles para caminhos local/remoto e cenários de CDN. Consulta: 2026-10-04.
- [Unity Addressables 2.7.6 — Set a build and load path](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/profiles-build-load-paths.html) — Explica associar variável de profile às configurações de build e load de grupo. Consulta: 2026-10-04.
