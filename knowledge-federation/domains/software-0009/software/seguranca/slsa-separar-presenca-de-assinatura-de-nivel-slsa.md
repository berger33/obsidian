---
id: software.seguranca.tranche20.001905
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

# SLSA: Separar presença de assinatura de nível SLSA

## Em uma frase
**SLSA — Separar presença de assinatura de nível SLSA:** Assinatura protege integridade da atestação, enquanto requisitos de nível incluem propriedades do sistema de build.

## Por que importa
O recorte de **separar presença de assinatura de nível slsa** ajuda a tornar origem e processo de compilação verificáveis para quem recebe artefatos de software. A equipe registra risco, evidência e responsável.

## Como funciona
Para **separar presença de assinatura de nível slsa**, produtor gera provenance ligada ao artifact; consumidores validam predicado, builder e garantias esperadas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Verifique assinatura e avalie separadamente os controles exigidos pelo nível declarado. Teste em staging autorizado.

## Limites e trade-offs
Uma provenance assinada por chave de desenvolvedor não implica builder isolado ou protegido. Exceções exigem responsável e prazo.

## Como verificar
Mapeie evidência de assinatura, builder e isolamento em itens diferentes da auditoria. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[slsa-endurecer-plataforma-de-build]] — Complementa o tópico com slsa: endurecer plataforma de build.

## Fontes
- [SLSA — Specification v1.0](https://slsa.dev/spec/v1.0/) — especificação oficial de tracks, provenance e requisitos SLSA; consultado em 2026-10-04.
- [SLSA — Build levels v1.0](https://slsa.dev/spec/v1.0/levels) — referência oficial das garantias progressivas dos níveis de build; consultado em 2026-10-04.
