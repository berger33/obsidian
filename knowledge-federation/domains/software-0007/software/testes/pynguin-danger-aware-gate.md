---
id: software.testes.tranche24.001772
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
fontes: ["https://pynguin.readthedocs.io/latest/user/quickstart.html", "https://pypi.org/project/pynguin/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PYNGUIN_DANGER_AWARE: o CLI que se recusa a rodar

## Em uma frase
Como proteção, a CLI do Pynguin aborta imediatamente a menos que a variável de ambiente PYNGUIN_DANGER_AWARE esteja definida; o valor atribuído pode ser arbitrário — a ferramenta só verifica se a variável existe — e defini-la é a declaração de que o usuário sabe dos perigos de executar código com entradas aleatórias.

## Por que importa
Esse desenho transforma um aviso ignorável em contrato: nenhum CI roda o gerador "por engano"; a equipe precisa escrever a variável no pipeline, e esse ato vira o ponto de revisão de segurança na configuração.

## Como funciona
Exporte PYNGUIN_DANGER_AWARE=1 (ou qualquer valor) na sessão ou no ambiente do job, e documente no arquivo de CI que a variável ali é a aceitação do risco de execução, junto das medidas de isolamento usadas.

## Exemplo
Em um job de GitHub Actions: env: PYNGUIN_DANGER_AWARE: 1, com o passo rodando dentro de um container que só enxerga o checkout; sem a variável, o comando nem começa.

## Limites e trade-offs
A variável é uma confirmação, não uma proteção: ela desliga o abortamento mas não adiciona sandbox — a mitigação real continua sendo o isolamento externo que o quickstart recomenda.

## Como verificar
O quickstart oficial descreve o abortamento, o valor arbitrário e o significado de definir a variável.

## Conexões
- [[pynguin-executes-code-danger]] — Veja também: O gerador executa o código sob teste — sem rede de segurança.
- [[pynguin-install-python-prereqs]] — Veja também: Instalação por pip e a janela curta de versões do Python.

## Fontes
- [Pynguin — Quickstart oficial no Read the Docs](https://pynguin.readthedocs.io/latest/user/quickstart.html) — Guia Quickstart oficial com PYNGUIN_DANGER_AWARE, isolamento em Docker, exemplo triangle anotado com PEP 484 e log de geração DYNAMOSA.; consultado em 2026-10-03.
- [Pynguin na página oficial do PyPI](https://pypi.org/project/pynguin/) — Página oficial do pacote pynguin no PyPI com descrição, avisos de execução, pré-requisitos de Python, instalação e governança.; consultado em 2026-10-03.
