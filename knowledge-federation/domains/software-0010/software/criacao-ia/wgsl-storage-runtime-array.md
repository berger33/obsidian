---
id: software.criacao_ia.tranche04.000314
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
fontes: ["https://www.w3.org/TR/WGSL/", "https://developer.mozilla.org/en-US/docs/Web/API/GPUBufferUsage"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WGSL: só o storage buffer aceita array de tamanho em tempo de execução

## Em uma frase
Para um array cujo comprimento é conhecido só no binding, declare o último membro da struct como array<T> no espaço storage — uniform rejeita isso por regra.

## Por que importa
Dados de instância (milhares de partículas, tiles, NPCs) não cabem no teto de uniform e não têm tamanho fixo. Um runtime-sized array resolve os dois; a restrição de posição (último membro) e o passo alinhado são o preço que o compilador cobra para não haver ambiguidade de layout.

## Como funciona
Modele a struct de buffer como { header: metadados fixos; itens: array<Item> }, crie o buffer com STORAGE | COPY_DST (adicione COPY_SRC para leitura de diagnóstico) e o layout com type:'storage' e access:'read'|'read_write'|'write' adequado. O passo de array<T> é o tamanho de T arredondado para seu alinhamento — para Item com vec3 dentro, calcule antes de escrever o upload. Acesso com índices limitados pelo comprimento real do buffer (a implementação não corta por você).

## Exemplo
Um sistema de partículas com contagem variável a cada frame usa um único storage buffer; o shader lê 'let count = dados.num_particles;' do header e itera 'dados.itens[i]', com i < count garantido no lado da CPU.

## Limites e trade-offs
read-only em estágio de fragment exige o binding correspondente no layout; write sem read funciona apenas em compute (ou onde permitido). stride de array com tipos de alinhamento 8 não sofre o piso 16 do uniform, mas herda a regra de arredondamento — e o upload CPU precisa replicá-la. Ler além do fim é comportamento indefinido que geralmente dá zero ou lixo, não exceção.

## Como verificar
Imprima via error scope a descrição rejeitada de um array runtime-sized em uniform. Compare o stride calculado à mão com o offset de dois itens escritos no buffer e lidos de volta via staging. Teste o caminho 'buffer menor que o iterado' para ver a falha que você quer prevenir.

## Conexões
- [[wgsl-alinhamento-uniform-cinco-regra]] — WGSL: o layout de uniform padroniza tudo em 16 bytes.
- [[wgsl-override-constantes-pipeline]] — WGSL: constantes overridables ajustam o pipeline sem recompilar o shader.

## Fontes
- [W3C — WGSL (especificação)](https://www.w3.org/TR/WGSL/) — define runtime-sized arrays e as restrições por espaço de armazenamento Consulta: 2026-10-04.
- [MDN — GPUBufferUsage](https://developer.mozilla.org/en-US/docs/Web/API/GPUBufferUsage) — lista as flags de uso de buffer exigidas pelo fluxo storage + cópias Consulta: 2026-10-04.
