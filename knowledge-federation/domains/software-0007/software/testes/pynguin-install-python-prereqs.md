---
id: software.testes.tranche24.001773
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
fontes: ["https://pypi.org/project/pynguin/", "https://pynguin.readthedocs.io/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Instalação por pip e a janela curta de versões do Python

## Em uma frase
A instalação oficial é "pip install pynguin" (a versão na página do PyPI é 0.47.0), com a ressalva de que o pip precisa ser o de uma versão suportada; os pré-requisitos pedem Python 3.10, com suporte a 3.11, 3.12, 3.13 e 3.14 explicitamente marcado como experimental, e o aviso "Pynguin now requires at least Python 3.10! Older versions are no longer supported!".

## Por que importa
A janela de suporte estreita é típica de protótipos de pesquisa que correm atrás do CPython: planear a geração no CI significa fixar o container em 3.10 para comportamento suportado, ou aceitar experimentalidade declarada em versões mais novas.

## Como funciona
Crie o ambiente virtual com Python 3.10, instale o pacote e confirme "pynguin --help" (fora de ambiente com a variável de perigo, a ferramenta lista parâmetros); em 3.11+, registre na decisão de adoção que o suporte é declarado experimental pelo README.

## Exemplo
python3.10 -m venv .venv e .venv/bin/pip install pynguin; no CI, a imagem do job fixada em 3.10 enquanto o README mantiver os rótulos de experimentalidade para as demais.

## Limites e trade-offs
O README também classifica a própria ferramenta como protótipo de pesquisa "not tailored towards production use whatsoever", com o desejo dos mantenedores de vê-la production-ready — adoção em pipeline é aposta própria, não suporte contratado.

## Como verificar
A versão, o comando pip, a exigência de Python 3.10 e a marcação experimental de 3.11–3.14 constam da página oficial do pacote no PyPI.

## Conexões
- [[pynguin-danger-aware-gate]] — Veja também: PYNGUIN_DANGER_AWARE: o CLI que se recusa a rodar.
- [[pynguin-cli-minimal]] — Veja também: A linha de comando mínima: três flags.

## Fontes
- [Pynguin na página oficial do PyPI](https://pypi.org/project/pynguin/) — Página oficial do pacote pynguin no PyPI com descrição, avisos de execução, pré-requisitos de Python, instalação e governança.; consultado em 2026-10-03.
- [Pynguin — índice da documentação oficial](https://pynguin.readthedocs.io/latest/index.html) — Índice da documentação oficial do Pynguin no Read the Docs.; consultado em 2026-10-03.
