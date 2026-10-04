---
id: software.testes.tranche21.001509
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
fontes: ["https://vcrpy.readthedocs.io/en/latest/usage.html", "https://vcrpy.readthedocs.io/en/latest/configuration.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# VCR.py: o que o cassette não substitui

## Em uma frase
O VCR.py cobre a camada HTTP do teste de integração; ele não valida contratos de esquema nem executa o serviço real, e serve como substituto de ambiente, não de suíte.

## Por que importa
Times que descobrem o gravador tendem a convertê-lo em única fonte de verdade e perdem os testes vivos que pegam degradações do serviço.

## Como funciona
Mantenha cassetes para a repetibilidade diária e reserve testes de contrato e sondas de sintônias para o contato real periódico.

## Exemplo
A esteira roda o dia inteiro com cassetes e um job noturno casa as respostas vivas com o contrato publicado.

## Limites e trade-offs
Cassetes envelhecem em silêncio enquanto o serviço vivo responde; sem regravação deliberada o teste reproduz uma API que não existe mais.

## Como verificar
Marque na esteira o tempo máximo de defasagem do cassette e falhe o build acima dele.

## Conexões
- [[vcrpy-override-hooks]] — Veja também: VCR.py: ganchos de personalização da classe-base.

## Fontes
- [VCR.py — Usage](https://vcrpy.readthedocs.io/en/latest/usage.html) — contexto, decorator, record modes e integrações de teste; consultado em 2026-10-03.
- [VCR.py — Configuration](https://vcrpy.readthedocs.io/en/latest/configuration.html) — objeto VCR, precedência de overrides e casamento de pedidos; consultado em 2026-10-03.
