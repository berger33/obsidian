---
id: software.criacao_ia.tranche04.000315
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/GPUProgrammableStage", "https://www.w3.org/TR/WGSL/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WGSL: constantes overridables ajustam o pipeline sem recompilar o shader

## Em uma frase
Um módulo pode declarar @override constantes cujo valor o pipeline de render substitui na criação, sem editar o código-fonte do shader.

## Por que importa
Variantes de qualidade (número de passos de um loop, tamanho de bloco, habilitar um efeito) sem override viram uma explosão de pipelines por combinação de texto-fonte. With overridables, o mesmo módulo atende dezenas de configurações e o sistema de cache vê menos artefatos.

## Como funciona
Declare no módulo uma constante de sobrecarga de pipeline, por exemplo 'override samples : i32 = 4;', e passe o mapa de valores no estágio correspondente via GPUProgrammableStage.constants na criação do pipeline. O compilador trata o valor substituído como constante: loops e condições dependentes dele são otimizados no pipeline resultante. Constantes sem override são puramente locais; para identificá-las na API, a especificação permite atribuir @id.

## Exemplo
O material de sombra expõe 'override shadow_steps:i32'; qualidade baixa cria o pipeline com constants {shadow_steps: 2}, alta com 8, ambos do mesmo shader module cacheado.

## Limites e trade-offs
O valor entra na criação do pipeline — mudar é recriar o pipeline, não um set barato por frame. Nem toda plataforma trata todo tipo/expressão de override igualmente; em caso de loop condicionalmente pesado, confirme empiricamente a otimização por driver. Constantes de módulo sem @id não são endereçáveis pela API.

## Como verificar
Crie dois pipelines com valores diferentes e confirme visualmente que o número de passos mudou (um buffer de depuração que soma as iterações conta isso melhor que o olho). Teste a criação com valor inválido (tipo errado) e espere a falha de validação documentada. Compare métricas de compilação entre variante por texto e por override.

## Conexões
- [[wgsl-storage-runtime-array]] — WGSL: só o storage buffer aceita array de tamanho em tempo de execução.
- [[wgsl-atomicos-compare-loop]] — WGSL: atômicos só em memória de escrita explícita, e CAS é loop manual.

## Fontes
- [MDN — GPUProgrammableStage](https://developer.mozilla.org/en-US/docs/Web/API/GPUProgrammableStage) — documenta o dicionário constants do estágio do pipeline Consulta: 2026-10-04.
- [W3C — WGSL (especificação)](https://www.w3.org/TR/WGSL/) — define constantes overridables, tipos aceitos e @id Consulta: 2026-10-04.
