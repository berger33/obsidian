---
id: software.testes.tranche24.001761
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
fontes: ["https://raw.githubusercontent.com/robotframework/robotframework/master/README.rst", "https://github.com/robotframework/robotframework"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Instalação por pip e a escada de versões do Python

## Em uma frase
A instalação oficial é "pip install robotframework" com Python e pip já presentes; o framework exige Python 3.8 ou mais novo, roda também sobre PyPy, e downloads oficiais são hospedados no PyPI.

## Por que importa
Projetos legados precisam saber exatamente até que versão subir: o README aponta Robot Framework 6.1.1 como a última com suporte a Python 3.6 e 3.7, e Robot Framework 4.1.3 para quem ainda depende de Python 2, Jython ou IronPython.

## Como funciona
Instale no ambiente virtual do projeto, confirme "robot --version" e, se a ferramenta exigir Python 2 ou interpretes alternativos, fixe explicitamente a tag 6.1.1 ou 4.1.3 no pip em vez de esperar que a linha principal suporte esse ambiente.

## Exemplo
pip install robotframework; para um CI antigo em Python 3.7, pip install robotframework==6.1.1; para Jython, pip install robotframework==4.1.3.

## Limites e trade-offs
O suporte a Jython/IronPython existe apenas nas linhas antigas (4.1.3); a versão atual não oferece isso, e o README documenta esses pins como a saída para quem não pode subir o Python.

## Como verificar
Conferi o comando de instalação, o requisito Python 3.8+, o suporte a PyPy e os pins 6.1.1/4.1.3 na seção Installation do README oficial.

## Conexões
- [[robotframework-what-it-is]] — Veja também: Robot Framework: automação genérica com sintaxe de texto puro.
- [[robotframework-suite-syntax]] — Veja também: A anatomia de uma suíte: tabelas Settings e Test Cases.

## Fontes
- [Robot Framework README.rst oficial](https://raw.githubusercontent.com/robotframework/robotframework/master/README.rst) — README.rst oficial do Robot Framework com introdução, instalação, exemplo de suíte, CLI robot/rebot, ecossistema, fundação e licenciamento.; consultado em 2026-10-03.
- [Repositório oficial robotframework/robotframework](https://github.com/robotframework/robotframework) — Repositório oficial no GitHub com código-fonte, histórico de commits, branches, tags e canais do projeto.; consultado em 2026-10-03.
