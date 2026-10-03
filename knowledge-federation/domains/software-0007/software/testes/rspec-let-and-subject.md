---
id: software.testes.tranche17.001148
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
fontes: ["https://rspec.info/features/3-12/rspec-core/", "https://github.com/rspec/rspec-core"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec: preparar dados com memorização preguiçosa

## Em uma frase
Os auxiliares de definição criam valores avaliados no primeiro uso e memorizados por exemplo, e o sujeito nomeado descreve o objeto principal.

## Por que importa
A avaliação preguiçosa evita preparar dados que o exemplo não usa e mantém cada caso isolado.

## Como funciona
Defina os valores com os auxiliares, nomeie o sujeito quando há um objeto central e sobreponha definições dentro de contextos quando o estado muda.

## Exemplo
Um contexto pode redefinir o usuário autenticado enquanto mantém a preparação comum definida no grupo externo.

## Limites e trade-offs
Auxiliares no nível errado são reavaliados a cada exemplo com custo desnecessário, e sobreposições escondem qual definição está ativa.

## Como verificar
Substitua um auxiliar por uma falha temporária e confirme que apenas os exemplos que o usam são afetados.

## Conexões
- [[rspec-expectations-matchers]] — Veja também: RSpec: escrever expectativas.
- [[rspec-hooks]] — Veja também: RSpec: usar ganchos com o escopo correto.

## Fontes
- [RSpec — Core](https://rspec.info/features/3-12/rspec-core/) — grupos de exemplos, contextos, ganchos, metadados e configuração; consultado em 2026-10-03.
- [RSpec — repositório oficial](https://github.com/rspec/rspec-core) — código-fonte e documentação do núcleo do framework; consultado em 2026-10-03.
