---
id: software.testes.tranche21.001506
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
fontes: ["https://vcrpy.readthedocs.io/en/latest/configuration.html", "https://vcrpy.readthedocs.io/en/latest/usage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# VCR.py: o que torna dois pedidos iguais

## Em uma frase
Por padrão o VCR considera idênticos os pedidos com mesmo método, esquema, host, porta, caminho e query, e a lista match_on aceita também uri, body, raw_body, headers e um alias url.

## Por que importa
A granularidade do casamento decide quando um teste encontra o cassette e quando quebra por um timestamp na query — é contrato, não detalhe.

## Como funciona
Afrouxe match_on para testes que não se importam com corpo (deixando method e path), e cadastre um matcher próprio quando as opções não alcançarem o caso.

## Exemplo
Uma API versionada no header pode usar match_on=['method', 'uri'] mais um matcher registrado para o cabeçalho de versão.

## Limites e trade-offs
Incluir raw_body de um POST multipart com limites aleatórios torna a reprodução impossível; excluir query demais casa pedidos que são casos diferentes.

## Como verificar
Mude um parâmetro de query irrelevante e confirme que o teste casa, depois repita com query relevante sob o default para ver a falha.

## Conexões
- [[vcrpy-vcr-config-object]] — Veja também: VCR.py: configurar um objeto VCR próprio.
- [[vcrpy-pytest-plugins]] — Veja também: VCR.py: pytest-vcr e pytest-recording.

## Fontes
- [VCR.py — Configuration](https://vcrpy.readthedocs.io/en/latest/configuration.html) — objeto VCR, precedência de overrides e casamento de pedidos; consultado em 2026-10-03.
- [VCR.py — Usage](https://vcrpy.readthedocs.io/en/latest/usage.html) — contexto, decorator, record modes e integrações de teste; consultado em 2026-10-03.
