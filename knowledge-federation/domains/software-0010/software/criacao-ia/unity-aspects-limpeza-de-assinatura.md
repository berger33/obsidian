---
id: software.criacao_ia.tranche04.000339
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/aspects-intro.html", "https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/programming-entities.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Entities: RefAspect limpa a assinatura do sistema, não o armazenamento

## Em uma frase
Um Aspect agrupa componentes em um único struct de acesso por entidade, trocando dez parâmetros de query por um tipo legível — sem tocar no layout chunk.

## Por que importa
A página do manual define ('Group together components in a single struct'); o ganho é de projeto, não de cache: queries longas viram assinatura de domínio, o acesso vira 'aspect.Position.Value' com regras de leitura/escrita declaradas por campo, e a mutação continua governada pelo safety system por componente — o Aspect não cria atomicidade, e quem assume isso cria um bug novo.

## Como funciona
Derive o Aspect dos componentes (com [ReadOnly]/mutabilidade por campo via SourceType), e o framework gera os getters/setters e a composição de query. Use nos três lados do padrão DOTS: IJobEntity, queries por sistema, e o main thread via SystemAPI. Para dados que não existem em toda entidade (componentes opcionais), a flag de tipo opcional na composição do Aspect evita o join implícito. O limite natural: Aspect não substitui a pergunta de layout — o armazenamento continua por arquétipo.

## Exemplo
O Aspect 'Mover' encapsula Position+Velocity+Mass; o sistema de física passa a ler 'for (var m in movers)' com mutação em Position declarada pelo Aspect, e o teste de unidade constrói o Aspect sem montar o mundo inteiro na mão.

## Limites e trade-offs
Não há transação entre os campos: um Aspect que escreve Position e falha no meio deixa o par inconsistente — igual a query múltipla, e pior se você esperava encapsulamento de consistência. Aspect com componentes faltantes em parte das entidades exige a variante opcional, que propaga null-checks para o laço. E cada abstração tem custo de build de código gerado em projeto grande — medir é do jogo.

## Como verificar
Compare duas versões do mesmo sistema (query longa vs. Aspect) no Profiler: a paridade é a prova de que o Aspect é sintaxe, não otimização. Um teste que escreve só o campo mutável (não os dois) documenta a ausência de atomicidade para o time. Verifique a query gerada no inspector de Entities para confirmar os componentes que entram no filtro.

## Conexões
- [[unity-blob-assets-imutavel-compacto]] — Unity Entities: Blob assets são o lado imutável do dado, não JSON serializado.
- [[unity-baking-ponteiro-cenario-para-ecs]] — Unity Entities: o baking é a fronteira de conversão cena↔ECS, e o runtime tem outra porta.

## Fontes
- [Unity Entities @1.4 — Aspect overview](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/aspects-intro.html) — página oficial que define o agrupamento de componentes em um struct Consulta: 2026-10-04.
- [Unity Entities @1.4 — Programming in Entities](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/programming-entities.html) — enquadra os mecanismos de iteração e acesso onde o Aspect opera Consulta: 2026-10-04.
