---
id: software.testes.tranche17.001150
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://rspec.info/features/3-12/rspec-mocks/", "https://github.com/rspec/rspec-core"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec: substituir dependências com dublês

## Em uma frase
Dublês verificados imitam a interface real, e permissões de recebimento configuram respostas sem exigir que a chamada aconteça.

## Por que importa
Dependências lentas ou indisponíveis isolam o comportamento sob teste, e o dublê verificado falha se o método imitado não existir.

## Como funciona
Prefira dublês verificados, permita apenas os métodos usados pelo exemplo e evite dublês de tipos que o exemplo não controla.

## Exemplo
Um repositório pode ser substituído por dublê verificado que devolve a entidade esperada para o cálculo sob teste.

## Limites e trade-offs
Dublês de tipos externos acoplam o teste à implementação de terceiros, e dublês não verificados aceitam métodos que nunca existirão.

## Como verificar
Renomeie um método no tipo real e confirme que o dublê verificado passa a falhar ao ser construído.

## Conexões
- [[rspec-hooks]] — Veja também: RSpec: usar ganchos com o escopo correto.
- [[rspec-message-expectations]] — Veja também: RSpec: declarar expectativas de mensagem.

## Fontes
- [RSpec — Mocks](https://rspec.info/features/3-12/rspec-mocks/) — dublês verificados, permissões de recebimento e expectativas de mensagem; consultado em 2026-10-03.
- [RSpec — repositório oficial](https://github.com/rspec/rspec-core) — código-fonte e documentação do núcleo do framework; consultado em 2026-10-03.
