---
id: software.seguranca.tranche20.001931
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-20.md"
fontes: ["https://github.com/CycloneDX/cdxgen", "https://github.com/CycloneDX/cdxgen/blob/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CycloneDX Generator (cdxgen): Gerar BOM de repositório

## Em uma frase
**CycloneDX Generator (cdxgen) — Gerar BOM de repositório:** cdxgen analisa projeto local e manifests para produzir inventário de componentes CycloneDX.

## Por que importa
O recorte de **gerar bom de repositório** ajuda a inventariar componentes para análise de supply chain, vulnerabilidades, licenças e proveniência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **gerar bom de repositório**, cdxgen inspeciona alvo e ecossistema, resolve componentes detectáveis e emite BOM CycloneDX para ferramentas downstream. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Rode geração em checkout limpo do commit de release e associe BOM à revisão. Teste em staging autorizado.

## Limites e trade-offs
Dependências dinâmicas ou metadados ausentes podem não aparecer no resultado. Exceções exigem responsável e prazo.

## Como verificar
Compare lista de manifests detectados, dependências resolvidas e contagem do BOM. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cdxgen-gerar-bom-de-imagem-container]] — Complementa o tópico com cyclonedx generator (cdxgen): gerar bom de imagem container.

## Fontes
- [CycloneDX cdxgen — Repository](https://github.com/CycloneDX/cdxgen) — repositório oficial de geração de BOM para projetos, containers e múltiplos ecossistemas; consultado em 2026-10-04.
- [CycloneDX cdxgen — README](https://github.com/CycloneDX/cdxgen/blob/master/README.md) — guia oficial de instalação, comandos, opções e formatos de saída; consultado em 2026-10-04.
