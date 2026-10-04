---
id: software.testes.tranche21.001476
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

# AVA: only, skip, todo e failing

## Em uma frase
O modificador .only recorta os casos do arquivo, .skip pula mantendo o caso visível, .todo reserva um placeholder só com título e .failing documenta um defeito esperado sem quebrar a esteira.

## Por que importa
Marcadores nativos de foco e pendência eliminam os comentários desligados na mão, que sempre sobrevivem ao merge e vazam para a CI.

## Como funciona
Combine .skipIf(condicao) e .runIf(condicao) para pular por plataforma, encadeie com .serial ou .failing e remova .only antes do commit.

## Exemplo
test.skipIf(process.platform === 'win32')('não roda no Windows', t => t.pass()) protege um teste sensível ao sistema.

## Limites e trade-offs
O .only vale por arquivo, não pela suíte inteira: outros arquivos continuam rodando; um .failing que passa vira erro com aviso para remover o modificador.

## Como verificar
Marque um caso como .failing, corrija o bug e confirme que o AVA falha pedindo a remoção do modificador.

## Conexões
- [[ava-serial-modifier]] — Veja também: AVA: casos .serial antes dos concorrentes.
- [[ava-hooks-lifecycle]] — Veja também: AVA: ganchos before, after e always.

## Fontes
- [AVA — Guia Writing tests](https://github.com/avajs/ava/blob/main/docs/01-writing-tests.md) — concorrência, modificadores, hooks e isolamento; consultado em 2026-10-03.
- [AVA — README oficial](https://github.com/avajs/ava/blob/main/readme.md) — proposta, instalação e destaques do runner; consultado em 2026-10-03.
