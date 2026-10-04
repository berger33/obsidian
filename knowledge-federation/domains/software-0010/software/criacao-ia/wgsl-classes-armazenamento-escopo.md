---
id: software.criacao_ia.tranche04.000311
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
fontes: ["https://www.w3.org/TR/WGSL/#address-spaces", "https://www.w3.org/TR/WGSL/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WGSL: escolher a classe de armazenamento pelo tempo de vida

## Em uma frase
Cada variável WGSL vive numa classe — function, private, workgroup, storage, uniform — que determina escopo, persistência e quem pode escrevê-la.

## Por que importa
Confundir classes gera dois erros caros: estado que deveria durar entre invocações de um mesmo workgroup posto em 'function' (some a cada invocação), e dados por-thread globais postos em 'private' quando poderiam ser parâmetros locais. A escolha também define quais operações atômicas e de sincronização são válidas.

## Como funciona
Use function para temporários; private para estado por-invocação acessível a funções auxiliares (não compartilha nada entre threads); workgroup para memória compartilhada dentro de um workgroup, visível após barrier(); storage para buffers grandes lidos/escritos por compute e legíveis como read-only em estágios de render; uniform para dados por-dispatch pequenos e de acesso rápido. O modo de acesso (read, read_write, write) é declarado junto e é contrato, não sugestão.

## Exemplo
Uma redução por workgroup acumula parciais em 'var<workgroup> shared: array<f32, 64>;', faz barrier() entre fases e só o thread 0 grava o resultado no storage buffer de saída — colocar o acumulador em private duplicaria por thread e perderia a fase.

## Limites e trade-offs
workgroup tem orçamento pequeno (o limite maxComputeWorkgroupStorageSize vale por default 16 KiB, e é negociável pelo seu limite); uniform tem teto bem menor que storage (64 KiB por binding no valor-padrão de limite). classes read_write em storage só com uso STORAGE_BINDING e visibilidade de compute (ou fragment onde o formato permitir).

## Como verificar
Troque workgroup por private num exemplo de redução e observe o resultado errado antes do barrier; é a prova viva do escopo. Compile com o modo de acesso violado (escrever em uniform) e confirme o erro de validação do compilador. Rode um caso que estoura o orçamento de workgroup e confirme a falha de criação do pipeline.

## Conexões
- [[wgsl-binding-layout-visibilidade]] — WGSL: pares @group/@binding são contrato com o layout do pipeline.

## Fontes
- [W3C — WGSL: endereços e classes](https://www.w3.org/TR/WGSL/#address-spaces) — seção normativa sobre address spaces e suas semânticas Consulta: 2026-10-04.
- [W3C — WGSL (especificação)](https://www.w3.org/TR/WGSL/) — texto completo do módulo, incluindo regras de acesso e visibilidade Consulta: 2026-10-04.
