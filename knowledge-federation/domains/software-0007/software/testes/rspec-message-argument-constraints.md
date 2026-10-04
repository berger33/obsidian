---
id: software.testes.tranche12.000616
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://rspec.info/features/3-13/rspec-mocks/setting-constraints/matching-arguments/", "https://rspec.info/features/3-13/rspec-mocks/verifying-doubles/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec 3.13: restringir argumentos de expectativas de mensagem

## Em uma frase
`with` limita quais argumentos satisfazem uma expectativa ou resposta configurada para uma mensagem recebida por double.

## Por que importa
Checar argumento junto da chamada impede que um colaborador seja considerado correto quando recebe identificador ou opção diferente do requisito.

## Como funciona
Combine valores literais com matchers como `anything`, `instance_of` ou `hash_including` e prefira a menor condição que representa a interface esperada.

## Exemplo
Um double de notificações pode aceitar `deliver` somente com o destinatário e assunto que o caso definiu, rejeitando chamadas acidentais para outra conta.

## Limites e trade-offs
Matchers amplos como `any_args` podem fazer a expectativa passar mesmo que uma regressão altere argumentos que deveriam ser protegidos.

## Como verificar
Mude um argumento por vez e confira se a mensagem de falha identifica claramente o valor esperado e o recebido.

## Conexões
- [[rspec-verifying-doubles-interface]] — Veja também: RSpec 3.13: doubles que verificam a interface.
- [[rspec-metadata-tag-selection]] — Veja também: RSpec 3.13: filtrar exemplos por metadata.

## Fontes
- [RSpec 3.13 — Matching arguments](https://rspec.info/features/3-13/rspec-mocks/setting-constraints/matching-arguments/) — restrições de argumentos de expectativas e stubs de mensagens; consultado em 2026-10-02.
- [RSpec 3.13 — Verifying doubles](https://rspec.info/features/3-13/rspec-mocks/verifying-doubles/) — double que valida métodos disponíveis na interface real; consultado em 2026-10-02.
