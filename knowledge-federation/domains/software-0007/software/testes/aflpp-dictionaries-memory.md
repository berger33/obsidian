---
id: software.testes.tranche23.001718
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md", "https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Dicionários automáticos e o limite de memória que ninguém configura

## Em uma frase
A doc de dicionários do guia começa pela pergunta "já existe?" — o diretório dictionaries/ do repositório cobre formatos conhecidos e entra via -x dictionaries/FORMAT.dict; mas o AFL++ também gera dicionário sozinho: com afl-clang-lto é autodictionary sem esforço nenhum, com afl-clang-fast usa-se AFL_LLVM_DICT2FILE=/caminho/novo.dic na compilação (mais AFL_LLVM_DICT2FILE_NO_MAIN=1 para ignorar parsing de argv, "often a good idea"), e a alternativa offline é o utils/libtokencap capturando tokens durante uma execução independente — ou escrever o .dic à mão.

## Por que importa
Dicionário é a diferença entre o mutator descobrir "GET " byte a byte e injetá-lo como token: para sintaxes verbosas — o quick start do README já mandava criar dicionário "when fuzzing verbose syntax (SQL, HTTP, etc.)" — o auto-dict barateia o que antes era curadoria.

## Como funciona
Na mesma seção de execução, o guia grava o limite de memória: -m em MB, "highly recommended", com dupla razão — evitar OOM na máquina e expor ausência de tratamento de malloc failure no alvo — e o conselho prático de subir de um valor pequeno até o dobro/quádruplo do que funciona com as seeds; sem limite, o afl-fuzz não enforce nada e o sistema pode estourar.

## Exemplo
Rode uma campanha com e sem -x contra um alvo HTTP: o tempo até primeiro request válido despenca com dicionário; depois repita com -m 256 e veja o log separar os casos de estouro como crash de meta-alvo em vez de hang.

## Limites e trade-offs
O DICT2FILE só existe nos modos LLVM (fast/lto) — quem instrumenta em GCC_PLUGIN fica no dicionário manual ou libtokencap; e o autodictionary do LTO não é qualidade garantida, apenas o caminho de menor atrito documentado.

## Como verificar
Abra a lista de opções de dicionário na seção 3a e o parágrafo do -m na seção 3b do fuzzing_in_depth; confirme a frase do quick start sobre SQL e HTTP no README.

## Conexões
- [[aflpp-run-basics]] — Veja também: Executando afl-fuzz: system-config, -i/-o, @@ e resume por traço.
- [[aflpp-parallel-campaign]] — Veja também: Campanha paralela: um -M main, N -S variantes e o mesmo -o.

## Fontes
- [AFL++ — Fuzzing in depth (guia oficial)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/docs/fuzzing_in_depth.md) — riscos, compiladores, sanitizers, corpus, execução, dicionários e paralelismo; consultado em 2026-10-03.
- [AFL++ — README oficial (stable)](https://github.com/AFLplusplus/AFLplusplus/blob/stable/README.md) — versão 5.03c, licenças, quick start, Docker e branches; consultado em 2026-10-03.
