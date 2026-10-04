---
id: software.seguranca.tranche20.001926
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
fontes: ["https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md", "https://edu.chainguard.dev/open-source/sbom/what-is-openvex/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenVEX: Referenciar produto com identificador consistente

## Em uma frase
**OpenVEX — Referenciar produto com identificador consistente:** Identificadores de produto conectam VEX a pacote, versão, CPE, purl ou SBOM conforme esquema utilizado.

## Por que importa
O recorte de **referenciar produto com identificador consistente** ajuda a reduzir ambiguidade na triagem de CVEs com afirmações contextualizadas sobre produtos e vulnerabilidades. A equipe registra risco, evidência e responsável.

## Como funciona
Para **referenciar produto com identificador consistente**, declarações associam produto, vulnerabilidade e status, com justificativa, impacto ou metadados de autor e tempo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use identificador estável e versionado para imagem de teste em vez de nome comercial genérico. Teste em staging autorizado.

## Limites e trade-offs
Correspondência frouxa pode aplicar uma declaração ao artefato errado. Exceções exigem responsável e prazo.

## Como verificar
Resolva produto VEX contra BOM do digest e compare versão e fornecedor. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[openvex-incluir-impacto-e-funcao-do-componente]] — Complementa o tópico com openvex: incluir impacto e função do componente.

## Fontes
- [OpenVEX — Specification](https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md) — especificação oficial do formato, statements, produtos, vulnerabilidades e status; consultado em 2026-10-04.
- [Chainguard — What is OpenVEX?](https://edu.chainguard.dev/open-source/sbom/what-is-openvex/) — guia técnico sobre uso de OpenVEX junto a SBOM e triagem de vulnerabilidades; consultado em 2026-10-04.
