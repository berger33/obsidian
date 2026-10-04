---
id: software.testes.tranche21.001528
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/boxed/mutmut", "https://github.com/boxed/mutmut/blob/main/README.rst"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# mutmut: escolher linhas com cobertura ou glob

## Em uma frase
Os padrões only_mutate e do_not_mutate filtram arquivos por glob estilo Unix, e mutate_only_covered_lines troca o critério de funções chamadas por linhas cobertas pelo coverage.py.

## Por que importa
Mutar módulo gerado ou código defensivo sem teste é ruído garantido; filtrar a fonte é o ajuste fino entre custo e sinal.

## Como funciona
Restrinja a mutação às pastas de negócio e ligue a filtragem por cobertura quando quiser pular linhas jamais executadas.

## Exemplo
do_not_mutate= *__tests.py exclui os próprios arquivos de teste da mutação, e as mutações focam em src/api/*.

## Limites e trade-offs
A linha coberta por um teste fraco ainda é mutada e sobrevive — cobertura restringe o alvo, não garante a qualidade do caçador.

## Como verificar
Configure do_not_mutate com um glob válido, inclua um arquivo de teste, e confirme que ele sai da contagem.

## Conexões
- [[mutmut-copy-stack-depth]] — Veja também: mutmut: also_copy e profundidade máxima de pilha.
- [[mutmut-typecheck-debug]] — Veja também: mutmut: filtrar mutantes por tipos e ativar verbosidade.

## Fontes
- [mutmut — README oficial](https://github.com/boxed/mutmut) — instalação, browse, configuração e filtros; consultado em 2026-10-03.
- [mutmut — repositório oficial](https://github.com/boxed/mutmut/blob/main/README.rst) — material-fonte do README e das releases; consultado em 2026-10-03.
