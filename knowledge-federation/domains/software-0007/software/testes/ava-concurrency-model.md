---
id: software.testes.tranche21.001470
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

# AVA: testes concorrentes por padrão

## Em uma frase
No AVA, os testes de um arquivo são definidos para rodar concorrentemente, e o executor só espera um teste terminar quando ele retorna uma promessa ou um observável.

## Por que importa
Testes unitários em Node.js raramente dependem entre si; executá-los em paralelo dentro do mesmo arquivo reduz o tempo da suíte sem mudar o código.

## Como funciona
Escreva testes atômicos, retorne a promessa quando houver trabalho assíncrono e evite compartilhar estado mutável entre casos do mesmo arquivo.

## Exemplo
Doze testes de parsing podem aguardar a mesma I/O simultaneamente e concluir no tempo de um único teste lento.

## Limites e trade-offs
Testes que disputam um recurso global precisam migrar para .serial ou para arquivos separados; concorrência não é mágica sobre estado compartilhado.

## Como verificar
Marque dois testes com atrasos distintos e confirme que o tempo total do arquivo não soma as duas esperas.

## Conexões
- [[ava-worker-isolation]] — Veja também: AVA: isolamento em worker threads.

## Fontes
- [AVA — Guia Writing tests](https://github.com/avajs/ava/blob/main/docs/01-writing-tests.md) — concorrência, modificadores, hooks e isolamento; consultado em 2026-10-03.
- [AVA — README oficial](https://github.com/avajs/ava/blob/main/readme.md) — proposta, instalação e destaques do runner; consultado em 2026-10-03.
