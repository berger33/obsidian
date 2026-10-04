---
id: software.testes.tranche17.001149
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

# RSpec: usar ganchos com o escopo correto

## Em uma frase
Ganchos de antes, depois e ao redor envolvem os exemplos, com escopo por exemplo, por grupo ou na suíte, respeitando a ordem dos grupos.

## Por que importa
Preparar no escopo errado mistura estado entre exemplos, e a limpeza correspondente precisa acontecer no mesmo nível da preparação.

## Como funciona
Coloque a preparação no escopo mais estreito possível, use o gancho ao redor quando o recurso exigir abertura e fechamento coordenados e mantenha a limpeza simétrica.

## Exemplo
Um gancho de grupo pode criar registros compartilhados, enquanto cada exemplo limpa apenas o que criou.

## Limites e trade-offs
Ganchos de suíte acumulam estado global, e a ordem entre ganchos de grupos externos e internos confunde quando a preparação depende de outra.

## Como verificar
Rode o mesmo exemplo isolado e dentro da suíte completa e confirme que o resultado não depende de estado deixado por outros exemplos.

## Conexões
- [[rspec-let-and-subject]] — Veja também: RSpec: preparar dados com memorização preguiçosa.
- [[rspec-doubles-and-stubs]] — Veja também: RSpec: substituir dependências com dublês.

## Fontes
- [RSpec — Core](https://rspec.info/features/3-12/rspec-core/) — grupos de exemplos, contextos, ganchos, metadados e configuração; consultado em 2026-10-03.
- [RSpec — repositório oficial](https://github.com/rspec/rspec-core) — código-fonte e documentação do núcleo do framework; consultado em 2026-10-03.
