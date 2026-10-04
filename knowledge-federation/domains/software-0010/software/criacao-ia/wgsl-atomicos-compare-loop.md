---
id: software.criacao_ia.tranche04.000316
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
fontes: ["https://www.w3.org/TR/WGSL/", "https://www.w3.org/TR/webgpu/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WGSL: atômicos só em memória de escrita explícita, e CAS é loop manual

## Em uma frase
Tipos atomic<i32>/<u32> existem apenas em storage read_write e workgroup read_write, e a troca condicional do WGSL retorna um struct que exige retry manual.

## Por que importa
Contadores globais, free lists e filas de trabalho são o tecido de sistemas paralelos na GPU; escrever sem atomicidade produz resultados que flutuam entre frames e não reproduzem em log. A API WGSL deliberadamente não oferece CAS atômica de um passo — ignorar isso leva a algoritmos errados que parecem certos.

## Como funciona
Declare 'var<storage, read_write> counters : atomic<i32>;' e use atomicAdd/atomicLoad/atomicStore para operações diretas; para um padrão 'só o primeiro thread faz', faça loop: leia, teste, atomicCompareExchangeWeak(expected, desired) e repita enquanto o membro 'exchanged' do resultado for falso. Em workgroup, combine atômicos com barrier() quando outros threads dependerem do valor. Atômicos não têm tipo 64-bit portável na especificação atual e não existem em uniform.

## Exemplo
Um pass de alocação de worklist: cada thread em loop tenta 'atomicCompareExchangeWeak(0, meu_valor)' no slot; quem conseguir 'exchanged' publica e sai, os demais re-leem e saem, sem lock entre workgroups.

## Limites e trade-offs
CAS fraca é fraca: mesmo quando retorna exchanged=true num contexto ABA, algoritmos que dependem de versão precisam de palavras de etiqueta. A disponibilidade por estágio é limitada a compute (e fragment onde o formato read_write permite); não espere atômicos no vertex. O retry loop sem teto vira hang se a lógica de sucesso for incompatível com a semântica fraca.

## Como verificar
Rode um contador com 100 mil increments por thread via atomicAdd e compare com o valor esperado — a versão não-atômica erra e é seu teste de referência. Verifique a recusa de compilação de um atomic em read-only. Adicione um ABA sintético se o algoritmo usar CAS para decisão estrutural.

## Conexões
- [[wgsl-override-constantes-pipeline]] — WGSL: constantes overridables ajustam o pipeline sem recompilar o shader.
- [[wgsl-textura-amostragem-tipo-view]] — WGSL: amostrar uma textura exige ver o tipo certo, não só o binding.

## Fontes
- [W3C — WGSL (especificação)](https://www.w3.org/TR/WGSL/) — define os tipos atômicos, seus espaços de armazenamento permitidos e o struct de compare-exchange Consulta: 2026-10-04.
- [W3C — WebGPU](https://www.w3.org/TR/webgpu/) — a API irmã define STORAGE_BINDING com acesso write-only e o que o layout aceita Consulta: 2026-10-04.
