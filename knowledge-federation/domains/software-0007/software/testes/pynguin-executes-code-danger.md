---
id: software.testes.tranche24.001771
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

# O gerador executa o código sob teste — sem rede de segurança

## Em uma frase
O README e o quickstart repetem o aviso: o Pynguin executa o módulo sob teste, e se esse código faz algo ruim — o exemplo oficial é "wipes your entire hard disk" — nada impede; a execução alcança também o código importado transitivamente pelo módulo, e os mantenedores declaram explicitamente que não fornecem suporte nem responsabilidade por danos ao rodar código aleatório da internet.

## Por que importa
Teste de unidade costuma ser atividade de baixa consequência; aqui, invocar o gerador é executar o alvo com entradas aleatórias em processo real, o que muda o cálculo de risco: um módulo com efeitos colaterais (arquivos, rede, variáveis de ambiente) pode causar dano durante a geração, não só nos testes.

## Como funciona
Rode o Pynguin apenas em ambiente isolado — container com permissões mínimas e montes controlados — e leia o código do módulo e seus imports antes de qualquer execução; o quickstart recomenda conferir o código antes de executar, "o que já é um bom conselho de qualquer forma".

## Exemplo
Antes de gerar testes para um pacote desconhecido, inspecione o que ele faz no import-time (scripts de setup, efeitos de módulo) e execute a geração dentro de um container descartável com o diretório do projeto montado somente-leitura quando possível.

## Limites e trade-offs
O aviso cobre o mecanismo de execução; a mitigação recomendada pelos mantenedores é isolamento via container, e o README admite que não existe ainda um mecanismo equivalente ao security manager do Java no Python.

## Como verificar
O parágrafo "Attention" do README no PyPI e a seção de aviso do Quickstart oficial listam os mesmos perigos e recomendações.

## Conexões
- [[pynguin-what-it-is]] — Veja também: Pynguin: gerador de testes unitários para linguagem dinâmica.
- [[pynguin-danger-aware-gate]] — Veja também: PYNGUIN_DANGER_AWARE: o CLI que se recusa a rodar.

## Fontes
- [Pynguin na página oficial do PyPI](https://pypi.org/project/pynguin/) — Página oficial do pacote pynguin no PyPI com descrição, avisos de execução, pré-requisitos de Python, instalação e governança.; consultado em 2026-10-03.
- [Pynguin — Quickstart oficial no Read the Docs](https://pynguin.readthedocs.io/latest/user/quickstart.html) — Guia Quickstart oficial com PYNGUIN_DANGER_AWARE, isolamento em Docker, exemplo triangle anotado com PEP 484 e log de geração DYNAMOSA.; consultado em 2026-10-03.
