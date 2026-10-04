---
id: software.seguranca.tranche20.001925
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

# OpenVEX: Usar under_investigation sem encerrar triagem

## Em uma frase
**OpenVEX — Usar under_investigation sem encerrar triagem:** Status de investigação comunica incerteza ativa em vez de declarar que produto está seguro ou vulnerável.

## Por que importa
O recorte de **usar under_investigation sem encerrar triagem** ajuda a reduzir ambiguidade na triagem de CVEs com afirmações contextualizadas sobre produtos e vulnerabilidades. A equipe registra risco, evidência e responsável.

## Como funciona
Para **usar under_investigation sem encerrar triagem**, declarações associam produto, vulnerabilidade e status, com justificativa, impacto ou metadados de autor e tempo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Associe prazo e responsável à declaração provisória para um advisory recém-publicado. Teste em staging autorizado.

## Limites e trade-offs
Status provisório sem atualização pode virar exceção permanente. Exceções exigem responsável e prazo.

## Como verificar
Acompanhe idade do statement e exija revisão quando investigação ou versão mudar. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[openvex-referenciar-produto-com-identificador-consistente]] — Complementa o tópico com openvex: referenciar produto com identificador consistente.

## Fontes
- [OpenVEX — Specification](https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md) — especificação oficial do formato, statements, produtos, vulnerabilidades e status; consultado em 2026-10-04.
- [Chainguard — What is OpenVEX?](https://edu.chainguard.dev/open-source/sbom/what-is-openvex/) — guia técnico sobre uso de OpenVEX junto a SBOM e triagem de vulnerabilidades; consultado em 2026-10-04.
