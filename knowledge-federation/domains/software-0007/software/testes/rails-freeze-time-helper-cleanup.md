---
id: software.testes.tranche14.000806
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://api.rubyonrails.org/classes/ActiveSupport/Testing/TimeHelpers.html", "https://guides.rubyonrails.org/testing.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Rails: congelar o relógio com restauração garantida

## Em uma frase
`travel_to` e `freeze_time` substituem fontes de tempo relevantes para testar vencimentos e agendamentos sem esperar pelo relógio real.

## Por que importa
Controle temporal torna limites de data determinísticos e remove sleeps demorados de cenários que dependem de prazo.

## Como funciona
Inclua `ActiveSupport::Testing::TimeHelpers` e use o helper em bloco quando a restauração imediata for útil; helpers de teste também limpam os stubs no teardown.

## Exemplo
Um teste congela o instante antes da meia-noite, executa a regra de expiração e verifica o dia calculado pela aplicação.

## Limites e trade-offs
Por padrão os microssegundos podem ser zerados para evitar arredondamento em sistemas externos; `with_usec` muda esse comportamento.

## Como verificar
Valide fuso horário, `Time.current` versus relógio do sistema e restauração após caso que levanta exceção.

## Conexões
- [[rails-parallel-process-test-isolation]] — Veja também: Rails: isolar banco e recursos entre workers paralelos.
- [[rails-activejob-enqueue-vs-perform]] — Veja também: Rails: distinguir job enfileirado de job executado.

## Fontes
- [Rails 8.1 — TimeHelpers](https://api.rubyonrails.org/classes/ActiveSupport/Testing/TimeHelpers.html) — travel_to, freeze_time, restauração automática do relógio e microssegundos; consultado em 2026-10-02.
- [Rails 8.1 — Testing Rails Applications](https://guides.rubyonrails.org/testing.html) — ambiente, fixtures, testes funcionais, integração, system tests e paralelismo; consultado em 2026-10-02.
