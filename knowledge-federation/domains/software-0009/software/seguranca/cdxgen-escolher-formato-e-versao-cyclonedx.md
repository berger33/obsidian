---
id: software.seguranca.tranche20.001936
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

# CycloneDX Generator (cdxgen): Escolher formato e versão CycloneDX

## Em uma frase
**CycloneDX Generator (cdxgen) — Escolher formato e versão CycloneDX:** Gerador oferece opções de formato e versão que afetam compatibilidade com consumidores.

## Por que importa
O recorte de **escolher formato e versão cyclonedx** ajuda a inventariar componentes para análise de supply chain, vulnerabilidades, licenças e proveniência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escolher formato e versão cyclonedx**, cdxgen inspeciona alvo e ecossistema, resolve componentes detectáveis e emite BOM CycloneDX para ferramentas downstream. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Emita JSON na versão suportada pelo scanner que recebe o BOM de teste. Teste em staging autorizado.

## Limites e trade-offs
Consumidor pode ignorar campos ou rejeitar versão diferente da configurada. Exceções exigem responsável e prazo.

## Como verificar
Valide BOM contra schema e importe-o no consumidor downstream. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cdxgen-gerar-bom-no-pipeline-reproduzivel]] — Complementa o tópico com cyclonedx generator (cdxgen): gerar bom no pipeline reproduzível.

## Fontes
- [CycloneDX cdxgen — Repository](https://github.com/CycloneDX/cdxgen) — repositório oficial de geração de BOM para projetos, containers e múltiplos ecossistemas; consultado em 2026-10-04.
- [CycloneDX cdxgen — README](https://github.com/CycloneDX/cdxgen/blob/master/README.md) — guia oficial de instalação, comandos, opções e formatos de saída; consultado em 2026-10-04.
