---
id: software.testes.tranche21.001502
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

# VCR.py: escolher entre once, new_episodes, none e all

## Em uma frase
Os modos de gravação controlam quando o VCR fala com a rede: once grava sem cassette e erro com novo pedido, new_episodes estende sempre, none proíbe rede, all regrava tudo.

## Por que importa
O mesmo teste precisa de comportamento diferente na gravação local, na CI e na auditoria de segurança da rede, e o modo declara essa diferença em vez de escondê-la em variáveis de ambiente.

## Como funciona
Deixar o default once na maioria, alternar para none na esteira que exige rede zero e usar all para regravar cassetes suspeitos de defasagem.

## Exemplo
A CI configura record_mode='none' e qualquer URI nova no código passa a falhar o build em vez de chamar o mundo.

## Limites e trade-offs
none com cassette inexistente também falha, o que confunde ausência de gravação com pedido indevido; all silencia divergências de resposta ao aceitar sempre a nova.

## Como verificar
Force um pedido não gravado sob none e confirme o erro explícito recusando a saída de rede.

## Conexões
- [[vcrpy-context-decorator]] — Veja também: VCR.py: gerenciar contexto ou decorar a função.
- [[vcrpy-vcrtestcase]] — Veja também: VCR.py: integração com unittest via VCRTestCase.

## Fontes
- [VCR.py — Usage](https://vcrpy.readthedocs.io/en/latest/usage.html) — contexto, decorator, record modes e integrações de teste; consultado em 2026-10-03.
- [VCR.py — Configuration](https://vcrpy.readthedocs.io/en/latest/configuration.html) — objeto VCR, precedência de overrides e casamento de pedidos; consultado em 2026-10-03.
