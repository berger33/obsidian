---
id: software.criacao_ia.tranche04.000336
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.entities@1.0/manual/concepts-safety.html", "https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/index.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Entities: iterar por chunk é o grão de leitura da arquitetura

## Em uma frase
O Entities guarda os dados em chunks de entidades de mesmo arquétipo, e o caminho de maior performance — do IJobChunk aos queries do framework — lê o chunk como unidade, não a entidade como objeto.

## Por que importa
A frase do manual de segurança é arquitetural: 'o Entities API guarda dados em chunks'. Quem pensa em entidades-objeto escreve acessos espalhados e perde a localidade que justifica a stack; quem pensa em colunas por chunk escreve loops de 'buffer[i]' contíguos que o Burst veta de SIMD a 90 graus. O modelo mental de grão é a diferença entre DOTS rápido e DOTS lento com o mesmo código.

## Como funciona
No IJobChunk, um 'ChunkRange' recebe os chunks do arquétipo; dentro dele, os NativeArray por componente têm comprimento igual a 'count' e índice 0..count-1 — o laço interno é sequencial. As APIs de mais alto (IJobEntity, SystemAPI, queries) geram o mesmo desenho sob o capô, o que explica o porquê de 'SharedComponent' quebrar o modelo (vai por outra via, com o EntityManager no caminho). A pergunta de performance por sistema: este dado pode ser lido com stride 1 dentro do chunk?

## Exemplo
Um sistema de 'scale por área' lê as colunas Position e ScaleType por chunk, aplica a transformação por índice e evita tocar em campos de 'entidade' como se fossem objetos — o diff de profile mostra a contiguidade pagando.

## Limites e trade-offs
Componentes habilitáveis/desabilitados por entidade criam máscaras que fragmentam o 'contíguo' — o custo aparece, não desaparece. Chunk ≠ cache guarantee: o tamanho de chunk, o número de componentes na query e os access patterns conjuntos ditam o que cabe. SharedComponents e ManagedComponents vivem fora do bloco e têm custo de acesso próprio (a restrição do IJobEntity é efeito disso).

## Como verificar
Compare no Profiler o mesmo cálculo por IJobChunk (lote por chunk) contra um foreach de 'EntityManager.GetComponentData' por entidade — a diferença é o argumento da página. Escreva um teste que valida soma coluna-por-coluna e confirme que a iteração interna não pula linhas (stride 1 visível em código).

## Conexões
- [[unity-parallelfor-indexo-proprio]] — Unity Jobs: em IJobParallelFor você escreve no seu índice e lê fora com intenção declarada.
- [[unity-refrw-invalidacao-apos-estrutural]] — Unity Entities: RefRW/RefRO são handles com verificação, não ponteiros para sempre.

## Fontes
- [Unity Entities @1.0 — Safety in Entities](https://docs.unity3d.com/Packages/com.unity.entities@1.0/manual/concepts-safety.html) — frase fundante sobre armazenamento em chunks e invalidação em mudanças estruturais Consulta: 2026-10-04.
- [Unity Entities @1.4 — Manual index](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/index.html) — porta de entrada do manual com a seção de conceitos de ECS e iteração Consulta: 2026-10-04.
