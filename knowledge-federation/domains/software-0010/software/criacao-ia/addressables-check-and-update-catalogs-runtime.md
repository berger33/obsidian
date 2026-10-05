---
id: software.criacao_ia.tranche05.000500
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/content-update-builds-check.html", "https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/ContentUpdateWorkflow.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Addressables: detectar atualizações e trocar catálogos no momento apropriado

## Em uma frase
`CheckForCatalogUpdates` identifica locators modificados e `UpdateCatalogs` aplica catálogos escolhidos ou todos os catálogos que precisam de atualização.

## Por que importa
Consultar catalog separado do boot permite informar tamanho/consentimento, coordenar atualização no menu e não interromper uma cena durante loads ativos.

## Como funciona
Inicialize Addressables, aguarde check, apresente resultado ao usuário ou atualize automaticamente e libere handles após ler status e locators; decida se deseja limpar cache antigo.

## Exemplo
No menu inicial, app checa atualizações, mostra aviso de conteúdo disponível, executa `UpdateCatalogs` com IDs selecionados e segue ao nível após conclusão.

## Limites e trade-offs
O retorno de check pode conter IDs de catálogo alterados; lista nula em `UpdateCatalogs` significa atualizar todos os catálogos pendentes. Defina política de falha e conectividade.

## Como verificar
Teste sem atualização, um catálogo e vários catálogos, falha de rede e update durante atividade; confira handle, cache opcional e consistência do load seguinte.

## Conexões
- [[addressables-content-only-update-build-state]] — Addressables: publicar conteúdo alterado com content update build e estado do release.

## Fontes
- [Unity Addressables 2.7.6 — Check for content updates](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/content-update-builds-check.html) — Mostra CheckForCatalogUpdates, lista de locators e chamada UpdateCatalogs. Consulta: 2026-10-04.
- [Unity Addressables 2.7.6 — Update builds workflow](https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/ContentUpdateWorkflow.html) — Relaciona catálogos runtime ao fluxo de publicação remota e ferramentas de update. Consulta: 2026-10-04.
