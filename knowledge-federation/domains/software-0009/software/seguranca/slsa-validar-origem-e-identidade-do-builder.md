---
id: software.seguranca.tranche20.001904
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
fontes: ["https://slsa.dev/spec/v1.0/", "https://slsa.dev/spec/v1.0/levels"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SLSA: Validar origem e identidade do builder

## Em uma frase
**SLSA — Validar origem e identidade do builder:** Verificador precisa confiar em identidade do builder e origem da atestação, não somente em arquivo presente.

## Por que importa
O recorte de **validar origem e identidade do builder** ajuda a tornar origem e processo de compilação verificáveis para quem recebe artefatos de software. A equipe registra risco, evidência e responsável.

## Como funciona
Para **validar origem e identidade do builder**, produtor gera provenance ligada ao artifact; consumidores validam predicado, builder e garantias esperadas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Permita apenas workflow de release conhecido como produtor do binário de staging. Teste em staging autorizado.

## Limites e trade-offs
Qualquer job capaz de publicar claims pode forjar provenance se identidade não for restringida. Exceções exigem responsável e prazo.

## Como verificar
Tente verificar atestação de outro repositório e confirme que a política rejeita a origem. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[slsa-separar-presenca-de-assinatura-de-nivel-slsa]] — Complementa o tópico com slsa: separar presença de assinatura de nível slsa.

## Fontes
- [SLSA — Specification v1.0](https://slsa.dev/spec/v1.0/) — especificação oficial de tracks, provenance e requisitos SLSA; consultado em 2026-10-04.
- [SLSA — Build levels v1.0](https://slsa.dev/spec/v1.0/levels) — referência oficial das garantias progressivas dos níveis de build; consultado em 2026-10-04.
