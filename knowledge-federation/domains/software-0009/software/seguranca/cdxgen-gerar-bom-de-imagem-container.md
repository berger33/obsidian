---
id: software.seguranca.tranche20.001932
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

# CycloneDX Generator (cdxgen): Gerar BOM de imagem container

## Em uma frase
**CycloneDX Generator (cdxgen) — Gerar BOM de imagem container:** Alvos de imagem podem ser inspecionados para identificar pacotes presentes no artefato.

## Por que importa
O recorte de **gerar bom de imagem container** ajuda a inventariar componentes para análise de supply chain, vulnerabilidades, licenças e proveniência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **gerar bom de imagem container**, cdxgen inspeciona alvo e ecossistema, resolve componentes detectáveis e emite BOM CycloneDX para ferramentas downstream. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Gere BOM a partir do digest exato que será publicado no registry. Teste em staging autorizado.

## Limites e trade-offs
Imagem mínima, pacote removido ou catálogo incompleto limita identificação de componentes. Exceções exigem responsável e prazo.

## Como verificar
Compare digest e inventário com conteúdo da imagem e ferramenta independente. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cdxgen-cobrir-ecossistemas-declarados]] — Complementa o tópico com cyclonedx generator (cdxgen): cobrir ecossistemas declarados.

## Fontes
- [CycloneDX cdxgen — Repository](https://github.com/CycloneDX/cdxgen) — repositório oficial de geração de BOM para projetos, containers e múltiplos ecossistemas; consultado em 2026-10-04.
- [CycloneDX cdxgen — README](https://github.com/CycloneDX/cdxgen/blob/master/README.md) — guia oficial de instalação, comandos, opções e formatos de saída; consultado em 2026-10-04.
