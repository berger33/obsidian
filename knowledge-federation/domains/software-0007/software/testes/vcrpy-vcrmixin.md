---
id: software.testes.tranche21.001504
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

# VCR.py: VCRMixin quando a hierarquia já tem base

## Em uma frase
Quando a classe de teste já herda de outra base de testes, o VCRMixin entra como mixin na frente do TestCase para obter a mesma gravação automática.

## Por que importa
Sem o mixin, a única alternativa seria quebrar a hierarquia compartilhada de fábrica de clientes e ambientes só para ganhar cassette.

## Como funciona
Misture VCRMixin na classe concreta que herda de unittest.TestCase e mantenha a base original intacta atrás do mixin.

## Exemplo
class MeuTeste(CliMixinBase, VCRMixin, unittest.TestCase) continua o padrão da casa com cassetes ligados.

## Limites e trade-offs
A ordem das bases define quem vence o setUp de quem; herdar VCRTestCase em cima de outra base já inicializada provoca conflito de construtor.

## Como verificar
Troque VCRTestCase por VCRMixin na mesma suíte e confirme que os cassetes continuam sendo resolvidos por método.

## Conexões
- [[vcrpy-vcrtestcase]] — Veja também: VCR.py: integração com unittest via VCRTestCase.
- [[vcrpy-vcr-config-object]] — Veja também: VCR.py: configurar um objeto VCR próprio.

## Fontes
- [VCR.py — Usage](https://vcrpy.readthedocs.io/en/latest/usage.html) — contexto, decorator, record modes e integrações de teste; consultado em 2026-10-03.
- [VCR.py — repositório oficial](https://github.com/kevin1024/vcrpy) — código-fonte, releases e changelog do projeto; consultado em 2026-10-03.
