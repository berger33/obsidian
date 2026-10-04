---
id: software.criacao_ia.tranche04.000338
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/blob-assets-intro.html", "https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/programming-entities.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Entities: Blob assets são o lado imutável do dado, não JSON serializado

## Em uma frase
Blob assets armazenam dados imutáveis binariamente compactados com acesso zero-overhead, e o manual os trata como a via canônica para lookup-tables e configuração do mundo ECS.

## Por que importa
Dados estáticos em componentes viram cópias por entidade (memória) ou consultas string-based (CPU); o modelo blob inverte: um bloco único por valor, referenciado por handle. A própria página do manual é taxonômica ('Store immutable data with blob assets') — a regra de ouro do DOTS é que mutável é componente, imutável é blob.

## Como funciona
A construção passa por um BlobAssetBuilder durante o baking/conversion (ou runtime, com o construtor equivalente), produzindo o BlobAssetReference<T> que os jobs e o main thread leem via Value sem cópia. Estruturas suportadas são as de layout previsível (números, vetores, arrays de tamanho em build, sub-blobs); geradores e 'shared statics' têm suas próprias armadilhas de atualização. O caso canônico das amostras — tabela de atributos por tipo de inimigo referenciada por todas as entidades do tipo — é literalmente por que o tipo existe.

## Exemplo
O Baker de 'EnemyAuthoring' resolve o preset de stats uma vez por tipo e grava um BlobAssetReference<EnemyStats> no componente; o IJobEntity de IA lê 'stats.Value.DetectionRadius' sem dicionário, sem string, sem copy por linha.

## Limites e trade-offs
Imutável significa imutável: alterar um blob exige reconstruir (e o handle muda). Dados com mutação frequente em blob é o anti-padrão que o manual desenha por omissão. O formato binário não é o lugar de compatibilidade de save-game sem versionamento — é cache de build, não arquivo de persistência.

## Como verificar
Um teste de Editor que faz rebuild do baking e assera que handles de blobs estáveis reusam (sem duplicação de assets). Compare a memória dos componentes com 'tabela inline' antes e depois da migração para blob — é o argumento do manual mensurável. Adicione um mutador indevido no construtor e confirme que a API recusa.

## Conexões
- [[unity-refrw-invalidacao-apos-estrutural]] — Unity Entities: RefRW/RefRO são handles com verificação, não ponteiros para sempre.
- [[unity-aspects-limpeza-de-assinatura]] — Unity Entities: RefAspect limpa a assinatura do sistema, não o armazenamento.

## Fontes
- [Unity Entities @1.4 — Blob assets](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/blob-assets-intro.html) — página oficial 'Store immutable data with blob assets' e o escopo do recurso Consulta: 2026-10-04.
- [Unity Entities @1.4 — Programming in Entities](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/programming-entities.html) — enquadra blob assets entre as formas organizadas de dados de projeto Consulta: 2026-10-04.
