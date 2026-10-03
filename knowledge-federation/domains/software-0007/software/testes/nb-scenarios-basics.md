---
id: software.testes.tranche20.001449
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://www.nuget.org/packages/NBomber", "https://github.com/PragmaticFlow/NBomber"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NBomber: escrever um cenário de carga

## Em uma frase
O cenário descreve a operação a executar em cada iteração, em código da própria linguagem, e devolve o resultado da operação.

## Por que importa
Escrever a carga em código permite reaproveitar clientes e lógica do projeto em vez de manter arquivos de configuração paralelos.

## Como funciona
Crie o cenário com nome descritivo, devolva resposta de sucesso ou falha conforme o resultado e meça a operação completa.

## Exemplo
O cenário pode consultar um endpoint com o cliente da aplicação e devolver falha quando o código de resposta não for o esperado.

## Limites e trade-offs
Medir apenas parte da operação produz números otimistas, e cenários que engolem exceções mascaram falhas sob carga.

## Como verificar
Introduza erro no serviço e confirme que as falhas aparecem contabilizadas no resumo da execução.

## Conexões
- [[nb-load-simulations]] — Veja também: NBomber: definir o perfil de carga.

## Fontes
- [NBomber — Pacote publicado](https://www.nuget.org/packages/NBomber) — versões, dependências e documentação do pacote; consultado em 2026-10-03.
- [NBomber — repositório oficial](https://github.com/PragmaticFlow/NBomber) — código-fonte, integrações e documentação do projeto; consultado em 2026-10-03.
