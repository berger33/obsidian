---
id: software.testes.tranche21.001472
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
fontes: ["https://github.com/avajs/ava/blob/main/readme.md", "https://github.com/avajs/ava/blob/main/docs/05-command-line.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# AVA: inicializar o projeto com npm init ava

## Em uma frase
O comando npm init ava instala o AVA como dependência de desenvolvimento e grava o script test apontando para o binário, já marcando o pacote como módulo ES.

## Por que importa
A configuração mínima fica um arquivo de distância: sem script test correto o AVA não roda, e é exatamente esse passo que o init automatiza.

## Como funciona
Rode o init na raiz do projeto, ou adicione ava --dev com Yarn, e invoque a suíte por npm test ou npx ava.

## Exemplo
Um pacote novo ganha devDependencies com ava e scripts.test com ava em um único comando interativo.

## Limites e trade-offs
O AVA não roda instalado globalmente; times que confiam em instalações globais quebram na primeira máquina sem histórico.

## Como verificar
Execute npx ava em um projeto recém-inicializado e confirme que o script test existe e a suíte mínima passa.

## Conexões
- [[ava-worker-isolation]] — Veja também: AVA: isolamento em worker threads.
- [[ava-declaring-tests]] — Veja também: AVA: declarar testes com título único.

## Fontes
- [AVA — README oficial](https://github.com/avajs/ava/blob/main/readme.md) — proposta, instalação e destaques do runner; consultado em 2026-10-03.
- [AVA — Guia Command line](https://github.com/avajs/ava/blob/main/docs/05-command-line.md) — flags do CLI, reporter TAP e modo watch; consultado em 2026-10-03.
