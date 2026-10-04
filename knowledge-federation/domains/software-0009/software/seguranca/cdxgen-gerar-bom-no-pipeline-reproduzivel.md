---
id: software.seguranca.tranche20.001937
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

# CycloneDX Generator (cdxgen): Gerar BOM no pipeline reproduzível

## Em uma frase
**CycloneDX Generator (cdxgen) — Gerar BOM no pipeline reproduzível:** Integrar gerador ao CI associa inventário a commit e evita depender de execução manual.

## Por que importa
O recorte de **gerar bom no pipeline reproduzível** ajuda a inventariar componentes para análise de supply chain, vulnerabilidades, licenças e proveniência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **gerar bom no pipeline reproduzível**, cdxgen inspeciona alvo e ecossistema, resolve componentes detectáveis e emite BOM CycloneDX para ferramentas downstream. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Fixe versão do cdxgen e publique saída como artifact imutável junto do digest. Teste em staging autorizado.

## Limites e trade-offs
Versão da ferramenta ou ambiente pode alterar BOM sem mudança de código. Exceções exigem responsável e prazo.

## Como verificar
Compare BOMs entre builds iguais e investigue diferenças não explicadas. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cdxgen-encadear-geracao-validacao-e-scan]] — Complementa o tópico com cyclonedx generator (cdxgen): encadear geração, validação e scan.

## Fontes
- [CycloneDX cdxgen — Repository](https://github.com/CycloneDX/cdxgen) — repositório oficial de geração de BOM para projetos, containers e múltiplos ecossistemas; consultado em 2026-10-04.
- [CycloneDX cdxgen — README](https://github.com/CycloneDX/cdxgen/blob/master/README.md) — guia oficial de instalação, comandos, opções e formatos de saída; consultado em 2026-10-04.
