---
id: software.testes.tranche24.001767
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

# Onde a documentação oficial mora

## Em uma frase
O README enumera os canais de referência: Robot Framework User Guide (linkado da página do projeto, âncora #user-guide), as Standard libraries, a API documentation hospedada em readthedocs e a documentação geral em robotframework.org, além de suporte via Slack, fórum oficial e a lista robotframework-users.

## Por que importa
Times novos tentam aprender o framework por blog posts de 2015; o guia do usuário e a documentação das bibliotecas padrão são mantidos no mesmo repositório/versionamento do produto, e a lista de canais do README é o caminho canônico que evita desatualização.

## Como funciona
Comece pelo User Guide para sintaxe e execução, use a documentação das standard libraries para as palavras-chave embutidas (String, Collections, OperatingSystem e similar), e reserve o readthedocs para a API de extensão em Python; dúvidas de uso vão para o fórum.

## Exemplo
Para checar o comportamento de uma diretiva como [Teardown], a busca começa no User Guide linkado do README, não em respostas empilhadas em sites de pergunta e resposta.

## Limites e trade-offs
O README lista os destinos mas não reproduz o conteúdo de cada um; a nota afirma apenas onde a documentação oficial está, conforme declarado pelo próprio projeto.

## Como verificar
Conferi a seção "Documentation" e a seção "Support and Contact" do README oficial.

## Conexões
- [[robotframework-ecosystem]] — Veja também: O ecossistema como parte do produto.
- [[robotframework-contributing]] — Veja também: Contribuir: do CONTRIBUTING.rst aos rótulos de issue.

## Fontes
- [Robot Framework README.rst oficial](https://raw.githubusercontent.com/robotframework/robotframework/master/README.rst) — README.rst oficial do Robot Framework com introdução, instalação, exemplo de suíte, CLI robot/rebot, ecossistema, fundação e licenciamento.; consultado em 2026-10-03.
- [Repositório oficial robotframework/robotframework](https://github.com/robotframework/robotframework) — Repositório oficial no GitHub com código-fonte, histórico de commits, branches, tags e canais do projeto.; consultado em 2026-10-03.
