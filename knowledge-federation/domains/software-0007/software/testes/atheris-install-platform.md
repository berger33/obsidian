---
id: software.testes.tranche23.001751
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
fontes: ["https://github.com/google/atheris/blob/master/README.md", "https://pypi.org/project/atheris/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Instalação: pip com libFuzzer embutido, LLVM novo quando há nativo

## Em uma frase
O README fixa o suporte: Linux de 32 e 64 bits e Mac OS X, Python 3.11 a 3.14 na fonte atual (versões 3.10 e abaixo "remain accessible in PyPI" mas não no código-fonte corrente), e a instalação padrão via pip3 install atheris traz wheels com um libFuzzer built-in que é "fine for fuzzing Python code".

## Por que importa
A decisão de instalação é determinada pelo alvo, não pela preferência: fuzzar extensões nativas pode exigir build from source para casar a versão do libFuzzer com o seu Clang — a página abre esse caminho com pip3 install --no-binary atheris atheris (release) ou clone e pip install . (dev).

## Como funciona
No macOS, o detalhe vem nomeado: "Apple Clang doesn't come with libFuzzer", então nativo no Mac passa pela seção Installing Against New LLVM — clonar llvm-project, cmake habilitando clang e compiler-rt, make (lento), e exportar CLANG_BIN apontando para o binário construído antes do pip install.

## Exemplo
Antes de planejar uma campanha sobre uma extensão C, rode python -c "import atheris" no ambiente alvo; se o wheel do pip resolver sem rebuild, o alvo é puro-Python-adequado; se o sanitizer for necessário, o caminho do LLVM da página vira pré-requisito.

## Limites e trade-offs
A faixa de versões de Python é a da página no snapshot (3.11 a 3.14) — a política explícita sobre 3.10-e-abaixo é "só PyPI", o que significa wheels existentes sem suporte na fonte; e o passo a passo LLVM constrói toolchain inteira, o custo real de nativo no Mac documentado não é o tempo do pip.

## Como verificar
Confirme o parágrafo de instalação, a nota do Apple Clang e o bloco de cmake com LLVM_ENABLE_PROJECTS no README oficial.

## Conexões
- [[atheris-what-it-is]] — Veja também: Atheris: fuzzer coverage-guided para Python que também encosta no nativo.
- [[atheris-minimal-harness]] — Veja também: O harness de cinco linhas e o que conta como crash.

## Fontes
- [Atheris — README oficial](https://github.com/google/atheris/blob/master/README.md) — definição, instalação, instrumentação, API e mutators custom; consultado em 2026-10-03.
- [Atheris — página no PyPI](https://pypi.org/project/atheris/) — distribuição pip citada pela política de versões do README; consultado em 2026-10-03.
