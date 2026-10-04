---
id: software.seguranca.tranche20.001924
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

# OpenVEX: Distinguir fixed de not_affected

## Em uma frase
**OpenVEX — Distinguir fixed de not_affected:** Fixed indica que produto ou versão incorpora correção; not_affected descreve falta de impacto no contexto avaliado.

## Por que importa
O recorte de **distinguir fixed de not_affected** ajuda a reduzir ambiguidade na triagem de CVEs com afirmações contextualizadas sobre produtos e vulnerabilidades. A equipe registra risco, evidência e responsável.

## Como funciona
Para **distinguir fixed de not_affected**, declarações associam produto, vulnerabilidade e status, com justificativa, impacto ou metadados de autor e tempo. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use fixed depois de atualizar componente para release que contém patch. Teste em staging autorizado.

## Limites e trade-offs
Afirmar fixed para versão que só tem workaround pode induzir consumidor a aceitar risco. Exceções exigem responsável e prazo.

## Como verificar
Verifique versão corrigida no inventário e teste regressão relevante. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[openvex-usar-under-investigation-sem-encerrar-triagem]] — Complementa o tópico com openvex: usar under_investigation sem encerrar triagem.

## Fontes
- [OpenVEX — Specification](https://github.com/openvex/spec/blob/main/OPENVEX-SPEC.md) — especificação oficial do formato, statements, produtos, vulnerabilidades e status; consultado em 2026-10-04.
- [Chainguard — What is OpenVEX?](https://edu.chainguard.dev/open-source/sbom/what-is-openvex/) — guia técnico sobre uso de OpenVEX junto a SBOM e triagem de vulnerabilidades; consultado em 2026-10-04.
