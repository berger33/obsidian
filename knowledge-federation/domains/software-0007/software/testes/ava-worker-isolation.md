---
id: software.testes.tranche21.001471
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/avajs/ava/blob/main/docs/01-writing-tests.md", "https://github.com/avajs/ava/blob/main/readme.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# AVA: isolamento em worker threads

## Em uma frase
Cada arquivo de teste roda em uma thread de worker nova, com opção de voltar a processos separados pela configuração workerThreads, e o NODE_ENV do teste é definido automaticamente.

## Por que importa
O isolamento impede que um arquivo vaze modificadores de módulos globais para outro, que é a fonte clássica de ordem-dependente nos testes de Node.

## Como funciona
Deixe o padrão agir por arquivo, use o modo de processo quando bibliotecas nativas brigarem com threads e conte com NODE_ENV=test já preenchido.

## Exemplo
Uma dependência que escolhe o banco pelo NODE_ENV passa a usar o banco de teste sem nenhum export manual no setup.

## Limites e trade-offs
Checagens como 'NODE_ENV' in process.env serão sempre verdadeiras, o que pode ativar caminhos que nunca rodam em produção sem a mesma variável.

## Como verificar
Imprima process.env.NODE_ENV em um teste sem configurar nada e confirme o valor test atribuído pelo AVA.

## Conexões
- [[ava-concurrency-model]] — Veja também: AVA: testes concorrentes por padrão.
- [[ava-setup-npm-init]] — Veja também: AVA: inicializar o projeto com npm init ava.

## Fontes
- [AVA — Guia Writing tests](https://github.com/avajs/ava/blob/main/docs/01-writing-tests.md) — concorrência, modificadores, hooks e isolamento; consultado em 2026-10-03.
- [AVA — README oficial](https://github.com/avajs/ava/blob/main/readme.md) — proposta, instalação e destaques do runner; consultado em 2026-10-03.
