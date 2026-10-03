---
id: software.testes.tranche21.001503
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

# VCR.py: integração com unittest via VCRTestCase

## Em uma frase
Herdar de vcr.unittest.VCRTestCase liga a gravação e a reprodução automaticamente a cada teste, com o cassette acessível em self.cassette e caminho padrão cassettes/Classe.metodo.yaml.

## Por que importa
A nomeação automática por classe e método elimina a linha de setup em cada teste e mantém um cassette previsível por caso de unittest.

## Como funciona
Substitua o TestCase padrão pelo VCRTestCase, escreva o teste como sempre e inspecione self.cassette.requests quando quiser afirmar a quantidade ou o URI gravado.

## Exemplo
self.assertEqual(len(self.cassette), 1) prova que o teste fez exatamente uma chamada externa.

## Limites e trade-offs
Quem define o próprio setUp precisa chamar o super para não perder a preparação dos cassetes — pegadinha declarada na documentação.

## Como verificar
Consulte o número de pedidos do cassette após um teste de requests.get e confirme o caminho do arquivo na subpasta cassettes.

## Conexões
- [[vcrpy-record-modes]] — Veja também: VCR.py: escolher entre once, new_episodes, none e all.
- [[vcrpy-vcrmixin]] — Veja também: VCR.py: VCRMixin quando a hierarquia já tem base.

## Fontes
- [VCR.py — Usage](https://vcrpy.readthedocs.io/en/latest/usage.html) — contexto, decorator, record modes e integrações de teste; consultado em 2026-10-03.
- [VCR.py — repositório oficial](https://github.com/kevin1024/vcrpy) — código-fonte, releases e changelog do projeto; consultado em 2026-10-03.
