---
id: software.testes.tranche21.001508
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

# VCR.py: ganchos de personalização da classe-base

## Em uma frase
A VCRTestCase expõe _get_vcr_kwargs, _get_cassette_library_dir e _get_cassette_name para reescrever configuração, pasta e nome, e _get_vcr permite registrar matchers antes do uso.

## Por que importa
Sem ganchos, quem não segue a convenção cassettes/Classe.metodo.yaml teria de copiar a implementação inteira do TestCase do VCR.

## Como funciona
Sobrescreva _get_vcr chamando o super, registre o matcher com register_matcher e atribua a lista match_on no objeto devolvido.

## Exemplo
myvcr.register_matcher('mymatcher', mymatcher); myvcr.match_on = ['mymatcher'] aparece literalmente no exemplo oficial.

## Limites e trade-offs
O gancho roda por teste, então lógica cara nele paga o preço em cada caso da suíte; mantenha o corpo barato.

## Como verificar
Subclasse, sobrescreva a pasta dos cassetes e confirme que a gravação cai no diretório alternativo.

## Conexões
- [[vcrpy-pytest-plugins]] — Veja também: VCR.py: pytest-vcr e pytest-recording.
- [[vcrpy-when-cassettes-fit]] — Veja também: VCR.py: o que o cassette não substitui.

## Fontes
- [VCR.py — Usage](https://vcrpy.readthedocs.io/en/latest/usage.html) — contexto, decorator, record modes e integrações de teste; consultado em 2026-10-03.
- [VCR.py — repositório oficial](https://github.com/kevin1024/vcrpy) — código-fonte, releases e changelog do projeto; consultado em 2026-10-03.
