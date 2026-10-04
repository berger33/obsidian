---
id: software.testes.tranche21.001507
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
fontes: ["https://vcrpy.readthedocs.io/en/latest/usage.html", "https://github.com/kevin1024/vcrpy"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# VCR.py: pytest-vcr e pytest-recording

## Em uma frase
Para o pytest existem duas integrações mantidas fora do núcleo: o plugin pytest-vcr e o pytest-recording, que também bloqueia o acesso à rede.

## Por que importa
O decorator manual funciona em qualquer executor, mas fixtures de cassette por teste e o bloqueio global de rede pedem a camada do plugin.

## Como funciona
Escolha pytest-vcr para a marcação declarativa e pytest-recording quando a política for derrubar qualquer tentativa de rede fora dos cassetes gravados.

## Exemplo
Um projeto adiciona o plugin e ganha a fixture vcr_cassette com configuração herdada de um único ponto.

## Limites e trade-offs
Plugin extra é dependência extra na esteira do time; os links oficiais moram em repositórios de terceiros, revise antes de fixar versões.

## Como verificar
Instale um dos plugins, rode sem rede e confirme que os testes com cassette passam e o acesso não autorizado é recusado.

## Conexões
- [[vcrpy-request-matching]] — Veja também: VCR.py: o que torna dois pedidos iguais.
- [[vcrpy-override-hooks]] — Veja também: VCR.py: ganchos de personalização da classe-base.

## Fontes
- [VCR.py — Usage](https://vcrpy.readthedocs.io/en/latest/usage.html) — contexto, decorator, record modes e integrações de teste; consultado em 2026-10-03.
- [VCR.py — repositório oficial](https://github.com/kevin1024/vcrpy) — código-fonte, releases e changelog do projeto; consultado em 2026-10-03.
