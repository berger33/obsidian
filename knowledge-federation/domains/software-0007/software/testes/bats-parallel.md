---
id: software.testes.tranche22.001567
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://bats-core.readthedocs.io/en/latest/usage.html", "https://bats-core.readthedocs.io/en/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# bats-core: --jobs com GNU parallel

## Em uma frase
Por padrão o Bats executa tudo serialmente, mas aceita paralelismo com -j/--jobs quando há GNU parallel (ou substituto compatível) instalado, acelerando suítes cujo gargalo é o custo de processo por teste.

## Por que importa
Cada teste já roda em processo próprio por isolamento, então a estrutura suporta a concorrência sem redesign — o ganho aparece justamente em arquivos com muitos casos curtos.

## Como funciona
bats --jobs 4 testes/ distribui os arquivos e os casos entre workers; --no-parallelize-across-files e --no-parallelize-within-files reprimem cada um dos dois eixos separadamente.

## Exemplo
Uma suíte de 200 casos de CLI cai de vários minutos para o tempo do gargalo de E/S quando paralelizada em quatro jobs.

## Limites e trade-offs
A ordem dos testes paralelos não é garantida; a documentação recomenda rodar várias vezes ao ativar --jobs para caçar dependências entre testes e comportamento não determinístico.

## Como verificar
Alterne dois runs com --jobs 8 num mesmo dataset e compare as saídas; qualquer diferença de resultado denuncia estado compartilhado.

## Conexões
- [[bats-focus-mode]] — Veja também: bats-core: o que fica marcado roda sozinho.
- [[bats-formatters]] — Veja também: bats-core: pretty, TAP, tap13 e JUnit.

## Fontes
- [Bats-core — Usage](https://bats-core.readthedocs.io/en/latest/usage.html) — opções do CLI, formatters, relatórios e execução paralela; consultado em 2026-10-03.
- [Bats-core — Documentação oficial (página inicial)](https://bats-core.readthedocs.io/en/latest/index.html) — índice: tutorial, instalação, usage, gotchas e FAQ; consultado em 2026-10-03.
