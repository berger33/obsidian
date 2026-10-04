---
id: software.testes.tranche23.001753
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
fontes: ["https://github.com/google/atheris/blob/master/README.md", "https://docs.python.org/3/reference/import.html#the-module-cache"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Três granularidades de instrumentação — e as pegadinhas de cada uma

## Em uma frase
O README enumera as três formas de inserir a instrumentação de cobertura no bytecode: o bloco instrument_imports() (que propaga às libs importadas e às que estas importam), o decorator @atheris.instrument_func por função, e atheris.instrument_all(), que varre todo o interpretador e instrumenta toda função Python carregada — "put this right before atheris.Setup()", com o aviso de que "might take a while".

## Por que importa
Os modos cobrem três situações de código diferentes, e a página define os limites de cada um: instrument_imports não alcança módulos importados antes — nem os requisitos do próprio Atheris — porque Python importa cada módulo uma única vez; instrument_func instrumenta in-place, afetando todos os call points, mas não pode ser chamado em método bound (usa-se a versão unbound); e instrument_all é marcado experimental, sendo o único que alcança funções do núcleo do interpretador.

## Como funciona
A lista de nomes que a instrumentação não pega é auditável na prática da própria doc: print(sys.modules.keys()) mostra o que já foi importado e está fora do alcance do bloco com.

## Exemplo
Para um serviço legado com imports no topo do módulo, aceite instrument_all(); para um parser isolado, o bloco com importando só ele; meça o trade-off de start no seu caso, pois o README documenta o custo (varredura lenta, import único) sem números.

## Limites e trade-offs
"Instrumentar tudo" não é instrumentar melhor: a nota de que o all demora é o preço da varredura, e a página o posiciona como último recurso para o que os imports não alcançam — o comportamento em frameworks com import-lazy ou import hooks customizados não é discutido na página.

## Como verificar
Abra a subseção Python coverage do README oficial e confirme a numeração 3 dos modos, a frase do import único, o constraint do bound method e o print(sys.modules.keys()).

## Conexões
- [[atheris-minimal-harness]] — Veja também: O harness de cinco linhas e o que conta como crash.
- [[atheris-no-interesting]] — Veja também: "No interesting inputs were found": a porta de entrada mais comum.

## Fontes
- [Atheris — README oficial](https://github.com/google/atheris/blob/master/README.md) — definição, instalação, instrumentação, API e mutators custom; consultado em 2026-10-03.
- [Python — The import system (docs oficiais)](https://docs.python.org/3/reference/import.html#the-module-cache) — seção 5.3.1: sys.modules é o cache de módulos já importados; consultado em 2026-10-03.
