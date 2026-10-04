---
id: software.testes.tranche21.001505
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

# VCR.py: configurar um objeto VCR próprio

## Em uma frase
Instanciar vcr.VCR com serializer, cassette_library_dir, record_mode e match_on cria uma configuração reutilizável, e cada use_cassette aceita overrides que vencem o global.

## Por que importa
Espalhar kwargs idênticos por dezenas de testes garante divergências; o objeto central é a mesma ideia do conftest para o pytest.

## Como funciona
Defina o VCR do projeto uma vez, aponte a pasta de fixtures, escolha o formato json e reutilize my_vcr.use_cassette nos testes.

## Exemplo
O diretório único fixtures/cassettes recebe arquivos .json gravados por todos os módulos de teste.

## Limites e trade-offs
Overrides por cassette resolvem exceções mas viram regra silenciosa quando dois desenvolvedores lembram de parâmetros diferentes; registre exceções em revisão.

## Como verificar
Mude o serializer no objeto e em um teste, e confirme que o override local decide o formato do arquivo.

## Conexões
- [[vcrpy-vcrmixin]] — Veja também: VCR.py: VCRMixin quando a hierarquia já tem base.
- [[vcrpy-request-matching]] — Veja também: VCR.py: o que torna dois pedidos iguais.

## Fontes
- [VCR.py — Configuration](https://vcrpy.readthedocs.io/en/latest/configuration.html) — objeto VCR, precedência de overrides e casamento de pedidos; consultado em 2026-10-03.
- [VCR.py — Usage](https://vcrpy.readthedocs.io/en/latest/usage.html) — contexto, decorator, record modes e integrações de teste; consultado em 2026-10-03.
