---
id: software.seguranca.tranche20.001934
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

# CycloneDX Generator (cdxgen): Analisar monorepo por diretório

## Em uma frase
**CycloneDX Generator (cdxgen) — Analisar monorepo por diretório:** Monorepo pode conter múltiplos projetos com manifests e limites de dependência separados.

## Por que importa
O recorte de **analisar monorepo por diretório** ajuda a inventariar componentes para análise de supply chain, vulnerabilidades, licenças e proveniência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **analisar monorepo por diretório**, cdxgen inspeciona alvo e ecossistema, resolve componentes detectáveis e emite BOM CycloneDX para ferramentas downstream. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Gere BOM por diretório de produto e também um inventário agregado para release integrada. Teste em staging autorizado.

## Limites e trade-offs
Scan de raiz pode misturar dev dependencies, fixtures e componentes implantáveis. Exceções exigem responsável e prazo.

## Como verificar
Rastreie cada componente a subprojeto e marque escopo de build versus teste. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cdxgen-controlar-escopo-e-exclusoes]] — Complementa o tópico com cyclonedx generator (cdxgen): controlar escopo e exclusões.

## Fontes
- [CycloneDX cdxgen — Repository](https://github.com/CycloneDX/cdxgen) — repositório oficial de geração de BOM para projetos, containers e múltiplos ecossistemas; consultado em 2026-10-04.
- [CycloneDX cdxgen — README](https://github.com/CycloneDX/cdxgen/blob/master/README.md) — guia oficial de instalação, comandos, opções e formatos de saída; consultado em 2026-10-04.
