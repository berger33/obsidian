---
id: software.testes.tranche21.001501
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

# VCR.py: gerenciar contexto ou decorar a função

## Em uma frase
O cassette pode envolver o código com vcr.use_cassette('caminho.yaml') como gerenciador de contexto ou como decorator sobre a função de teste.

## Por que importa
Os dois formulários atendem a correntes diferentes de escrita: blocos explícitos para trechos pequenos, decorator para o teste inteiro, sem API separada.

## Como funciona
Use o decorator com ou sem caminho: omitido o argumento, o arquivo ganha o nome da função de teste e é criado ao lado do arquivo que a define.

## Exemplo
@vcr.use_cassette() sobre test_iana cria fixtures ao lado do módulo com o nome exato do caso.

## Limites e trade-offs
O nome automático depende da função de teste e da localização do módulo; renomear testes muda o cassette esperado silenciosamente.

## Como verificar
Renomeie a função decorada sem mover o cassette e confirme que a gravação cria o arquivo com o novo nome.

## Conexões
- [[vcrpy-record-replay-contract]] — Veja também: VCR.py: gravar uma vez, repetir sempre.
- [[vcrpy-record-modes]] — Veja também: VCR.py: escolher entre once, new_episodes, none e all.

## Fontes
- [VCR.py — Usage](https://vcrpy.readthedocs.io/en/latest/usage.html) — contexto, decorator, record modes e integrações de teste; consultado em 2026-10-03.
- [VCR.py — Configuration](https://vcrpy.readthedocs.io/en/latest/configuration.html) — objeto VCR, precedência de overrides e casamento de pedidos; consultado em 2026-10-03.
