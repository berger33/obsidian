---
id: software.testes.tranche23.001755
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
fontes: ["https://github.com/google/atheris/blob/master/README.md", "https://coverage.readthedocs.io/", "https://github.com/google/atheris/blob/master/native_extension_fuzzing.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Ver cobertura linha a linha com coverage.py e -atheris_runs

## Em uma frase
A página documenta a compatibilidade com o coverage.py: roda-se o fuzzer sob python3 -m coverage run your_fuzzer.py -atheris_runs=10000, seguido de coverage html para gerar o relatório navegável — com a razão declarada: examinar quais linhas são executadas ajuda a entender a efetividade do fuzzer, no mesmo modelo visual usado para qualquer programa Python.

## Por que importa
O detalhe que separa relatório de silêncio é o contrato de exit: relatórios só saem em término gracioso — a contagem do -atheris_runs sendo alcançada, exceção Python, ou sys.exit() — e a página nomeia os dois assassinos do relatório: crash em código nativo e a flag -runs do libFuzzer (daí o -atheris_runs dedicado; em SIGINT o Atheris até tenta, mas pode não conseguir).

## Como funciona
Há também o recipe de replay de corpus da seção: rodar o fuzzer sobre os arquivos do diretório com -atheris_runs=$(( 1 + $(ls corpus_dir | wc -l) )) para reproduzir o corpus inteiro sob medição — com a nota de que o set vazio é sempre o primeiro input, mesmo sem arquivo vazio no corpus.

## Exemplo
Rode dez mil runs sob coverage, abra o HTML e confirme visualmente que as linhas do parser — não só o harness — aparecem coloridas; é o teste definitivo de que a instrumentação chegou onde deveria.

## Limites e trade-offs
A própria página crava o custo: coverage.py deixa o fuzzer "significantly" mais lento — a ferramenta é de diagnóstico, "don't use it all the time"; e o shell do recipe assume corpus em um diretório sem subníveis (contagem via ls), um detalhe de script shell não generalizado pela doc.

## Como verificar
Confirme a subseção Visualizing Python code coverage do README oficial: o comando de exemplo, a lista de três exits graciosos, o duplo aviso sobre -runs versus -atheris_runs e o bloco do corpus com a nota do empty data set.

## Conexões
- [[atheris-no-interesting]] — Veja também: "No interesting inputs were found": a porta de entrada mais comum.
- [[atheris-setup-api]] — Veja também: A API de três faces: Setup, Fuzz e o internal_libfuzzer.

## Fontes
- [Atheris — README oficial](https://github.com/google/atheris/blob/master/README.md) — definição, instalação, instrumentação, API e mutators custom; consultado em 2026-10-03.
- [coverage.py — documentação oficial](https://coverage.readthedocs.io/) — ferramenta de visualização referenciada pelo README do Atheris; consultado em 2026-10-03.
- [Atheris — Native Extension Fuzzing](https://github.com/google/atheris/blob/master/native_extension_fuzzing.md) — documento dedicado à instrumentação de extensões nativas; consultado em 2026-10-03.
