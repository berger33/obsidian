---
id: software.testes.tranche23.001752
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
fontes: ["https://github.com/google/atheris/blob/master/README.md", "https://docs.python.org/3/library/sys.html#sys.argv"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# O harness de cinco linhas e o que conta como crash

## Em uma frase
O exemplo oficial é o esqueleto completo: importar atheris, abrir um bloco with atheris.instrument_imports(): importando a lib sob teste, definir TestOneInput(data) que chama a função de parsing, e fechar com atheris.Setup(sys.argv, TestOneInput) mais atheris.Fuzz() — quatro peças e nada além delas.

## Por que importa
A definição do que falha é o contrato que assusta quem vem de testes clássicos: "When fuzzing Python, Atheris will report a failure if the Python code under test throws an uncaught exception" — ou seja, qualquer exceção vazada é crash reportado, sem asserção escrita, porque a premissa do fuzzing é que o código não deve quebrar em formato nenhum.

## Como funciona
A ordem Setup-antes-de-Fuzz é obrigatória e documentada, e a separação dos dois calls existe por um motivo funcional declarado: o libFuzzer consome os seus args da argv primeiro, deixando você reler os restantes antes de outra inicialização sua.

## Exemplo
Envolva um parser de formato textual seu com o esqueleto e deixe rodar um minuto; um ValueError não tratado do parser aparece no log como Uncaught Python exception com traceback, exatamente o formato que a página mostra.

## Limites e trade-offs
Tratar exceções dentro do TestOneInput — o catch-all tentador — desliga o oráculo; a página demonstra o raise explícito (RuntimeError Boom) como alvo a alcançar, então a política de quais exceções são falhas precisa ser intencional, não acidental.

## Como verificar
Copie o bloco de código da seção Using Atheris/Example do README oficial e confirme as cinco linhas, a frase da exceção não capturada e a nota de ordem da seção API.

## Conexões
- [[atheris-install-platform]] — Veja também: Instalação: pip com libFuzzer embutido, LLVM novo quando há nativo.
- [[atheris-instrumentation-modes]] — Veja também: Três granularidades de instrumentação — e as pegadinhas de cada uma.

## Fontes
- [Atheris — README oficial](https://github.com/google/atheris/blob/master/README.md) — definição, instalação, instrumentação, API e mutators custom; consultado em 2026-10-03.
- [Python — sys.argv (docs oficiais)](https://docs.python.org/3/library/sys.html#sys.argv) — lista de argumentos de processo que o Setup do Atheris consome; consultado em 2026-10-03.
