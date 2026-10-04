---
id: software.seguranca.tranche20.001935
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

# CycloneDX Generator (cdxgen): Controlar escopo e exclusões

## Em uma frase
**CycloneDX Generator (cdxgen) — Controlar escopo e exclusões:** Opções de diretório e exclusão alteram arquivos examinados e componentes presentes na saída.

## Por que importa
O recorte de **controlar escopo e exclusões** ajuda a inventariar componentes para análise de supply chain, vulnerabilidades, licenças e proveniência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **controlar escopo e exclusões**, cdxgen inspeciona alvo e ecossistema, resolve componentes detectáveis e emite BOM CycloneDX para ferramentas downstream. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Exclua cache e diretório gerado apenas após confirmar que não entram no pacote final. Teste em staging autorizado.

## Limites e trade-offs
Excluir vendored code ou imagem base pode subestimar inventário entregue. Exceções exigem responsável e prazo.

## Como verificar
Audite arquivos ignorados e compare SBOM com árvore do artefato. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cdxgen-escolher-formato-e-versao-cyclonedx]] — Complementa o tópico com cyclonedx generator (cdxgen): escolher formato e versão cyclonedx.

## Fontes
- [CycloneDX cdxgen — Repository](https://github.com/CycloneDX/cdxgen) — repositório oficial de geração de BOM para projetos, containers e múltiplos ecossistemas; consultado em 2026-10-04.
- [CycloneDX cdxgen — README](https://github.com/CycloneDX/cdxgen/blob/master/README.md) — guia oficial de instalação, comandos, opções e formatos de saída; consultado em 2026-10-04.
