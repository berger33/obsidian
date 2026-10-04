---
id: software.seguranca.tranche20.001923
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

# OpenVEX: Justificar not_affected com evidência

## Em uma frase
**OpenVEX — Justificar not_affected com evidência:** `not_affected` deve explicar por que vulnerabilidade não impacta produto, incluindo justificativa ou análise aplicável.

## Por que importa
O recorte de **justificar not_affected com evidência** ajuda a reduzir ambiguidade na triagem de CVEs com afirmações contextualizadas sobre produtos e vulnerabilidades. A equipe registra risco, evidência e responsável.

## Como funciona
Para **justificar not_affected com evidência**, declarações associam produto, vulnerabilidade e status, com justificativa, impacto ou metadados de autor e tempo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Registre que código afetado não está presente no componente de runtime de um build identificado. Teste em staging autorizado.

## Limites e trade-offs
Ausência de exploit conhecido ou baixa severidade não prova que produto não seja afetado. Exceções exigem responsável e prazo.

## Como verificar
Exija justificativa técnica reproduzível e revisão do owner do componente. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[openvex-distinguir-fixed-de-not-affected]] — Complementa o tópico com openvex: distinguir fixed de not_affected.

## Fontes
- [OpenVEX — Specification](https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md) — especificação oficial do formato, statements, produtos, vulnerabilidades e status; consultado em 2026-10-04.
- [Chainguard — What is OpenVEX?](https://edu.chainguard.dev/open-source/sbom/what-is-openvex/) — guia técnico sobre uso de OpenVEX junto a SBOM e triagem de vulnerabilidades; consultado em 2026-10-04.
