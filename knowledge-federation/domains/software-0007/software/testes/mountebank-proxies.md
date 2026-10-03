---
id: software.testes.tranche19.001281
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://www.mbtest.org/docs/api/proxies", "https://www.mbtest.org/docs/api/overview"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mountebank: gravar e reproduzir com proxies

## Em uma frase
Uma resposta em modo proxy encaminha a requisição ao serviço real e pode registrar a resposta para reprodução posterior.

## Por que importa
A gravação produz respostas realistas sem depender do serviço real em toda execução, reduzindo acoplamento e instabilidade.

## Como funciona
Configure o destino sem caminho base, escolha o modo de gravação e defina geradores de predicado que repliquem a correspondência original.

## Exemplo
O proxy pode gravar uma vez a resposta de consulta de catálogo e servi-la nas execuções seguintes a partir do arquivo salvo.

## Limites e trade-offs
Gravações antigas deixam de refletir o serviço real, e proxies que encaminham tudo mantêm a dependência que se pretendia remover.

## Como verificar
Compare uma resposta gravada com a do serviço real no mesmo momento e avalie a defasagem.

## Conexões
- [[mountebank-predicates]] — Veja também: Mountebank: decidir a correspondência com predicados.
- [[mountebank-behaviors]] — Veja também: Mountebank: ajustar respostas com comportamentos.

## Fontes
- [Mountebank — Proxies](https://www.mbtest.org/docs/api/proxies) — encaminhamento ao serviço real, gravação e reprodução; consultado em 2026-10-03.
- [Mountebank — API overview](https://www.mbtest.org/docs/api/overview) — interface administrativa, criação de impostores e remoção; consultado em 2026-10-03.
