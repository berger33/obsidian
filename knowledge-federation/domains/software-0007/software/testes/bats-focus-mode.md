---
id: software.testes.tranche22.001566
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://bats-core.readthedocs.io/en/latest/writing-tests.html", "https://bats-core.readthedocs.io/en/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# bats-core: o que fica marcado roda sozinho

## Em uma frase
A tag especial bats:focus faz o Bats filtrar a suíte inteira para executar apenas os casos com ela, e em modo foco o código de saída de uma passada limpa vira 1 de propósito.

## Por que importa
Quem desenvolve testes marca um caso com focus para iterar rápido, mas o commit acidental desse marcador deixaria o CI verificando um subconjunto silencioso — o código de saída forçado é a proteção contra isso.

## Como funciona
Tague o teste com bats:focus, rode bats normalmente e veja só ele executar; se precisar do exit code verdadeiro (um git bisect, por exemplo), exporte BATS_NO_FAIL_FOCUS_RUN=1.

## Exemplo
# bats test_tags=bats:focus sobre o caso "aceita --dry-run" concentra o run nesse teste durante o desenvolvimento.

## Limites e trade-offs
O guia avisa explicitamente para não commitar a exceção BATS_NO_FAIL_FOCUS_RUN junto com a suíte, pois ela desarma a trava de segurança do modo foco.

## Como verificar
Deixe um bats:focus esquecido num arquivo e confirme que o pipeline falha mesmo com todos os testes verdes.

## Conexões
- [[bats-tagging]] — Veja também: bats-core: tags, filtros e modo foco.
- [[bats-parallel]] — Veja também: bats-core: --jobs com GNU parallel.

## Fontes
- [Bats-core — Writing tests](https://bats-core.readthedocs.io/en/latest/writing-tests.html) — run, tags, setup/teardown, ganchos e armadilhas de escrita; consultado em 2026-10-03.
- [Bats-core — Documentação oficial (página inicial)](https://bats-core.readthedocs.io/en/latest/index.html) — índice: tutorial, instalação, usage, gotchas e FAQ; consultado em 2026-10-03.
