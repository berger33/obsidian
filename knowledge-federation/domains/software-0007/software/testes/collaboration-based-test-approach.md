---
id: software.testes.collaboration-based.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-06.md"
revisor: ""
fontes: ["https://astqb.org/4-5-collaboration-based-test-approaches/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Collaboration-based test approaches", "Abordagens colaborativas buscam evitar defeitos antes de codificar"]
lote: software-testes-2000-0001
---

# Abordagens colaborativas buscam evitar defeitos antes de codificar

## Em uma frase
Abordagens colaborativas usam comunicação entre stakeholders, negócio, desenvolvimento e teste para esclarecer requisitos e evitar defeitos.

## Por que importa
Técnicas de teste normalmente procuram revelar defeitos no produto; colaboração também tenta evitar que ambiguidades sejam introduzidas. Perguntas discutidas antes da implementação podem alinhar entendimento e reduzir retrabalho.

## Como funciona
O CTFL trata escrita colaborativa de histórias, critérios de aceitação e ATDD. Conversa entre diferentes perspectivas revela exemplos, restrições e resultados esperados. Os casos de ATDD são criados antes da implementação e podem ser manuais ou automatizados. O formato exato deve refletir a forma como stakeholders usam e compram o sistema.

## Exemplo
Antes de implementar renovação automática, product owner, suporte e desenvolvimento acordam quando uma cobrança ocorre, como falhas são comunicadas e como o usuário pode cancelar.

## Limites e trade-offs
Discussão colaborativa não garante consenso correto, nem substitui teste executável ou revisão. Uma pessoa que representa usuários pode não cobrir todas as necessidades; decisões e divergências precisam ser registradas.

## Como verificar
Confirme presença das perspectivas relevantes, critérios observáveis, cenários alternativos e registro das decisões antes da implementação.

## Conexões
- [[early-frequent-stakeholder-feedback]] — promove feedback ao longo do ciclo.
- [[acceptance-test-driven-development]] — deriva casos antes da implementação.

## Fontes
- [ASTQB — CTFL §4.5, Collaboration-based Test Approaches](https://astqb.org/4-5-collaboration-based-test-approaches/) — foco em colaboração e prevenção de defeitos; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §4.5; acesso em 2026-10-01.
