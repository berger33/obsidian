---
id: software.criacao_ia.tranche04.000312
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
fontes: ["https://www.w3.org/TR/WGSL/", "https://developer.mozilla.org/en-US/docs/Web/API/GPUBindGroup"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WGSL: pares @group/@binding são contrato com o layout do pipeline

## Em uma frase
Todo recurso externamente ligado é identificado por @group(g) @binding(b), e o conjunto de declarações deve coincidir com o bind group layout na visibilidade e no tipo.

## Por que importa
A API de execução não resolve nomes — resolve posições. Se o shader declara um binding em visibility vertex mas o layout diz fragment, a compatibilidade de pipeline falha; se a ordem muda, recursos inteiros são lidos do slot errado silenciosamente em implementações que só validam parte disso.

## Como funciona
Escreva o shader como espelho do layout: para cada entry do GPUBindGroupLayoutDescriptor, uma declaração com mesmo group, binding e tipo (sampler, textura com viewSampleType compatível, buffer com access e tamanho mínimo). Mantenha convenções: group 0 global por-frame, group 1 por-material, group 2 por-objeto é um padrão comum, não normativa. Ao trocar o layout, regere os shaders — diff entre as listas de binding é revisão obrigatória.

## Exemplo
O uniform de câmera migra do binding 3 do group 0 para um novo group 0 binding 0 compartilhado com outro pass; os dois shaders que liam a matriz antiga precisam da nova dupla, e o layout do pipeline que os compõe ganha um entry deslocado.

## Limites e trade-offs
Duplicar o mesmo binding em dois shaders de um mesmo pipeline exige declarações idênticas; divergência mínima (um array sem tamanho vs. com) já é incompatibilidade. A visibilidade por estágio restringe onde o recurso é legível — declarar 'todos os estágios' é permissivo demais e pode custar otimizações de driver.

## Como verificar
Gere a lista de bindings do layout e do pré-processamento do shader por script e compare na CI (erro de compatibilidade vira falha de build, não de runtime). Inverta dois bindings num fixture e confirme que a criação do pipeline falha com error scope ativo.

## Conexões
- [[wgsl-classes-armazenamento-escopo]] — WGSL: escolher a classe de armazenamento pelo tempo de vida.
- [[wgsl-alinhamento-uniform-cinco-regra]] — WGSL: o layout de uniform padroniza tudo em 16 bytes.

## Fontes
- [W3C — WGSL (especificação)](https://www.w3.org/TR/WGSL/) — define a atribuição group/binding e o vínculo com o layout de binding Consulta: 2026-10-04.
- [MDN — GPUBindGroup](https://developer.mozilla.org/en-US/docs/Web/API/GPUBindGroup) — mostra o lado JS do contrato: entradas numeradas por binding dentro de um layout Consulta: 2026-10-04.
