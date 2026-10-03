---
id: software.testes.tranche24.001774
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://pypi.org/project/pynguin/", "https://pynguin.readthedocs.io/latest/user/quickstart.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# A linha de comando mínima: três flags

## Em uma frase
O exemplo mínimo do README e do quickstart tem o mesmo esqueleto: "pynguin --project-path /tmp/foo --output-path /tmp/testgen --module-name foo.bar" — caminho do projeto, destino dos testes gerados e o módulo alvo — rodando com a abordagem whole-suite para um módulo do projeto.

## Por que importa
Três flags cobrem o contrato inteiro de entrada/saída da ferramenta: não há arquivo de projeto, DSL ou anotação extra; isso mantém a integração trivial (um passo de shell) e deixa claro que a unidade de geração é o módulo.

## Como funciona
Instale no ambiente virtual, invoque de dentro dele (o quickstart assume o sourcing manual do venv), aponte as três flags e aguarde: a execução padrão "roda por um momento sem mostrar nenhuma saída" — para acompanhar, adicione -v.

## Exemplo
Gerando para o exemplo bundled: pynguin --project-path ./docs/source/_static --output-path /tmp/pynguin-results --module-name example; o arquivo de teste sai no diretório de resultado configurado.

## Limites e trade-offs
O README descreve o formato "minimal"; parâmetros adicionais (critérios e condições de parada) existem e estão na documentação, mas o quickstart não os detalha no exemplo mínimo — que nem define condição de parada, como o próprio log mostra.

## Como verificar
As três flags e o comportamento silencioso do exemplo mínimo vêm da seção "Using Pynguin" do README e do Quickstart oficial.

## Conexões
- [[pynguin-install-python-prereqs]] — Veja também: Instalação por pip e a janela curta de versões do Python.
- [[pynguin-generation-internals]] — Veja também: O log de geração: DYNAMOSA, seed e timeout de 600s.

## Fontes
- [Pynguin na página oficial do PyPI](https://pypi.org/project/pynguin/) — Página oficial do pacote pynguin no PyPI com descrição, avisos de execução, pré-requisitos de Python, instalação e governança.; consultado em 2026-10-03.
- [Pynguin — Quickstart oficial no Read the Docs](https://pynguin.readthedocs.io/latest/user/quickstart.html) — Guia Quickstart oficial com PYNGUIN_DANGER_AWARE, isolamento em Docker, exemplo triangle anotado com PEP 484 e log de geração DYNAMOSA.; consultado em 2026-10-03.
